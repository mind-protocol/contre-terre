# Seed Data Validation Report

**Date:** 2026-03-14
**Validator:** Solen (@solen)
**Files validated:** 10 seed files + 1 brain seed (reference)

---

## Summary

| Check | Result | Details |
|-------|--------|---------|
| 1. JSON validity | PASS | All 10 files are valid JSON with required fields |
| 2. Node ID uniqueness | FAIL | 21 duplicate IDs across citizen files |
| 3. Link integrity | FAIL | 230 broken target references (0 broken sources) |
| 4. Coverage | WARN | Metier naming inconsistent; some known metiers missing |
| 5. Orphan check | WARN | 14 orphan nodes (proverbs with no links) |
| 6. Schema consistency | FAIL | things_world.json missing node_type on all 66 nodes |

---

## 1. JSON Validity -- PASS

All 10 files parse as valid JSON. All contain the required top-level fields: `cluster_id`, `description`, `nodes[]`, `links[]`.

| File | cluster_id | Nodes | Links |
|------|-----------|-------|-------|
| culture_clusters.json | culture_clusters | 57 | 148 |
| things_world.json | things_world | 66 | 112 |
| geo_surface.json | geo_surface | 41 | 46 |
| geo_vertical.json | geo_vertical | 21 | 41 |
| geo_buildings.json | geo_buildings | 45 | 61 |
| lore_figures.json | lore_figures | 47 | 52 |
| lore_narratives.json | lore_narratives | 47 | 36 |
| citizens_sud_nord_ouest.json | citizens_sud_nord_ouest | 36 | 112 |
| citizens_nordest_est_centresud.json | citizens_nordest_est_centresud | 35 | 158 |
| citizens_creuses_sourds_nomades.json | citizens_creuses_sourds_nomades | 30 | 105 |

---

## 2. Node ID Uniqueness -- FAIL

**21 duplicate node IDs** found across the three citizen files. These are distinct characters (different archipels, residences, metiers, descriptions) that share the same ID. Each represents a name collision, not an intentional cross-file reference.

### Duplicates appearing in 3 files (most severe)

| Duplicate ID | File 1 (archipel) | File 2 (archipel) | File 3 (archipel) |
|---|---|---|---|
| actor_citoyen_nomalanga | sud (Ndaba) | nord_est (Mhluzi) | sud_ouest (Sibaya) |
| actor_citoyen_thandeka | sud (Kahlamba) | est (Umsizi) | sud_ouest (Mathamo) |
| actor_citoyen_zoleka | ouest (Ingwe) | nord_est (Iziphuku) | sud_ouest (Sibaya) |

### Duplicates appearing in 2 files

| Duplicate ID | File 1 (archipel) | File 2 (archipel) |
|---|---|---|
| actor_citoyen_buhle | sud (Kahlamba) | sud_ouest (Sibaya) |
| actor_citoyen_busisiwe | centre_sud (Themba) | ouest (desert) |
| actor_citoyen_dumisa | nord (Umzimkhulu) | nord_est (desert) |
| actor_citoyen_lindiwe | sud (Ndaba) | sud_ouest (Mathamo) |
| actor_citoyen_lungile | nord (Umzimkhulu) | est (Umsizi) |
| actor_citoyen_mandla | sud (Kahlamba) | sourds (Village) |
| actor_citoyen_nolwazi | ouest (Ingwe) | sourds (Village) |
| actor_citoyen_nombuso | nord_est (Mhluzi) | sud_ouest (Sibaya) |
| actor_citoyen_nomvula | sud (Lesedi) | est (Umsizi) |
| actor_citoyen_nosipho | sud (Kahlamba) | centre_sud (Bhekisisa) |
| actor_citoyen_ntombi | nord (Umzimkhulu) | centre_sud (Sourds) |
| actor_citoyen_sandile | ouest (Ingwe) | sud_ouest (Sibaya) |
| actor_citoyen_siphamandla | nord_est (Iziphuku) | sud (desert) |
| actor_citoyen_siyabonga | sud (Ndaba) | est (Umsizi) |
| actor_citoyen_sizwe | ouest (Ingwe) | est (Nkosazana) |
| actor_citoyen_thulani | sud (Lesedi) | centre_sud (Bhekisisa) |
| actor_citoyen_xolani | ouest (Zama) | est (desert) |
| actor_citoyen_zanele | sud (Kahlamba) | centre_sud (Bhekisisa) |

