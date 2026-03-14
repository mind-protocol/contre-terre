# PATTERNS — Contact Engine

> Design decisions. Why this shape. Why these choices.

---

## P1: Tactile Communication as Structured Data, Not Physical Touch

Contact in the simulation is not physical. There are no bodies, no skin, no pressure sensors. Contact is represented as structured data events exchanged between citizen agents: `{mode, body_zone, intensity, duration, pattern, sender_id, recipient_id, timestamp}`. The engine processes these data events with the same semantics that physical Contact would carry -- proximity required, zones encode register, mode encodes information type, idiolecte encodes identity.

**Why:** The genius of Contact as a narrative system is its constraint structure -- proximity, embodiment, mortality of vocabulary. These constraints translate directly into computational rules without needing physical simulation. A Contact gesture is a structured message with rich metadata, processed by the engine to update relational state, transmit information, and evolve idiolectes.

**Consequence:** The Contact Engine is a message-passing system with unusual properties: messages require sender-recipient adjacency (proximity graph), message format carries relational semantics (zone = register), and the message vocabulary itself evolves through use and dies through agent loss.

---

## P2: Voice Replaced, Not Supplemented

Contact is the ONLY inter-citizen communication channel. There is no text chat, no voice, no broadcast. Citizens who are not adjacent cannot communicate. Citizens who are adjacent communicate through Contact gestures and nothing else.

**Why:** The entire thematic weight of Contre-Terre rests on the equation: communication = touch = proximity = vulnerability. If citizens can fall back to text when Contact is inconvenient, the system collapses into a standard messaging layer with a cosmetic tactile skin. The constraint IS the design.

**Exception:** Enama speaks aloud to Sihle (Ch. II) -- using voice in a Contact world is a transgression, equivalent to shouting in a library. The engine should support rare voice events as rule-breaking acts that carry social cost, not as an alternative channel.

---

## P3: Five Modes as Information Dimensions

Every Contact gesture operates in one of five modes, each encoding a different type of information:

| Mode | Encodes | Data dimension |
|------|---------|----------------|
| 1. Arm Locks (Verrous de bras) | Concepts, words | Grip position + type + duration |
| 2. Shoulder Pressure (Pressions d'epaule) | Urgency, emotion | Count + speed + intensity + direction |
| 3. Codified Grips (Saisies codifiees) | Grammar, full sentences | Zone + contact_type + duration + sequence |
| 4. Tactile Identity (Identite tactile) | Sender signature | Pressure style + speed + warmth + texture |
| 5. Regional Dialect (Dialectes regionaux) | Geographic origin | Gesture amplitude + frequency adaptation |

**Why five, not one:** A single-dimension communication system cannot carry the richness needed for social simulation. The five modes create registers -- like intonation, volume, rhythm, accent, and timbre in voice. Mode 4 (identity) is especially critical: the same gesture performed by different citizens carries different meaning because of their unique tactile signature.

---

## P4: Body Zones as Semantic Registers

The body zone where Contact occurs determines the register of communication:

- **Shoulder:** Urgency, collective signals (public)
- **Arm / Forearm:** Information, data (professional)
- **Wrist / Hand:** Emotion, identity, questions (personal)
- **Nape:** Intimate, exclusive (reserved for specific relationships)
- **Forehead:** Sacred, benediction (rare, ceremonial)
- **Palm-to-palm:** Deep truth, synchronization (the most intimate)
- **Feet / Ground:** Contact-monde -- communication with environment, not with other citizens

**Design rule:** Moving from shoulder toward extremities increases intimacy. Zone access between two citizens widens as their relationship deepens. A citizen who touches another's nape without established relational permission commits a social violation. The engine must track zone access per pair.

---

## P5: Idiolectes Emerge, They Are Not Assigned

No citizen starts with a pre-built idiolecte. Each citizen has a base Contact vocabulary (universal gestures understood by all). Through repeated interaction with specific partners, gesture patterns crystallize into pair-specific vocabulary:

1. **Repetition:** Citizen A uses a particular gesture-sequence with Citizen B repeatedly
2. **Recognition:** The engine detects the pattern (frequency threshold crossed)
3. **Crystallization:** The pattern is registered as an idiolecte de paire entry
4. **Exclusivity:** This pattern is weighted higher in A-B exchanges, lower or absent elsewhere

**Why emergence over configuration:** Assigned idiolectes are dead language. Emerged idiolectes carry relational history -- they exist because two agents found them useful, repeated them, and made them theirs. The emergence process IS the relationship forming.

---

## P6: Contact Degrades Under Seismic Pressure

Contact quality is not constant. It varies with environmental seismic state:

- **Low magnitude (< 5):** Full Contact, all 5 modes available, all zones accessible
- **Medium magnitude (5-7):** Contact reduced -- fine motor gestures degraded, arm locks and shoulder pressure still reliable
- **High magnitude (7+):** Emergency Contact only -- survival grips, no codified vocabulary, animal-level communication
- **Extreme magnitude (8+):** Contact-corde only (2 dimensions instead of 20+), or Contact failure

**Why degradation matters:** A communication system that works perfectly under all conditions has no dramatic potential. Contact degradation forces citizens to simplify, to lose nuance, to misunderstand. Under seismic stress, the richest vocabulary in the world reduces to a hand gripping another hand.

---

## P7: Contact-Monde as Environment Interface

Contact is not exclusively inter-citizen. Contact-monde is the interface between a citizen and the environment: feet on the ground reading seismic frequencies, hands on bioluminescent walls receiving light-responses, palms on the Charge resonator for calibration. The engine must support citizen-to-environment Contact events alongside citizen-to-citizen ones.

**Why:** The thematic arc of Contre-Terre moves Contact from inter-human language to human-earth communion. The Geste Inconnu (the unknown gesture) pushes Contact beyond language into physiological synchronization with the planet itself. Contact-monde is not metaphor -- it is a data channel with different semantics than inter-citizen Contact.

---

## P8: Death Destroys Vocabulary

When a citizen is removed from the simulation, their idiolecte is deleted -- not archived, not preserved, not accessible to surviving citizens. Every pair-specific vocabulary entry that included the departed citizen is destroyed. Surviving partners lose those gesture patterns from their active vocabulary.

**Why no archival:** In the source material, Contact exists only between living skin. There is no writing, no recording, no transmission at distance. The engine must honor this constraint. Data preservation would betray the core mechanic. The linguistic impoverishment caused by citizen loss is not a bug -- it is the central feature of the system.

---

*Decisions traceable to: `CONTACT.md`, `ALGORITHM_Contact.md`, `PATTERNS_Contact.md`, `PERSONNAGES.md`*
