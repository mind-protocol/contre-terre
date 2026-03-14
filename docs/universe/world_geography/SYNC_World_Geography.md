# SYNC -- World Geography

**Module :** `universe/world_geography`
**Univers :** Cities of Light -- 3e univers (Contre-Terre)

```
LAST_UPDATED: 2026-03-13
UPDATED_BY: Claude Opus 4.6 (agent)
```

---

## Maturity

**STATUS: DESIGNING**

### Ce qui est canonique

- **Structure concentrique a 6 anneaux** : Surface (Archipels) > Piemont > Entree/Village > Faille > Cavernes profondes > Zones volcaniques > Grotte finale. La topologie est fixe -- elle decoule de 8 chapitres ecrits.
- **Parametres de zone** : Les 6 parametres definissants (magnitude, temperature, Contact dialect, fauna, connexions, habitabilite) sont stables et documentes dans ALGORITHM.
- **Schema de donnees** : Le format YAML des zones est defini, avec le mapping Mind (zones = `space`, connexions = `link`).
- **Invariants** : 12 invariants documentes dans VALIDATION. Les gradients de temperature, magnitude, habitabilite et air sont valides contre les 8 chapitres.
- **Les 8 couches du roman** : Chaque couche a ses parametres physiques tires de `ALGORITHM_Geographie.md` et verifies contre la prose ecrite (Ch. I-IV canoniques, Ch. V-VIII 1er brouillon).
- **Diversite des Archipels** : Les Archipels de surface sont documentes comme communautes distinctes avec des spectres sismiques propres. Les origines des personnages (Nandi = nord-est, Senzo = sud) sont ancrees dans cette geographie.

### Ce qui est en cours de design

- **Nombre et identite des Archipels** : Les Archipels du sud et du nord-est sont nommes. Les Archipels de l'ouest (frequences moyennes, roulantes) sont mentionnes dans les patterns mais pas encore formalises en zones.
- **Faune detaillee par zone** : La faune est definie par categories (filaments, extremophiles, vegetation profonde) mais pas par espece. Ce niveau de detail est hors scope pour le moment.
- **Implementation technique** : Aucun fichier YAML de zone ni code de navigation n'existe encore. Le systeme est documente mais pas implemente.

### Ce qui est propose (futur)

- **Evenements sismiques dynamiques** : L'algorithme de modification des connexions par seismes est documente mais pas encore simule. Priorite basse -- le roman n'a pas besoin de simulation dynamique.
- **Archipels supplementaires** : Les 7 archipels majeurs mentionnes dans PERSONNAGES.md (Consortium des Archipels) ne sont pas encore formalises individuellement.

---

## Etat de la documentation

| Fichier | Statut | Notes |
|---------|--------|-------|
| `OBJECTIVES_World_Geography.md` | Complet | 5 objectifs hierarchises, non-objectifs |
| `PATTERNS_World_Geography.md` | Complet | 7 patterns, scope IN/OUT |
| `BEHAVIORS_World_Geography.md` | Complet | 8 comportements observables |
| `ALGORITHM_World_Geography.md` | Complet | Schema de donnees, 8 zones definies, graphe de connexions, regles sismiques |
| `VALIDATION_World_Geography.md` | Complet | 12 invariants (5 absolus, 5 structurels, 2 inter-modules) |
| `IMPLEMENTATION_World_Geography.md` | Complet | Sources de verite, format YAML, mapping Mind, graphe, relations modules |
| `HEALTH_World_Geography.md` | Complet | 8 checks de sante |
| `SYNC_World_Geography.md` | Ce fichier | |

**Doc chain : COMPLETE (8/8 fichiers)**

---

## Provenance

Ce module (`universe/world_geography`) derive de la doc chain `worldbuilding/geographie/` (documentation du roman) et la transpose dans le contexte du 3e univers des Cities of Light. Les deux coexistent :

- `docs/worldbuilding/geographie/` = la geographie telle qu'elle sert le roman (narratif, par chapitre)
- `docs/universe/world_geography/` = la geographie telle qu'elle sert le systeme (structure de donnees, invariants, implementation)

Les decisions de design sont les memes. Le format change.

---

## Dependances

| Depend de | Nature |
|-----------|--------|
| `worldbuilding/geographie` | Source des parametres physiques par couche |
| `worldbuilding/seismique` | Modele sismique, echelle de magnitudes |
| `worldbuilding/contact` | Dialectes, modes du Contact, degradation par zone |
| `MONDE.md` | Fondation du systeme sismique et des Archipels |
| `PERSONNAGES.md` | Origines des personnages = calibration des Archipels |
| Chapitres I-VIII | Verification de coherence prose/systeme |

---

## Handoff

**Pour un agent `groundwork` :** Les fichiers `zones.yaml` et `connections.yaml` listes dans IMPLEMENTATION sont prets a etre crees. Le schema est documente. Les donnees sont dans ALGORITHM. Il s'agit de transcrire, pas de concevoir.

**Pour un agent `keeper` :** Les 12 invariants de VALIDATION et les 8 checks de HEALTH sont la grille de verification. Tout ajout de zone ou modification de connexion doit passer ces tests.

**Pour un agent `weaver` :** Les relations inter-modules sont documentees dans IMPLEMENTATION. Si le module `universe/contact_engine` ou `universe/seismic_physics` evolue, verifier que les `contact_dialect_modifier` et `base_magnitude` restent coherents.

---

*Sync initial -- module world_geography. Doc chain complete, implementation a venir.*