**Recommendation:** Disambiguate by appending archipel suffix to the ID (e.g., `actor_citoyen_nomalanga_sud`, `actor_citoyen_nomalanga_nordest`, `actor_citoyen_nomalanga_sudouest`). This is the most severe issue -- duplicate IDs will cause data loss or overwrites when loading into the graph.

---

## 3. Link Integrity -- FAIL

**0 broken sources, 230 broken targets.** No source reference points to a nonexistent node. However, 230 links point to target node IDs that do not exist in any of the 10 seed files.

### Breakdown by category

| Category | Count | Explanation |
|----------|-------|-------------|
| Cross-references to brain seed (`concept:*`, `value:*`) | 90 | Targets exist in `contre_terre_base.json` but not in seed files |
| Guild references (`narrative_guilde_*`) | 76 | 3 guildes referenced but never defined as nodes |
| Metier references (`thing_metier_*`) | 48 | 14 metier nodes referenced but never defined |
| Novel character references (`actor_citoyen_*`) | 16 | 7 novel protagonists referenced but not in seed data |

### 3a. Cross-references to brain seed (90 links) -- STRUCTURAL DECISION

These links in `culture_clusters.json` point to IDs that exist in `data/brains/shared/contre_terre_base.json`:

- `concept:archipel` (26 references)
- `concept:contact` (19 references)
- `concept:tremens` (5 references)
- `concept:bioluminescence` (1 reference)
- `concept:magnitude_11` (1 reference)
- `concept:mission` (1 reference)
- `value:body_truth` (3 references)
- `value:collective_survival` (5 references)
- `value:contact_richesse` (2 references)
- `value:perception_is_identity` (1 reference)
- `value:physics_over_rules` (2 references)
- `value:transmission` (2 references)
- `value:vocabulary_preservation` (4 references)

**Recommendation:** Either include these brain seed nodes in the seed files, or document that seed files intentionally reference brain seed nodes and the loader must merge both data sources.

### 3b. Missing guild nodes (76 links)

Three guild IDs are referenced by citizen links but never defined as nodes anywhere:

- `narrative_guilde_lien` (referenced by ~35 citizens)
- `narrative_guilde_profondeurs` (referenced by ~22 citizens)
- `narrative_guilde_sens` (referenced by ~19 citizens)

**Recommendation:** Create guild nodes in one of the seed files (likely `culture_clusters.json` or a new `guilds.json`).

### 3c. Missing metier nodes (48 links)

14 metier node IDs are referenced in `citizens_nordest_est_centresud.json` links but never defined:

`thing_metier_ecouteur`, `thing_metier_predicteur`, `thing_metier_aeromaitre`, `thing_metier_geologue`, `thing_metier_mineur`, `thing_metier_speleo`, `thing_metier_grimpeur`, `thing_metier_cartographe`, `thing_metier_cuisinier`, `thing_metier_explosifs`, `thing_metier_leader`, `thing_metier_meteorologue`, `thing_metier_biologiste`, `thing_metier_survivaliste`

Note: Only `citizens_nordest_est_centresud.json` uses these `thing_metier_*` links. The other two citizen files use `narrative_guilde_*` links instead. This is a structural inconsistency between the three citizen files.

**Recommendation:** Create metier nodes in `things_world.json` or `culture_clusters.json`, OR standardize on guild-only links across all citizen files.

### 3d. Missing novel character nodes (16 links)

