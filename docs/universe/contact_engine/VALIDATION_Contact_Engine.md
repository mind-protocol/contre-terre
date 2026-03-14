# VALIDATION — Contact Engine

> Invariants. Rules that cannot break. If any of these fail, the engine is wrong.

---

## Structural Invariants

### V1: Contact Requires Adjacency

Two citizens must be adjacent in the proximity graph to exchange Contact. No exceptions. No remote communication. No delayed transmission. If they are not touching-distance apart, they cannot speak. Distance is silence. This is not a limitation -- it is the entire point.

**Contact-corde exception:** Citizens linked by rope can exchange Contact-corde (2 dimensions, not 20+). The rope is a physical medium, not a bypass. Rope must exist as an entity in the simulation connecting both citizens.

**Test:** Attempt to send a ContactGesture between two non-adjacent citizens with no rope link. The engine must reject it. No fallback. No queue. No "deliver when adjacent." Silence.

---

### V2: No Fallback to Text or Voice

The Contact Engine is the ONLY inter-citizen communication channel. No text. No voice. No broadcast. No notification system. If the Contact Engine is down, communication is down. Period.

**Voice exception:** Voice events exist as transgressions -- rule-breaking acts that carry social cost. They are not an alternative channel. A voice event emits a social violation marker, not a message.

**Test:** Search the entire codebase for any inter-citizen message-passing that does not route through the Contact Engine. If found, it is a bug.

---

### V3: Dead Citizen Vocabulary Is Deleted, Not Archived

When a citizen departs, their idiolecte and every pair-specific vocabulary entry involving them is destroyed. Not moved to cold storage. Not marked as inactive. Not archived for historical analysis. Deleted. Permanently. The data must not be recoverable by any surviving citizen or system query.

**Single exception:** The `pattern_signature` of the departed citizen is retained internally for Contact-fantome generation. This is not archival -- it is neurological residue in the surviving citizen's stress-response system. No external system can access it.

**Test:** After citizen departure, query all pair vocabularies, all idiolecte entries, all zone access maps for any reference to the departed citizen. Result must be empty. Verify surviving partners' `total_vocabulary` count has decreased.

---

### V4: Contact-Fantome Carries No Distinguishing Flag

Phantom Contact events are processed identically to real Contact by the experiencing citizen's system. No `is_phantom` field. No `source: hallucination` tag. No metadata that would allow the recipient to programmatically distinguish phantom from genuine.

External monitoring systems can detect the absence of a living sender (there is no adjacent citizen matching the signature). But the recipient citizen's internal processing does not distinguish. The engine must not make it easy to separate signal from ghost.

**Test:** Generate a Contact-fantome event. Inspect it from the recipient citizen's perspective. It must be indistinguishable from a ContactGesture sent by a living, adjacent citizen.

---

### V5: Idiolectes Emerge, Never Pre-Assigned

No citizen enters the simulation with pair-specific vocabulary. Idiolectes de paire form exclusively through the crystallization algorithm: repeated interaction, frequency threshold, registration. There is no admin tool, no configuration file, no seed data that pre-populates pair vocabulary.

A citizen may enter with base vocabulary (universal gestures) and a regional dialect. These are not idiolectes -- they are shared linguistic infrastructure.

**Test:** Initialize a new citizen. Their `idiolecte_de_paire` map for every other citizen must be empty. Only after sufficient interaction (>= CRYSTALLIZATION_THRESHOLD exchanges of a given pattern) should entries appear.

---

## Relational Invariants

### V6: Zone Access Reflects Relationship Depth

Body zone permissions between two citizens correspond strictly to their relational depth. Shoulder and arm are universal. Wrist and hand require acquaintance. Nape and palm require intimacy. Forehead requires sacred context. No citizen touches another's nape on first meeting.

**Test:** For every Contact event in the system, verify that the sender has relational permission for the body_zone used with that specific recipient. Zone violations emit social cost events -- they are not silently accepted.

---

### V7: Vocabulary Size Correlates With Graph Weight

The link weight between two citizen nodes in the graph must correlate directly with their pair-specific vocabulary size, Contact frequency, and zone diversity. There is no separate "relationship score." Contact IS the relationship. If the vocabulary is rich, the weight is high. If the vocabulary dies, the weight drops.

**Test:** Compare link weights with vocabulary metrics for all citizen pairs. Correlation must be positive and strong. A pair with zero Contact history must have zero (or absent) link weight.

---

## Processing Invariants

### V8: Seismic Degradation Is Mode-Sensitive

Fine motor modes (CODIFIED_GRIP, TACTILE_IDENTITY) degrade faster than gross motor modes (ARM_LOCK, SHOULDER_PRESSURE) as seismic magnitude increases. At magnitude 8+, only gross motor Contact survives. The engine must not allow a citizen to perform a delicate 3-finger high-resolution grip during a magnitude 8 seismic event.

**Test:** Simulate Contact at magnitude 8. Only modes with fidelity above their threshold should succeed. CODIFIED_GRIP and TACTILE_IDENTITY must fail or degrade to unrecognizable noise.

---

### V9: Dialect Friction Is Real and Measurable

Citizens from different seismic zones experience reduced Contact intelligibility on first interaction. The friction factor must decrease with sustained interaction. It must never start at zero (unless same dialect) and it must never remain at maximum indefinitely.

**Test:** Create two citizens from different zones. Measure parse success rate on first interaction. It must be lower than baseline. After N interactions, measure again. It must be higher. The convergence rate must be proportional to interaction frequency.

---

### V10: Contact-Corde Is Strictly Poorer Than Direct Contact

Contact-corde supports exactly 2 dimensions (tension + movement). No emotional register. No body zone semantics. No tactile identity. The rope anonymizes the sender. If a system transmits rich Contact data over a rope link, the engine is lying.

**Test:** Inspect Contact-corde events. They must contain only tension, movement, count, and involuntary_component. Any field from ContactGesture that implies body zone, identity, or mode richness must be absent or null.

---

*Invariants derived from: `ALGORITHM_Contact_Engine.md`, `VALIDATION_Contact.md`, `PATTERNS_Contact_Engine.md`, `OBJECTIVES_Contact_Engine.md`*
