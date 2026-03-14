# IMPLEMENTATION: Seismic Physics

**Module:** `universe/seismic_physics`
**Question:** How does the seismic layer sit in the codebase? What are the code boundaries, data flows, and graph node types?

---

## I1: Architecture -- seismic layer atop ngram graph physics

The seismic physics engine is not a standalone simulation. It is a domain-specific extension of the Venezia-derived `GraphTickV1_2` narrative physics. The standard tick runs 8 phases (generation through rejection). The seismic extension adds 5 phases (9 through 13) that execute after the narrative phases complete. Both layers operate on the same FalkorDB graph -- seismic events become narrative moments, narrative energy feeds back into seismic tension.

```
GraphTickV1_2 (Venezia base)
│
├── Phases 1-8: narrative physics (energy, tension, decay, completion)
│   └── Operates on: actor, moment, narrative, space, thing nodes
│
└── Phases 9-13: seismic extension (Contre-Terre)
    ├── 9:  seismic_tension_accumulation (per zone)
    ├── 10: seismic_event_generation (probabilistic)
    ├── 11: seismic_magnitude_propagation (zone + adjacent)
    ├── 12: tremens_update_per_citizen (per actor)
    └── 13: contact_quality_computation (per actor)
```

The seismic phases read and write the same graph properties that the narrative phases use. A seisme event is a `moment` node. A zone is a `space` node. A citizen is an `actor` node. No custom node types -- the Mind Protocol schema (5 node types + 1 link type) covers everything.

---

## I2: FalkorDB node types and properties

### Space nodes (zones)

Each geological zone is a `space` node with seismic properties:

| Property | Type | Description |
|----------|------|-------------|
| `node_type` | enum | `space` |
| `type` | string | Zone subtype: `surface_desert`, `piedmont`, `cavern_village`, `faille`, `deep_cavern`, `volcanic`, `interior`, `grotte_finale` |
| `frequency_band` | int (1-8) | Spectral signature band |
| `background_magnitude` | float | Baseline magnitude (always >= 3.0) |
| `current_magnitude` | float | Current tick magnitude (background + active seismes) |
| `tension` | float (0.0-1.0) | Accumulated tectonic tension |
| `depth_factor` | float | Depth multiplier for tension accumulation |
| `temperature` | float | Zone temperature (increases with depth) |
| `has_bioluminescence` | bool | Whether filaments are present |
| `bioluminescence_intensity` | float | Current pulse intensity |
| `dampening_factor` | float | Engineering reduction (village = 0.6, others = 1.0) |
| `lateral_amplification` | float | Geometry amplification (faille = 1.5, others = 1.0) |
| `has_water` | bool | Enables tsunami/geyser cataclysm types |
| `is_volcanic` | bool | Enables eruption type |
| `is_enclosed` | bool | Enables effondrement/bang types |

### Actor nodes (citizens)

Each citizen is an `actor` node with tremens-related properties:

| Property | Type | Description |
|----------|------|-------------|
| `node_type` | enum | `actor` |
| `natal_zone` | ref | Link to birth zone space node |
| `sensitivity` | float | Tremens sensitivity coefficient (predicteur > 1.0, standard 0.3-0.5) |
| `is_predicteur` | bool | Whether citizen reads unreleased tension |
| `tremens` | float (0.0-1.0) | Current tremens intensity |
| `tremens_status` | string | Classified status: imperceptible/mild/moderate/severe/extreme/critical |
| `contact_quality` | float (0.0-1.0) | Current Contact quality modifier |
| `ticks_in_current_zone` | int | Adaptation counter |
| `total_tremens_exposure` | float | Cumulative fatigue tracker |

### Moment nodes (seismes)

Each seisme event is a `moment` node:

