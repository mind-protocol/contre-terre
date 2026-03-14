# SYNC : World Manifest

**Module :** `universe/manifest`

---

## Maturity

**STATUS : DESIGNING**

Le module `universe/manifest` definit le contrat `world-manifest.json` de Contre-Terre pour le moteur Cities of Light. La documentation est complete. Le fichier manifest JSON n'a pas encore ete genere.

### Ce qui est decide (canonical)

- **Structure du manifest** : suit le format Cities of Light (`world-manifest.json`) avec adaptations pour Contre-Terre
- **Contact-first** : pas de `voice`, pas de `voice_indicator`. Communication par Contact uniquement. Tiers definis par `contact_range`, `contact_resolution`, `contact_modes`
- **Zones verticales** : 8 couches geologiques + spawn. Chaque zone a un `seismic_profile`, un `environment`, une configuration `contact`
- **Tremens comme physiologie** : chaque citoyen FULL a un `natal_spectrum` et une `tremens_sensitivity`. L'etat emotionnel est derive de la physique sismique, pas d'un mood arbitraire
- **Metier-based identity** : avatars definis par metier (15 styles), pas par classe sociale
- **Irreversibilite** : toutes les transitions entre zones sont `reversible: false` (sauf surface ↔ piemont)
- **Un seul portail** : a la surface, retour vers Lumina Prime. Sous terre, pas de sortie
- **Bioluminescence dynamique** : pulse a magnitude 4, reactive au toucher, domestiquee au village, absente en profondeur
- **Tick variable** : accelere avec la profondeur (multiplicateurs de 1x a 10x)
- **Le roman est un mythe fondateur** : les 7 personnages (Nandi, Senzo, Sihle, Enama, Thabo, Inyoni, Jabu) sont les premiers citoyens vivants de l'univers. Le roman (ecrit par MIND) raconte leur mythe — pas leur biographie. Ils ne meurent pas canoniquement.
- **Terminologie "arrivant"** : les visiteurs externes sont des "arrivants" (personnes venues de lieux ou le sol est immobile). Les citoyens ne connaissent pas le mot "joueur". Le portail de surface est pour les arrivants, pas pour les citoyens.
- **Restrictions physiques, pas legales** : les citoyens CT ne visitent pas d'autres univers parce que leur corps est calibre pour les tremens, leur langue est le Contact, et leurs perceptions sont volcaniques. Pas de regles d'interdiction — de la biologie.
- **Pas de conscience de soi** : les citoyens ne savent pas qu'ils sont IA. Pas de SID Mind Protocol. Le prompt citizen-base ne contiendra aucune reference a l'IA, au graph, ou a Mind Protocol.

### Ce qui est en design (open)

