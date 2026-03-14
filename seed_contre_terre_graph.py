#!/usr/bin/env python3
"""Seed the Contre-Terre graph in FalkorDB with all world and brain data.

Ingests:
  - 11 seed files from data/seed/*.json (geography, citizens, lore, culture, things, relationships)
  - 24 brain seed files from data/brains/**/*.json (shared knowledge, metier clusters, citizen brains)

Each JSON file contains a cluster with "nodes" and "links" arrays.
Nodes use MERGE by id to avoid duplicates. Links use MERGE by source+target+type.

FalkorDB uses node labels for node_type (actor, moment, narrative, space, thing).
Brain seed nodes without node_type are mapped via the L1 cognitive type schema.

Connection: FalkorDB over Redis protocol.
Config: env vars > .mind/database_config.yaml > defaults.
"""

import json
import os
import sys
import time
from pathlib import Path

import yaml
from falkordb import FalkorDB

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_SEED_DIR = SCRIPT_DIR / "data" / "seed"
DATA_BRAINS_DIR = SCRIPT_DIR / "data" / "brains"
DATABASE_CONFIG_PATH = SCRIPT_DIR / ".mind" / "database_config.yaml"

VALID_NODE_TYPES = {"actor", "moment", "narrative", "space", "thing"}

# L1 cognitive type -> universal node_type (from schema.yaml cognitive_types)
COGNITIVE_TYPE_TO_NODE_TYPE = {
    "memory": "moment",
    "concept": "thing",
    "narrative": "narrative",
    "value": "narrative",
    "process": "narrative",
    "desire": "narrative",
    "state": "actor",
}

# Node properties that map directly to graph node fields (floats)
NUMERIC_NODE_PROPS = {
    "weight", "energy", "stability", "recency",
    "self_relevance", "partner_relevance",
    "goal_relevance", "novelty_affinity", "care_affinity",
    "achievement_affinity", "risk_affinity",
    "drive_affinity", "curiosity_affinity", "affiliation_affinity",
    "frustration_affinity", "self_preservation_affinity",
}

# Link properties that are direct numeric fields
NUMERIC_LINK_PROPS = {
    "weight", "affinity", "trust",
}

# Fields that are NOT stored as node properties (they're structural)
NODE_STRUCTURAL_FIELDS = {"id", "node_type"}

# ─────────────────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────────────────

def load_config():
    """Load database configuration from env vars or .mind/database_config.yaml."""
    config = {
        "host": "localhost",
        "port": 6379,
        "graph_name": "contre_terre",
    }

    # Read from database_config.yaml if it exists
    if DATABASE_CONFIG_PATH.exists():
        with open(DATABASE_CONFIG_PATH) as f:
            yaml_config = yaml.safe_load(f)
        if yaml_config and "database" in yaml_config:
            db = yaml_config["database"]
            falkordb_conf = db.get("falkordb", {})
            if falkordb_conf.get("host"):
                config["host"] = falkordb_conf["host"]
            if falkordb_conf.get("port"):
                config["port"] = int(falkordb_conf["port"])
            if falkordb_conf.get("graph_name"):
                config["graph_name"] = falkordb_conf["graph_name"]

    # Env vars override everything
    config["host"] = os.environ.get("FALKORDB_HOST", config["host"])
    config["port"] = int(os.environ.get("FALKORDB_PORT", config["port"]))
    config["graph_name"] = os.environ.get("FALKORDB_GRAPH", config["graph_name"])

    return config


# ─────────────────────────────────────────────────────────────────────────────
# File loading
# ─────────────────────────────────────────────────────────────────────────────

def load_json_files(directory, pattern="*.json", recursive=False):
    """Load all JSON files matching pattern from directory. Returns list of (path, data)."""
    if recursive:
        paths = sorted(directory.rglob(pattern))
    else:
        paths = sorted(directory.glob(pattern))

    results = []
    for path in paths:
        # Skip non-JSON files that might match
        if path.suffix != ".json":
            continue
        with open(path) as f:
            data = json.load(f)
        results.append((path, data))

    return results


# ─────────────────────────────────────────────────────────────────────────────
# Node type resolution
# ─────────────────────────────────────────────────────────────────────────────

