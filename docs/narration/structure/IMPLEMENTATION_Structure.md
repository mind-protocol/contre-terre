# IMPLEMENTATION: Structure Narrative

**Module :** `narration/structure`
**Source de verite :** `STRUCTURE.md`, `SQUELETTE.md`
**Derniere mise a jour :** 2026-03-11

---

## Ou vit le contenu structurel

Ce projet est un roman litteraire. Il n'y a pas de code — il y a des fichiers de texte. Ce document localise chaque element structurel dans le systeme de fichiers.

---

## Fichiers source (worldbuilding & planification)

| Fichier | Contenu | Role structurel |
|---------|---------|-----------------|
| `CONCEPT.md` | Premisse, inversion de Damasio, themes | Fondation thematique |
| `STRUCTURE.md` | 8 chapitres = 8 couches, scenes cles, influences | Architecture narrative de haut niveau |
| `SQUELETTE.md` | Squelette complet : arcs, personnages, chapitrage scene par scene | **Document de reference principal** pour l'ecriture |
| `PERSONNAGES.md` | 7 personnages, arcs, dynamiques | Arcs individuels et interactions |
| `CONTACT.md` | Systeme linguistique tactile, 5 modes, mort linguistique | Colonne vertebrale du Contact |
| `MONDE.md` | Systeme sismique, tremens, architecture, faune | Worldbuilding physique |
| `METIERS.md` | 15 metiers, cascade de competences | Repartition et perte de competences |

### Hierarchie des sources pour les decisions structurelles

```
SQUELETTE.md (scene par scene)
    ↓ derive de
STRUCTURE.md (architecture)
    ↓ derive de
CONCEPT.md (premisse)
```

En cas de contradiction, `SQUELETTE.md` fait autorite pour l'ordre des scenes et des morts. `STRUCTURE.md` fait autorite pour les principes structurels. `CONCEPT.md` fait autorite pour le theme.

---

## Fichiers narratifs (chapitres ecrits)

| Fichier | Chapitre | Mots | Statut |
|---------|----------|------|--------|
| `chapitre_01.md` | I — Surface du Desert | ~9 700 | CANONICAL |
| `chapitre_02.md` | II — Zones Intermediaires | ~20 500 | CANONICAL |
| `chapitre_03.md` | III — Le Dernier Village | ~22 600 | CANONICAL |
| `chapitre_04.md` | IV — La Faille | ~31 200 | CANONICAL |
| `chapitre_05.md` | V — Cavernes Profondes | — | A ECRIRE |
| `chapitre_06.md` | VI — Zones Volcaniques | — | A ECRIRE |
| `chapitre_07.md` | VII — Interieur du Volcan | — | A ECRIRE |
| `chapitre_08.md` | VIII — Grotte Finale | — | A ECRIRE |

### Convention de nommage

Les fichiers de chapitres suivent le format `chapitre_XX.md` ou XX est le numero a deux chiffres (01-08). Chaque fichier commence par le titre du chapitre en H1, suivi des scenes en H2.

### Format interne des chapitres

```markdown
# [Numero] — [Titre]

## Scene [N] — [Titre de scene]

[Prose]

---

## Scene [N+1] — [Titre de scene]

[Prose]
```

Les scenes sont separees par des lignes horizontales (`---`). Chaque scene a un titre descriptif court.

---

## Documentation (doc chain)

| Fichier | Contenu | Chemin |
|---------|---------|--------|
| OBJECTIVES | Ce que la structure optimise | `docs/narration/structure/OBJECTIVES_Structure.md` |
| PATTERNS | Decisions de design | `docs/narration/structure/PATTERNS_Structure.md` |
| BEHAVIORS | Effets observables | `docs/narration/structure/BEHAVIORS_Structure.md` |
| ALGORITHM | Mecanique scene par scene | `docs/narration/structure/ALGORITHM_Structure.md` |
| VALIDATION | Invariants | `docs/narration/structure/VALIDATION_Structure.md` |
| IMPLEMENTATION | Ce fichier | `docs/narration/structure/IMPLEMENTATION_Structure.md` |
| HEALTH | Checks de qualite | `docs/narration/structure/HEALTH_Structure.md` |
| SYNC | Etat courant | `docs/narration/structure/SYNC_Structure.md` |

---

## Relations avec les autres modules

### Modules dependants

| Module | Relation | Direction |
|--------|----------|-----------|
| `narration/personnages` | Les arcs des personnages s'inscrivent dans la structure des chapitres | structure → personnages |
| `narration/metiers` | La cascade de competences depend de l'ordre des morts | structure → metiers |
| `worldbuilding/contact` | L'erosion du Contact est dicte par la structure des morts | structure → contact |
| `worldbuilding/geographie` | Chaque chapitre = une couche geologique | structure ← geographie |
| `worldbuilding/seismique` | Les seismes rythment les chapitres | structure ← seismique |

### Flux de decisions

```
geographie (couches) ──→ structure (chapitres) ──→ personnages (arcs)
                                    │
seismique (seismes)  ──→            ├──→ contact (erosion)
                                    │
                                    └──→ metiers (cascade)
```

La geologie determine la structure. La structure determine les arcs, l'erosion et la cascade.

---

## Processus d'ecriture d'un nouveau chapitre

### Etapes

1. **Lire le squelette** — `SQUELETTE.md`, section du chapitre concerne
2. **Lire le chapitre precedent** — Verifier l'etat des survivants, le vocabulaire Contact restant, les tensions ouvertes
3. **Verifier les invariants** — `VALIDATION_Structure.md` : POV, pas d'exposition, ouverture sensorielle
4. **Ecrire les scenes** — Dans l'ordre du squelette, en respectant les transitions
5. **Verifier l'erosion** — Les gestes des morts ont-ils disparu ? De nouveaux gestes sont-ils inventes par necessite (pas par confort) ?
6. **Verifier la fermeture** — La derniere phrase est-elle un seuil ?
7. **Mettre a jour SYNC** — `SYNC_Structure.md` et `.mind/state/SYNC_Project_State.md`

### Checklist pre-ecriture

- [ ] Quels personnages sont encore vivants ?
- [ ] Quels gestes de Contact sont encore disponibles ?
- [ ] Quel est le POV principal ? Le secondaire ?
- [ ] Quelle est la couche geologique ? Ses contraintes physiques ?
- [ ] Y a-t-il une mort dans ce chapitre ? Qui ? Comment ?
- [ ] Le geste inconnu de la vieille femme doit-il etre mentionne ?
- [ ] Quelle est la tension narrative principale du chapitre ?