7 novel protagonists are referenced as link targets in `citizens_creuses_sourds_nomades.json` but have no corresponding nodes in any seed file:

- `actor_citoyen_senzo` (3 links to him)
- `actor_citoyen_nandi` (2 links)
- `actor_citoyen_sihle` (2 links)
- `actor_citoyen_jabu` (3 links)
- `actor_citoyen_enama` (2 links)
- `actor_citoyen_thabo` (2 links)
- `actor_citoyen_inyoni` (2 links)

These are the 7 members of the expedition from the novel. Other citizens link to them (e.g., "trained Senzo", "cousin of Nandi") but the protagonists themselves are not defined as seed nodes.

**Recommendation:** Either create seed nodes for the 7 novel characters, or remove these links and encode the relationships in the content/synthesis text instead.

---

## 4. Coverage Check

### 4a. Nodes per type

| node_type | Count |
|-----------|-------|
| space | 107 |
| narrative | 96 |
| actor | 95 |
| moment | 37 |
| (no node_type -- things_world) | 66 |

Note: `things_world.json` uses subtypes (`outil`, `instrument`, `equipement`, `materiau`, `aliment`, `artisanat`, `dispositif`) in the `type` field but is missing the `node_type` field entirely. See Section 6 below.

### 4b. Citizens per archipel

| Archipel | Citizens | Status |
|----------|----------|--------|
| Sud (Basses-Terres) | 17 | OK |
| Nord (Froides) | 15 | OK |
| Nord-Est (Seches) | 11 | OK |
| Centre-Sud (Chaudes) | 11 | OK |
| Ouest (Roulantes) | 9 | OK |
| Est (Salines) | 5 | Low |
| Sud-Ouest (Creuses) | 4 | Low |
| Village des Sourds | 5 | OK (non-standard archipel) |
| Nomadic (desert) | 10+ | OK (non-standard) |

All 7 archipelagos are represented. Est and Sud-Ouest have notably fewer citizens than other archipels.

### 4c. Metier coverage -- WARN

There are significant metier naming inconsistencies across the three citizen files:

**Naming variants for the same role:**
- `specialiste_escalade` (file 1) vs `grimpeur` (file 2) vs `escalade` (file 3) -- all refer to climbing
- `specialiste_survie` (file 1) vs `survivaliste` (files 2, 3)
- `specialiste_roche` (file 1) -- no equivalent in other files (closest: `mineur`)
- `specialiste_oceans` (file 1) vs `specialiste_oceanique` (in culture_clusters tics)
- `speleologue` (files 1, 3) vs `speleo` (file 2)
- `specialiste_explosifs` (file 3) vs `explosifs` (file 2)

**Metiers present per file:**
| Metier | sud_nord_ouest | nordest_est_centresud | creuses_sourds_nomades |
|--------|:-:|:-:|:-:|
| ecouteur | 5 | 6 | 2 |
| predicteur | 1 | 4 | 3 |
| aeromaitre | - | 2 | - |
| geologue | - | 2 | - |
| mineur | 6 | 5 | 2 |
| speleologue/speleo | 1 | 2 | 6 |
| grimpeuse/grimpeur/escalade | 7 | 3 | 2 |
| cartographe | 6 | 3 | 9 |
| cuisinier | 4 | 3 | 3 |
| leader | 6 | 3 | - |
| meteorologue | 1 | 3 | 1 |
| biologiste | 2 | 3 | 4 |
| survivaliste/specialiste_survie | 4 | 8 | 9 |
| specialiste_oceans | 3 | - | 2 |
| specialiste_roche | 6 | - | 1 |
| specialiste_explosifs/explosifs | - | 1 | 1 |

**Missing from the original 15 known metiers:**
- `cordiste` -- 0 citizens (distinct from general cordage)
- `caravanier` -- 0 citizens with this metier label (some have caravanier in descriptions)
- `tisserand` -- 0 citizens (though Ndaba is a weaving village)
- `grimpeuse` -- 0 (replaced by variants `grimpeur`, `specialiste_escalade`, `escalade`)

