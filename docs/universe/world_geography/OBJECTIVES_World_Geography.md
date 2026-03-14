# OBJECTIVES -- World Geography

**Module :** `universe/world_geography`
**Univers :** Cities of Light -- 3e univers (Contre-Terre)

---

## Ce que la geographie du monde optimise

La geographie de Contre-Terre n'est pas une carte. C'est un systeme vivant -- un reseau de zones interconnectees ou la sismicite, la temperature et la profondeur dictent comment les citoyens vivent, se deplacent, communiquent et meurent. Le volcan n'est pas un decor : c'est le centre du monde, un organisme dont chaque couche possede ses propres lois physiques. La geographie EST la physique. Les zones sismiques definissent les dialectes du Contact. Les gradients de temperature definissent les limites de la survie. La profondeur definit le danger.

Ce document hierarchise les objectifs que le systeme geographique doit satisfaire dans le contexte du 3e univers des Cities of Light.

---

## O1 : La geographie comme experience vecue, pas comme carte

**Priorite : CRITIQUE**

La geographie n'est jamais survolee. Elle est traversee, sentie, subie. Chaque zone existe par ses effets sur le corps : le sol sous les pieds, la qualite de l'air dans les poumons, la temperature sur la peau, les frequences sismiques dans les os. Un citoyen ne "regarde pas" une carte de Contre-Terre -- il ressent la zone ou il se trouve, et cette zone le transforme.

**Ce que ca implique :**
- Chaque zone possede une signature sensorielle unique (ce qu'on voit, touche, sent, entend)
- Les transitions entre zones sont des ruptures perceptibles, pas des frontieres arbitraires
- Le citoyen qui traverse une zone en ressort change -- son Contact est modifie, son corps est recalibre
- La geographie est decouverte par l'experience, jamais par l'exposition

---

## O2 : Les zones sismiques definissent les dialectes du Contact

**Priorite : HAUTE**

Chaque zone geographique possede un spectre sismique propre -- des frequences de base qui ont calibre les corps des habitants depuis des generations. Ces frequences ne sont pas un detail technique : elles determinent comment le Contact s'exprime. Les basses profondes du desert du sud produisent des gestes amples et lents. Les hautes seches des archipels du nord-est produisent des gestes brefs et nerveux. Le village souterrain, avec son amortissement de 40%, a developpe un Contact haute-resolution a trois doigts.

**Ce que ca implique :**
- Le `contact_dialect_modifier` de chaque zone est derive de son spectre sismique
- Un citoyen qui se deplace entre zones subit un recalibrage de Contact (tremens linguistique)
- Les dialectes ne sont pas des variations superficielles -- ils encodent des percepts differents
- La profondeur modifie le Contact parce qu'elle modifie les frequences

---

## O3 : La profondeur comme gradient de difficulte

**Priorite : HAUTE**

Plus on descend, plus tout empire. La temperature monte. L'air se rarefie. Les seismes s'intensifient. Les passages se retrecissent. Les citoyens se font rares. La profondeur n'est pas une direction -- c'est une mesure de danger. Chaque couche ajoutee est un seuil d'hostilite supplementaire.

**Ce que ca implique :**
- Le `habitability_score` decroit strictement avec la profondeur
- Les zones profondes ont moins de citoyens, moins de ressources, plus de cataclysmes
- La descente est mecaniquement irreversible : les seuils entre couches sont des points de non-retour
- La difficulte n'est pas lineaire -- elle suit une courbe exponentielle dans les dernieres couches

---

## O4 : Le volcan comme centre du monde

**Priorite : HAUTE**

Le volcan n'est pas un point sur la carte -- il est LE point. La geographie entiere de Contre-Terre s'organise en cercles concentriques autour de lui. Les archipels du desert l'entourent. Les zones souterraines le penetrent. La grotte finale est son coeur. Le volcan est a Contre-Terre ce que Venise est aux Cities of Light : le centre de gravite geographique, sauf qu'ici le centre n'est pas une ville -- c'est une force.

**Ce que ca implique :**
- La structure geographique est concentrique : surface > piemont > entree > cavernes > zones volcaniques > grotte finale
- Le volcan a un interieur explorable, avec des couches de difficulte croissante
- Chaque anneau concentrique a son caractere, sa sismicite, sa faune, son Contact
- Le centre est inaccessible sauf par la descente -- pas de raccourci

---

## O5 : Les archipels comme communautes distinctes

**Priorite : MOYENNE**

La surface du monde est un desert sismique parseme d'ilots habites -- les Archipels. Chaque archipel est une communaute autonome avec ses propres frequences, ses propres dialectes, ses propres adaptations. Les Archipels sont la geographie horizontale de Contre-Terre : ils expliquent la diversite des Contacts, la variete des tremens, et les origines des personnages.

**Ce que ca implique :**
- Les Archipels de surface sont des zones distinctes avec leurs propres parametres
- Les differences de Contact entre personnages derivent de leurs archipels d'origine
- La geographie horizontale (Archipels) contraste avec la geographie verticale (volcan)
- Chaque archipel a un spectre sismique propre qui calibre ses habitants

---

## Hierarchie des objectifs

```
O1 (experience vecue) > O2 (dialectes sismiques) = O3 (gradient de profondeur) > O4 (volcan-centre) > O5 (archipels)
```

En cas de conflit : l'experience prime. Si un systeme de zones est logiquement coherent mais ne se sent pas dans le corps du citoyen, le systeme est mauvais. La geographie doit etre ressentie avant d'etre comprise.

---

## Non-objectifs

- **Cartographie exhaustive** -- Pas de carte complete du monde. La geographie est decouverte, pas documentee.
- **Realisme geologique** -- La geologie sert le systeme, pas l'inverse. Les mecanismes sont plausibles, pas scientifiques.
- **Symetrie avec Venise** -- 120 iles vs des archipels dynamiques, 255 buildings vs des zones vivantes. Les paralleles existent mais ne sont pas forces.

---

*Derive de : `docs/worldbuilding/geographie/` (doc chain complete), `MONDE.md`, `CONTACT.md`, chapitres I-VIII*
