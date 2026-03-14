# BEHAVIORS: Seismic Physics

**Module:** `universe/seismic_physics`
**Question:** What are the observable effects of the seismic physics engine on citizens, structures, and narrative?

---

## Principle: The engine produces state; citizens experience consequences

The seismic physics engine does not "describe" earthquakes. It produces magnitude values, frequency spectra, and tension levels per zone per tick. Citizens react to these values through their tremens function, their Contact quality modifier, and their physical state. The engine never tells a citizen "you are in an earthquake" -- it sets magnitude to 7.2 in their zone, and the citizen's body responds according to its calibration.

---

## B1: Citizens react to seismes through tremens

**Observable effect:** When a seisme event fires in a zone (magnitude 5+), every citizen in that zone receives a tremens pulse proportional to the seisme magnitude and their sensitivity coefficient. A predicteur citizen receives the pulse BEFORE the seisme event resolves (their tremens function reads the pre-release tension, not the release itself). Standard citizens react during or after.

**Sequence per seisme event:**
1. Tension accumulates in zone (invisible to most citizens)
2. Predicteur citizens experience pre-symptom tremens (nausea, "frequency inflection")
3. Ecouteur citizens sense the imminent event (trained perception, seconds before)
4. Seisme event fires -- magnitude applied to zone
5. All citizens in zone receive impact: physical displacement, Contact disruption
6. Post-seismic tremens: residual vertigo, recalibration period
7. Zone tension partially drains; bioluminescence flashes then resettles

**Tremens severity ladder:**
- Magnitude 5-6: salivation, mild discomfort (noticed only by sensitives)
- Magnitude 7: vomiting, jaw clenching, blurred vision
- Magnitude 8: uncontrollable trembling, burst capillaries, falls
- Magnitude 9+: hallucinations, partial incapacitation, body-as-seismograph

---

## B2: Tremens-sensitive citizens predict events

**Observable effect:** Predicteur citizens (sensitivity > 1.0) produce tremens responses to tension that has not yet released as a seisme. Their bodies read the unreleased tension variable directly. This means they experience nausea, frequency dissonance, and physical distress BEFORE the event that causes it. The physics engine computes predicteur tremens from `zone_tension + global_11_tension`, not from `current_magnitude`.

**Behavioral pattern:**
- Predicteur tremens intensifies over minutes/hours before a seisme
- The tremens is physically indistinguishable from illness (vomiting, shaking)
- No instrument in the simulation can correlate the tremens to an upcoming event
- After the seisme, the predicteur's tremens partially resolves (tension drained)
- For the building 11: predicteur tremens intensifies monotonically because the global tension never drains

---

## B3: Contact degrades during high magnitude

**Observable effect:** The `contact_quality` modifier drops as seismic magnitude increases. At magnitude 4-5 (background), Contact operates at full quality. At magnitude 7, Contact vocabulary shrinks to survival signals -- fine gestural grammar becomes impossible when hands shake and surfaces vibrate. At magnitude 8+, Contact is reduced to grip-or-release binary. In volcanic zones where temperature exceeds skin tolerance, Contact becomes physically painful (burns).

**Degradation curve:**
| Zone magnitude | Contact quality | Available vocabulary |
|---------------|----------------|---------------------|
| 4-5 | 1.0 | Full grammar, all 5 modes |
| 6 | 0.8 | Standard grammar, reduced nuance |
| 7 | 0.5 | Survival signals, basic verbs, crampes replace verrous |
| 8 | 0.2 | Grip/release, directional pushes |
| 9+ | 0.05 | Binary: alive/dead, hold/let go |

---

## B4: Buildings and structures affected by seismic state

**Observable effect:** Structures in the world have a `structural_integrity` value that decreases with each seisme event proportional to magnitude. Architecture designed for seismic zones (no right angles, elastic suspension, deep anchoring) degrades slowly. Rigid structures or improvised shelters degrade fast. When structural integrity reaches zero, the structure collapses (effondrement event).

**Zone-specific structural behavior:**
- Surface (desert): sand absorbs some energy, structures rare but resilient
- Piedmont: basalt rock transmits energy rigidly -- structures must be anchored deep
- Caverns: village-style dampening reduces effective magnitude by 40%, but only in engineered zones
- Faille: lateral seismes stress structures from the side (compression), not just vertically
- Deep volcanic: no permanent structures survive; only passage geometry matters

---

## B5: Migration patterns driven by seismic escalation

**Observable effect:** As the simulation timeline advances and the building 11 increases global tension, citizens in deep zones experience increasing seisme frequency and tremens severity. Citizens with low tremens sensitivity may not notice until seismes become destructive. Citizens with high sensitivity (predicteurs) begin avoiding deep zones or signaling distress earlier. The physics engine does not enforce migration -- it produces the conditions that make staying in deep zones increasingly costly.

**Escalation by simulation phase (mapped to novel chapters):**

| Phase | Background magnitude | Seisme frequency | Tremens baseline | Citizen behavior |
|-------|---------------------|-----------------|-----------------|-----------------|
| I (surface) | 4-5 | Rare | Imperceptible | Normal life |
| II (transition) | 5-6 | Occasional | First symptoms | Alert, cautious |
| III (cavern) | 4 dampened | Low (engineered) | Relief | False security |
| IV (faille) | 5-7 | Frequent lateral | "Eating from inside" | First death, fear |
| V (deep cavern) | 6-8 | Multiple | Near-incapacitation | Survival mode |
| VI (volcanic) | 7-9 | Continuous | Bone pain | Desperate |
| VII (interior) | 8-9+ | Precursors | Hallucinations | Last survivors |
| VIII (grotte) | 9-11 | The detonation | Body IS seisme | Terminal |

---

## B6: Bioluminescence as seismic state witness

**Observable effect:** Bioluminescent filaments in underground zones pulse at the background magnitude frequency (magnitude 4). When magnitude changes (seisme event), the filaments flash brighter, then resettle. They react to citizen touch (intensify). In deep/hot zones, they degrade and eventually disappear -- even life adapted to permanent trembling has limits.

**Tick behavior:**
- Each tick: bioluminescence intensity = `baseline_pulse * (current_magnitude / 4.0)`
- Seisme event: flash to `intensity * magnitude_ratio` for 2-3 ticks, then decay
- Touch: local intensification for 1 tick, immediate area
- Depth > volcanic threshold: intensity degrades to zero over ~50 ticks

---

## Recurring motifs produced by the engine

### The micro-silence
Before high-magnitude seismes, the engine produces a 1-2 tick window where background vibration drops slightly. This is the tension "holding its breath" before release. Predicteur citizens feel this as a specific tremens signature. The micro-silence is not scripted -- it emerges from the tension-to-release mechanics.

### The post-seismic recalibration
After a seisme drains zone tension, citizen tremens enters a "residual vertigo" state that decays over 10-20 ticks. This recalibration period shortens with repeated exposure (adaptation) but never reaches zero (the body does not fully adapt when descent is faster than recalibration).

### The instrument gap
Sismographe instruments read `current_magnitude` and `zone_frequency`. They cannot read `zone_tension` (unreleased) or `global_11_tension`. Every tick, there is a gap between what instruments report and what predicteur bodies feel. This gap widens as the building 11 intensifies.

---

*Created: 2026-03-13 -- Source: BEHAVIORS_Seismique.md, ALGORITHM_Seismique.md, tick_v1_2_types.py, Venezia tick architecture*
