# SYNC -- Context Assembly

> Etat actuel du module. Ou on en est, ce qui est fait, ce qui reste.

```
LAST_UPDATED: 2026-03-13
UPDATED_BY: Claude Opus 4.6 (agent, voice)
STATUS: DESIGNING
```

---

## Etat General

Le module context_assembly definit comment assembler les prompts des citoyens de Contre-Terre. Le pipeline adapte l'architecture de Venezia (`poc_mind_context_assembly.py`) en remplacant l'economie par le corps, les classes sociales par les metiers, le trust numerique par l'historique Contact, et en ajoutant un substrat sismique permanent qui n'a pas d'equivalent dans Venezia.

La doc chain est complete (8 fichiers). Le design est stable. L'implementation n'a pas commence -- le module est en phase de specification.

---

## Maturity

**STATUS: DESIGNING**

**Ce qui est canonique :**
- La structure en 6 blocs (PATTERNS P2) -- substituant la structure Venezia
- Le mood triaxial tremens x Contact x physique (PATTERNS P3) -- pas de scores Ekman
- Le filtre metier comme angle de perception (PATTERNS P4)
- Les invariants (VALIDATION V1-V10) -- pas de finance, sismique toujours present, morts au passe
- Le pipeline A1-A6 (ALGORITHM) -- ordre des etapes et pseudocode
- **Traduction semantique AVANT le pipeline (nouveau)** -- la parole de l'arrivant est mappee par embeddings au concept CT le plus proche dans le graph cerebral du citoyen (347 noeuds). Ce step intervient AVANT A1, il transforme l'input externe en input coherent avec le vocabulaire du citoyen. "Facebook" → "village/archipel", "iPhone" → "instrument/sismographe", "money" → "eau/ressource". Le vocabulaire de traduction = les noeuds du brain seed du citoyen.
- **Terminologie "arrivant"** -- le bloc [CE QU'ILS T'ONT DIT] reference un "arrivant", pas un "joueur". Le citoyen ne sait pas ce qu'est un joueur.

**Ce qui est encore en design :**
- Les templates metier-specifiques pour chaque profession (15 metiers, chacun avec son vocabulaire sensoriel)
- Le calibrage exact de la MOOD_MATRIX (seuils de richness, intensite)
- La generation des descriptions Contact qualitatives (comment traduire un historique de gestes en texte naturel)
- Le format exact des sorties `metier_perception()` et `contact_behavior_constraints()`
- L'algorithme exact de la traduction semantique (nearest neighbor dans l'espace d'embedding, seuil de distance, fallback si aucun concept proche)

**Ce qui est propose (v2) :**
- Contact-fantome dans le prompt (Nandi seule, Ch. VIII) -- hallucinations tactiles comme bloc additionnel
- Degradation progressive du system prompt (le system prompt lui-meme se simplifie a mesure que les partenaires meurent)
- Interferences tremens - Contact (le tremens eleve brouille la lecture Contact)

---

## Architecture de Reference

Le pipeline Venezia (`poc_mind_context_assembly.py`) est la reference structurelle. Les adaptations sont documentees dans IMPLEMENTATION :

| Composant Venezia | Adaptation Contre-Terre | Statut |
|-------------------|------------------------|--------|
| `compute_financial_state()` | `compute_physical_state()` | Specifie (ALGORITHM A1) |
| `social_class` - registre | `metiers` - filtre sensoriel | Specifie (PATTERNS P4) |
| `trust_score` | historique Contact | Specifie (PATTERNS P6) |
| `ekman_mood` | MOOD_MATRIX triaxial | Specifie (ALGORITHM A3) |
| `recent_interactions` (social) | `recent_interactions` (Contact) | Specifie (ALGORITHM A2) |
| -- (pas d'equivalent) | `query_seismic_situation()` | Specifie (ALGORITHM A5) |

---

## Dependances

```
citizen_model ──────→ context_assembly (identite, tremens, idiolectes)
contact_engine ─────→ context_assembly (interactions recentes, registres)
seismic_physics ────→ context_assembly (magnitude, tendance, frequence)
world_geography ────→ context_assembly (temperature, air, frequence locale)
narrative_engine ───→ context_assembly (croyances, rumeurs)
```

Aucun de ces modules n'est encore implemente. Le context_assembly est le consommateur -- il tire des donnees mais ne produit que du texte (prompt).

---

## Ce Qui Reste a Faire

### Specification (priorite haute)
- [ ] Templates metier : ecrire les 15 templates de `metier_perception()` -- un par metier, avec vocabulaire sensoriel specifique
- [ ] Templates Contact : definir `contact_behavior_constraints()` -- comment le niveau de saturation modifie les contraintes de reponse
- [ ] Descriptions qualitatives : comment traduire `{partner: "Senzo", registers: ["nuque", "main"], frequency: 47}` en "Senzo te touchait la nuque. Personne d'autre ne le faisait. Il est mort."

### Implementation (priorite moyenne, depend des modules source)
- [ ] Implementer `compute_physical_state()` -- connexion au citizen_model et world_geography
- [ ] Implementer `compute_contact_state()` -- connexion au contact_engine
- [ ] Implementer `compute_mood()` -- la MOOD_MATRIX en code
- [ ] Implementer `assemble_prompt()` -- production du texte final
- [ ] Tests : generer un prompt pour Nandi (Ch. I), Nandi (Ch. VIII), Thabo (Ch. VI), Sihle (Ch. IV) -- verifier que les invariants VALIDATION tiennent

### Validation (priorite haute, peut commencer sans code)
- [ ] Test papier : ecrire a la main un prompt pour Nandi avec tremens eleve, Contact affame, pieds degrades. Le soumettre a un LLM. La reponse sent-elle le monde sismique ?
- [ ] Test de differentiation : ecrire deux prompts (Aeromaitre vs Predictrice) dans la meme zone. Les reponses divergent-elles sur la perception ?
- [ ] Test d'appauvrissement : comparer un prompt Contact-sature vs Contact-affame pour le meme citoyen. L'affame est-il mesurablment plus pauvre ?

---

## Handoff

**Pour l'agent groundwork (implementation) :**
- Lire la doc chain dans l'ordre : OBJECTIVES - PATTERNS - BEHAVIORS - ALGORITHM - VALIDATION - IMPLEMENTATION
- Le pseudocode dans ALGORITHM est la specification -- l'implementer en Python
- Les 5 modules source n'existent pas encore en code -- commencer par des mocks qui retournent les structures attendues
- Premier test : generer un prompt pour un citoyen-type et verifier la checklist HEALTH

**Pour Nicolas :**
- Le design du pipeline est complet. L'inversion Venezia - Contre-Terre est documentee.
- Decision en attente : les templates metier (15 professions x vocabulaire sensoriel) -- faut-il les ecrire manuellement ou les deriver des chapitres existants ?
- Le test papier peut etre fait des maintenant sans code : ecrire un prompt a la main, le donner a un LLM, observer si le citoyen sent le sol.

---

*Derniere mise a jour : 2026-03-13*
