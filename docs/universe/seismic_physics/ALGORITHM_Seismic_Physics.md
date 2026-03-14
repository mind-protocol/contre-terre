# ALGORITHM: Seismic Physics

**Module:** `universe/seismic_physics`
**Question:** How does the seismic physics engine work? What are the tick-level procedures?

---

## A1: Magnitude tick (every 5 seconds world-time)

The seismic tick runs as a phase extension of the Venezia-derived `GraphTickV1_2`. Each tick executes 5 seismic sub-phases after the standard 8 narrative physics phases.

```
STANDARD TICK (Venezia v1.2):
  1. generation
  2. moment_draw
  3. moment_flow
  4. moment_interaction
  5. narrative_backflow
  6. link_cooling
  7. completion
  8. rejection

SEISMIC EXTENSION (Contre-Terre):
  9.  seismic_tension_accumulation
  10. seismic_event_generation
  11. seismic_magnitude_propagation
  12. tremens_update_per_citizen
  13. contact_quality_computation
```

### Phase 9: Seismic tension accumulation

```
FOR each zone in world:
    zone.tension += tension_accumulation_rate * zone.depth_factor
    zone.tension = clamp(zone.tension, 0.0, 1.0)

    # Depth increases accumulation speed
    # Surface zones: depth_factor = 0.5
    # Cavern zones: depth_factor = 1.0
    # Volcanic zones: depth_factor = 2.0
    # Interior zones: depth_factor = 3.0

global_11_tension += global_accumulation_rate  # NEVER drains
global_11_tension = clamp(global_11_tension, 0.0, 1.0)
```

### Phase 10: Seismic event generation

```
FOR each zone in world:
    IF zone.tension > seisme_threshold (0.75):
        probability = (zone.tension - seisme_threshold) / (1.0 - seisme_threshold)
        probability = probability ^ 2  # exponential curve

        IF random() < probability:
            type = select_cataclysm_type(zone)
            magnitude = compute_magnitude(zone.tension, zone.depth_factor)
            duration_ticks = compute_duration(magnitude)

            CREATE seisme_moment(zone, type, magnitude, duration_ticks)

            # Drain tension (partial -- seismes don't reset to zero)
            zone.tension -= drain_factor * (magnitude / max_magnitude)
            zone.tension = max(zone.tension, 0.1)  # never fully drains
```

### Phase 11: Seismic magnitude propagation

```
FOR each active seisme_moment:
    # Set zone magnitude to max(background, seisme_magnitude)
    zone.current_magnitude = max(zone.background_magnitude, seisme.magnitude)

    # Propagate to adjacent zones (attenuated)
    FOR each adjacent_zone:
        distance_attenuation = 0.7 ^ distance_in_zones
        propagated = seisme.magnitude * distance_attenuation
        adjacent_zone.current_magnitude = max(
            adjacent_zone.current_magnitude,
            propagated
        )

    # Bioluminescence update
    IF zone.has_bioluminescence:
        zone.bioluminescence_intensity = zone.current_magnitude / 4.0
```

---

## A2: Frequency zone computation

Each zone has a spectral signature defined by frequency band, amplitude pattern, and geological character.

```
ZONE SPECTRAL SIGNATURES:

SURFACE_DESERT:
    frequency_band: 1  # lowest
    amplitude: low (4-5)
    character: "long, deep, slow"
    descriptor: "an animal breathing in its sleep"

PIEDMONT:
    frequency_band: 3
    amplitude: variable (5-7)
    character: "dry, nervous, clacking"
    descriptor: "sharp cracks climbing through the ankles"

CAVERN_VILLAGE:
    frequency_band: 2
    amplitude: dampened (4 effective, 40% reduction)
    character: "infra-bass, below consciousness"
    descriptor: "vibrations entering the bones"
    special: dampening_factor = 0.6

FAILLE:
    frequency_band: 4
    amplitude: amplified by geometry (5-7 effective, feels like 7-8)
    character: "lateral, bouncing between walls"
    descriptor: "compression waves, walls closing"
    special: lateral_amplification = 1.5

DEEP_CAVERN:
    frequency_band: 5
    amplitude: high (6-8)
    character: "multiple, superposed, chaotic"
    descriptor: "signals the sismograph cannot separate"

VOLCANIC:
    frequency_band: 6
    amplitude: extreme (7-9+)
    character: "heat-deformed, mixed with thermal convection"
    descriptor: "waves melting into each other"

INTERIOR:
    frequency_band: 7
    amplitude: near-constant extreme (8-9+)
    character: "precursors of the 11"
    descriptor: "the ground speaks"

GROTTE_FINALE:
    frequency_band: 8  # highest -- all frequencies simultaneously
    amplitude: escalating to 11
    character: "full spectrum"
    descriptor: "Nandi IS the frequency"
```

### Frequency distance computation

```
FUNCTION frequency_distance(natal_zone, current_zone):
    band_diff = abs(natal_zone.frequency_band - current_zone.frequency_band)
    RETURN band_diff / max_band_range  # normalized 0.0 to 1.0

# Nandi: born in band 7-8 (archipelago = high, dry)
#         descending through bands 1-2 (desert = low, deep)
#         then back up through 3-8 (into the volcano)
# Her distance is maximal at the surface, partially resolves
# in deep zones (closer to natal frequency), then diverges
# again as volcanic harmonics differ from archipelago harmonics.
```

---

## A3: Tremens update per citizen