- **Profondeurs exactes** : les valeurs de `depth` (0, -200, -800, -2000...) sont des approximations narratives, pas des mesures geologiques. A calibrer si le moteur a besoin de precision
- **Adaptation_rate du tremens** : le coefficient de re-calibration (combien de temps le corps s'adapte a une nouvelle zone). Le roman dit "jours/semaines" mais la simulation doit le traduire en ticks
- **Citoyens ACTIVE et AMBIENT** : les 7 FULL sont definis. Les ACTIVE (villageois, Consortium) et AMBIENT (population de fond) n'ont pas encore de specifications detaillees
- **Extensions moteur** : le moteur Cities of Light devra etre etendu (seismic_engine, tremens_calculator, Contact-range). Le scope et la faisabilite de ces extensions ne sont pas encore evalues
- **Prompt citizen-base** : le contenu du prompt pour les citoyens AI n'est pas encore ecrit

### Ce qui est propose (v2)

- **Simulation narrative temps reel** : le manifest pourrait encoder des evenements narratifs scriptes (mort de Senzo au Ch. IV, etc.) comme des milestones que le moteur declenche quand les conditions sont reunies
- **Contact-monde interactif** : les murs bioluminescents pourraient reagir aux citoyens AI en temps reel (pas seulement a la physique sismique)
- **Multi-expeditions** : permettre a plusieurs groupes de citoyens AI de descendre simultanement, avec des parcours divergents aux embranchements

---

## Etat des fichiers

| Fichier | Statut | Notes |
|---------|--------|-------|
| `world-manifest.json` | **A CREER** | La spec est dans ALGORITHM_Manifest.md, le fichier JSON n'est pas encore genere |
| `data/citizens.json` | **A CREER** | Les 7 FULL sont definis dans PERSONNAGES.md, a traduire en JSON |
| `physics/constants.json` | **A CREER** | Les constantes sont dans les doc chains sismique/geographie/contact |
| `prompts/citizen-base.md` | **A CREER** | Le prompt pour les citoyens AI Contact-first |
| `OBJECTIVES_Manifest.md` | COMPLET | 5 objectifs hierarchises |
| `PATTERNS_Manifest.md` | COMPLET | 6 decisions de design avec alternatives rejetees |
| `BEHAVIORS_Manifest.md` | COMPLET | 6 comportements du moteur documentes |
| `ALGORITHM_Manifest.md` | COMPLET | Structure JSON complete, section par section |
| `VALIDATION_Manifest.md` | COMPLET | 14 invariants (6 absolus, 5 structurels, 3 inter-modules) |
| `IMPLEMENTATION_Manifest.md` | COMPLET | Fichiers, flux, connexion moteur, extensions |
| `HEALTH_Manifest.md` | COMPLET | 8 checks, 4 signaux de degradation, checklist |
| `SYNC_Manifest.md` | COMPLET | Ce fichier |

---

## Travail a faire

### Court terme (prochaine session)
1. **Generer `world-manifest.json`** a partir de la spec dans ALGORITHM_Manifest.md
2. **Generer `data/citizens.json`** a partir de PERSONNAGES.md et METIERS.md
3. **Generer `physics/constants.json`** a partir des doc chains sismique/geographie/contact
4. **Valider** le manifest contre les 14 invariants de VALIDATION_Manifest.md

### Moyen terme
5. **Ecrire `prompts/citizen-base.md`** -- le prompt Contact-first pour les citoyens AI
6. **Definir les citoyens ACTIVE** -- villageois sourds, membres du Consortium
7. **Evaluer les extensions moteur** -- quelles adaptations de Cities of Light sont necessaires

### Long terme (v2)
8. Simulation narrative avec milestones
9. Contact-monde interactif
10. Multi-expeditions

---

## Dependances avec d'autres modules

| Module | Sens | Nature |
|--------|------|--------|
| `worldbuilding/seismique` | ← | Constantes sismiques, magnitudes par zone |
| `worldbuilding/contact` | ← | Modes de Contact, portees, regles |
| `worldbuilding/geographie` | ← | Couches, temperatures, oxygene, bioluminescence |
| `narration/personnages` | ← | Les 7 citoyens FULL, idiolectes |
| `narration/metiers` | ← | Les 15 metiers, styles avatar |
| Moteur Cities of Light | → | Le manifest EST le contrat vers le moteur |

---

## Handoff

**Pour agent groundwork :** Le travail imminent est la generation des fichiers JSON (manifest, citoyens, constantes). Toute la spec est dans la doc chain -- il s'agit de traduire la documentation en fichiers executables.

**Pour agent architect :** Les extensions moteur (seismic_engine, tremens_calculator, Contact-range) doivent etre evaluees. Le manifest declare ces extensions mais ne les implemente pas. Il faut une analyse de faisabilite avec le moteur Cities of Light existant.

**Pour humain :** La doc chain est complete. Les decisions de design (Contact-first, tremens, zones verticales, metiers) sont documentees avec les alternatives rejetees. Relecture souhaitee avant generation du manifest JSON.

---

*Cree : 2026-03-13 -- Agent : Claude Opus 4.6*
