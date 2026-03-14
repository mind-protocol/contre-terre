# ALGORITHM — Contact Engine

> The core. Data structures, processing logic, idiolecte evolution, degradation rules.

---

## 1. Contact Gesture Data Structure

A single Contact gesture is the atomic unit of communication:

```
ContactGesture {
    gesture_id:        uuid
    timestamp:         datetime
    sender_id:         citizen_id
    recipient_id:      citizen_id | "environment"    # environment for Contact-monde

    # The 5-mode encoding
    mode:              enum(ARM_LOCK, SHOULDER_PRESSURE, CODIFIED_GRIP, TACTILE_IDENTITY, DIALECT_MARKER)
    body_zone:         enum(FOREHEAD, NAPE, SHOULDER, TORSO, ARM, FOREARM, WRIST, HAND, PALM, FEET_GROUND)

    # Signal dimensions
    intensity:         float [0.0 - 1.0]             # pressure force
    duration:          float (seconds)                # hold time
    speed:             float [0.0 - 1.0]             # gesture execution speed
    direction:         enum(LATERAL, DESCENDING, ASCENDING, ROTATIONAL, STATIC)
    contact_type:      enum(FULL_GRIP, TWO_FINGER, OPEN_PALM, NAILS, FIST, SLIDING, TREMBLING)

    # Idiolecte layer
    pattern_signature: hash                           # derived from sender's tactile identity
    sequence_position: int                            # position in multi-gesture utterance
    sequence_total:    int                            # total gestures in utterance

    # Environmental modifiers
    seismic_magnitude: float                          # current seismic state at moment of gesture
    fidelity:          float [0.0 - 1.0]             # actual transmission quality after degradation
}
```

**Key properties:**
- `body_zone` determines register (public/professional/personal/intimate/sacred)
- `mode` determines information type (vocabulary/urgency/grammar/identity/origin)
- `pattern_signature` is unique per sender -- the same gesture from two different citizens produces different signatures
- `fidelity` is computed from `seismic_magnitude` at transmission time, not stored statically

---

## 2. Contact Utterance (Multi-Gesture Sequence)

A complete communication unit is a sequence of gestures forming an utterance:

```
ContactUtterance {
    utterance_id:      uuid
    sender_id:         citizen_id
    recipient_id:      citizen_id | "environment"
    gestures:          ordered_list[ContactGesture]   # sequence_position ordered
    semantic_content:  string | null                   # resolved meaning (if parseable)
    idiolecte_markers: list[idiolecte_entry_id]       # which pair-vocabulary entries were invoked
    understood:        bool                            # did recipient successfully parse?
    timestamp_start:   datetime
    timestamp_end:     datetime
}
```

---

## 3. Contact Exchange Processing Pipeline

When a citizen initiates Contact:

```
1. PROXIMITY CHECK
   - Are sender and recipient adjacent? (proximity graph)
   - If not adjacent → Contact FAILS (silent failure is the design: distance = silence)
   - Exception: Contact-corde if rope-linked

2. SEISMIC DEGRADATION
   - Read current seismic_magnitude at sender's location
   - Compute fidelity = degradation_curve(seismic_magnitude, mode)
   - If fidelity < MODE_THRESHOLD[mode] → mode unavailable, gesture dropped or downgraded

   Degradation curve:
     fidelity = max(0, 1.0 - (magnitude / 10.0) * mode_sensitivity[mode])

   Mode sensitivities (higher = more fragile):
     ARM_LOCK:           0.8  (robust -- gross motor)
     SHOULDER_PRESSURE:  0.9  (robust)
     CODIFIED_GRIP:      1.5  (fragile -- fine motor)
     TACTILE_IDENTITY:   1.8  (fragile -- subtle signals)
     DIALECT_MARKER:     1.2  (moderate)

3. ZONE ACCESS CHECK
   - Does the sender have relational permission for this body_zone with this recipient?
   - Zone access tiers:
     SHOULDER, ARM, FOREARM → universal (any citizen)
     WRIST, HAND           → requires relationship_depth >= ACQUAINTED
     NAPE, PALM            → requires relationship_depth >= INTIMATE
     FOREHEAD              → requires relationship_depth >= SACRED (ceremonial context)
     TORSO                 → requires relationship_depth >= TRUSTED
   - Violation → social cost event emitted (not blocked, but flagged)

4. PATTERN MATCHING
   - Compare gesture sequence against:
     a. Universal vocabulary (base Contact known to all)
     b. Sender's regional dialect vocabulary
     c. Pair-specific vocabulary (idiolecte de paire between sender & recipient)
   - Resolution priority: pair-specific > dialect > universal
   - If no match → GESTE_INCONNU (unknown gesture) -- logged, not resolved

5. RECIPIENT PROCESSING
   - Recipient attempts to parse the utterance
   - Parse success depends on:
     a. Shared vocabulary (does recipient know this pattern?)
     b. Dialect compatibility (cross-dialect friction factor)
     c. Current fidelity (degraded gestures are harder to read)
   - Parse probability = shared_vocab_score * dialect_compat * fidelity
   - If parse fails → misinterpretation event or request-for-repeat

6. IDIOLECTE UPDATE
   - If this gesture pattern was successfully exchanged → increment frequency counter
   - If frequency crosses crystallization threshold → register as idiolecte de paire entry
   - Update graph weight between sender and recipient nodes
```

---

## 4. Idiolecte Evolution Algorithm

Pair-specific vocabulary forms through repeated successful Contact:

```
IDIOLECTE CRYSTALLIZATION:

For each (citizen_A, citizen_B) pair:

  pattern_registry[A,B] = {}  # tracks gesture patterns and their frequencies

  On each successful ContactUtterance between A and B:
    pattern = extract_pattern(utterance)  # normalized gesture sequence

    if pattern in pattern_registry[A,B]:
      pattern_registry[A,B][pattern].frequency += 1
      pattern_registry[A,B][pattern].last_used = now()
    else:
      pattern_registry[A,B][pattern] = {frequency: 1, first_seen: now(), last_used: now()}

    # Crystallization check
    if pattern_registry[A,B][pattern].frequency >= CRYSTALLIZATION_THRESHOLD:
      if pattern not in idiolecte_de_paire[A,B]:
        CRYSTALLIZE(pattern, A, B)
        # This pattern is now recognized as pair-specific vocabulary
        # It carries higher semantic weight in future A-B exchanges
        # It is ABSENT from all other pair vocabularies

CRYSTALLIZATION_THRESHOLD = 7
  # Source: "seven" recurs in the novel (7 characters, 7 archipels)
  # Pragmatic: enough repetition to be intentional, not accidental

DECAY:
  # Idiolecte entries that go unused decay
  For each entry in idiolecte_de_paire[A,B]:
    if (now() - entry.last_used) > DORMANCY_PERIOD:
      entry.strength *= DECAY_FACTOR  # 0.95 per period
    if entry.strength < EXTINCTION_THRESHOLD:
      DELETE entry  # vocabulary atrophies without use
```

---

## 5. Citizen Departure — Vocabulary Death

```
On citizen_departure(citizen_X):

  # 1. Destroy all pair-specific vocabularies involving X
  for each partner_Y in all_partners(citizen_X):
    DELETE idiolecte_de_paire[X, Y]       # entire pair vocabulary gone
    DELETE idiolecte_de_paire[Y, X]       # bidirectional

    # 2. Reduce partner's communicative capacity
    partner_Y.total_vocabulary -= count(idiolecte_de_paire[X, Y])
    partner_Y.zone_access_map.remove(X)   # zone permissions gone

    # 3. Check for zone orphaning
    # If X was the ONLY partner granting Y access to a zone (e.g., NAPE)
    # then Y loses that zone entirely
    for zone in zones_accessed_only_with(Y, X):
      partner_Y.active_zones.remove(zone)

    # 4. Update graph
    DELETE link(X, Y)                      # Contact-weighted edge removed
    RECALCULATE partner_Y.linguistic_capacity

  # 5. Delete X's idiolecte (individual tactile signature)
  DELETE idiolecte[X]

  # NO ARCHIVAL. The vocabulary is gone.
```

---

## 6. Contact-Monde Processing

```
On contact_monde_event(citizen, surface_type, location):

  gesture = ContactGesture(
    sender_id = citizen,
    recipient_id = "environment",
    mode = determined_by(surface_type),
    body_zone = FEET_GROUND or PALM (depending on contact surface),
    ...environmental parameters...
  )

  # Environment responds based on surface type
  response = environment.process(gesture, location)

  # Response types:
  #   GROUND → seismic frequency data, magnitude prediction
  #   BIOLUMINESCENT_WALL → light pattern (confirmation, warning, echo)
  #   WATER_CHANNEL → flow variation (hydraulic Contact, village-specific)
  #   CHARGE_RESONATOR → calibration feedback (Ch. VIII specific)

  # Citizen's Contact-monde vocabulary affects interpretation depth
  interpretation = citizen.contact_monde_vocab.parse(response)

  # Richer Contact-monde vocabulary → more information extracted
  # Nandi (feet) reads frequency. Enama (hands) reads direction.
  # Same ground, different readings, different Contact-monde idiolectes.
```

---

## 7. Contact-Corde (Rope Channel)

```
ContactCordeGesture {
    # Reduced to 2 dimensions (vs 20+ for direct Contact)
    tension:     float [0.0 - 1.0]    # rope tension level
    movement:    enum(SHORT_SHAKE, LONG_SHAKE, SERIES, SLACK, TENSION_RELEASE)
    count:       int                    # number of repetitions

    # Inherits involuntary signals
    involuntary_component: float [0.0 - 1.0]  # fear, fatigue bleed-through

    # No emotional register
    # No body zone (rope has no anatomy)
    # No tactile identity (vibrations anonymize the sender)
}

# Vocabulary is invented in real-time by the rope-linked group
# Contact-corde vocabulary does NOT persist after the rope is untied
```

---

## 8. Contact-Fantome Generation

```
On isolation_and_stress(citizen, stress_level, departed_partners):

  if stress_level > PHANTOM_THRESHOLD and len(departed_partners) > 0:

    # Select a departed partner weighted by relational depth
    phantom = weighted_random(departed_partners, weight=former_pair_vocabulary_size)

    # Generate gesture using the dead citizen's exact tactile signature
    phantom_gesture = reconstruct_from_idiolecte(
      departed_citizen = phantom,
      signature = archived_pattern_signature[phantom],  # only case where signature is retained
      body_zone = phantom.characteristic_zone,
      intensity = phantom.characteristic_intensity
    )

    # CRITICAL: phantom_gesture is processed identically to real Contact
    # No flag. No distinction. The citizen's system treats it as genuine.
    process_contact(phantom_gesture, recipient=citizen)

    # Progression: isolated phantoms → overlapping phantoms → full circle → dissolution
```

---

*Algorithm traceable to: `ALGORITHM_Contact.md`, `PATTERNS_Contact.md`, `CONTACT.md`, `PERSONNAGES.md`*
