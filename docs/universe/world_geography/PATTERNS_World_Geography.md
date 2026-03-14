# PATTERNS -- World Geography

**Module :** `universe/world_geography`
**Univers :** Cities of Light -- 3e univers (Contre-Terre)

---

## Pourquoi cette structure geographique. Pourquoi ces zones.

La geographie de Contre-Terre est concentrique. Le volcan est au centre. Tout s'organise autour de lui en anneaux de profondeur croissante. Ce n'est pas un choix esthetique -- c'est une consequence de la physique du monde : la sismicite emane du volcan, les frequences se propagent en cercles, et les communautes humaines se sont installees la ou les vibrations etaient tolerables.

Ce document explique les decisions de design de la structure geographique et le role de chaque zone.

---

## P1 : Structure concentrique depuis le volcan

**Decision :** La geographie s'organise en 6 anneaux concentriques autour du volcan, de la surface vers le coeur.

```
SURFACE (Archipels du Desert)
    |
    v
PIEMONT (flancs du volcan, entrees)
    |
    v
ENTREE (cavernes d'entree, bioluminescence)
    |
    v
CAVERNES PROFONDES (reseaux, air rarefie)
    |
    v
ZONES VOLCANIQUES (lave, fumerolles, gaz)
    |
    v
GROTTE FINALE (coeur du volcan, detonation)
```

**Pourquoi :** La concentricite cree un gradient naturel de difficulte. Chaque anneau interieur est plus chaud, plus instable, plus dangereux. Le volcan comme centre de gravite unifie la geographie -- tout converge vers un point.

**Consequence :** Les citoyens vivent principalement dans les anneaux exterieurs (surface + piemont). Les anneaux interieurs sont exploratoires, dangereux, partiellement habites (village des sourds) ou inhabites (zones volcaniques, grotte finale).

---

## P2 : Chaque zone possede 6 parametres definissants

**Decision :** Chaque zone geographique est definie par un ensemble coherent de parametres physiques qui determinent tout le reste.

| Parametre | Effet | Derive de |
|-----------|-------|-----------|
| `base_magnitude` | Intensite sismique de fond | Profondeur + proximite du volcan |
| `temperature_range` | Fourchette de temperature | Geothermie + ventilation |
| `contact_dialect_modifier` | Comment le Contact change | Spectre sismique local |
| `fauna` | Organismes presents | Temperature + lumiere + vibrations |
| `connections` | Zones accessibles | Geologie (tunnels, failles, passages) |
| `habitability_score` | Capacite d'habitation humaine | Synthese des 5 autres parametres |

**Pourquoi :** Six parametres suffisent pour derivier toute l'experience d'une zone. La temperature dicte le confort. La magnitude dicte le danger. Le dialecte dicte la communication. La faune dicte la couleur sensorielle. Les connexions dictent la navigation. L'habitabilite synthetise le tout.

---

## P3 : Les Archipels du Desert comme communautes de surface

**Decision :** La surface du monde est un desert sismique parseme d'ilots habites. Chaque archipel est une communaute autonome -- entre 200 et 5000 habitants -- calibree sur ses frequences locales.