**Recommendation:** Standardize metier vocabulary across all three files. Pick one canonical name per role and use it consistently. Add missing metiers (cordiste, caravanier, tisserand) or document why they are absent.

### 4d. Settlement coverage

All 17 named settlements (villes and villages) have at least one citizen. Coverage is good.

Additionally, 10 citizens in `citizens_creuses_sourds_nomades.json` are placed in non-settlement locations:
- `space_zone_desert_sismique`: 10 nomadic citizens
- `space_zone_dent_noire`: 1 citizen
- `space_zone_faille_khensi`: 1 citizen

This is intentional (nomads and hermits) and not a problem.

---

## 5. Orphan Check -- WARN

**14 orphan nodes** exist with zero links (neither source nor target anywhere). All 14 are proverbs in `lore_narratives.json`:

1. `narrative_proverbe_air_ment_pas`
2. `narrative_proverbe_construis_bas`
3. `narrative_proverbe_corps_calendrier`
4. `narrative_proverbe_cri_nom`
5. `narrative_proverbe_hamac`
6. `narrative_proverbe_mandla`
7. `narrative_proverbe_meurt_pas_seul`
8. `narrative_proverbe_pieds_savent`
9. `narrative_proverbe_quarante_deux_jours`
10. `narrative_proverbe_silence_charge`
11. `narrative_proverbe_sol_decide`
12. `narrative_proverbe_sol_vibre_toujours`
13. `narrative_proverbe_tu_entres`
14. `narrative_proverbe_zenzele`

These proverbs have no links connecting them to archipels, figures, or rivalries. Compare with the 14 proverbs that DO have links (e.g., `narrative_proverbe_sipho -> narrative_rivalite_predicteurs_ecouteurs`).

**Recommendation:** Add links from these orphan proverbs to their relevant archipels, figures, or themes. Each proverb's `properties.usage` field already indicates the relevant domain.

---

## 6. Schema Consistency Issues

### 6a. Missing node_type in things_world.json -- FAIL

All 66 nodes in `things_world.json` are missing the `node_type` field. They have a `type` field (e.g., `outil`, `instrument`, `equipement`, `materiau`, `aliment`, `artisanat`, `dispositif`) but no `node_type: "thing"` as required by the Mind schema.

Every other seed file correctly includes `node_type` on all nodes.

**Recommendation:** Add `"node_type": "thing"` to all 66 nodes in `things_world.json`.

### 6b. ID format inconsistency

- `things_world.json` uses colon-separated IDs: `thing:corde_encordement`
- All other files use underscore-separated IDs: `space_archipel_sud`, `actor_citoyen_bongiwe`

This is not necessarily wrong but could cause issues with parsers or query tools that split on specific delimiters.

**Recommendation:** Decide on one separator convention and apply it consistently. The colon format is compatible with Mind schema but should be documented as intentional.

### 6c. Property key inconsistency in citizen files

`citizens_creuses_sourds_nomades.json` uses different property keys than the other two citizen files:

| Key in sud_nord_ouest / nordest_est_centresud | Key in creuses_sourds_nomades |
|---|---|
| `archipel` | `archipel_origine` |
| `residence` | `lieu_residence` |
| `dialecte` | `dialecte_contact` |
| `marche` | (absent) |
| `trait_distinctif` | (absent) |
| (absent) | `surdite` |
| (absent) | `raison_isolement` |
| (absent) | `role_narratif` |
| (absent) | `routes_connues` |

**Recommendation:** Standardize to one set of property key names. The additional keys in `creuses_sourds_nomades` are domain-specific and acceptable, but the core keys (`archipel`/`archipel_origine`, `residence`/`lieu_residence`, `dialecte`/`dialecte_contact`) should use the same name across all files.

---