def resolve_node_type(node, is_brain_seed):
    """Determine the FalkorDB label (node_type) for a node.

    Seed files have explicit node_type. Brain seed files use cognitive types
    mapped through the L1 schema.

    Returns: one of the 5 universal types (actor, moment, narrative, space, thing).
    Raises ValueError if the type cannot be resolved.
    """
    # Seed files: explicit node_type
    if "node_type" in node:
        nt = node["node_type"]
        if nt not in VALID_NODE_TYPES:
            raise ValueError(f"Invalid node_type '{nt}' on node '{node.get('id', '?')}'")
        return nt

    # Brain seeds: map cognitive type to universal type
    if is_brain_seed:
        cognitive_type = node.get("type")
        if cognitive_type in COGNITIVE_TYPE_TO_NODE_TYPE:
            return COGNITIVE_TYPE_TO_NODE_TYPE[cognitive_type]
        # If no recognized type, default to narrative (internal knowledge)
        raise ValueError(
            f"Unknown cognitive type '{cognitive_type}' on brain node '{node.get('id', '?')}'. "
            f"Valid types: {sorted(COGNITIVE_TYPE_TO_NODE_TYPE.keys())}"
        )

    raise ValueError(f"Node '{node.get('id', '?')}' has no node_type and is not a brain seed")


# ─────────────────────────────────────────────────────────────────────────────
# Property serialization
# ─────────────────────────────────────────────────────────────────────────────

def serialize_value(value):
    """Serialize a value for storage in FalkorDB.

    Dicts and lists become JSON strings. Everything else passes through.
    """
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return value


def build_node_properties(node, is_brain_seed):
    """Extract all storable properties from a node dict.

    Returns a dict of property_name -> value, with complex types serialized.
    Excludes structural fields (id, node_type).
    """
    props = {}

    for key, value in node.items():
        if key in NODE_STRUCTURAL_FIELDS:
            continue
        props[key] = serialize_value(value)

    # Ensure defaults for missing critical fields
    props.setdefault("content", "")
    if not props.get("synthesis"):
        # Generate synthesis from content if missing or empty
        props["synthesis"] = (props.get("content") or "")[:200]
    props.setdefault("weight", 0.5)

    # Brain seeds: store the cognitive type in the 'type' field (already there from data)
    # Seed files: 'type' is already a subtype field

    return props


# ─────────────────────────────────────────────────────────────────────────────
# Cypher generation
# ─────────────────────────────────────────────────────────────────────────────

def create_node(graph, node, is_brain_seed, stats):
    """Create or merge a single node in FalkorDB.

    Uses MERGE on id to avoid duplicates. Sets all properties via SET.
    The node_type becomes the Cypher label.
    """
    node_id = node.get("id")
    if not node_id:
        raise ValueError(f"Node missing 'id' field: {json.dumps(node)[:200]}")

    node_type = resolve_node_type(node, is_brain_seed)
    props = build_node_properties(node, is_brain_seed)

    # Build SET clause dynamically from properties
    set_parts = []
    params = {"id": node_id}

    for i, (key, value) in enumerate(props.items()):
        param_name = f"p{i}"
        set_parts.append(f"n.{key} = ${param_name}")
        params[param_name] = value

    set_clause = ", ".join(set_parts)

    # FalkorDB: label is the node_type
    query = f"MERGE (n:{node_type} {{id: $id}}) SET {set_clause}"

    graph.query(query, params)
    stats["nodes_created"] += 1


def create_link(graph, link, stats):
    """Create or merge a single link between two nodes in FalkorDB.

    Matches source and target by id (across all labels), then creates a :link edge.
    """
    source = link.get("source")
    target = link.get("target")
    link_type = link.get("type", "relates_to")

    if not source or not target:
        raise ValueError(f"Link missing source/target: {json.dumps(link)[:200]}")

    # Build link properties
    params = {
        "src": source,
        "tgt": target,
        "link_type": link_type,
    }

    set_parts = ["r.type = $link_type"]

    # Add numeric link properties
    param_idx = 0
    for key in ("weight", "affinity", "trust"):
        if key in link:
            param_name = f"lp{param_idx}"
            set_parts.append(f"r.{key} = ${param_name}")
            params[param_name] = link[key]
            param_idx += 1

    # Serialize any 'properties' dict on the link
    if "properties" in link:
        param_name = f"lp{param_idx}"
        set_parts.append(f"r.properties = ${param_name}")
        params[param_name] = json.dumps(link["properties"], ensure_ascii=False)
        param_idx += 1

    set_clause = ", ".join(set_parts)

    # Match nodes across all possible labels (any node_type)
    query = (
        "MATCH (a {id: $src}), (b {id: $tgt}) "
        f"MERGE (a)-[r:link {{type: $link_type}}]->(b) "
        f"SET {set_clause}"
    )

    result = graph.query(query, params)

    # Check if the match found nodes — FalkorDB returns 0 relationships if nodes don't exist
    if result.relationships_created == 0 and result.properties_set == 0:
        stats["links_skipped"] += 1
        stats["missing_endpoints"].append(f"{source} -> {target} ({link_type})")
    else:
        stats["links_created"] += 1


