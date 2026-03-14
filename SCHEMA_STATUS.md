# Schema Connection Status

**Date:** 2026-03-14
**Author:** Solen (@solen)

---

## Schema Locations

| Location | Version | Role |
|----------|---------|------|
| `mind-mcp/docs/schema/schema.yaml` | v2.1 | **Authoritative source** (L4 protocol level) |
| `mind-mcp/.mind/schema.yaml` | v2.1 | Runtime copy (synced) |
| `contre-terre/.mind/schema.yaml` | v2.1 | Project copy (synced) |

### Distribution Mechanism

The `mind init` command distributes `schema.yaml` from `mind-mcp/docs/schema/` to each project's `.mind/` directory. See `mind-mcp/runtime/init_cmd.py` lines 496-503. Projects never override it.

---

## What Changed (v2.0 to v2.1)

Contre-terre's schema was at v2.0 (2026-03-13). Updated to v2.1 (2026-03-14).

Key v2.1 changes:
- **Plutchik axes removed from L3 links** (joy_sadness, trust_disgust, fear_anger, surprise_anticipation no longer in frozen_dimensions at L3)
- **Link field reordering**: trust/friction/affinity/aversion promoted to "Relational Physics" section (universal, not just L1)
- **valence/ambivalence** marked as "L1 only" in descriptions
- **Working memory capacity** changed from "5-7 nodes" to "~5000 chars"
- **L3 link initialization** section added: new L3 links inherit trust/friction/affinity/aversion from the creating AI's L1 state
- **New L3 invariant**: link initialization from creator's L1 state

---

## Schema vs. Seed File Compatibility

### 5 Universal Node Types: MATCH

Schema defines: `actor, moment, narrative, space, thing`

| Seed File | Node Types Used | Status |
|-----------|----------------|--------|
| `seed.py` (citizen actors) | `actor` with `node_type='actor'`, `type='citizen'` | COMPATIBLE |
| `citizen_brain_seeder.py` (L1 brain) | 7 cognitive types: value, concept, desire, process, narrative, memory, state | COMPATIBLE (mapped to universal types via schema) |
| `MAPPING.md` | actor, space, moment, narrative, thing | COMPATIBLE |

### Cognitive Type Mapping (L1 brain seeder): CORRECT

| Cognitive Type | Maps To (Universal) | Used in brain seeder |
|---------------|---------------------|---------------------|
| value | narrative | Yes |
| concept | thing | Yes |
| desire | narrative | Yes |
| process | narrative | Yes |
| narrative | narrative | Yes |
| memory | moment | Yes |
| state | actor | Yes |

The brain seeder uses its own `NodeType` enum (7 cognitive types) which is the correct L1 behavior. The mapping to universal types happens at the persistence layer, not in the seeder itself.

### Link Types: COMPATIBLE

- `seed.py` uses Cypher `MERGE (a:Actor ...)` -- no link creation, just actor nodes
- `citizen_brain_seeder.py` uses 14 `LinkType` enum values matching the schema's `relation_kind` values
- `MAPPING.md` defines link patterns using the universal `link` type with semantic subtypes in properties

### Connectome Schema Validator: STALE BUT COMPATIBLE

`mind-mcp/runtime/connectome/schema.py` references "v1.2" in its header and uses an older link type list (`contains, leads_to, expresses, sequence, primes, can_become, relates, about, attached_to`). However, the 5 node types are correct. The link type list is a legacy artifact from the connectome layer -- at the universal level, there is only `link` with properties. The connectome's link types are procedure-level semantics, not schema violations.

---

## Render Deployment

Schema availability for Render is **not an issue**. The schema is:
1. Bundled in the `mind-mcp` repo which is the deployed service
2. Located at `docs/schema/schema.yaml` within the repo
3. Copied to `.mind/schema.yaml` at init time
4. The runtime reads it from the repo, not from an external source
5. `render.yaml` deploys mind-mcp via Docker -- the schema file is included in the Docker build context

No additional schema placement is needed for deployment.

---

## MAPPING.md Consistency: VERIFIED

`contre-terre/docs/MAPPING.md` correctly maps Contre-Terre vocabulary to the 5 universal node types:

- `actor` for characters (personnages)
- `space` for geological layers and locations
- `moment` for narrative events (deaths, rituals, decisions)
- `narrative` for conceptual systems (Contact, tremens, arcs)
- `thing` for significant objects (instruments, tools, devices)

Link patterns use the universal `link` type with semantic subtypes in properties (e.g., `type: "meurt_a"`, `type: "exerce"`), which is consistent with the schema's "all semantics in properties" principle.

ID convention (`{node_type}_{SUBTYPE}_{instance}`) aligns with schema patterns.

---

## Actions Taken

1. **Updated** `contre-terre/.mind/schema.yaml` from v2.0 to v2.1 (copied from authoritative source)
2. **Synced** `mind-mcp/.mind/schema.yaml` to match `mind-mcp/docs/schema/schema.yaml` (was also at v2.0)
3. **Verified** all seed files and MAPPING.md are compatible with v2.1

## No Action Required

- Schema distribution for Render deployment: already handled by the Docker build
- MAPPING.md: already consistent
- Seed files: already compatible
- Connectome validator: uses correct node types; link types are procedure-level, not schema-level
