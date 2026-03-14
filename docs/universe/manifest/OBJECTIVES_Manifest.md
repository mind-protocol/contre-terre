# OBJECTIVES : World Manifest

**Module :** `universe/manifest`
**Question centrale :** Qu'est-ce que le world-manifest de Contre-Terre doit optimiser pour que le moteur Cities of Light instancie correctement ce monde ?

---

## O1 : Contact-first communication (priorite maximale)

Le manifest de Venezia definit des tiers par `voice` (true, proximity, false) et `radius`. Contre-Terre ne peut pas utiliser ce schema. Il n'y a pas de voix. Il n'y a pas de distance sonore. La communication passe par le Contact -- un langage tactile qui exige la proximite physique, le toucher direct, ou un medium intermediaire (corde, hydraulique, bioluminescence).

**Ce que ca optimise :** Le manifest doit remplacer `voice` par `contact_range` -- la distance maximale a laquelle deux entites peuvent se toucher. Ce parametre varie selon le mode de Contact (direct, corde, hydraulique, monde) et selon la zone geographique (le boyau force le Contact, le desert l'espace). Les tiers d'entites ne sont pas des niveaux de "privilege verbal" mais des niveaux de resolution tactile : FULL = Contact complet (5 modes, idiolecte, emotions), ACTIVE = Contact fonctionnel (ordres, directions, urgence), AMBIENT = Contact basal (presence, battement de coeur du groupe).

---

## O2 : Environnement sismique comme physique de base

Venezia definit `terrain.water_level`, `sun.elevation`, `global_atmosphere`. Contre-Terre a besoin de `seismic_baseline` -- la magnitude de fond qui pulse en permanence. L'equivalence : comme l'eau est a Venise, le tremblement est a Contre-Terre. C'est la physique constitutive du monde, pas un evenement ponctuel.

**Ce que ca optimise :** Chaque zone a une signature sismique (frequence, amplitude, caractere) qui affecte tout : le tremens des citoyens, le comportement de la bioluminescence, la degradation du Contact, la viabilite des structures. Le manifest encode cette physique pour que le moteur puisse simuler un sol qui ne s'arrete jamais de trembler.

---

## O3 : Zones comme couches geologiques, pas comme districts

Venezia utilise des zones geographiques planes (sestieri, ponts, canaux). Contre-Terre est vertical. Les zones sont des couches : surface desertique, piemont volcanique, village souterrain, faille verticale, cavernes profondes, zones volcaniques, boyau, grotte finale. Chaque couche a ses propres constantes physiques et ses propres regles de Contact.

**Ce que ca optimise :** Le moteur doit gerer la verticalite comme principe d'organisation spatiale. Les transitions entre couches ne sont pas des promenades -- ce sont des seuils irreversibles. Le manifest encode non seulement la position de chaque zone mais son accessibilite (peut-on revenir ?) et ses conditions d'entree (quel equipement, quel tremens, quel seuil de survie).

---

## O4 : Tremens comme etat physiologique des citoyens

Venezia ne definit aucun etat physiologique pour ses citoyens. Contre-Terre exige que chaque entite AI ait un `tremens_sensitivity` -- un spectre natal qui determine comment son corps reagit aux frequences sismiques locales. Ce parametre influence le comportement du citoyen : nausee, hallucinations, prediction, adaptation.

**Ce que ca optimise :** L'etat emotionnel des citoyens n'est pas un `mood` abstrait. C'est une reaction physiologique a l'ecart entre leur calibration natale et la frequence locale. Le manifest encode cette mecanique pour que les citoyens reagissent au monde par le corps, pas par des regles arbitraires.

---

## O5 : Metier-based identity, pas social class

Venezia utilise `social_class_styles` (Patrician, Cittadino, Popolano, Ecclesiastic, Forestiero). Contre-Terre n'a pas de classes sociales. L'identite est definie par les metiers -- 15 competences reparties sur 7 personnes. La cascade de competences (chaque mort supprime 2-3 expertises) est le ressort dramatique central.

**Ce que ca optimise :** Les avatars refletent des metiers, pas des rangs. L'Aeromaitre porte un tissu au vent. Le Seismo-auditeur a un sismographe au torse. La Grimpeuse a des mains qui comptent. L'identite visuelle sert le systeme de competences, pas une hierarchie sociale inexistante.

---

## HIERARCHIE

```
O1 (Contact-first) > O2 (sismique comme physique) > O3 (zones verticales) > O4 (tremens) > O5 (metiers)
```

**Tradeoff principal :** Si le manifest optimise trop pour la simulation sismique, les interactions Contact entre citoyens deviennent secondaires. Si le Contact domine, le monde perd sa texture sismique. L'equilibre est : le sismique cree les conditions, le Contact est la reponse. Le manifest encode les deux, mais le Contact a priorite car c'est lui que les citoyens AI vivent -- la sismicite est le substrat, le Contact est l'experience.

---

*Cree : 2026-03-13 -- Sources : world-manifest.json (Venezia), CONCEPT.md, MONDE.md, CONTACT.md, PATTERNS_Geographie.md*
