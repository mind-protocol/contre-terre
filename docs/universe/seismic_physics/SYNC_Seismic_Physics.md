# SYNC: Seismic Physics

```
LAST_UPDATED: 2026-03-13
UPDATED_BY: Claude Opus 4.6 (agent, subtype: voice)
```

---

## MATURITY

**STATUS: DESIGNING**

### What is canonical (from worldbuilding source):

- The permanent seismic background (magnitude 4-5 = silence of this world) -- established in all 8 chapters
- The tremens system: natal frequency calibration, frequency distance, symptom ladder -- described in detail across all chapters
- The Echelle de Capitulation (sismographes -> ecouteurs -> predicteurs) -- embodied by Sihle/Enama/Nandi
- The building 11 as horizon event: monotonically increasing, never measured by instruments, felt only by predicteurs
- 10 cataclysm types with distinct mechanics (seismes, bangs, eruptions, glissements, geysers, tsunamis, coulees, sables, effondrements, tempetes)
- Bioluminescence pulsing at magnitude 4, degrading with depth/temperature
- The micro-silence as pre-seisme signal (absence = inverted signal for glissements)
- Frequency zones with distinct spectral signatures from surface to grotte finale
- Architecture as seismic response (no right angles, elastic suspension, liquid food, anchored objects)
- Contact degradation under seismic stress (noise + tremens + temperature)

### What is being designed (this doc chain):

- Tick-based simulation architecture extending Venezia's GraphTickV1_2
- 5 seismic sub-phases (tension accumulation, event generation, magnitude propagation, tremens update, contact quality)
- Data structures for zone seismic state, citizen tremens state, seisme moment nodes
- Constants file for Contre-Terre physics parameters
- Integration points with narrative physics (seisme moments as narrative moments)
- Code organization under `runtime/physics/seismic/`
- The building 11 algorithm (monotonic accumulation with acceleration and precursors)

### What is proposed (not yet decided):

