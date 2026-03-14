# SYNC: Narrative Engine

**Module :** `universe/narrative_engine`
**Derniere mise a jour :** 2026-03-13

---

## STATUS : DESIGNING

Le moteur narratif est entierement concu sur papier. Le doc chain est complet (8 fichiers). L'architecture est definie : trois systemes de tension paralleles alimentant le moteur ngram, avec des event generators et propagators specifiques au monde sismique de Contre-Terre.

Aucun code n'existe encore. L'implementation depend de :
1. La disponibilite du runtime ngram (copie depuis mind-platform)
2. La finalisation du Contact Engine (qui fournit les logs d'interaction)
3. La finalisation du Seismic Physics module (qui fournit les constantes de zone)
4. La finalisation du World Geography module (qui fournit la topologie spatiale)

---

## Maturity

**Ce qui est CANONICAL :**
- L'architecture a trois systemes de tension (sismique, Contact, social)
- L'integration avec ngram via hooks pre/post-phase
- Les invariants de validation (V1-V9)
- Le principe que les seismes emergent de l'accumulation de tension (pas de generation aleatoire)

**Ce qui est encore DESIGNING :**
- Les constantes exactes par zone (les valeurs du tableau ALGORITHM A2 sont indicatives, non calibrees)
- Le couplage entre les trois systemes (comment un evenement d'un systeme affecte les tensions des deux autres)
- La formule exacte de conversion energie → magnitude (logarithmique confirmee, base et offsets a calibrer)
- Le mecanisme de Contact_vitality (poids des composantes a affiner)

**Ce qui est PROPOSED (v2) :**
- Generation procedurale de nouveaux types de cataclysmes par le moteur (au-dela des 10 documentes)
- Adaptation dynamique des constantes de zone en fonction de l'historique sismique
- Mecanisme de "memoire sismique" : les zones qui ont flippe recemment conservent une trace qui modifie les flips suivants

---

## Dependencies

| Module | Statut | Ce qu'il fournit |
|--------|--------|-----------------|
| `universe/contact_engine` | DESIGNING | Logs d'interaction, metrique Contact_vitality |
| `universe/seismic_physics` | DESIGNING | Constantes de zone, modele de tremens |
| `universe/world_geography` | DESIGNING | Topologie spatiale, liens entre zones |
| `universe/citizen_model` | DESIGNING | Types de citoyens (predicteur, ecouteur, etc.) |
| ngram runtime (mind-platform) | EXISTANT | Phases physiques, graph operations |

---

## Ce qui a ete fait

- [2026-03-13] Creation du doc chain complet (8 fichiers)
- [2026-03-13] Architecture des trois systemes de tension definie
- [2026-03-13] Constantes indicatives par zone documentees (ALGORITHM A2)
- [2026-03-13] 9 invariants de validation documentes (VALIDATION V1-V9)
- [2026-03-13] Architecture d'integration avec ngram documentee (IMPLEMENTATION I1)
- [2026-03-13] 7 signaux de sante documentes (HEALTH H1-H7)
- [2026-03-13] PATTERNS enrichi : adaptation Venezia blood-ledger (axe economique → axe sismique)
- [2026-03-13] BEHAVIORS enrichi : B7 (mort cascade a travers les 3 systemes) + B8 (magnitude 11 = convergence des 3 tensions)
- [2026-03-13] ALGORITHM enrichi : A6 (formule Contact_vitality avec poids, composantes, courbe du roman) + A7 (narrative backflow, Contact-fantome comme backflow maximal)

---

## Prochaines etapes

1. **Calibration des constantes** — Simuler les constantes par zone avec un prototype minimal pour verifier que les cycles tension-relachement correspondent au rythme narratif du roman (cycles courts en surface, acceleration en profondeur, accumulation en grotte finale)
2. **Definir le couplage** — Documenter precisement comment chaque type d'evenement affecte les tensions des deux autres systemes (matrice de couplage)
3. **Implementer les tension computers** — Les trois fichiers `*_tension_*_computer.py` sont le minimum viable pour un premier tick
4. **Tester avec le Contact Engine** — Alimenter les tension computers avec des interactions Contact simulees et verifier que des percees/ruptures emergent
5. **Valider V1 et V6** — Les deux invariants les plus critiques (tension jamais zero, determinisme) doivent etre les premiers testes

---

## HANDOFF: FOR AGENTS

**Likely agent subtype:** groundwork (implementation des tension computers et event generators)

**Key context:**
- Le moteur ne reimplemente pas ngram -- il injecte des hooks specifiques au monde sismique
- Les trois systemes de tension sont paralleles mais couples
- Les constantes par zone sont indicatives (ALGORITHM A2) -- la calibration est le travail principal de la prochaine phase
- L'invariant V9 (magnitude 11 unique) est structurel : sans la Charge (resonateur), la tension ne peut pas atteindre ce niveau

**Watch out for:**
- Ne pas reimplementer les phases ngram existantes (generation, moment_draw, etc.)
- Ne pas rendre les seismes aleatoires (l'invariant V6 est non-negociable)
- Le Contact Engine doit exister avant que le Contact tension computer puisse fonctionner
- Les constantes sont sensibles : un petit changement de decay_rate change radicalement le comportement du monde

---

*Sources : OBJECTIVES, PATTERNS, BEHAVIORS, ALGORITHM, VALIDATION, IMPLEMENTATION, HEALTH — tous dans `docs/universe/narrative_engine/`*
