# HEALTH — Contact Engine

> Health checks. How to know the engine is alive, working, and honest.

---

## Contact Vitality Metric

The primary health signal of the Contact Engine is **Contact Vitality** -- the ratio of successful Contact utterances to attempted Contact utterances across all citizen pairs in a given time window.

```
contact_vitality = successful_utterances / attempted_utterances
```

**Healthy range:** 0.60 - 0.95 (depending on seismic state).

Below 0.60 outside of seismic crisis: something is broken. The engine is rejecting too many gestures, or proximity constraints are too tight, or vocabulary matching is failing where it shouldn't.

Above 0.95: suspicious. Real Contact in a trembling world should have friction. If everything is succeeding, the degradation curve may be disabled or the seismic interface may be returning false calm.

A vitality of 1.0 is a bug. A world that never trembles is not Contre-Terre.

---

## Vocabulary Growth / Death Rates

### Growth Rate

Track the rate of idiolecte crystallization events across the simulation:

- **Healthy:** New pair vocabulary entries form at a rate proportional to citizen interaction density. Early simulation (many new pairings) should show rapid growth. Mature simulation should show slower, steadier growth.
- **Degraded:** Zero crystallization over extended periods with active citizen pairs. Either the CRYSTALLIZATION_THRESHOLD is too high, or the pattern extraction is failing to recognize repeated gestures.
- **Pathological:** Explosive crystallization (hundreds of entries per tick). The threshold is too low, or the pattern normalization is broken, treating every gesture as unique.

### Death Rate

Track the rate of vocabulary deletion (both decay-based and departure-based):

- **Healthy:** Decay-based deletion is slow and steady. Departure-based deletion is sudden and catastrophic -- a spike followed by a new equilibrium at a lower vocabulary level. This is the intended behavior: death impoverishes.
- **Degraded:** No decay ever occurs. Vocabulary accumulates without attrition. Dormant entries never die. This means the decay timer is broken.
- **Pathological:** Vocabulary is deleted without citizen departure or dormancy. Something is destroying active vocabulary unprompted.

### The Death Ratio

After every citizen departure, measure:

```
death_ratio = vocabulary_destroyed / departing_citizen.total_pair_vocabulary
```

This must equal 1.0. If vocabulary survives the citizen it belonged to, the engine is archiving when it should be destroying.

---

## Dialect Friction Check

Verify that cross-dialect friction is working correctly:

1. Create two citizens from maximally distant seismic zones.
2. Measure their first-interaction parse success rate.
3. It must be significantly lower than same-dialect baseline.
4. After sustained interaction, measure again. Friction must decrease.
5. Friction must never reach zero (dialects converge but never fully merge -- some accent always remains).

**Healthy:** First-interaction friction between distant dialects produces 20-40% parse failure. Converges to 5-10% after extended interaction.

**Degraded:** No friction at all (everyone understands everyone perfectly from the first touch). Or friction that never decreases (citizens cannot learn each other's dialect).

---

## Seismic Degradation Check

Verify the degradation curve is honest:

1. At magnitude 0: all modes should work at full fidelity.
2. At magnitude 5: CODIFIED_GRIP should show measurable degradation.
3. At magnitude 7: TACTILE_IDENTITY should be unreliable.
4. At magnitude 8+: only ARM_LOCK and SHOULDER_PRESSURE should survive.

**Degradation must be felt.** If citizens can perform delicate 3-finger high-resolution Contact during a magnitude 8 earthquake, the engine is lying about its seismic interface.

---

## Phantom Integrity Check

1. Create an isolated citizen under extreme stress with departed partners.
2. Verify phantom events are generated.
3. Verify phantom events carry the exact tactile signature of the departed citizen (not a generic placeholder).
4. Verify phantom events enter the processing pipeline identically to real Contact.
5. Verify no `is_phantom` or equivalent flag exists anywhere in the event data accessible to the recipient citizen.

If phantoms are distinguishable, the engine has broken the most sacred rule: the dead must touch as if alive.

---

## Departure Cascade Check

The most critical health check. Simulate a citizen departure and verify:

1. All pair vocabularies involving the departed citizen are destroyed (count = 0).
2. Surviving partners' vocabulary counts have decreased by the exact amount of the destroyed pair vocabulary.
3. Zone orphaning has occurred where applicable (if departed was the only intimate-zone partner, surviving citizen loses that zone).
4. No reference to the departed citizen exists in any vocabulary store or zone access map.
5. Graph links to the departed citizen are deleted.
6. The only retained data is the pattern_signature in surviving citizens' phantom state.

If any vocabulary survives departure, the engine has betrayed the central mechanic. The dead do not leave words behind.

---

*Health checks derived from: `ALGORITHM_Contact_Engine.md`, `VALIDATION_Contact_Engine.md`, `OBJECTIVES_Contact_Engine.md`*
