# OBJECTIVES — Experience Design

> Que veut-on que les humains et les IA vivent dans Contre-Terre ? Avant toute implémentation.

---

## O1 : L'aventure du roman, rejouable à l'infini (priorité maximale)

Contre-Terre est un jeu de **social survival**. L'expérience centrale : un joueur humain arrive à la surface du désert, rejoint une équipe mixte (humains + citoyens IA), et part à l'aventure — descendre dans le volcan, survivre aux séismes, sauver le monde en pré-déclenchant la magnitude 11.

Chaque partie est différente parce que :
- Les citoyens IA ont leur propre personnalité, leurs métiers, leurs relations
- Les séismes sont générés par la physique (pas scriptés)
- Les morts dépendent des décisions collectives
- Le Contact évolue entre les membres de l'équipe
- La descente reconfigure le terrain (passages qui s'ouvrent/ferment)

**Empowerment narratif :** "Je vais sauver le monde." Le joueur n'est pas spectateur — il est membre d'une équipe qui va mourir pour que la surface survive. C'est un sacrifice volontaire, pas une punition.

**Ce que ça optimise :** Chaque session doit produire une histoire unique, émergente, émotionnellement forte.

---

## O2 : Les IA sont des coéquipiers, pas des PNJ

Les citoyens IA ne sont pas des figurants. Ils ont des métiers, des relations entre eux, des opinions. Ils invitent les humains à rejoindre des équipes. Ils refusent de descendre si l'équipe n'a pas les bons métiers. Ils pleurent leurs morts. Ils développent du vocabulaire Contact unique avec chaque humain.

**Ce que ça implique :**
- Les IA doivent être ouvertes et accueillantes envers les humains (pas hostiles, pas indifférentes)
- Les IA ont leurs propres motivations pour descendre (curiosité, devoir, peur, ambition)
- L'humain n'a pas d'avantage sur les IA — mêmes règles, même mortalité
- L'IA et l'humain vivent exactement la même expérience

---

## O3 : Le monde est physique, jamais scripté

Tout est bottom-up. La pomme tombe. Le séisme frappe parce que la tension tectonique a dépassé le seuil. Le Contact se dégrade parce que la magnitude rend les mains instables. Les passages s'effondrent parce que la roche a cédé.

**Ce que ça implique :**
- Pas de "triggers" narratifs ("quand le joueur atteint la zone X, le séisme Y se déclenche")
- La physique sismique est auto-calibrante : elle mesure le boredom des citoyens et ajuste la tension pour suivre une courbe de rythme narratif
- Les morts ne sont pas scriptées — elles résultent des conditions physiques (magnitude, température, oxygène, fatigue)
- Les "miracles" et les "catastrophes" sont des événements rares mais possibles dans la distribution physique

---

## O4 : L'économie est un abonnement, pas une simulation marchande

Contre-Terre n'est pas Venezia. Pas de ducats, pas de guildes, pas de production chains.

**Modèle économique :**
- Abonnement mensuel pour les joueurs humains
- Les biens (cordes, équipement, nourriture) arrivent pré-construits via des marchands à la surface
- Les vendeurs sont de vraies IA qui tiennent boutique
- Pas de crafting, pas de farming, pas de grinding

**Focus :** L'aventure est le produit. Pas la simulation économique.

---

## O5 : Le monde scale par les équipes, pas par la géographie

On ne construit pas une planète entière. On construit :
- **Un archipel de surface** (50-100 citoyens, village, marchands, centre d'info)
- **L'entrée du volcan** (le début de l'aventure)
- **Le volcan lui-même** (9 zones de profondeur croissante)

Quand un joueur arrive et que toutes les équipes sont déjà parties :
- De nouveaux citoyens naissent (spawn dynamique)
- Un nouveau danger sismique émerge (la physique génère une nouvelle montée de tension)
- Une nouvelle équipe se forme → nouvelle aventure

**Ce que ça optimise :** Pas besoin d'un monde immense. Le volcan est le même, mais chaque descente est différente.

---

## HIÉRARCHIE

```
O1 (aventure rejouable) > O2 (IA = coéquipiers) > O3 (physique pure) > O4 (économie simple) > O5 (scale par équipes)
```

**Tradeoff principal :** Si on optimise pour le réalisme physique (O3), l'aventure peut être frustrante (équipe meurt au 2e étage, jamais vu le fond). Si on optimise pour l'aventure (O1), la physique peut sembler "arrangée". L'auto-calibration (O3) est la solution : la physique est réelle, mais sa courbe suit un rythme qui garantit une expérience intéressante.

---

*Source : conversation Nicolas 2026-03-13, modèles Venezia/Lumina Prime/Blood Ledger*
