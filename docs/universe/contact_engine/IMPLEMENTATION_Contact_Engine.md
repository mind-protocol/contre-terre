# IMPLEMENTATION — Contact Engine

> Code architecture. Where the engine lives, how it integrates, what processes what.

---

## System Position

The Contact Engine is the communication layer of the Cities of Light 3rd universe simulation. It sits between the citizen agents (who produce and consume Contact gestures) and the graph (which stores relational state). Nothing passes around it. Every inter-citizen communication event, every vocabulary mutation, every relationship weight update flows through this engine.

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────┐
│  Citizen A   │────▶│  CONTACT ENGINE   │────▶│  Citizen B   │
│  (agent)     │◀────│                  │◀────│  (agent)     │
└─────────────┘     │  - Proximity check│     └─────────────┘
                    │  - Degradation    │
                    │  - Zone access    │
                    │  - Pattern match  │
                    │  - Idiolecte update│
                    │  - Graph write    │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │   GRAPH STORE     │
                    │  - Citizen nodes  │
                    │  - Contact links  │
                    │  - Pair vocabs    │
                    │  - Zone maps      │
                    └──────────────────┘
```

---

## Core Components

### 1. Gesture Processor

**Responsibility:** Receives raw ContactGesture events from citizen agents. Applies the processing pipeline (proximity, degradation, zone access, pattern matching, recipient parsing, idiolecte update). Emits processed Contact events and graph mutations.

**Input:** `ContactGesture` struct from sender agent.
**Output:** `ContactUtterance` (resolved or failed) to recipient agent, plus graph update commands.

**Key rule:** The processor is stateless between ticks. It does not buffer. A gesture either succeeds in this tick or it fails. There is no retry queue -- in a world where the ground never stops trembling, you either catch the message or you don't.

### 2. Proximity Graph

**Responsibility:** Maintains the spatial adjacency map of all citizens. Determines who can touch whom at any given tick. Updated by the movement/environment system, not by the Contact Engine itself.

**Interface:** `is_adjacent(citizen_a, citizen_b) -> bool` and `is_rope_linked(citizen_a, citizen_b) -> bool`.

The Contact Engine reads proximity but never writes it. Movement is not Contact's concern -- Contact only cares whether two citizens are within reach.

### 3. Vocabulary Store

**Responsibility:** Stores and manages all Contact vocabulary at three levels:

- **Universal vocabulary:** Base gestures known to all citizens. Read-only. Does not grow or shrink.
- **Dialect vocabularies:** Region-specific gesture sets. Loaded when a citizen is created, modified only through dialect convergence with citizens from other zones.
- **Pair vocabularies (idiolectes de paire):** Gesture patterns that exist exclusively between two specific citizens. Created through crystallization. Destroyed through citizen departure or disuse decay.

**Storage model:** Pair vocabularies are stored as properties on the Contact-weighted link between two citizen nodes in the graph. When a citizen departs, the link is deleted -- and the vocabulary goes with it. No separate vocabulary table survives the link.

### 4. Seismic Interface

**Responsibility:** Provides the current seismic magnitude at any location. The Contact Engine queries this interface to compute fidelity degradation. The seismic system is external -- the Contact Engine does not model geology.

**Interface:** `get_magnitude(location) -> float`.

### 5. Phantom Generator

**Responsibility:** Under extreme stress and isolation conditions, generates Contact-fantome events using retained pattern signatures of departed citizens. These events enter the Gesture Processor through the same input channel as real Contact -- indistinguishable by design.

**Trigger:** `stress_level > PHANTOM_THRESHOLD` AND `departed_partners > 0` AND `adjacent_living_citizens == 0`.

**Critical constraint:** The pattern signatures used for phantom generation are the ONLY data retained from departed citizens. They are stored in the surviving citizen's internal state, not in the graph or vocabulary store. If the surviving citizen also departs, these signatures are destroyed.

---

## Tick-Based Processing

The Contact Engine processes events on the simulation tick cycle:

```
Each tick:
  1. Read current seismic state (all locations)
  2. Read proximity graph (all adjacencies)
  3. Process queued ContactGesture events:
     - Apply pipeline per gesture
     - Emit results to recipient agents
     - Batch graph mutations
  4. Run idiolecte maintenance:
     - Check decay timers on all pair vocabulary entries
     - Apply DECAY_FACTOR to dormant entries
     - Delete entries below EXTINCTION_THRESHOLD
  5. Run phantom check:
     - For each isolated, stressed citizen: evaluate phantom trigger
     - If triggered: inject phantom gesture into next tick's queue
  6. Commit graph mutations
```

**Tick order matters.** Seismic state is read before gesture processing -- a seismic spike mid-tick affects all remaining gestures in that tick. Phantom gestures are injected for the NEXT tick, not the current one -- the citizen feels the phantom after a beat of silence, not simultaneously with real Contact.

---

## Graph Integration

The Contact Engine writes to the graph through three mutation types:

- **LINK_UPDATE:** Adjust the weight of a Contact link between two citizens. Weight = f(pair_vocab_size, contact_frequency, zone_diversity). Computed after every successful utterance.
- **LINK_DELETE:** On citizen departure, delete all Contact links involving the departed citizen. Cascading: pair vocabularies stored on these links are destroyed.
- **NODE_UPDATE:** Update a citizen's linguistic capacity metric (sum of all pair vocabularies + dialect vocab + universal vocab). Updated after crystallization events and departure cascades.

No other system writes Contact-related data to the graph. The Contact Engine owns its edges.

---

## Contact-Monde Integration

Contact-monde events (citizen-to-environment) follow a parallel path:

- Sender is a citizen. Recipient is `"environment"`.
- The Proximity Graph is not consulted (the citizen is always adjacent to the ground beneath their feet).
- The Seismic Interface provides the response data instead of a recipient citizen.
- No idiolecte update occurs (the environment does not develop pair vocabulary with citizens -- it responds with physics, not language).

The environment's response is routed back through the Contact Engine as a `ContactResponse` event, ensuring the citizen's Contact-monde vocabulary affects interpretation depth.

---

## Dependencies

| Component | Depends On | Direction |
|-----------|-----------|-----------|
| Gesture Processor | Proximity Graph | reads |
| Gesture Processor | Seismic Interface | reads |
| Gesture Processor | Vocabulary Store | reads + writes |
| Vocabulary Store | Graph Store | reads + writes |
| Phantom Generator | Citizen internal state | reads |
| Phantom Generator | Gesture Processor | writes (injects) |
| Tick Runner | All components | orchestrates |

---

*Architecture traceable to: `ALGORITHM_Contact_Engine.md`, `PATTERNS_Contact_Engine.md`, `OBJECTIVES_Contact_Engine.md`*