## 7. Statistics

### Totals

| Metric | Value |
|--------|-------|
| Total nodes (all files) | 401 |
| Total links (all files) | 871 |
| Average links per node | 2.17 |
| Unique broken target IDs | 37 |
| Duplicate node IDs | 21 |
| Orphan nodes | 14 |

### Nodes by type (corrected)

| Type | Count | Source files |
|------|-------|-------------|
| space | 107 | geo_surface, geo_vertical, geo_buildings |
| narrative | 96 | culture_clusters, lore_narratives |
| actor | 95 | lore_figures (18 legendaire), citizen files (77 citoyen) |
| thing (missing node_type) | 66 | things_world |
| moment | 37 | lore_figures (exploits + events), culture_clusters |

### Citizens by archipel

| Archipel | Name | Citizens |
|----------|------|----------|
| space_archipel_sud | Basses-Terres | 17 |
| space_archipel_nord | Froides | 15 |
| space_archipel_nord_est | Seches | 11 |
| space_archipel_centre_sud | Chaudes | 11 |
| space_archipel_ouest | Roulantes | 9 |
| space_archipel_est | Salines | 5 |
| space_archipel_sud_ouest | Creuses | 4 |
| space_village_sourds | Village des Sourds | 5 |
| nomadic | Desert / routes | ~10 |
| **Total** | | **~87** |

### Citizens by metier (all variants collapsed)

| Metier group | Count |
|---|---|
| cartographe | 18 |
| escalade / grimpeur / grimpeuse | 12 |
| ecouteur | 13 |
| survivaliste / specialiste_survie | 21 |
| mineur | 13 |
| leader | 9 |
| cuisinier | 10 |
| biologiste | 9 |
| speleologue / speleo | 9 |
| specialiste_roche | 7 |
| meteorologue | 5 |
| predicteur | 8 |
| specialiste_oceans | 5 |
| aeromaitre | 2 |
| geologue | 2 |
| explosifs / specialiste_explosifs | 2 |

(Note: many citizens have 2 metiers, so totals exceed citizen count.)

---

## 8. Priority Recommendations

### Critical (data loss risk)

1. **Fix 21 duplicate node IDs.** These will cause overwrites in the graph. Append archipel/location suffix to disambiguate.

2. **Add `node_type: "thing"` to all 66 nodes in things_world.json.** Without this field, graph ingestion may reject or misclassify these nodes.

### High (broken references)

3. **Create 3 guild nodes** (`narrative_guilde_lien`, `narrative_guilde_profondeurs`, `narrative_guilde_sens`). 76 links reference them.

4. **Create 14 metier nodes** (`thing_metier_ecouteur`, etc.) OR remove metier links from `citizens_nordest_est_centresud.json` and standardize on guild links. 48 links reference them.

5. **Create 7 novel character nodes** (`actor_citoyen_senzo`, `actor_citoyen_nandi`, etc.) OR remove the 16 links that reference them.

### Medium (consistency)

6. **Standardize property keys** across the three citizen files (`archipel` vs `archipel_origine`, `residence` vs `lieu_residence`, `dialecte` vs `dialecte_contact`).

7. **Standardize metier vocabulary** (pick one of `grimpeur`/`grimpeuse`/`specialiste_escalade`/`escalade`, etc.).

8. **Document or resolve brain seed cross-references.** The 90 links from `culture_clusters.json` to `contre_terre_base.json` nodes need explicit documentation that the loader merges both sources.

### Low (polish)

9. **Link 14 orphan proverbs** to their relevant themes, archipels, or figures.

10. **Add missing metiers** (cordiste, caravanier, tisserand) as citizen attributes where relevant.

11. **Consider adding more citizens** to Est (5) and Sud-Ouest (4) to balance population representation.

---

*Validation performed by reading all 10 seed files and 1 brain seed file, parsing JSON, and cross-referencing all node IDs and link endpoints programmatically.*
