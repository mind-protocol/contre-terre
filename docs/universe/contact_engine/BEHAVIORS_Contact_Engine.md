# BEHAVIORS — Contact Engine

> Observable effects. What the system should do.

---

## B1: Citizens Develop Pair-Specific Vocabulary

When two citizens interact repeatedly through Contact, unique gesture patterns emerge between them that do not exist in any other pairing. After sufficient interaction (threshold defined in ALGORITHM), these patterns crystallize into idiolecte de paire entries visible in the graph as weighted links.

**Observable:** Query the Contact history between Citizen A and Citizen B after 50+ exchanges. Patterns should appear that are statistically absent from A's exchanges with C, D, or E. The pair-specific vocabulary grows logarithmically -- rapid initial formation, then slower enrichment as the relationship matures.

**Example from source:** Senzo and Nandi develop the richest idiolecte in the novel -- the nape touch (exclusive to them), three slow pressures meaning "follow me / the world still trembles," the descending arc meaning "we don't go back up." None of these gestures exist between any other pair.

---

## B2: Contact Quality Varies by Seismic State

The environment's seismic magnitude directly affects Contact fidelity. In calm conditions, citizens use all 5 modes across all body zones with full nuance. As magnitude increases, fine motor control degrades, modes collapse, and Contact reduces to emergency-level grip communication.

**Observable:** During a magnitude 7+ seismic event, Contact gestures in the system should show reduced mode diversity (only modes 1-2 survive), increased intensity (louder signals to cut through noise), and higher error rates (misinterpretation probability rises). Citizens should not be able to perform delicate Mode 3 (codified grips) sequences during high seismic activity.

**Degradation curve:**
- Mag < 5: 100% fidelity, all modes
- Mag 5-6: 85% fidelity, Mode 3 accuracy drops
- Mag 7: 60% fidelity, Modes 3-4 unreliable
- Mag 8+: 30% fidelity, emergency only (Mode 1 arm locks + Mode 2 shoulder pressure)

---

## B3: New Citizens Learn Contact From Established Ones

A citizen entering the simulation with only base vocabulary acquires new gestures through interaction with established citizens. Learning is not instant -- it follows exposure curves. A new citizen exposed to a dialectally rich community gradually acquires that community's vocabulary, starting with high-frequency universal gestures and progressing to rarer, more specialized ones.

**Observable:** Track a new citizen's active vocabulary size over time. It should grow in proportion to the diversity and frequency of their Contact interactions. Citizens who interact primarily with one partner develop vocabulary biased toward that partner's idiolecte. Citizens who interact with many develop broader but shallower vocabularies.

**Source parallel:** The expedition team arrives at the deaf village (Ch. III) and encounters Contact haute resolution -- a 3-finger dialect radically different from surface Contact. They do not instantly understand it. The vieille femme teaches through demonstration, not explanation. Nandi learns the Geste Inconnu through direct transmission, not instruction.

---

## B4: Loss of a Citizen Triggers Vocabulary Death

When a citizen departs (dies, disconnects, is removed), every pair-specific vocabulary entry they participated in is destroyed. Their surviving partners experience measurable vocabulary loss -- certain gesture patterns they could perform with the departed citizen no longer have a recipient, and the patterns themselves are deleted from the engine's active vocabulary store.

**Observable:** Before departure: Citizen A has 47 pair-specific gestures with Citizen B. After B's departure: those 47 gestures are gone from A's active vocabulary. A's total communicative capacity (measured as sum of all pair vocabularies) decreases. This loss is permanent and irreversible.

**Cascade effect:** If Citizen B was the only partner with whom Citizen A used certain body zones (e.g., nape Contact), A loses access to those zones entirely until a new relationship reaches sufficient depth.

**Source parallel:** When Senzo dies (Ch. IV), Nandi's nape is never touched again. The most intimate phrase in their shared Contact has no speaker left. When Enama dies (Ch. VI), the grip de calibration disappears -- Nandi must face her tremens alone.

---

## B5: Contact-Corde Operates as Degraded Channel

When citizens are physically separated but connected by a rope (or analogous link), Contact-corde provides a 2-dimensional communication channel (tension + movement) instead of the 20+ dimensions of direct Contact. Vocabulary is invented in real-time and is shared only among the rope-linked group.

**Observable:** Contact-corde messages carry lower information density, higher ambiguity, and no emotional register. The rope also transmits involuntary signals (fear, hesitation, fatigue) that are indistinguishable from intentional messages to untrained recipients. Citizens with high Contact skill can separate signal from noise; others cannot.

---

## B6: Contact-Fantome Manifests in Isolation

A citizen who has lost all partners and is under extreme physiological stress may generate Contact-fantome events -- hallucinated Contact gestures that reproduce the idiolectes of departed citizens. These events are processed identically to real Contact by the experiencing citizen's system. No flag distinguishes them from genuine Contact.

**Observable:** In the engine's logs, Contact-fantome events carry the tactile signatures of dead citizens. The experiencing citizen responds to them as if real. External observers (other systems, monitoring) can detect the absence of a living sender, but the recipient citizen's processing does not distinguish.

**Source parallel:** Nandi alone in Ch. VIII feels Senzo's warm pressure on her nape, Sihle's cold two-finger technical Contact, Enama's grip, Inyoni's counting fingers. Each phantom carries the exact signature of the dead citizen. The novel never flags these as hallucinations.

---

## B7: Contact-Monde Produces Environment Responses

Citizens who perform Contact-monde (hands or feet on the ground, hands on bioluminescent walls) receive data from the environment processed through the Contact Engine. The environment responds -- seismic frequency readings through the feet, bioluminescent light changes through the walls, echo patterns through palmed stone.

**Observable:** A citizen performing Contact-monde receives structured environmental data (seismic frequency, temperature gradient, gas composition proxied through vibration patterns). This data is formatted as Contact events with `sender: environment` and processed through the citizen's Contact vocabulary. Citizens with richer Contact-monde vocabulary extract more information from the same environmental signal.

---

## B8: Dialect Friction Between Zones

Citizens from different geographic regions experience reduced Contact intelligibility when first interacting. High-frequency zone citizens (brief, sharp gestures) and low-frequency zone citizens (slow, ample gestures) partially misread each other. Friction decreases with sustained interaction as implicit dialect negotiation occurs.

**Observable:** First interactions between cross-dialect citizens show higher misinterpretation rates, longer processing times, and more repair sequences (repeated gestures). After a convergence period proportional to dialect distance, friction decreases to baseline.

---

*Behaviors traceable to: `CONTACT.md`, `ALGORITHM_Contact.md`, `PATTERNS_Contact.md`, `PERSONNAGES.md`*