**Proprietes des Archipels :**
- Chaque archipel a son spectre sismique (basses profondes au sud, hautes seches au nord-est, moyennes roulantes a l'ouest)
- Le spectre determine le dialecte du Contact (gestes amples vs brefs, rythme lent vs rapide)
- Le tremens se declenche quand on passe d'un archipel a un autre (distance frequentielle)
- L'architecture est adaptee aux frequences locales (materiaux souples au sud, ancrages profonds au nord)
- Les Archipels sont relies par des routes commerciales traversant le desert -- des caravanes sismiques

**Pourquoi :** Les Archipels fournissent la diversite horizontale. Sans eux, le monde serait uniforme en surface. Les dialectes differents, les calibrations differentes, les architectures differentes -- tout decoule de la variabilite sismique entre Archipels.

---

## P4 : Le monde souterrain comme exploration dangereuse

**Decision :** L'interieur du volcan est un reseau de zones de profondeur croissante, chacune avec son caractere propre. Plus on descend, plus les passages se retrecissent, l'air se rarefie, la chaleur augmente et les seismes s'intensifient.

**Zones souterraines et leur caractere :**

| Zone | Caractere | Element dominant |
|------|-----------|-----------------|
| Piemont | Indifferent -- la roche ne sait pas que vous etes la | Gravier, basalte |
| Entree / Cavernes | Vivant -- bioluminescence, filaments reactifs | Lumiere bleue, pulsation |
| Village des sourds | Hospitalier -- le seul lieu ou la geographie accueille | Amortissement, eau |
| Faille verticale | Hostile -- les murs se referment | Etroitesse, soufre |
| Cavernes profondes | Chaotique -- passages multiples, air rarefie | Obscurite, instabilite |
| Zones volcaniques | Cruel -- la chaleur brule, le gaz empoisonne | Lave, fumerolles |
| Grotte finale | Terminal -- ici tout se termine | Magma, detonation |

**Pourquoi :** Le caractere croissant de chaque zone cree une courbe narrative. L'exploration n'est pas monotone -- chaque couche est un monde different avec ses propres regles de survie.

---

## P5 : Les seismes remodellent les connexions

**Decision :** Le reseau de passages entre zones n'est pas fixe. Les seismes ouvrent de nouvelles voies et en ferment d'autres. Un tunnel accessible hier peut etre bouche demain. Une paroi qui s'effondre peut reveler un passage inconnu.

**Mecanisme :**
- Les seismes de magnitude 6+ peuvent modifier les connexions entre zones
- Les glissements de terrain bouchent les passages (irreversible)
- Les effondrements ouvrent de nouvelles cavites (decouverte)
- Les seismes lateraux dans les failles modifient les largeurs de passage
- Les crues souterraines (tsunamis internes) redirigent les cours d'eau et les passages inondes

**Pourquoi :** La geographie dynamique empeche la cartographie definitive. Le monde n'est pas un donjon statique avec des salles fixes -- c'est un organisme qui bouge. La carte de Senzo devient blanche apres le village parce que la carte n'a pas tort : le terrain a change.

---

## P6 : La bioluminescence comme navigation souterraine

**Decision :** Les filaments bioluminescents bleus courent le long des parois depuis l'entree des cavernes jusqu'au village des sourds. Ils pulsent a magnitude 4, reagissent au toucher, et ont ete domestiques par le village (sillons graves, cycles de 6 heures).

**Role dans la navigation :**
- Les filaments marquent la zone habitable du monde souterrain
- Leur densite augmente en approchant du village (signe de proximite humaine)
- Leur disparition apres le village signale l'entree dans l'inhabitable
- Leur pulsation au rythme sismique confirme la magnitude de fond
- Au village, ils fonctionnent comme horloge (cycle 6h) et eclairage canalise

**Pourquoi :** Dans un monde sans soleil, la navigation est un probleme existentiel. La bioluminescence fournit une reponse organique : la terre elle-meme guide ceux qui savent lire ses signaux. Quand les filaments cessent, on est seul.

---

## P7 : L'habitabilite comme spectre, pas comme binaire

**Decision :** Il n'y a pas de frontiere nette entre "habitable" et "inhabitable". L'habitabilite est un score continu qui decroit avec la profondeur, avec un seuil critique autour du village des sourds.

```
Archipels (surface)     : 0.9 - 1.0  (vie normale, communautes stables)
Piemont                 : 0.6 - 0.8  (passage, pas d'habitation permanente)
Cavernes d'entree       : 0.4 - 0.6  (exploration avec equipement)
Village des sourds       : 0.5 - 0.7  (habite, mais au prix de la surdite)
Faille verticale        : 0.2 - 0.3  (traversee dangereuse)
Cavernes profondes      : 0.1 - 0.2  (survie limitee)
Zones volcaniques       : 0.05 - 0.1 (minutes a heures)
Grotte finale           : 0.0 - 0.05 (terminale)
```

**Pourquoi :** Le spectre continu evite le probleme du "mur invisible". Les citoyens ne buttent pas sur une frontiere -- ils sentent l'habitabilite decroitre graduellement. Le village des sourds est habite a un score de 0.5-0.7, ce qui montre qu'on PEUT vivre en profondeur -- mais a un prix (la surdite, l'isolation, le Contact comme seul langage).

---

## Scope

**IN :**
- Structure concentrique des zones (surface a grotte finale)
- Parametres de chaque zone (magnitude, temperature, Contact, faune, connexions, habitabilite)
- Dynamique des connexions (seismes qui ouvrent/ferment des passages)
- Archipels comme communautes de surface distinctes
- Bioluminescence comme systeme de navigation souterraine
- Gradient d'habitabilite continu

**OUT :**
- Carte precise du monde (pas de coordonnees GPS)
- Geologie detaillee (la physique narrative prime sur la geologie reelle)
- Histoire politique des Archipels (evoquee, pas definie)
- Faune detaillee (definie par zone, pas par espece)

---

*Decisions tracables aux fichiers : `docs/worldbuilding/geographie/PATTERNS_Geographie.md`, `MONDE.md`, `CONTACT.md` (dialectes regionaux), chapitres I-IV (zones canoniques)*