```
FUNCTION compute_tremens(citizen, zone, global_11_tension):

    # Base tremens from frequency displacement
    freq_dist = frequency_distance(citizen.natal_zone, zone)
    base_tremens = citizen.sensitivity * freq_dist * (zone.current_magnitude / 4.0)

    # Predicteur bonus: reads unreleased tension
    IF citizen.is_predicteur:
        tension_signal = zone.tension + global_11_tension
        base_tremens += citizen.sensitivity * tension_signal * 0.5

    # Adaptation decay (slow -- descent is faster than adaptation)
    IF citizen.ticks_in_current_zone > adaptation_start_ticks:
        adaptation = min(0.3, (citizen.ticks_in_zone - adaptation_start) * adaptation_rate)
        base_tremens *= (1.0 - adaptation)

    # Cumulative fatigue (tremens wears the body down)
    cumulative_factor = 1.0 + (citizen.total_tremens_exposure * fatigue_rate)
    final_tremens = base_tremens * cumulative_factor

    # Clamp and assign status
    citizen.tremens = clamp(final_tremens, 0.0, 1.0)
    citizen.tremens_status = classify_tremens(citizen.tremens)

    RETURN citizen.tremens

FUNCTION classify_tremens(value):
    IF value < 0.1: RETURN "imperceptible"
    IF value < 0.3: RETURN "mild"       # salivation, discomfort
    IF value < 0.5: RETURN "moderate"    # vomiting, jaw clenching
    IF value < 0.7: RETURN "severe"      # trembling, burst capillaries
    IF value < 0.9: RETURN "extreme"     # hallucinations, partial incapacitation
    RETURN "critical"                     # body-as-seismograph, near-total incapacitation
```

---

## A4: Seisme event generation -- probability from accumulated tension

```
FUNCTION seisme_probability(zone):
    IF zone.tension <= seisme_threshold:
        RETURN 0.0

    excess = zone.tension - seisme_threshold
    normalized = excess / (1.0 - seisme_threshold)
    RETURN normalized ^ 2  # quadratic -- probability rises steeply near 1.0

FUNCTION compute_magnitude(zone_tension, depth_factor):
    # Base magnitude from tension level
    base = 5.0 + (zone_tension * 4.0)  # range 5.0 to 9.0

    # Depth amplification
    magnitude = base * (1.0 + (depth_factor - 1.0) * 0.2)

    # Cap at 9.5 for generated seismes (11 is global only)
    RETURN min(magnitude, 9.5)

FUNCTION select_cataclysm_type(zone):
    # Weighted random based on zone properties
    weights = {}
    weights["seisme"] = 1.0  # always possible

    IF zone.has_water:
        weights["tsunami"] = 0.3
        weights["geyser"] = 0.2

    IF zone.is_volcanic:
        weights["eruption"] = 0.4

    IF zone.is_enclosed:
        weights["effondrement"] = 0.3
        weights["bang"] = 0.2

    IF zone.has_loose_material:
        weights["glissement"] = 0.3
        weights["coulee_boue"] = 0.1

    RETURN weighted_random_choice(weights)
```

---

## A5: How magnitude affects Contact range and quality

```
FUNCTION compute_contact_quality(citizen, zone):
    # Seismic noise factor
    seismic_noise = max(0.0, (zone.current_magnitude - 5.0) / 5.0)

    # Tremens motor impairment
    tremens_impairment = citizen.tremens * 0.8

    # Temperature pain factor (volcanic zones)
    temp_pain = 0.0
    IF zone.temperature > skin_tolerance_threshold:
        temp_pain = (zone.temperature - skin_tolerance) / max_temperature_range

    # Combined degradation
    total_degradation = min(1.0, seismic_noise + tremens_impairment + temp_pain)

    # Quality is inverse of degradation
    citizen.contact_quality = max(0.0, 1.0 - total_degradation)

    RETURN citizen.contact_quality
```

### Contact mode availability by quality

```
quality >= 0.8: All 5 modes (standard, urgent, intime, technique, poetic)
quality >= 0.6: Standard + urgent + technique
quality >= 0.4: Urgent + basic technique (survival signals)
quality >= 0.2: Grip/release, directional pushes
quality <  0.2: Binary (alive/dead, hold/let go)
quality == 0.0: No Contact possible (incapacitation or separation)
```

---

## A6: The building 11 algorithm

```
FUNCTION update_building_11(global_state, tick):
    # Monotonic increase -- NEVER decreases
    global_state.tension_11 += global_11_rate

    # Acceleration: rate increases as tension approaches threshold
    IF global_state.tension_11 > 0.5:
        acceleration = 1.0 + (global_state.tension_11 - 0.5) * 2.0
        global_state.tension_11 += global_11_rate * acceleration * 0.1

    # Precursor generation (deep zones feel it first)
    IF global_state.tension_11 > 0.6:
        precursor_interval = max(5, int(100 * (1.0 - global_state.tension_11)))
        IF tick % precursor_interval == 0:
            # Generate a deep harmonic -- not a seisme, but a tremens-only signal
            FOR each zone WHERE zone.depth_factor > 2.0:
                zone.deep_harmonic = global_state.tension_11 * 0.3

    # Detonation condition
    IF global_state.tension_11 >= 1.0:
        TRIGGER magnitude_11_event()
        # This is terminal. The world changes.

    RETURN global_state.tension_11
```

---

*Created: 2026-03-13 -- Source: ALGORITHM_Seismique.md, tick_v1_2.py, tick_v1_2_types.py, tick_runner.py, constants.json*
