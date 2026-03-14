# Seed Data Fix Log

**Date:** 2026-03-14
**Author:** Solen (@solen)
**Scope:** 5 validation fixes across 5 seed files

---

## FIX 1: Duplicate Citizen IDs (CRITICAL)

**Problem:** 21 citizen IDs appeared in multiple files, representing distinct characters with the same name but different archipels, residences, and descriptions. Loading these into the graph would cause data loss via overwrites.

**Solution:** Appended archipel suffix to all 45 duplicate ID occurrences (21 unique IDs x 2-3 files each). Updated all link source/target references in the same file.

**Files modified:**
- `citizens_sud_nord_ouest.json` -- 18 IDs renamed
- `citizens_nordest_est_centresud.json` -- 13 IDs renamed
- `citizens_creuses_sourds_nomades.json` -- 14 IDs renamed

**Suffix convention:** `_sud`, `_nord`, `_ouest`, `_nordest`, `_est`, `_centresud`, `_sudouest`, `_sourds`

**Examples:**
| Old ID | New IDs |
|--------|---------|
| `actor_citoyen_nomalanga` | `actor_citoyen_nomalanga_sud`, `actor_citoyen_nomalanga_nordest`, `actor_citoyen_nomalanga_sudouest` |
| `actor_citoyen_thandeka` | `actor_citoyen_thandeka_sud`, `actor_citoyen_thandeka_est`, `actor_citoyen_thandeka_sudouest` |
| `actor_citoyen_zoleka` | `actor_citoyen_zoleka_ouest`, `actor_citoyen_zoleka_nordest`, `actor_citoyen_zoleka_sudouest` |

**Verification:** 0 duplicate IDs remain across all three citizen files.

---

## FIX 2: Missing node_type in things_world.json

**Problem:** All 66 nodes in `things_world.json` were missing the `node_type` field required by the Mind schema. The existing `type` field (`outil`, `instrument`, `equipement`, `materiau`, `aliment`, `artisanat`, `dispositif`) is the subtype and was preserved.

**Solution:** Added `"node_type": "thing"` to all 66 nodes.

**File modified:** `things_world.json`

**Verification:** 0 nodes missing `node_type`.

---

## FIX 3: Created Missing Guild Nodes

**Problem:** 76 links across all citizen files referenced 3 guild IDs that were never defined as nodes: `narrative_guilde_profondeurs`, `narrative_guilde_sens`, `narrative_guilde_lien`.

**Solution:** Created 3 narrative nodes with type `guilde` and added them to `geo_surface.json`.

**File modified:** `geo_surface.json`

**Nodes created:**
| ID | Content |
|----|---------|
| `narrative_guilde_profondeurs` | Speleologues, geologues, mineurs, aeromaitres -- les metiers qui descendent |
| `narrative_guilde_sens` | Predicteurs, ecouteurs, meteorologues, biologistes -- les metiers qui percoivent |
| `narrative_guilde_lien` | Cartographes, survivalistes, cuisiniers, oceanologues, explosivistes, chefs -- les metiers qui relient |

**Verification:** All 3 guild nodes now exist in the node set.

---

## FIX 4: Normalized Property Keys in citizens_creuses_sourds_nomades.json

**Problem:** `citizens_creuses_sourds_nomades.json` used different property key names than the other two citizen files for the same concepts.

**Solution:** Renamed keys in all 30 nodes:
| Old key | New key |
|---------|---------|
| `archipel_origine` | `archipel` |
| `lieu_residence` | `residence` |
| `dialecte_contact` | `dialecte` |

Domain-specific keys unique to this file (`surdite`, `raison_isolement`, `role_narratif`, `routes_connues`) were left unchanged -- they carry information not present in other files and do not conflict.

**File modified:** `citizens_creuses_sourds_nomades.json`

**Verification:** 0 nodes with old property keys remain.

---

## FIX 5: Fixed Metier Link References in citizens_nordest_est_centresud.json

**Problem:** `citizens_nordest_est_centresud.json` used `thing_metier_*` IDs as link targets (48 links), but no such nodes existed. The other two citizen files used `narrative_guilde_*` links instead -- a structural inconsistency.

**Solution:** Removed all 48 broken `thing_metier_*` links. Added 2 new guild links where citizens were not already linked to their guild (most citizens already had guild links from other link types). The file now has 42 guild links total, consistent with the other citizen files.

**Mapping applied:**
| thing_metier_* | Mapped to guild |
|----------------|-----------------|
| `thing_metier_ecouteur`, `thing_metier_predicteur`, `thing_metier_meteorologue`, `thing_metier_biologiste` | `narrative_guilde_sens` |
| `thing_metier_aeromaitre`, `thing_metier_geologue`, `thing_metier_mineur`, `thing_metier_speleo`, `thing_metier_grimpeur` | `narrative_guilde_profondeurs` |
| `thing_metier_cartographe`, `thing_metier_cuisinier`, `thing_metier_explosifs`, `thing_metier_leader`, `thing_metier_survivaliste` | `narrative_guilde_lien` |

**File modified:** `citizens_nordest_est_centresud.json`

**Verification:** 0 broken `thing_metier_*` links remain.

---

## Remaining Known Issues (not in scope)

These were documented in the validation report but not part of the requested fixes:

1. **7 novel character references** -- `actor_citoyen_senzo`, `actor_citoyen_nandi`, `actor_citoyen_sihle`, `actor_citoyen_jabu`, `actor_citoyen_enama`, `actor_citoyen_thabo`, `actor_citoyen_inyoni` are referenced by 16 links but have no seed nodes. These are the expedition protagonists from the novel.

2. **90 brain seed cross-references** -- Links in `culture_clusters.json` point to `concept:*` and `value:*` IDs that exist in `data/brains/shared/contre_terre_base.json`, not in the seed files. The loader must merge both data sources.

3. **14 orphan proverbs** -- Proverbs in `lore_narratives.json` with no links.

4. **Metier vocabulary inconsistency** -- Different files use different names for the same role (e.g., `specialiste_escalade` vs `grimpeur` vs `escalade`).
