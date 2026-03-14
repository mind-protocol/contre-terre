"""
Contre-Terre Server — In-memory graph membrane.

Loads the world seed (JSON files) into memory at startup.
Serves queries via keyword search on node content/synthesis.
No Redis dependency — the JSON files ARE the database.

Endpoints:
  /health           — liveness probe
  /membrane/query   — keyword search across nodes
  /membrane/info    — graph statistics
  /citizens         — citizen list for 3D engine
"""

import json
import time
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")
logger = logging.getLogger("contre-terre")

PROJECT_ROOT = Path(__file__).parent

# ── In-Memory Graph ──────────────────────────────────────────────────────────

_nodes: dict[str, dict] = {}  # id → node
_links: list[dict] = []       # list of {source, target, type, ...}
_started_at: float = 0


def _load_graph():
    """Load all seed + brain JSON files into memory."""
    global _nodes, _links

    dirs = [
        PROJECT_ROOT / "data" / "seed",
        PROJECT_ROOT / "data" / "brains" / "shared",
        PROJECT_ROOT / "data" / "brains" / "citizens",
        PROJECT_ROOT / "data" / "brains" / "metier_clusters",
    ]

    for d in dirs:
        if not d.exists():
            continue
        for f in sorted(d.glob("*.json")):
            try:
                data = json.loads(f.read_text())
                nodes = data.get("nodes", [])
                links = data.get("links", [])
                for n in nodes:
                    _nodes[n["id"]] = n
                _links.extend(links)
                logger.info(f"  {f.name}: {len(nodes)} nodes, {len(links)} links")
            except Exception as e:
                logger.error(f"  Failed {f.name}: {e}")

    logger.info(f"Graph loaded: {len(_nodes)} nodes, {len(_links)} links")


def _search(query: str, top_k: int = 5) -> list[dict]:
    """Simple keyword search across node content and synthesis."""
    q = query.lower()
    scored = []
    for nid, node in _nodes.items():
        content = (node.get("content") or "").lower()
        synthesis = (node.get("synthesis") or "").lower()
        score = 0
        if q in synthesis:
            score += 2
        if q in content:
            score += 1
        if q in nid.lower():
            score += 3
        if score > 0:
            weight = node.get("weight", 0.5)
            scored.append((score * weight, node))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [
        {
            "id": n["id"],
            "node_type": n.get("node_type", ""),
            "type": n.get("type", ""),
            "content": n.get("content", ""),
            "synthesis": n.get("synthesis", ""),
            "weight": n.get("weight", 0.5),
            "score": round(s, 3),
        }
        for s, n in scored[:top_k]
    ]


def _get_neighbors(node_id: str) -> list[dict]:
    """Get all nodes connected to a given node."""
    neighbor_ids = set()
    for link in _links:
        src = link.get("source", link.get("from", ""))
        tgt = link.get("target", link.get("to", ""))
        rel = link.get("type", "link")
        if src == node_id and tgt in _nodes:
            neighbor_ids.add((tgt, rel, "outgoing"))
        elif tgt == node_id and src in _nodes:
            neighbor_ids.add((src, rel, "incoming"))
    return [
        {
            "id": nid,
            "relation": rel,
            "direction": direction,
            "synthesis": (_nodes[nid].get("synthesis") or "")[:200],
        }
        for nid, rel, direction in neighbor_ids
    ]


# ── App ──────────────────────────────────────────────────────────────────────

app = FastAPI(title="Contre-Terre", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    global _started_at
    _started_at = time.time()
    logger.info("Loading Contre-Terre graph into memory...")
    _load_graph()


# ── Health ───────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {
        "status": "ok" if _nodes else "empty",
        "nodes": len(_nodes),
        "links": len(_links),
        "uptime_seconds": round(time.time() - _started_at),
    }


# ── Query ────────────────────────────────────────────────────────────────────

class QueryRequest(BaseModel):
    queries: list[str]
    top_k: int = 5
    expand: bool = True


@app.post("/membrane/query")
def membrane_query(req: QueryRequest):
    results = []
    for q in req.queries:
        matches = _search(q, req.top_k)
        if req.expand and matches:
            for m in matches:
                m["neighbors"] = _get_neighbors(m["id"])
        results.append({"query": q, "matches": matches})
    return {"results": results}


# ── Info ─────────────────────────────────────────────────────────────────────

@app.get("/membrane/info")
def membrane_info():
    counts: dict[str, int] = {}
    for n in _nodes.values():
        nt = n.get("node_type", n.get("type", "unknown"))
        counts[nt] = counts.get(nt, 0) + 1
    return {
        "nodes": len(_nodes),
        "links": len(_links),
        "by_type": counts,
    }


# ── Citizens (for 3D engine) ────────────────────────────────────────────────

@app.get("/citizens")
def citizens():
    citizens_file = PROJECT_ROOT / "data" / "citizens.json"
    if citizens_file.exists():
        return json.loads(citizens_file.read_text())
    return []


# ── Citizen info by handle ────────────────────────────────────────────────────

@app.get("/infos/@{handle}")
def citizen_info(handle: str):
    """Get full citizen profile: identity, neighbors, relationships, location."""
    # Find the citizen node
    citizen_id = f"actor_citoyen_{handle}"
    if citizen_id not in _nodes:
        # Try without suffix — search all nodes
        matches = [nid for nid in _nodes if nid.startswith(f"actor_citoyen_{handle}")]
        if not matches:
            raise HTTPException(404, f"Citizen @{handle} not found")
        citizen_id = matches[0]

    citizen = _nodes[citizen_id]
    neighbors = _get_neighbors(citizen_id)

    # Split neighbors by type
    knows = [n for n in neighbors if n["relation"] in ("connait", "ami_de", "collegue_de", "marie_a", "parent_de")]
    trained_by = [n for n in neighbors if n["relation"] in ("forme_par", "enseigne")]
    conflicts = [n for n in neighbors if n["relation"] in ("en_conflit_avec", "rival_de")]
    location = [n for n in neighbors if n["relation"] in ("habite",)]
    guild = [n for n in neighbors if n["relation"] in ("membre_de",)]
    respects = [n for n in neighbors if n["relation"] == "respecte"]
    debts = [n for n in neighbors if n["relation"] == "doit_a"]

    # Read CLAUDE.md if available
    claude_md = ""
    claude_path = PROJECT_ROOT / "citizens" / handle / "CLAUDE.md"
    if claude_path.exists():
        claude_md = claude_path.read_text()

    return {
        "handle": handle,
        "id": citizen_id,
        "identity": claude_md,
        "node": citizen,
        "location": location,
        "guild": guild,
        "knows": knows,
        "trained_by": trained_by,
        "conflicts": conflicts,
        "respects": respects,
        "debts": debts,
        "all_connections": len(neighbors),
    }


# ── Node detail ──────────────────────────────────────────────────────────────

@app.get("/node/{node_id}")
def get_node(node_id: str):
    if node_id not in _nodes:
        raise HTTPException(404, f"Node {node_id} not found")
    node = _nodes[node_id]
    return {
        **node,
        "neighbors": _get_neighbors(node_id),
    }
