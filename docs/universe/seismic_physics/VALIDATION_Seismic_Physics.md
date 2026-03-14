# VALIDATION: Seismic Physics

**Module:** `universe/seismic_physics`
**Question:** What invariants must the seismic physics engine never violate?

---

## Absolute invariants

These rules are structural. Violating them means the engine is broken, not miscalibrated.

### V1: Background magnitude never drops below 3.0

**Rule:** No zone, at any tick, may have `current_magnitude < 3.0`. The world never stops trembling. The engine initializes every zone at 4.0 and clamps any decay at 3.0. There is no stillness in Contre-Terre -- not in the desert, not in the caverns, not in the volcanic interior. The only exception is the post-detonation state (after the magnitude 11 event fires), which is terminal and outside normal tick processing.

**Verification:** Assert `zone.current_magnitude >= 3.0` at the end of every tick for every zone. If any zone reads below 3.0, the tension accumulation or magnitude propagation phase has a bug.

**Why this matters:** Background vibration is constitutive, not episodic. If the engine produces silence, it is simulating Earth, not Contre-Terre.

---

### V2: The magnitude 11 is never measurable by instruments

**Rule:** The `global_11_tension` variable is excluded from every instrument query function. Sismographe nodes read `zone.current_magnitude` and `zone.frequency_band`. They never read `global_11_tension`. No instrument node, no measurement function, no reporting system may access the global 11 state. Only predicteur citizens -- through their tremens function, which includes `global_11_tension` as input -- can sense it.

**Verification:** Audit every query path available to instrument nodes. None may reference `global_11_tension`. The variable exists in the physics state. It does not exist in the instrument API.

**Why this matters:** The epistemological gap between instruments and bodies IS the central conflict. If an instrument detects the 11, the Scale of Capitulation collapses. The gap must be structurally encoded, not narratively enforced.

---

### V3: Tremens severity correlates with natal-vs-current frequency distance

**Rule:** A citizen in their natal frequency zone has tremens approaching zero. A citizen maximally displaced from their natal frequency band has maximum tremens. The function `frequency_distance(natal_zone, current_zone)` is the primary input to tremens intensity. Two citizens standing in the same zone at the same tick MUST produce different tremens values if their natal zones differ. Tremens is personal, not environmental.

**Verification:** For any two citizens with different natal zones, assert `citizen_A.tremens != citizen_B.tremens` when both are in the same zone (unless both happen to have identical sensitivity coefficients and symmetrical frequency distances, which is astronomically unlikely). For any citizen in their natal zone, assert `tremens < 0.1`.

**Why this matters:** If tremens were uniform, geography would not be personal. Nandi's suffering in the deep south is not generic altitude sickness -- it is the specific physics of being born in high-frequency archipelago cliffs and descending into low-frequency volcanic interior.

---

### V4: Seismes drain zone tension partially, never fully

**Rule:** When a seisme fires, it drains tension from its zone by `drain_factor * (magnitude / max_magnitude)`. But `zone.tension` must never drop below 0.1 after a drain. Tension never resets to zero. The world always has potential energy. A seisme is a release, not a reset.

**Verification:** Assert `zone.tension >= 0.1` after every seisme event drain. If tension reaches 0.0, the zone would need to re-accumulate from nothing, producing unrealistically long quiet periods.

---

### V5: The global 11 tension increases monotonically

**Rule:** `global_11_tension` only ever increases. No seisme event, no narrative moment, no tick phase may decrease it. It is the irreversible approach of the world's terminal event. Local seismes drain local tension -- the global 11 is untouched. The detonation is the only event that resolves it, and that event is terminal.

**Verification:** Assert `global_11_tension(tick_N) >= global_11_tension(tick_N-1)` for every consecutive tick pair. Any decrease is a critical bug.

---

### V6: Temperature increases with depth

**Rule:** Zone temperature is a monotonically increasing function of depth. Surface zones are tolerable. Volcanic zones exceed skin tolerance. Interior zones approach temperatures where Contact becomes physically painful and bioluminescence ceases. The engine must never produce a deep zone cooler than a shallow zone in the same geological column.

**Verification:** For any two zones where `zone_A.depth > zone_B.depth`, assert `zone_A.temperature >= zone_B.temperature`.

---

## Strong invariants

Important constraints that may have rare justified exceptions.

### V7: Predicteur citizens sense seismes before instruments register them

**Rule:** For any seisme event of magnitude 6+, the predicteur tremens pulse must fire during the tension accumulation phase (phase 9), BEFORE the seisme event generation phase (phase 10). Instruments read `current_magnitude`, which only updates in phase 11 (propagation). Predicteurs read `zone.tension`, which updates in phase 9. The ordering of tick phases guarantees this -- if the phases run in order, the invariant holds automatically.

**Verification:** Confirm tick phase ordering: 9 (tension) before 10 (event) before 11 (propagation). Predicteur tremens computation must occur after phase 9 and before phase 11.

---

### V8: Each frequency zone has a distinct spectral signature

**Rule:** No two zones may share the same `frequency_band` value unless they are geologically identical (e.g., two surface desert tiles). Zone transitions must produce a measurable change in frequency band, which triggers tremens recalibration in traversing citizens. The 8 frequency bands (1 through 8) map to the 8 geological layers from surface to grotte finale.

**Verification:** For any zone transition event, assert `zone_A.frequency_band != zone_B.frequency_band` (unless same geological type). Assert that every geological layer type maps to exactly one frequency band.

---

### V9: Bioluminescence intensity tracks magnitude

**Rule:** Bioluminescent filaments pulse at an intensity proportional to `current_magnitude / 4.0`. At background magnitude (4.0), they pulse at baseline. During a seisme, they flash brighter. In zones where temperature exceeds the bioluminescence survival threshold, intensity decays to zero. The filaments are a visible witness to seismic state -- they never pulse at an arbitrary rhythm disconnected from physics.

---

### V10: Contact quality is computed per citizen per tick

**Rule:** The `contact_quality` modifier is not a zone-wide value. It is per-citizen, because it depends on that citizen's tremens (personal) and position (zone magnitude). Two citizens in the same zone have different Contact quality if their tremens differs. The engine must compute Contact quality after tremens update (phase 12) and output it as phase 13.

---

## Validation checklist for engine integrity

Before considering the seismic engine operational:

- [ ] No zone magnitude drops below 3.0 across 1000 ticks (V1)
- [ ] `global_11_tension` is absent from all instrument query functions (V2)
- [ ] Citizens with different natal zones produce different tremens in the same zone (V3)
- [ ] Zone tension never drops below 0.1 after seisme drain (V4)
- [ ] `global_11_tension` is strictly non-decreasing across all ticks (V5)
- [ ] Temperature is monotonically increasing with depth (V6)
- [ ] Predicteur tremens fires before instrument magnitude update (V7)
- [ ] Zone transitions produce frequency band changes (V8)
- [ ] Bioluminescence tracks magnitude, not arbitrary rhythm (V9)
- [ ] Contact quality computed per citizen, not per zone (V10)

---

*Created: 2026-03-13 -- Source: VALIDATION_Seismique.md, ALGORITHM_Seismic_Physics.md, PATTERNS_Seismic_Physics.md*
