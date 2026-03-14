# PATTERNS: Seismic Physics

**Module:** `universe/seismic_physics`
**Question:** Why is the seismic physics engine designed this way? What decisions, and why?

---

## P1: Tick-based magnitude cycles layered on Venezia's ngram physics

**Decision:** The seismic physics runs as a tick layer on top of the existing ngram narrative physics (energy/decay/tension from Venezia). Each tick (5 seconds world-time, matching Venezia's `GraphTickV1_2`), the seismic engine computes: (a) background magnitude for each zone, (b) tension accumulation toward discrete seismes, (c) tremens updates for each citizen. The seismic layer reads from and writes to the same graph as the narrative physics -- seismic events become narrative moments, and narrative energy feeds back into seismic tension.

**Why:** Contre-Terre is the 3rd Cities of Light universe. All three share the tick-based physics substrate. Venezia proved the architecture: `generation -> draw -> flow -> interaction -> backflow -> cooling -> completion -> rejection`. Seismic physics adds a domain-specific layer that uses the same energy/tension primitives but interprets them through geological mechanics. A seisme is a `moment` node that completes when accumulated tension exceeds threshold. The tremens is an energy field on citizen `actor` nodes that decays or intensifies based on zone frequency distance.

**What this prevents:** A separate, disconnected physics engine. The seismic system is not a parallel simulation -- it is a specialization of the same graph physics. When a seisme generates narrative energy, that energy flows through the same links and affects the same moments as any other narrative event.

---

## P2: Background vibration as constant -- magnitude 4 is silence

**Decision:** The world-level background magnitude is always 4-5. It never drops below 3. There is no stillness in this world. The physics engine initializes every zone with a baseline magnitude of 4 and a `background_vibration` property that never decays to zero. Citizens calibrated to this baseline perceive it as silence.

**Why:** In Damasio's *La Horde du Contrevent*, the wind blows permanently -- it is the condition of the world, not a weather event. Contre-Terre inverts the element (wind to earth) but preserves the principle: the seismic activity is constitutive, not episodic. A world that sometimes shakes is a world with earthquakes. A world that always shakes is Contre-Terre. The physics engine enforces this by clamping minimum magnitude at 3.0 for any zone, with surface zones at 4-5.

**Format reference (Venezia):**
```json
{
  "generation_rate": 0.08,
  "decay_rate": 0.05,
  "tension_threshold": 0.7,
  "max_energy": 1.0,
  "homeostasis_target": 0.3
}
```

Contre-Terre equivalent:
```json
{
  "background_magnitude": 4.0,
  "tension_accumulation_rate": 0.06,
  "seisme_threshold": 0.75,
  "max_magnitude": 11.0,
  "tremens_decay_rate": 0.02,
  "zone_frequency_bands": 8
}
```

---

## P3: Seismes as discrete events generated from accumulated tension

**Decision:** Seismes are not scheduled -- they are generated probabilistically when accumulated tectonic tension in a zone exceeds a threshold. The probability of a seisme increases exponentially as tension approaches 1.0. Once triggered, a seisme is a graph `moment` node with magnitude, duration, and type properties. The seisme drains tension from the zone (partially), produces narrative energy, and affects all citizens in the zone.

**Why:** Scheduled seismes would be predictable. Random seismes would be arbitrary. Tension-based generation means seismes emerge from accumulated physical state -- long quiet periods mean bigger eventual seismes (the silence-as-trap pattern from Chapter IV). The physics is honest: tension builds, and it will release. The only question is when and how violently.

**10 cataclysm types:**

| Type | Generation condition | Magnitude range |
|------|---------------------|-----------------|
| Seisme classique | Standard tension release | 5-9 |
| Bang (seismic acoustic) | Pressure differential in enclosed zones | 5-7 |
| Eruption volcanique | Thermal tension + depth > 4 | 7-9+ |
| Glissement de terrain | Prolonged silence (low tension release) | 5-8 |
| Geyser | Water + thermal in cavern zones | 4-6 |
| Tsunami souterrain | Water zones + seisme in adjacent zone | 6-8 |
| Coulee de boue | Surface/piedmont + seisme + water | 4-6 |
| Sables mouvants | Surface zones, sustained low magnitude | 3-5 |
| Effondrement | Cavern/faille zones, structural fatigue | 5-8 |
| Tempete | Surface atmospheric, linked to deep seismic | 4-7 |

---

## P4: The building 11 as looming systemic threat

**Decision:** The magnitude 11 is modeled as a global tension variable that increases monotonically across the simulation timeline. It is separate from per-zone tension -- it is the world-level accumulation that no local seisme can drain. The 11 tension feeds into predicteur tremens but is invisible to simulated instruments (sismographe nodes cannot read it). The building 11 manifests as: shortening intervals between deep precursors, intensifying predicteur tremens, and subtle frequency harmonics in deep zones.

**Why:** The magnitude 11 is the epistemological horizon of the novel. If instruments could detect it, the conflict between science and body dissolves. The physics engine must model something real (the tension exists in the simulation) that instruments cannot access (the sismographe query function does not include the global tension variable). Only predicteur citizens, whose tremens function includes the global tension as input, can sense it. The gap between what the simulation knows and what instruments report is structurally encoded, not narratively faked.

---

## P5: Tremens sensitivity spectrum across citizens

**Decision:** Each citizen has a natal frequency calibration (determined by birth zone) and a tremens sensitivity coefficient. The tremens intensity for a citizen in a given zone is: `tremens = sensitivity * frequency_distance(natal_zone, current_zone) * current_magnitude / baseline_magnitude`. Predicteur citizens have sensitivity > 1.0 (their bodies amplify the signal). Standard citizens have sensitivity ~0.3-0.5. Ecouteurs have sensitivity ~0.6-0.8. The tremens produces status effects: nausea (mild), vomiting (moderate), trembling (severe), hallucinations (extreme), incapacitation (critical).

**Why:** Not all citizens experience the world the same way. The tremens spectrum creates physiological diversity -- a citizen born in the volcanic interior would feel nothing descending to where the expedition suffers. Nandi's extreme tremens (born in the northeast archipelago, descending to the deep south) is the maximum possible distance on the frequency spectrum. Her suffering is not arbitrary -- it is the physics of being maximally displaced from her natal calibration.

---

## P6: How seismic state affects Contact quality

**Decision:** Contact (the tactile language) degrades under seismic stress through three mechanisms: (a) magnitude > 6 introduces physical noise -- hands shake, surfaces vibrate, signals mix with seismic tremor; (b) tremens above "severe" impairs fine motor control, reducing Contact vocabulary to basic survival signals; (c) temperature above threshold makes skin-to-skin contact painful (volcanic zones). The physics engine outputs a `contact_quality` modifier per citizen per tick, ranging from 1.0 (perfect) to 0.0 (impossible).

**Why:** The Contact system and the seismic system are not independent modules. The seismic activity is the ecological pressure that created Contact (speech is useless in a world that never stops rumbling), and it is also the force that degrades Contact under extreme conditions. This creates the central tragedy: the deeper the expedition goes, the more they need Contact (danger requires communication), and the harder Contact becomes (seismic stress degrades it). The physics engine must make this tradeoff quantifiable and continuous, not binary.

---

## OPEN DESIGN QUESTIONS

| Question | Impact | Priority |
|----------|--------|----------|
| Exact tick-to-world-time ratio for Contre-Terre (5s like Venezia, or different?) | Determines simulation granularity | High |
| How does the bioluminescence pulse integrate with tick physics? | Visual feedback of seismic state | Medium |
| Should the global 11 tension be visible to admin/narrator, or truly hidden? | Narrative tooling | Low |
| How does the seismic layer interact with citizen memory/trauma nodes? | Long-term citizen state | Medium |

---

*Created: 2026-03-13 -- Source: PATTERNS_Seismique.md, ALGORITHM_Seismique.md, Venezia tick_v1_2.py, nature_physics.yaml, constants.json*