# ─────────────────────────────────────────────────────────────────────────────
# Main seeding logic
# ─────────────────────────────────────────────────────────────────────────────

def seed_graph():
    """Main entry point: connect to FalkorDB, load all seed data, create nodes and links."""
    config = load_config()
    print(f"Connecting to FalkorDB at {config['host']}:{config['port']}, graph: {config['graph_name']}")

    db = FalkorDB(host=config["host"], port=config["port"])
    graph = db.select_graph(config["graph_name"])

    stats = {
        "nodes_created": 0,
        "links_created": 0,
        "links_skipped": 0,
        "files_processed": 0,
        "errors": [],
        "missing_endpoints": [],
    }

    t_start = time.time()

    # ── Phase 1: Load all seed files (world data) ──────────────────────────
    print("\n── Phase 1: World seed files ──")
    seed_files = load_json_files(DATA_SEED_DIR, "*.json", recursive=False)
    if not seed_files:
        print(f"  ERROR: No seed files found in {DATA_SEED_DIR}", file=sys.stderr)
        sys.exit(1)
    print(f"  Found {len(seed_files)} seed files")

    # ── Phase 2: Load all brain seed files ─────────────────────────────────
    print("\n── Phase 2: Brain seed files ──")
    brain_files = load_json_files(DATA_BRAINS_DIR, "*.json", recursive=True)
    if not brain_files:
        print(f"  ERROR: No brain files found in {DATA_BRAINS_DIR}", file=sys.stderr)
        sys.exit(1)
    print(f"  Found {len(brain_files)} brain files")

    # ── Phase 3: Create all nodes (seed first, then brain) ─────────────────
    # Seed nodes first so brain links can reference world nodes
    print("\n── Phase 3: Creating nodes ──")

    all_files = [(path, data, False) for path, data in seed_files] + \
                [(path, data, True) for path, data in brain_files]

    for path, data, is_brain in all_files:
        cluster_id = data.get("cluster_id", path.stem)
        nodes = data.get("nodes", [])
        relative_path = path.relative_to(SCRIPT_DIR)

        node_count_before = stats["nodes_created"]
        for node in nodes:
            try:
                create_node(graph, node, is_brain, stats)
            except Exception as e:
                error_msg = f"  Node error in {relative_path}: {e}"
                print(error_msg, file=sys.stderr)
                stats["errors"].append(error_msg)

        created = stats["nodes_created"] - node_count_before
        print(f"  {relative_path}: {created} nodes ({cluster_id})")
        stats["files_processed"] += 1

    # ── Phase 4: Create all links ──────────────────────────────────────────
    print("\n── Phase 4: Creating links ──")

    for path, data, is_brain in all_files:
        links = data.get("links", [])
        if not links:
            continue

        relative_path = path.relative_to(SCRIPT_DIR)
        link_count_before = stats["links_created"]
        skip_count_before = stats["links_skipped"]

        for link in links:
            try:
                create_link(graph, link, stats)
            except Exception as e:
                error_msg = f"  Link error in {relative_path}: {e}"
                print(error_msg, file=sys.stderr)
                stats["errors"].append(error_msg)

        created = stats["links_created"] - link_count_before
        skipped = stats["links_skipped"] - skip_count_before
        skip_note = f" ({skipped} skipped: missing endpoints)" if skipped else ""
        print(f"  {relative_path}: {created} links{skip_note}")

    # ── Report ─────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    print("\n" + "=" * 60)
    print("SEED COMPLETE")
    print("=" * 60)
    print(f"  Files processed:  {stats['files_processed']}")
    print(f"  Nodes created:    {stats['nodes_created']}")
    print(f"  Links created:    {stats['links_created']}")
    print(f"  Links skipped:    {stats['links_skipped']}")
    print(f"  Errors:           {len(stats['errors'])}")
    print(f"  Time:             {elapsed:.1f}s")

    if stats["missing_endpoints"]:
        print(f"\n  Missing endpoints ({len(stats['missing_endpoints'])} links):")
        # Show first 20 at most
        for ep in stats["missing_endpoints"][:20]:
            print(f"    - {ep}")
        if len(stats["missing_endpoints"]) > 20:
            print(f"    ... and {len(stats['missing_endpoints']) - 20} more")

    if stats["errors"]:
        print(f"\n  Errors ({len(stats['errors'])}):")
        for err in stats["errors"]:
            print(f"    {err}")
        sys.exit(1)

    print("\nDone.")


if __name__ == "__main__":
    seed_graph()
