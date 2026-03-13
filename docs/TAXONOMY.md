# Contre-Terre — Taxonomie Centrale

Vocabulaire canonique du projet. Tous les modules y font référence. Les termes sont extraits des fichiers source (CONCEPT, MONDE, CONTACT, PERSONNAGES, STRUCTURE, SQUELETTE, METIERS) et des 4 chapitres écrits.

---

## TERMES

### Contact

```yaml
id: term_contact
definition: |
  Système linguistique tactile complet, né de la nécessité dans un monde où le sol
  gronde en permanence et rend le son peu fiable. Le corps devient le médium de
  communication. Le Contact a sa syntaxe, ses dialectes, ses poètes, ses idiolectes.
  Il est la colonne vertébrale narrative du roman.

properties:
  - modes: 5 (verrous de bras, pressions d'épaule, saisies codifiées, identité tactile, dialectes régionaux)
  - mortalité: chaque mort humaine supprime un vocabulaire unique
  - évolution: crée du vocabulaire jusqu'au dernier souffle

_meta:
  abstraction_level: 1
  importance: ★★★★★
  confidence: 95%
  precision: 90%

related_terms:
  - idiolecte: "signature tactile unique d'un individu"
  - tremens: "le corps qui traduit les vibrations — lien sensoriel avec le Contact"
  - contact_corde: "variante médiatisée par la corde"
```

### Contact-corde

```yaml
id: term_contact_corde
definition: |
  Variante du Contact née dans la faille verticale (Ch. IV). Quand les corps sont
  séparés par la corde d'encordement et ne peuvent pas se toucher directement, les
  vibrations intentionnelles dans la corde deviennent langage. Vocabulaire réduit
  (survie, pas pensée) : 3 secousses = stop, 2 courtes = OK, 1 longue = avance.

properties:
  - médium: corde de fibre tressée
  - résolution: basse (2 dimensions vs 20 pour le Contact tactile direct)
  - limitation: ne sait pas dire "j'ai peur" ou "écoute le sol"

_meta:
  abstraction_level: 2
  importance: ★★★★
  confidence: 95%
  precision: 90%

related_terms:
  - contact: "système linguistique parent"
  - inyoni: "grimpeuse dont le Contact-corde est le plus précis"
```

### Contact-forcé

```yaml
id: term_contact_force
definition: |
  Contact imposé par l'architecture, pas par le choix. Dans le boyau (60cm de
  diamètre), les corps ne peuvent pas ne pas se toucher. Le Contact-forcé pose
  la question : le langage a-t-il la même valeur quand on n'a pas le choix ?

properties:
  - lieu: boyau (Ch. VII)
  - nature: contrainte architecturale → contact involontaire

_meta:
  abstraction_level: 3
  importance: ★★★
  confidence: 90%
  precision: 85%

related_terms:
  - contact: "système parent"
  - boyau: "lieu qui impose le Contact-forcé"
```

### Contact-fantôme

```yaml
id: term_contact_fantome
definition: |
  Hallucinations tactiles des coéquipiers morts, vécues par Nandi seule dans la
  grotte finale (Ch. VIII). Les mains des morts se posent sur elle. Le Contact
  d'outre-mort — la langue qui n'existe plus, parlée par des absents.

properties:
  - lieu: grotte finale (Ch. VIII)
  - sujet: Nandi
  - nature: hallucination sensorielle (tremens + chaleur + privation d'oxygène)

_meta:
  abstraction_level: 3
  importance: ★★★★
  confidence: 80%
  precision: 70%

related_terms:
  - contact: "système parent"
  - tremens: "cause physiologique des hallucinations"
  - nandi: "seule à le vivre"
```

### Contact-monde

```yaml
id: term_contact_monde
definition: |
  Geste d'Enama dans la caverne bioluminescente (Ch. II) — main ouverte posée
  à plat sur la roche vivante, doigts écartés. Pas du Contact humain : du Contact
  avec la terre elle-même. Préfigure le geste final de Nandi (mains sur le détonateur
  = dernier Contact avec la Terre).

properties:
  - première occurrence: Enama, Ch. II (paroi bioluminescente)
  - occurrence finale: Nandi, Ch. VIII (détonateur)

_meta:
  abstraction_level: 4
  importance: ★★★★
  confidence: 85%
  precision: 75%

related_terms:
  - contact: "système parent"
  - bioluminescence: "les filaments répondent au toucher"
```

### Tremens

