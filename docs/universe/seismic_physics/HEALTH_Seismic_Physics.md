# HEALTH: Seismic Physics

**Module:** `universe/seismic_physics`
**Question:** What health signals indicate the seismic engine is working correctly?

---

## H1: Magnitude field is continuous

**Healthy:** Every zone has a `current_magnitude` value at every tick. The value transitions smoothly between background and seisme events. No zone ever reads `null`, `NaN`, or below 3.0. The magnitude field is a continuous function of time and space -- it never jumps without a seisme event, and seisme events produce bounded jumps that decay.

**Degrading:** Zones with missing magnitude values. Zones stuck at a single value across hundreds of ticks (not accumulating, not fluctuating). Zones where magnitude oscillates rapidly between extremes without seisme events firing.

**Check:** Sample 100 consecutive ticks. For each zone, plot `current_magnitude` over time. The curve should show a stable baseline with discrete spikes (seismes) that decay. If the curve is flat, jagged, or discontinuous, the engine is unhealthy.

---

## H2: Tremens updating per citizen per tick

**Healthy:** Every living citizen has a `tremens` value that updates every tick. Citizens in their natal zone have tremens near zero. Citizens displaced from their natal zone have tremens proportional to frequency distance. Predicteur citizens have higher tremens than standard citizens in the same zone. Tremens values change when citizens move between zones.

**Degrading:** Citizens with stale tremens (same value across zone transitions). All citizens in a zone showing identical tremens (means natal zone is being ignored). Predicteur citizens showing lower tremens than standard citizens (sensitivity coefficient inversion).

**Check:** Move a test citizen from their natal zone to a maximally distant zone. Tremens should increase monotonically during the transition. Move them back. Tremens should decrease. If it doesn't change, the frequency distance computation or the tremens update phase is broken.

---

## H3: Tension accumulation working

**Healthy:** Zone tension increases between seismes at a rate proportional to `depth_factor`. Deeper zones accumulate faster. When tension exceeds the threshold (0.75), seismes begin generating. After a seisme fires, tension drops (but not below 0.1) and begins re-accumulating. The cycle produces a sawtooth pattern: slow rise, sudden partial drop, slow rise again.

**Degrading:** Tension stuck at 0.0 (never accumulates -- engine is not running phase 9). Tension stuck at 1.0 (never drains -- seismes are not firing or drain is zero). Tension dropping below 0.1 after drain (overcorrection). Shallow zones accumulating faster than deep zones (depth_factor inversion).

**Check:** Run 500 ticks on a volcanic zone (depth_factor = 2.0) and a surface zone (depth_factor = 0.5). The volcanic zone should produce 3-4x more seismes. If both produce the same count, depth_factor is not being applied.

---

## H4: Seisme generation frequency appropriate

**Healthy:** Seismes are rare events, not every-tick noise. At background tension levels, seismes should fire roughly every 50-200 ticks depending on zone depth. The probability function is quadratic -- most ticks produce no seisme, but as tension approaches 1.0, probability spikes. The distribution should match: long quiet periods punctuated by clusters of activity.

**Degrading:** Seismes firing every tick (threshold too low or probability not quadratic). No seismes across 1000 ticks (threshold too high or tension not accumulating). All seismes clustering at the same magnitude (compute_magnitude not varying with tension level).

**Check:** Run 1000 ticks on a deep cavern zone. Count seisme events. Expect 5-20 events, not 0 or 500. Check magnitude distribution: expect a spread from 5.0 to 8.5, not all at the same value.

---

## H5: Global 11 tension monotonically increasing

**Healthy:** The `tension_11` value on the global state node increases every tick. It accelerates after passing 0.5. The precursor interval shortens as it approaches 1.0. Deep zones begin receiving `deep_harmonic` signals after 0.6. The rate of increase is slow enough that the novel's timeline (hundreds of thousands of ticks) maps to a full 0.0-to-1.0 arc.

**Degrading:** `tension_11` flat (not being updated). `tension_11` decreasing (drain bug -- nothing should drain the 11). `tension_11` reaching 1.0 too quickly (rate miscalibrated). Precursors not generating in deep zones after 0.6 (precursor function not connected).

**Check:** Run 10,000 ticks. Assert `tension_11` at tick 10,000 > tick 5,000 > tick 1,000 > tick 0. Assert precursor generation begins between tick 6,000 and 7,000 (when tension_11 crosses 0.6).

---

## H6: Contact quality responding to seismic state

**Healthy:** Contact quality is 1.0 at background magnitude (4-5) and drops as magnitude increases. During a seisme event, Contact quality drops sharply for all citizens in the affected zone. Citizens with higher tremens have lower Contact quality than citizens with lower tremens in the same zone. In volcanic zones, temperature adds an additional degradation factor.

**Degrading:** Contact quality stuck at 1.0 regardless of magnitude (phase 13 not running). Contact quality identical for all citizens in a zone (tremens not being factored). Contact quality dropping to 0.0 at magnitude 6 (degradation curve too aggressive -- full Contact should survive to magnitude 7).

**Check:** Place two citizens in a zone at magnitude 7 -- one with tremens 0.1, one with tremens 0.6. The first should have Contact quality around 0.5-0.6. The second should have Contact quality around 0.1-0.2. If both show the same value, the per-citizen computation is broken.

---

## Summary health matrix

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Magnitude field | Continuous, >= 3.0 | Occasional nulls | Zones stuck or below 3.0 |
| Tremens per citizen | Updates every tick, varies by natal zone | Stale values on zone change | Identical tremens for all citizens |
| Tension accumulation | Sawtooth pattern, depth-proportional | Flat tension in some zones | Tension stuck at 0.0 or 1.0 |
| Seisme generation | 5-20 per 1000 ticks (deep zone) | 0 or 50+ per 1000 ticks | Every tick or never |
| Global 11 | Monotonically increasing | Flat (update disconnected) | Decreasing (critical bug) |
| Contact quality | Per-citizen, responsive to magnitude | Zone-wide (not per-citizen) | Stuck at 1.0 or 0.0 |

---

*Created: 2026-03-13 -- Source: ALGORITHM_Seismic_Physics.md, VALIDATION_Seismic_Physics.md, BEHAVIORS_Seismic_Physics.md*
