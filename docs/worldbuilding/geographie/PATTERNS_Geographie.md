# PATTERNS -- Geographie

**Module :** `worldbuilding/geographie`
**Projet :** Contre-Terre (roman litteraire)

---

## Pourquoi cette geographie. Pourquoi cette forme.

La geographie de Contre-Terre repose sur un principe fondateur : **la structure du livre epouse la structure de la terre**. Le roman est litteralement une coupe transversale. Pas une metaphore -- une equivalence. Chaque chapitre = une couche geologique. Tourner les pages = descendre.

Ce document explique les decisions de design qui ont mene a cette geographie, et pourquoi chaque couche existe.

---

## P1 : Verticalite comme principe structurant

**Decision :** Le roman descend. Pas de retour en arriere, pas de digressions horizontales, pas de flashbacks.

**Pourquoi :** L'irreversibilite geologique cree l'irreversibilite narrative. Un eboulement qui bloque le retour = un chapitre qu'on ne peut pas relire (metaphoriquement). La gravite est une force narrative : elle tire le recit vers le bas, vers la fin, vers la detonation.

**Alternative rejetee :** Un parcours en spirale (descendre puis remonter partiellement). Rejete parce que la remontee diluerait la tension. Chaque metre de remontee serait un metre d'espoir, et l'espoir est incompatible avec une mission-suicide assumee.

**Consequence :** Chaque seuil entre chapitres doit etre un point de non-retour physique. Le lecteur doit sentir la porte se fermer derriere l'equipe.

---

## P2 : 8 couches = 8 chapitres

**Decision :** Le decoupage en chapitres suit les couches geologiques traversees, pas les arcs narratifs.

**Pourquoi :** La geographie dicte le rythme. Ce n'est pas "il se passe quelque chose, donc nouveau chapitre." C'est "on change de roche, de temperature, de pression, donc nouveau chapitre." Le sol sous les pieds change = le monde change = le chapitre change.

| Chapitre | Couche | Signature |
|----------|--------|-----------|
| I | Surface desertique | Sable, chaleur seche, horizon plat, magnitude de fond 4 |
| II | Piemont volcanique / cavernes d'entree | Gravier basaltique, bioluminescence, premiere obscurite |
| III | Village souterrain (dernier habitat humain) | Amortissement sismique, bioluminescence domestiquee, hydraulique |
| IV | Faille verticale | Verticalite, etroitesse, contact-corde, roche humide et chaude |
| V | Reseau de cavernes profondes | Air rarefie, passages inondes, tremens maximal |
| VI | Zones volcaniques / fumerolles | Chaleur extreme, gaz toxiques, geysers, lave visible |
| VII | Chambre volcanique profonde / boyau | Noir absolu, boyau de 60cm, chaleur insoutenable |
| VIII | Chambre de detonation | Coeur du volcan, lave, detonation |

**Consequence :** Le chapitrage n'est pas negogiable. Si un arc narratif deborde sur deux couches, l'arc s'adapte a la geographie, pas l'inverse.

---

## P3 : Chaque couche a un element-tueur

**Decision :** Chaque mort est causee par un element geologique different. La geographie ne tue pas deux fois de la meme facon.

| Element | Personnage | Couche | Mecanisme |
|---------|-----------|--------|-----------|
| Terre | Senzo | Faille (IV) | Glissement de terrain, pan de paroi |
| Vide | Sihle | Cavernes (V) | Chute dans le vide |
| Eau | Jabu | Cavernes (V) | Noyade, torrent souterrain |
| Feu | Enama | Zones volcaniques (VI) | Coulee de lave |
| Pierre | Thabo + Inyoni | Chambre profonde (VII) | Ensevelissement dans le boyau |
| Tout | Nandi | Chambre de detonation (VIII) | Detonation magnitude 11 |

**Pourquoi :** L'unicite des elements renforce l'idee que le volcan est un ecosysteme complet, pas un couloir a pieges repetes. Chaque mort porte la signature de sa couche.

---

## P4 : La bioluminescence comme fil conducteur souterrain

**Decision :** Des filaments lumineux bleus courent le long des parois depuis l'entree des cavernes (Ch. II) jusqu'au village des sourds (Ch. III). Ils reagissent au toucher et pulsent au rythme de la magnitude de fond.