```yaml
id: term_tremens
definition: |
  Système immunitaire physiologique. Le corps humain se calibre sur les fréquences
  sismiques de sa zone de naissance. Traverser des zones de fréquences différentes
  (comme descendre dans un volcan) déclenche le tremens : vomissements, salivation,
  tremblements, hallucinations. Intensité proportionnelle à la distance fréquentielle
  par rapport à la zone d'origine.

properties:
  - calibration: dès la naissance, sur le spectre sismique local
  - symptômes: nausée, tremblements, hallucinations, capillaires éclatés
  - fonction narrative: pré-symptôme sismique — le corps sent le séisme avant l'instrument
  - personnage central: Nandi (calibration extrême — son corps EST un sismographe)

_meta:
  abstraction_level: 1
  importance: ★★★★★
  confidence: 95%
  precision: 90%

related_terms:
  - contact: "le tremens nourrit la sensibilité tactile"
  - magnitude: "le tremens réagit aux changitudes de magnitude"
  - predicteur: "humain dont le tremens devient don prédictif"
  - ecouteur: "niveau de perception intermédiaire"
```

### Magnitude

```yaml
id: term_magnitude
definition: |
  Mesure de la puissance sismique. Dans le monde de Contre-Terre, la magnitude
  de fond est 4-5 (bruit de fond permanent, personne ne le remarque). Les séismes
  significatifs vont de 6 à 9+. La magnitude 11 est l'objectif de la mission —
  jamais mesurée, jamais enregistrée, sentie uniquement par les prédicteurs.

properties:
  - fond: magnitude 4-5 (le pouls du monde)
  - significatif: 6-9+ (événements sismiques notables)
  - objectif: 11 (détonation contrôlée, jamais observée)
  - échelles propres: mentionnées "à développer" dans MONDE.md

_meta:
  abstraction_level: 1
  importance: ★★★★★
  confidence: 95%
  precision: 85%

related_terms:
  - tremens: "le corps réagit aux changements de magnitude"
  - sismographe: "instrument de mesure mécanique"
```

### Idiolecte (tactile)

```yaml
id: term_idiolecte
definition: |
  Signature tactile unique d'un individu dans le Contact. Chaque personne a sa
  manière propre de toucher — pression, vitesse, zone du corps, durée. L'idiolecte
  est aussi relationnel : chaque paire de personnages peut avoir son propre
  vocabulaire (signatures relationnelles). Quand quelqu'un meurt, son idiolecte
  meurt avec lui. Les mêmes gestes, faits par un autre, ne disent pas la même chose.

properties:
  - exemples: nuque de Senzo (intime, intraduisible), trois doigts du village des sourds
  - perte: irréversible à la mort du locuteur
  - héritage: possible (Nandi reprend le geste arc-descendant de Senzo)

_meta:
  abstraction_level: 2
  importance: ★★★★★
  confidence: 95%
  precision: 85%

related_terms:
  - contact: "système linguistique parent"
  - dernier_contact: "la mort du dernier idiolecte"
```

### Échelle de Capitulation

```yaml
id: term_echelle_capitulation
definition: |
  Hiérarchie de la perception sismique, du plus technique au plus intuitif.
  La progression vers la capitulation = accepter que le corps en sait plus
  que l'instrument. Tension narrative centrale (Sihle vs Enama vs Nandi).

properties:
  - niveau_1: Sismographes (instruments mécaniques, objectifs, fiables)
  - niveau_2: Écouteurs (humains entraînés à percevoir les séismes avant les instruments)
  - niveau_3: Prédicteurs (humains dont le corps prédit via le tremens — rejetés par la science)

_meta:
  abstraction_level: 2
  importance: ★★★★
  confidence: 95%
  precision: 90%

related_terms:
  - sihle: "représente le niveau 1-2 (instruments + écoute)"
  - enama: "représente le niveau 2-3 (écoute + corps)"
  - nandi: "représente le niveau 3 pur (prédiction corporelle)"
```

### Écouteur

```yaml
id: term_ecouteur
definition: |
  Humain entraîné à percevoir les séismes avant les instruments (niveau 2 de
  l'Échelle de Capitulation). Perception du présent — sent les séismes en cours
  ou imminents. Accepté par la communauté scientifique. Sihle est séismo-auditeur.

_meta:
  abstraction_level: 2
  importance: ★★★
  confidence: 95%
  precision: 90%

related_terms:
  - echelle_capitulation: "niveau 2"
  - predicteur: "niveau 3, rejeté par les écouteurs"
  - sihle: "séismo-auditeur de l'expédition"
```

