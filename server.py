"""
Contre-Terre Server — Graph membrane HTTP endpoint.

A lightweight FastAPI application that exposes the Contre-Terre knowledge graph
(worldbuilding, characters, geography, lore) through the Mind membrane protocol.

Runs alongside an embedded FalkorDB instance on Render. The graph is seeded
from JSON files in data/seed/ on first boot and persisted to disk at /data/.

Endpoints:
  /health           — liveness probe for Render
  /membrane/query   — semantic graph query (MCP graph_query equivalent)
  /membrane/info    — graph statistics and available clusters
"""

import os
import sys
import json
import time
import logging
from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

# Runtime path: the mind runtime lives in .mind/runtime/
PROJECT_ROOT = Path(__file__).parent
RUNTIME_ROOT = PROJECT_ROOT / ".mind" / "runtime"
sys.path.insert(0, str(RUNTIME_ROOT))
sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv
load_dotenv(PROJECT_ROOT / ".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)
logger = logging.getLogger("contre-terre")

# ── State ────────────────────────────────────────────────────────────────────

_state = {
    "started_at": None,
    "graph_connected": False,
    "graph_name": os.environ.get("FALKORDB_GRAPH", "contre_terre"),
    "seeded": False,
    "node_count": 0,
}


def _check_graph() -> bool:
    """Test FalkorDB connectivity."""
    try:
        from infrastructure.database.factory import get_database_adapter
        adapter = get_database_adapter()
        # Simple test query
        adapter.query("RETURN 1")
        return True
    except Exception as e:
        logger.warning(f"Graph connection check failed: {e}")
        return False


def _get_node_count() -> int:
    """Count nodes in the graph."""
    try:
        from infrastructure.database.factory import get_database_adapter
        adapter = get_database_adapter()
        result = adapter.query("MATCH (n) RETURN count(n) AS cnt")
        if result and result.result_set:
            return result.result_set[0][0]
    except Exception:
        pass
    return 0


def _seed_graph_if_empty():
    """Load seed JSON files into FalkorDB if the graph is empty."""
    count = _get_node_count()
    if count > 0:
        logger.info(f"Graph already seeded: {count} nodes. Skipping seed.")
        _state["seeded"] = True
        _state["node_count"] = count
        return

    seed_dir = PROJECT_ROOT / "data" / "seed"
    if not seed_dir.exists():
        logger.warning(f"No seed directory at {seed_dir}")
        return

    seed_files = sorted(seed_dir.glob("*.json"))
    if not seed_files:
        logger.warning("No seed JSON files found")
        return

    logger.info(f"Seeding graph from {len(seed_files)} files...")

    try:
        from infrastructure.database.factory import get_database_adapter
        adapter = get_database_adapter()

        total_nodes = 0
        total_links = 0

        for seed_file in seed_files:
            try:
                with open(seed_file, "r") as f:
                    data = json.load(f)

                cluster_id = data.get("cluster_id", seed_file.stem)
                nodes = data.get("nodes", [])
                links = data.get("links", [])

                for node in nodes:
                    node_id = node["id"]
                    node_type = node.get("node_type", "thing")
                    content = node.get("content", "")
                    synthesis = node.get("synthesis", "")
                    weight = node.get("weight", 0.5)
                    ntype = node.get("type", "")
                    props = node.get("properties", {})

                    # Build properties string for Cypher
                    props_str = json.dumps(props) if props else "{}"

                    query = (
                        f"MERGE (n {{id: $id}}) "
                        f"SET n.node_type = $node_type, "
                        f"n.type = $ntype, "
                        f"n.content = $content, "
                        f"n.synthesis = $synthesis, "
                        f"n.weight = $weight, "
                        f"n.properties = $props"
                    )
                    adapter.query(
                        query,
                        params={
                            "id": node_id,
                            "node_type": node_type,
                            "ntype": ntype,
                            "content": content,
                            "synthesis": synthesis,
                            "weight": weight,
                            "props": props_str,
                        },
                    )
                    total_nodes += 1

                for link in links:
                    src = link.get("source", link.get("from", ""))
                    tgt = link.get("target", link.get("to", ""))
                    rel = link.get("type", "link")
                    lweight = link.get("weight", 0.5)
                    lsynthesis = link.get("synthesis", "")
                    laffinity = link.get("affinity", 0.5)
                    lprops = link.get("properties", {})
                    lprops_str = json.dumps(lprops) if lprops else "{}"

                    query = (
                        "MATCH (a {id: $src}), (b {id: $tgt}) "
                        "MERGE (a)-[r:LINK {type: $rel}]->(b) "
                        "SET r.weight = $weight, r.synthesis = $synthesis, "
                        "r.affinity = $affinity, r.properties = $props"
                    )
                    adapter.query(
                        query,
                        params={
                            "src": src,
                            "tgt": tgt,
                            "rel": rel,
                            "weight": lweight,
                            "synthesis": lsynthesis,
                            "affinity": laffinity,
                            "props": lprops_str,
                        },
                    )
                    total_links += 1

                logger.info(f"  Loaded {cluster_id}: {len(nodes)} nodes, {len(links)} links")

            except Exception as e:
                logger.error(f"  Failed to load {seed_file.name}: {e}")

        _state["seeded"] = True
        _state["node_count"] = total_nodes
        logger.info(f"Seeding complete: {total_nodes} nodes, {total_links} links")

    except Exception as e:
        logger.error(f"Seeding failed: {e}")


# ── Lifespan ─────────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: connect to graph, seed if empty."""
    logger.info("Starting Contre-Terre server")
    _state["started_at"] = time.time()
    _state["graph_connected"] = _check_graph()

    if _state["graph_connected"]:
        logger.info(f"FalkorDB connected (graph: {_state['graph_name']})")
        _seed_graph_if_empty()
    else:
        logger.warning("FalkorDB not available at startup")

    yield

    logger.info("Shutting down Contre-Terre server")


# ── App ──────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Contre-Terre",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Health ───────────────────────────────────────────────────────────────────

@app.get("/health")
async def health():
    """Liveness probe for Render."""
    uptime = time.time() - _state["started_at"] if _state["started_at"] else 0

    # Lazy reconnect if graph was down at startup
    if not _state["graph_connected"]:
        _state["graph_connected"] = _check_graph()
        if _state["graph_connected"]:
            _seed_graph_if_empty()

    return {
        "status": "ok" if _state["graph_connected"] else "degraded",
        "graph": _state["graph_name"],
        "graph_connected": _state["graph_connected"],
        "seeded": _state["seeded"],
        "node_count": _state["node_count"],
        "uptime_seconds": round(uptime),
    }


# ── Membrane Query ───────────────────────────────────────────────────────────

class QueryRequest(BaseModel):
    queries: list[str]
    top_k: int = 5
    expand: bool = True


@app.post("/membrane/query")
async def membrane_query(req: QueryRequest):
    """Semantic search across the Contre-Terre graph."""
    if not _state["graph_connected"]:
        raise HTTPException(status_code=503, detail="Graph not connected")

    try:
        from graph_query import run_graph_query
        results = run_graph_query(
            queries=req.queries,
            top_k=req.top_k,
            expand=req.expand,
        )
        return {"results": results}
    except ImportError:
        # Fallback: direct Cypher keyword search
        from infrastructure.database.factory import get_database_adapter
        adapter = get_database_adapter()

        all_results = []
        for q in req.queries:
            query = (
                "MATCH (n) WHERE n.synthesis CONTAINS $q OR n.content CONTAINS $q "
                "RETURN n.id, n.node_type, n.synthesis, n.weight "
                "ORDER BY n.weight DESC LIMIT $limit"
            )
            result = adapter.query(query, params={"q": q, "limit": req.top_k})
            matches = []
            if result and result.result_set:
                for row in result.result_set:
                    matches.append({
                        "id": row[0],
                        "node_type": row[1],
                        "synthesis": row[2],
                        "weight": row[3],
                    })
            all_results.append({"query": q, "matches": matches})

        return {"results": all_results}


@app.get("/membrane/info")
async def membrane_info():
    """Graph statistics and metadata."""
    if not _state["graph_connected"]:
        raise HTTPException(status_code=503, detail="Graph not connected")

    from infrastructure.database.factory import get_database_adapter
    adapter = get_database_adapter()

    # Count by node_type
    counts = {}
    try:
        result = adapter.query(
            "MATCH (n) RETURN n.node_type, count(n) ORDER BY count(n) DESC"
        )
        if result and result.result_set:
            for row in result.result_set:
                counts[row[0] or "unknown"] = row[1]
    except Exception:
        pass

    # Count links
    link_count = 0
    try:
        result = adapter.query("MATCH ()-[r]->() RETURN count(r)")
        if result and result.result_set:
            link_count = result.result_set[0][0]
    except Exception:
        pass

    return {
        "graph": _state["graph_name"],
        "node_counts": counts,
        "link_count": link_count,
        "seeded": _state["seeded"],
    }


# ── Error handling ───────────────────────────────────────────────────────────

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled error on {request.url.path}")
    return JSONResponse(
        status_code=500,
        content={"error": "internal_server_error", "detail": str(exc)},
    )
