# SYNC -- Geographie

**Module :** `worldbuilding/geographie`
**Projet :** Contre-Terre (roman litteraire)

```
LAST_UPDATED: 2026-03-11
UPDATED_BY: Claude (agent, voice)
```

---

## Maturity

**STATUS : DESIGNING**

### Ce qui est canonique (etabli dans la prose) :

- **Couches I-IV** entierement ecrites et deployees dans la prose
- **Surface desertique** (Ch. I) : sable, vibration de fond magnitude 4, architecture sismique (hamacs, cordes, caissons), volcan a l'horizon
- **Piemont volcanique** (Ch. II) : gravier basaltique, frequences seches, bioluminescence (filaments bleus, pulsent a magnitude 4, reagissent au toucher), entree en caverne
- **Village des sourds** (Ch. III) : habitations souples, amortissement 40%, bioluminescence domestiquee (sillons graves), Contact hydraulique (rigoles), Contact haute-definition (3 doigts), le geste inconnu de la vieille femme
- **Faille verticale** (Ch. IV) : 2-3m de large, 60 degres, basalte humide, soufre, Contact-corde, silence-piege, glissement de terrain, mort de Senzo
- **Nandi pieds nus** comme constante narrative
- **Le tremens** comme mecanisme de recalibrage corporel a chaque transition
- **Le schema de transition** : perception (Nandi) -> confirmation -> manifestation -> adaptation (Contact) -> seuil

### Ce qui est en design (prevu dans SQUELETTE.md, pas encore ecrit) :

- **Cavernes profondes** (Ch. V) : reseau, air rarefie, passage eau/roche, tremens maximal
- **Zones volcaniques** (Ch. VI) : fumerolles, geysers, chaleur extreme, gaz toxiques
- **Boyau** (Ch. VII) : tube 60cm, Contact force, effondrement
- **Chambre de detonation** (Ch. VIII) : coeur du volcan, lave, detonation

### Ce qui est propose (idees, pas encore dans le plan) :

- Echelles de mesure sismiques propres au monde (mentionnees "a developper" dans MONDE.md)
- Ecosysteme souterrain detaille (MONDE.md : "a developper")
- Les Archipels du Desert comme geographie evoquee plus en detail

---

## Etat des fichiers de la doc chain

| Fichier | Statut | Notes |
|---------|--------|-------|
| OBJECTIVES_Geographie.md | CREE | 5 objectifs hierarchises |
| PATTERNS_Geographie.md | CREE | 9 patterns de design |
| BEHAVIORS_Geographie.md | CREE | 9 comportements observables |
| ALGORITHM_Geographie.md | CREE | Mecaniques par couche, 5 parametres |
| VALIDATION_Geographie.md | CREE | 14 invariants, matrice de verification |
| IMPLEMENTATION_Geographie.md | CREE | Cartographie fichiers, passages cles |
| HEALTH_Geographie.md | CREE | 10 tests, tableau recapitulatif |
| SYNC_Geographie.md | CREE | Ce fichier |

---

## Ce qui a ete fait

**2026-03-11 :** Creation de la doc chain complete `docs/worldbuilding/geographie/`. Huit fichiers couvrant l'integralite du systeme geographique du roman -- de la surface desertique a la chambre de detonation. Analyse des 4 chapitres ecrits pour identifier les patterns etablis, verification de coherence, et projection sur les 4 chapitres a ecrire.

---

## Travail a venir

### Priorite haute
- **Ecrire les chapitres V-VIII** en respectant les invariants de VALIDATION_Geographie.md
- **Valider chaque chapitre ecrit** contre la matrice de HEALTH_Geographie.md

### Priorite moyenne
- **Developper l'ecosysteme souterrain** (MONDE.md mentionne "a developper") : quels organismes vivent en profondeur ? Comment se nourrissent-ils ? Les filaments bioluminescents sont-ils un organisme ou une colonie ?
- **Preciser les Archipels du Desert** : combien ? Noms ? Frequences propres ? Utile pour enrichir les backstories des personnages

### Priorite basse
- **Echelles de mesure sismiques propres** (MONDE.md) : le monde a peut-etre ses propres unites, pas Richter
- **Cartographie du village des sourds** : plan spatial pour coherence interne (pas de carte publiee -- juste un outil d'ecriture)

---

## Tensions et questions ouvertes

| Question | Impact | Notes |
|----------|--------|-------|
| Les filaments bioluminescents sont-ils un organisme unique ou une colonie ? | Faible | Enama (biologiste) pourrait le commenter au Ch. II. Pas fait explicitement. |
| Quel est le mecanisme exact de l'amortissement du village ? | Faible | Sihle note "tranchees" et "materiaux absorbants". Le detail n'est pas necessaire pour le recit. |
| Comment Nandi survit-elle pieds nus sur la roche a 90C+ ? | Moyen | Il faudra adresser cela au Ch. VI-VII. Possibilite : ses pieds sont detruits mais elle ne s'arrete pas. Le cout physique EST le recit. |
| Le boyau (Ch. VII) est-il naturel ou artificiel ? | Faible | Le SQUELETTE.md dit "tube metallique" puis les chapitres l'appellent "tube de roche." A clarifier. |
| Le silence post-detonation (epilogue) est-il total ou relatif ? | Moyen | SQUELETTE.md propose deux options : silence absolu ou "rythme change." Decision non prise. |

---

## Dependances avec d'autres modules

| Module | Nature de la dependance |
|--------|------------------------|
| `worldbuilding/contact` | La geographie modifie le mode de Contact a chaque couche. Toute modification geographique doit verifier l'impact sur le Contact. |
| `worldbuilding/seismique` | Le systeme sismique est le moteur de la geographie. Les frequences, magnitudes, et types de cataclysmes definis dans `seismique` s'appliquent a chaque couche. |
| `narration/personnages` | Les personnages sont les interfaces entre la geographie et le lecteur. Nandi (pieds), Thabo (air), Senzo (carte), Enama (sol), Sihle (sismographe). |
| `narration/structure` | La structure 8 chapitres = 8 couches est une equivalence stricte. Modifier la geographie = modifier la structure. |

---

## Handoff

**Pour l'agent qui ecrit le Ch. V :**
- Lire ALGORITHM_Geographie.md, section "Couche V"
- Verifier les invariants de VALIDATION_Geographie.md (V1-V14)
- Le groupe passe de 6 a 4 dans ce chapitre (Jabu + Sihle meurent)
- L'air se rarefie -- Thabo devient central
- Le tremens de Nandi est a son paroxysme
- Le conflit Sihle/Enama se resout par la mort des deux camps
- L'embranchement eau/roche est le mecanisme de separation
- Apres ce chapitre : plus de carte, plus de chef, plus de camp scientifique vs camp instinct. Juste quatre personnes et un volcan.

**Pour l'agent qui documente d'autres modules :**
- La doc chain geographie est complete et peut servir de modele pour les autres modules (contact, seismique, personnages, structure, metiers)
- Les invariants de VALIDATION sont les plus critiques a respecter lors de l'ecriture
- HEALTH fournit des tests concrets applicables chapitre par chapitre

---

*Derniere mise a jour : 2026-03-11*