### Prédicteur

```yaml
id: term_predicteur
definition: |
  Humain dont le corps prédit les séismes via le tremens (niveau 3 de l'Échelle
  de Capitulation). Perception du futur — sent ce qui va arriver. Rejeté par la
  science. Nandi est prédictrice. Son "handicap" (tremens extrême) est son don.

_meta:
  abstraction_level: 2
  importance: ★★★★
  confidence: 95%
  precision: 90%

related_terms:
  - echelle_capitulation: "niveau 3"
  - ecouteur: "niveau 2, accepté contrairement au prédicteur"
  - tremens: "mécanisme de la prédiction"
  - nandi: "prédictrice de l'expédition"
```

### Aéromaître

```yaml
id: term_aeromaitre
definition: |
  Spécialiste de l'air. Le rôle le plus sensoriel de l'expédition. L'air est
  le premier vecteur du signal sismique — changements de pression, courants,
  qualité de l'oxygène. En profondeur, quand l'air se raréfie, ce métier
  devient vital. Thabo est l'Aéromaître — il teste l'air avec un tissu.

properties:
  - outil: tissu (fibres qui dansent dans le courant d'air)
  - criticité: augmente avec la profondeur (gaz toxiques, CO2)
  - mort de Thabo (Ch. VII): personne ne peut lire l'air quand l'oxygène devient critique

_meta:
  abstraction_level: 2
  importance: ★★★★
  confidence: 95%
  precision: 90%

related_terms:
  - thabo: "Aéromaître de l'expédition"
  - effet_cascade: "sa mort supprime la lecture de l'air"
```

### Bioluminescence

```yaml
id: term_bioluminescence
definition: |
  Filaments lumineux bleutés courant le long des parois des cavernes souterraines.
  Matière organique pulsant au rythme de la vibration de fond (magnitude 4).
  Réagit au toucher humain (s'intensifie au contact). Domestiquée par le village
  des sourds (canalisée dans des sillons taillés). Un Contact-monde : la roche
  répond au toucher avec de la lumière.

properties:
  - couleur: bleuté (pâlit puis reprend en cycles de ~6 heures)
  - réaction: s'intensifie au toucher humain
  - village des sourds: domestiquée, canalisée, utilisée comme marqueur temporel

_meta:
  abstraction_level: 2
  importance: ★★★
  confidence: 95%
  precision: 85%

related_terms:
  - contact_monde: "la roche répond au toucher"
  - village_sourds: "a domestiqué la bioluminescence"
```

### Boyau

```yaml
id: term_boyau
definition: |
  Tube de 60cm de diamètre — en dessous du seuil où un humain peut se retourner.
  Passage horizontal obligatoire (Ch. VII). Impose le Contact-forcé par architecture.
  Lieu de la mort de Thabo et Inyoni (séisme précurseur → effondrement → ensevelissement).

properties:
  - diamètre: 60cm
  - contrainte: impossible de se retourner
  - contact: forcé par l'architecture (les corps ne peuvent pas ne pas se toucher)

_meta:
  abstraction_level: 2
  importance: ★★★
  confidence: 95%
  precision: 90%

related_terms:
  - contact_force: "type de Contact imposé ici"
  - thabo: "meurt dans le boyau"
  - inyoni: "meurt dans le boyau"
```

### Village des Sourds

```yaml
id: term_village_sourds
definition: |
  Dernière communauté humaine avant le fond du volcan (Ch. III). Habitants rendus
  sourds par les dommages acoustiques sismiques (infra-basses détruisant les cellules
  ciliées). Communiquent EXCLUSIVEMENT par le Contact — preuve que le Contact est
  langue primaire, pas substitut du son. Leur Contact est plus fin (trois doigts
  au lieu de la paume entière), plus économe, plus haute définition.

properties:
  - contact_local: trois doigts (pouce, index, majeur) — précision vs paume large de surface
  - innovation: transfert d'état physiologique par le toucher (la vieille femme "calme" Nandi)
  - tremblement_volontaire: geste inconnu transmis à Nandi — tremens reproduit intentionnellement
  - contact_hydraulique: variations de débit d'eau dans les rigoles = messages
  - amortissement sismique: 40% d'amortissement vs roche nue (ingénierie sans instruments)

_meta:
  abstraction_level: 2
  importance: ★★★★★
  confidence: 95%
  precision: 85%

related_terms:
  - contact: "prouve que le Contact est primaire"
  - geste_inconnu: "transmis par la vieille femme à Nandi"
  - nandi: "apprend le Contact haute définition ici"
```

