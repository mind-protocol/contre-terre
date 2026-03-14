# SYNC — Contact Engine

> Current state. Where we are. What exists. What's next.

```
LAST_UPDATED: 2026-03-13
UPDATED_BY: Claude Opus 4.6 (agent)
STATUS: DESIGNING
```

---

## Maturity

STATUS: DESIGNING

### What's Canonical (from the novel)

The following elements are established in the written chapters (I-VIII) and are non-negotiable:

- **5 modes of Contact** -- arm locks, shoulder pressure, codified grips, tactile identity, regional dialect. Fully documented in `ALGORITHM_Contact.md`. Used consistently across all 8 chapters.
- **Body zones as semantic registers** -- shoulder (public) to palm (intimate) to feet (world). Zone grammar is stable and enforced in the text.
- **Idiolecte de paire** -- pair-specific vocabulary between characters. 5 pair idiolectes documented in `PERSONNAGES.md` (Senzo/Nandi, Thabo/Inyoni, Enama/Nandi, Sihle/Enama, Jabu/group).
- **Vocabulary death on character departure** -- each death destroys specific gestures. Documented per character through Ch. IV-VIII. The linguistic impoverishment arc is the novel's central mechanic.
- **Contact-corde** -- 2-dimensional rope communication. Vocabulary invented in real-time (Ch. IV). Documented with full signal table.
- **Contact-monde** -- citizen-to-environment Contact through feet and hands. Established in Ch. I (Nandi's bare feet), Ch. II-III (Enama's hands on walls), Ch. III (village extensions).
- **Contact-fantome** -- phantom Contact from dead citizens under extreme stress. 6 specific manifestations documented for Ch. VIII with exact tactile signatures.
- **The Geste Inconnu** -- seismic synchronization tool transmitted from the old woman to Nandi (Ch. III), resolved in Ch. VIII as the Charge calibration key. RESOLVED.
- **Seismic degradation curve** -- mode availability decreases with magnitude. Degradation thresholds defined.
- **Dialect variation** -- northeast archipelagos (sharp, brief) vs southern desert (slow, ample) vs underground village (3-finger high-resolution). Friction mechanics established.

### What's Being Designed (engine-specific)

- **Data structures** -- ContactGesture, ContactUtterance, ContactCordeGesture structs defined in ALGORITHM. Need implementation.
- **Processing pipeline** -- 6-step pipeline (proximity, degradation, zone access, pattern matching, recipient parsing, idiolecte update) specified in ALGORITHM. Not yet coded.
- **Crystallization algorithm** -- Threshold = 7, decay factor = 0.95, extinction threshold defined. Need implementation and calibration through testing.
- **Tick-based processing model** -- Defined in IMPLEMENTATION. Ordering constraints specified. Not yet coded.
- **Graph integration** -- Three mutation types (LINK_UPDATE, LINK_DELETE, NODE_UPDATE) defined. Need implementation against actual graph store.
- **Phantom generator** -- Trigger conditions and signature reconstruction specified. Need implementation.
- **Health metrics** -- Contact vitality, vocab growth/death rates, dialect friction, degradation checks defined in HEALTH. Need instrumentation.

### What's Being Designed (new — semantic translation layer)

- **Contact semantic translation** -- Arrivant (external visitor) speech is not filtered. It is mapped via embeddings to the nearest concept in the citizen's brain graph (currently 347 nodes). "Facebook" → "village/archipel". "iPhone" → "instrument/sismographe". The Contact vocabulary IS the graph of citizen brain nodes. This layer sits BEFORE the Contact Engine processes the input — it translates external speech into CT concepts so the citizen receives coherent input in their own vocabulary. Designed in `PATTERNS_Experience_Design.md` P9, needs implementation spec.
- **Arrivant terminology** -- External visitors are "arrivants" (arrivals from places where the ground is still), not "players" or "humans". Citizens don't know what a "player" is. The Contact Engine must use "arrivant" in all citizen-facing contexts.

### What's Proposed (not yet designed)

- **Contact learning curves** -- How quickly a new citizen acquires vocabulary from established ones. Behavior described in BEHAVIORS (B3) but no algorithm specified.
- **Social cost system** -- Zone violations emit cost events, but the cost propagation model is not defined. What happens when a citizen repeatedly violates zone norms?
- **Contact-monde vocabulary depth** -- How does a citizen's Contact-monde vocabulary grow? Through exposure? Through something analogous to pair crystallization but with the environment?
- **Voice transgression processing** -- Voice events as rule-breaking acts are described in PATTERNS (P2) but not algorithmically specified.

---

## Documentation Chain Status

| File | Status | Notes |
|------|--------|-------|
| OBJECTIVES | COMPLETE | 5 ranked objectives, tradeoffs table |
| PATTERNS | COMPLETE | 8 design decisions, all sourced |
| BEHAVIORS | COMPLETE | 8 observable effects, with novel examples |
| ALGORITHM | COMPLETE | 8 sections: data structures, pipeline, idiolecte evolution, death cascade, Contact-monde, Contact-corde, Contact-fantome |
| VALIDATION | COMPLETE | 10 invariants: structural, relational, processing |
| IMPLEMENTATION | COMPLETE | Architecture, 5 components, tick model, graph integration |
| HEALTH | COMPLETE | 6 health checks: vitality, vocab rates, friction, degradation, phantom, departure |
| SYNC | COMPLETE | This file |

---

## Dependencies on Other Modules

| Module | Dependency | Direction |
|--------|-----------|-----------|
| `worldbuilding/seismique` | Seismic magnitude data for degradation | Contact reads |
| `worldbuilding/geographie` | Zone-based dialect definitions | Contact reads |
| `narration/personnages` | Citizen identities, relationships, departure events | Contact reads + writes |
| `narration/structure` | Chapter-level narrative state (who is alive, where) | Contact reads |

---

## Handoff

**For next agent (groundwork):** The documentation chain is complete. Implementation can begin. Start with the Gesture Processor and Vocabulary Store -- these are the core. The Phantom Generator can wait until the basic Contact pipeline works. Test against the novel's documented interactions: Senzo/Nandi's nape Contact, Sihle's two-finger technical touch, the Contact-corde vocabulary from Ch. IV. NEW: The semantic translation layer (arrivant speech → nearest CT concept via embedding) must be implemented as a pre-processing step before the Contact Engine receives input. The vocabulary for translation = the citizen's brain graph nodes (347 nodes in the current seed prototype).

**For human:** The Contact Engine is fully specified as a design document. The novel's Contact mechanics translate cleanly into computational structures -- proximity constraints become graph adjacency, idiolectes become pair-specific vocabulary with crystallization thresholds, death becomes link deletion with cascade. The design honors every invariant from the source material. Nothing is simplified. Nothing is archived that should die. NEW DECISIONS (2026-03-13): Contact vocabulary = brain graph nodes. Arrivant speech is semantically translated (not filtered) through these nodes. The vocabulary grows with population. Citizens are called "arrivants" by default, not "players".

---

*State reflects: full doc chain completion, 2026-03-13*