| Property | Type | Description |
|----------|------|-------------|
| `node_type` | enum | `moment` |
| `type` | string | Cataclysm subtype (seisme, bang, eruption, glissement, geyser, tsunami, coulee_boue, sables_mouvants, effondrement, tempete) |
| `magnitude` | float | Event magnitude (5.0-9.5 for generated; 11.0 for terminal) |
| `duration_ticks` | int | How many ticks the event remains active |
| `zone` | ref | Link to the zone space node where it originated |
| `energy` | float | Narrative energy produced (feeds back into standard tick phases) |

### Global state (thing node)

The building 11 state is a `thing` node:

| Property | Type | Description |
|----------|------|-------------|
| `node_type` | enum | `thing` |
| `type` | string | `global_seismic_state` |
| `tension_11` | float (0.0-1.0) | Monotonically increasing global tension |
| `global_11_rate` | float | Base accumulation rate per tick |

---

## I3: Tick processing pipeline

```
TICK START
│
├── [Venezia phases 1-8 execute on narrative graph]
│
├── Phase 9: FOR each space WHERE type IN seismic_zone_types:
│       UPDATE tension += rate * depth_factor
│       UPDATE global_thing.tension_11 += global_rate
│
├── Phase 10: FOR each space WHERE tension > threshold:
│       COMPUTE probability
│       IF triggered: CREATE moment node (seisme)
│       UPDATE space.tension (drain)
│
├── Phase 11: FOR each active moment WHERE type IN cataclysm_types:
│       UPDATE origin space.current_magnitude
│       TRAVERSE adjacent spaces: UPDATE propagated magnitude
│       UPDATE bioluminescence_intensity
│
├── Phase 12: FOR each actor WHERE alive = true:
│       COMPUTE frequency_distance(actor.natal_zone, current_space)
│       COMPUTE tremens (sensitivity * freq_dist * magnitude / baseline)
│       IF is_predicteur: ADD tension_signal
│       APPLY adaptation decay, cumulative fatigue
│       CLASSIFY tremens_status
│
├── Phase 13: FOR each actor WHERE alive = true:
│       COMPUTE contact_quality (seismic_noise + tremens + temp_pain)
│       UPDATE actor.contact_quality
│
TICK END
```

---

## I4: Integration with ngram narrative physics

The seismic and narrative layers share state through three feedback loops:

**Seismic -> Narrative:** When a seisme moment is created (phase 10), it enters the narrative graph as a moment node with energy. Phases 1-8 of the NEXT tick pick it up: it flows through moment_flow, interacts with adjacent moments, produces narrative backflow. A seisme that kills a citizen is both a seismic event and a narrative moment -- one node, two physics layers reading it.

**Narrative -> Seismic:** High narrative tension (from character conflict, death events, mission decisions) feeds into zone tension through backflow links. A zone where a citizen has just died accumulates seismic tension slightly faster -- the narrative physics considers it a high-energy area, and that energy translates to seismic potential.

**Shared constants:** Both layers reference the same `constants.json` configuration. The Venezia defaults (`generation_rate`, `decay_rate`, `tension_threshold`) have Contre-Terre equivalents (`background_magnitude`, `tension_accumulation_rate`, `seisme_threshold`). These are tuned together, not independently.

---

## I5: File locations (projected)

```
.mind/mind/physics/
├── tick_v1_2.py              # Base tick (Venezia) -- phases 1-8
├── tick_seismic_extension.py # Seismic phases 9-13 (TO BUILD)
├── constants.json            # Shared constants (both layers)
└── seismic/
    ├── tension.py            # Phase 9: tension accumulation
    ├── events.py             # Phase 10: seisme generation
    ├── propagation.py        # Phase 11: magnitude propagation
    ├── tremens.py            # Phase 12: tremens per citizen
    └── contact_quality.py    # Phase 13: Contact quality
```

**Status:** The seismic extension is DESIGNED, not yet implemented. The tick architecture and node schema are defined. The constants exist in draft. The code files are projected -- they will be built when the engine moves from DESIGNING to IMPLEMENTING.

---

*Created: 2026-03-13 -- Source: ALGORITHM_Seismic_Physics.md, PATTERNS_Seismic_Physics.md, tick_v1_2.py architecture, FalkorDB schema*