### Geste inconnu

```yaml
id: term_geste_inconnu
definition: |
  Geste transmis par la vieille femme du village des sourds à Nandi (Ch. III, Scène 5).
  Un tremblement volontaire, micro-contrôlé, qui part des avant-bras, traverse les
  paumes et entre dans les mains de l'autre. Reproduit les vibrations de la terre et
  les envoie dans un autre corps. Le Contact poussé à son extrémité : ne plus parler
  du tremblement, mais trembler ensemble. Nandi le reçoit mais ne le comprend pas.
  Doit trouver son sens au Ch. VIII.

properties:
  - nature: tremblement volontaire transmis main-à-main
  - signification: inconnue au moment de la réception
  - portée: Nandi le garde — "un mot appris en rêve"
  - résolution attendue: Ch. VIII (détonation finale)

_meta:
  abstraction_level: 4
  importance: ★★★★★
  confidence: 80%
  precision: 60%

related_terms:
  - contact: "extension extrême du système"
  - tremens: "le geste reproduit le tremens intentionnellement"
  - village_sourds: "lieu d'origine"
  - nandi: "destinataire et porteuse du geste"
```

### Bangs (séismes acoustiques)

```yaml
id: term_bangs
definition: |
  Séismes si violents qu'ils rendent sourds près de l'épicentre. Potentiellement
  destructeurs pour le Contact — forcent un repli proprioceptif où même le toucher
  pourrait ne plus suffire. Le village des sourds est la preuve vivante des dégâts
  des bangs.

properties:
  - effet: surdité (temporaire ou permanente)
  - menace: peut "tuer" le Contact (forcer repli sensoriel total)

_meta:
  abstraction_level: 2
  importance: ★★★
  confidence: 90%
  precision: 80%

related_terms:
  - village_sourds: "conséquence des bangs"
  - contact: "menacé par les bangs"
```

### Effet cascade

```yaml
id: term_effet_cascade
definition: |
  Conséquence de la structure 15 métiers / 7 personnes. Chaque personnage cumule
  2-3 compétences. La mort d'un seul brise plusieurs expertises. L'Aéromaître
  (Thabo) meurt quand l'air devient critique. L'explosiviste principal (Inyoni)
  meurt — Nandi active la charge en backup. Le ressort dramatique central.

properties:
  - ratio: 15 métiers / 7 personnes
  - compounding: les pertes s'aggravent géométriquement
  - exemples: mort Thabo (air) au moment où O2 critique ; mort Inyoni (explosifs) → Nandi backup

_meta:
  abstraction_level: 2
  importance: ★★★★
  confidence: 95%
  precision: 90%

related_terms:
  - metiers: "les 15 rôles spécialisés"
  - idiolecte: "chaque mort supprime aussi du vocabulaire"
```

### Dernier Contact

```yaml
id: term_dernier_contact
definition: |
  Double sens du titre potentiel. 1) Dernière communication entre survivants
  (quand il ne reste plus qu'un). 2) Dernier toucher physique avant la détonation —
  les mains de Nandi sur le détonateur = Contact avec la Terre elle-même.
  La langue tactile, née parce que la terre tremblait, retourne à la terre.

_meta:
  abstraction_level: 4
  importance: ★★★★★
  confidence: 90%
  precision: 80%

related_terms:
  - contact: "système qui meurt avec la mission"
  - contact_monde: "préfiguration du Contact avec la Terre"
  - nandi: "dernière locutrice"
```

---

## TERMINOLOGY DECISIONS

| Terme retenu | Alternative rejetée | Raison |
|-------------|---------------------|--------|
| Contact (majuscule) | contact, le Toucher | Majuscule = nom propre d'un système linguistique |
| tremens | le Tremens, tremor | Minuscule = phénomène physiologique, pas institution |
| Aéromaître | aéromètre, air-maître | Cohérent avec le registre Damasio |
| Contact-corde | corde-parole, vibro-code | Famille "Contact-X" pour les variantes |
| idiolecte | signature tactile | Terme linguistique précis |
| Échelle de Capitulation | hiérarchie sismique | Le nom dit la thèse : la science capitule devant le corps |

---

*Créé : 2026-03-11 — Extrait de CONCEPT.md, MONDE.md, CONTACT.md, PERSONNAGES.md, STRUCTURE.md, SQUELETTE.md, METIERS.md et chapitres I–IV*