- Exact tick-to-world-time ratio for Contre-Terre (currently assumed 5s like Venezia)
- Bioluminescence as tick-level visual feedback (intensity formula exists, rendering unclear)
- Whether global 11 tension should be visible to admin/narrator tooling
- Citizen memory/trauma integration with tremens exposure history
- Multiplayer/multi-citizen tremens interaction (does one citizen's tremens affect nearby citizens?)

---

## RELATIONSHIP TO WORLDBUILDING DOCS

This module (`universe/seismic_physics`) is the **simulation implementation** of what `worldbuilding/seismique` describes **narratively**. The worldbuilding docs define what the seismic system means for the novel. This doc chain defines how to simulate it as a tick-based physics engine in the Cities of Light universe.

| Aspect | worldbuilding/seismique | universe/seismic_physics |
|--------|------------------------|--------------------------|
| Perspective | Narrative, literary | Computational, simulational |
| Magnitude | What it means to characters | How it is computed per tick |
| Tremens | What it feels like in prose | How it is calculated per citizen |
| Seismes | How they are described in text | How they are generated from tension |
| The 11 | The novel's epistemological horizon | A monotonic variable approaching threshold |
| Contact | How seismic stress degrades language | A `contact_quality` float computed per tick |

---

## SOURCE MATERIAL CALIBRATION

The novel's text is the canonical reference for engine calibration. The physics engine must produce states that match these narrative moments:

| Chapter | Seismic event | Engine must produce |
|---------|--------------|-------------------|
| I | Background 4-5, Nandi's first pressentiment | Steady baseline, predicteur pre-signal |
| II | Magnitude 7 seisme (8 seconds), first tremens vomiting | Tension spike, event generation, tremens escalation |
| III | Village dampening (40%), old man's shortening intervals | Dampening factor, global 11 precursors |
| IV | Seismic silence -> glissement, Senzo killed | Tension accumulation without release, glissement type selection |
| V | Deep cavern magnitude 6-8, inundation kills Jabu, effondrement kills Sihle | Multi-type cataclysm generation in deep zones |
| VI | Volcanic 7-9+, heat-deformed waves, Contact painful | Temperature gradient, volcanic zone properties |
| VII | Interior 8-9+ quasi-permanent, boyau collapse | Extreme sustained magnitude, effondrement in enclosed zone |
| VIII | Full spectrum escalation to 11, detonation | Global 11 reaching threshold, terminal event |

---

## DOCUMENTATION CHAIN STATUS

| Document | Status | Content |
|----------|--------|---------|
| OBJECTIVES | Complete | 5 ranked objectives with hierarchy and tradeoffs |
| PATTERNS | Complete | 6 design decisions with rationale, Venezia constants reference |
| BEHAVIORS | Complete | 6 observable effects, escalation table, recurring motifs |
| ALGORITHM | Complete | Pseudocode for all 5 tick phases, building 11, frequency model |
| VALIDATION | Complete | 12 invariants (5 absolute, 4 strong, 3 coherence) + per-tick checklist |
| IMPLEMENTATION | Complete | Node schema, code organization, cross-module dependencies, constants |
| HEALTH | Complete | 8 health checks with healthy/degrading indicators, health matrix |
| SYNC | Complete | This file |

---

## DEPENDENCIES

| Module | Relationship | Status |
|--------|-------------|--------|
| `universe/narrative_engine` | Seismic moments feed into narrative physics | DESIGNING (no docs yet) |
| `universe/citizen_model` | Citizen properties (natal zone, sensitivity) read by tremens | DESIGNING (no docs yet) |
| `universe/contact_engine` | Reads contact_quality output from seismic physics | DESIGNING (no docs yet) |
| `universe/world_geography` | Zone layout, adjacency, properties | DESIGNING (no docs yet) |
| `worldbuilding/seismique` | Narrative source material for all seismic mechanics | CANONICAL (8 files, 13 invariants) |
| Venezia `GraphTickV1_2` | Base tick architecture (phases 1-8) | CANONICAL |

---

## OPEN QUESTIONS

| Question | Impact | Priority |
|----------|--------|----------|
| Tick rate for Contre-Terre (5s? different?) | Determines all time-dependent computations | High |
| How to seed initial zone tension for narrative coherence | First seismes must happen at the right story moment | High |
| Should seisme events be deterministic given seed (reproducibility)? | Testing, debugging, narrative design | Medium |
| How does the post-detonation silence work in the tick engine? | Final sequence behavior | Low (needed at end) |
| Multi-citizen tremens interaction | Whether proximity to a trembling citizen affects others | Low |

---

## RISKS

| Risk | Severity | Mitigation |
|------|----------|------------|
| Seismic physics disconnected from narrative physics | High | V4 invariant: seismes MUST create moment nodes. Integration test required. |
| Tremens computation too uniform across citizens | Medium | Test with citizens of different natal zones and sensitivities. Verify diversity. |
| Building 11 accumulation rate wrong (detonation too early/late) | High | Parameterize rate. Test with simulation of full novel timeline. Adjust constants. |
| Cataclysm types not diverse enough in practice | Medium | Log type distribution over simulation runs. Adjust weights if one type dominates. |
| Contact quality formula too aggressive | Medium | Test with representative magnitude/tremens ranges. Calibrate against narrative. |

---

## HANDOFF

### For the next agent (implementation)

**Recommended subtype:** groundwork (implementation)

**Context to load:**
- This full doc chain (8 files)
- `docs/worldbuilding/seismique/ALGORITHM_Seismique.md` (narrative mechanics to match)
- Venezia `tick_v1_2.py` and `tick_v1_2_types.py` (base architecture to extend)
- Venezia `nature_physics.yaml` (link type vocabulary for seisme moments)

**First implementation steps:**
1. Create `seismic_constants.py` from the constants in IMPLEMENTATION_Seismic_Physics.md
2. Create `seismic_tick.py` with the 5 sub-phases as stubs
3. Implement phase 9 (tension accumulation) and phase 10 (event generation) first
4. Test with a minimal zone graph (3 zones, surface/cavern/volcanic) and verify tension/seisme/drain cycle
5. Then add tremens (phase 12) and contact quality (phase 13)

### For keeper agent (validation)

The 12 invariants are defined. When code exists, write automated tests that assert every invariant across 1000+ tick runs. Pay special attention to V2 (predicteur tremens always positive), V3 (global 11 monotonic), and V6 (instruments cannot read global 11).

### For the human (Nicolas)

The novel's seismic events are the ground truth. If the engine produces behavior inconsistent with chapters I-VIII, the engine is wrong, not the novel. This doc chain translates the literary seismic system into Cities of Light simulation architecture. Key questions for you: tick rate (5s?), whether the building 11 should be visible in admin tools, and whether the tremens sensitivity values feel right for the narrative.

---

*Created: 2026-03-13*