**Pourquoi :** La bioluminescence accomplit trois fonctions :
1. **Sensorielle** -- Remplace la lumiere du soleil. Donne une couleur au monde souterrain (bleu vs le vert des batons chimiques vs l'orange de la lave).
2. **Thematique** -- Les filaments reagissent au toucher = le monde lui-meme pratique le Contact. La terre repond quand on la touche. Prefiguration du theme "le corps avait raison."
3. **Narrative** -- Les villageois ont domestique la bioluminescence (sillons creuses, lumiere canalisee). Cela montre une civilisation adaptee, pas primitive. Quand les filaments disparaissent apres le village, l'equipe entre dans un monde que personne n'a habite.

**Proprietes des filaments :**
- Bleus, tenus, organiques (entre mousse et lichen)
- Pulsent a magnitude 4 (rythme du monde)
- S'intensifient au toucher (bleu -> blanc) puis se calment
- Domestiques par le village : canalises dans des sillons graves dans la roche
- Disparaissent progressivement apres le Ch. III

---

## P5 : Le village des sourds comme miroir geographique

**Decision :** Le dernier habitat humain (Ch. III) est un village de personnes devenues sourdes par exposition aux infra-basses sismiques. Leur architecture absorbe 40% des vibrations. Leur Contact est plus fin, plus econome, exclusivement tactile.

**Pourquoi ce village est un pivot geographique :**
- Il est le dernier lieu habite. Apres : plus rien d'humain.
- Son ingenierie (tranchees d'amortissement, cordages profonds, structures souples) montre qu'on PEUT vivre avec les seismes -- mais seulement a ce prix.
- Le Contact hydraulique (variations de debit d'eau = messages) introduit l'idee que le Contact peut passer par d'autres mediums que la peau.
- Le village marque le seuil: en deca, le monde est habitable. Au-dela, il ne l'est plus.

---

## P6 : La chaleur comme gradient narratif

**Decision :** La temperature augmente de facon continue avec la profondeur. Ce n'est pas un detail -- c'est un arc physique qui structure l'experience sensorielle du roman.

| Couche | Temperature approximative | Effet sur le Contact |
|--------|--------------------------|---------------------|
| Surface (I) | Chaude, seche (desert) | Contact normal |
| Piemont (II) | Tiede, humide | Contact inchange |
| Village (III) | Chaude, organique | Contact facilite (amortissement) |
| Faille (IV) | Eau chaude, soufre | Contact impossible (faille), corde |
| Cavernes (V) | Chaleur croissante | Debut d'inconfort tactile |
| Zones volcaniques (VI) | Extreme | Contact douloureux (peau brule) |
| Chambre/Boyau (VII) | Insoutenable | Contact force (boyau) |
| Detonation (VIII) | Mortelle | Plus de Contact (Nandi seule) |

**Pourquoi :** La chaleur est le mecanisme par lequel le Contact devient physiquement couteux. Quand toucher l'autre brule, le langage a un prix. Ce prix monte avec la profondeur jusqu'a ce que le Contact devienne impossible -- non par absence de mots, mais par douleur.

---

## P7 : L'air comme ressource narrative decroissante

**Decision :** L'oxygene se rarefie avec la profondeur. Le role de l'Aeromaitre (Thabo) devient critique. La privation d'oxygene provoque delire, hallucinations, irritabilite.

**Pourquoi :** L'air est invisible mais vital. Sa disparition progressive est le parfait contrepoint aux dangers visibles (lave, eboulement). L'air qui manque affecte la psychologie avant de tuer le corps. Le delire d'hypoxie se combine au tremens et a la chaleur pour creer un etat hallucinatoire croissant -- necessaire pour le Ch. VIII (Nandi hallucine les mains de ses coequipiers morts).

**Mort de Thabo (Ch. VII) = perte de l'Aeromaitre.** L'air se rarefie justement quand plus personne ne sait le lire. La geographie punit par l'absence de competence.

---

## P8 : Les Archipels du Desert (geographie horizontale)

**Decision :** La surface du monde est organisee en "archipels" -- ilots habites dans un desert sismique. Chaque archipel a ses frequences propres, ses dialectes du Contact, son calibrage tremens.

**Pourquoi :** Les Archipels fournissent l'horizon du monde sans detourner de la descente. Ils sont evoques, pas explores. Ils expliquent pourquoi les personnages ont des Contacts differents (dialectes regionaux) et pourquoi le tremens de Nandi est si violent (elle vient des archipels du nord-est, frequences hautes et seches, incompatibles avec les basses du desert du sud).

**Consequence :** Les Archipels sont de la geographie evoquee. Ils n'apparaissent jamais directement dans le recit. Leur existence est vehiculee par les differences entre les personnages.

---

## P9 : Terra incognita apres le village

**Decision :** La carte de l'expedition (dessinee a partir de notes d'une expedition anterieure dont personne n'est revenu) devient blanche apres le village des sourds.

**Pourquoi :** Le roman passe de geographie connue a geographie decouverte au Ch. IV. Avant le village, Senzo pouvait consulter la carte. Apres, la carte est blanche. Le savoir cartographique meurt avec Senzo. A partir de ce moment, la geographie n'est plus lue (carte, sismographe) mais sentie (Nandi, Enama, les pieds nus sur la roche).

**Consequence narrative :** Le passage de la carte au corps est aussi le passage de Sihle (raison, instruments) a Nandi/Enama (corps, tremens). La geographie valide le corps contre l'instrument.

---

*Decisions traceables aux fichiers : MONDE.md (systeme sismique, faune, profondeur), STRUCTURE.md (chapitres = couches), SQUELETTE.md (scenes par chapitre), CONCEPT.md (inversion de Damasio).*
