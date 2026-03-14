# OBJECTIVES — Graph Schema

**Module :** `universe/graph_schema`
**Question centrale :** Comment le graph FalkorDB de Contre-Terre capture l'etat du monde -- citoyens, zones, Contact, seismes, equipement -- pour que les requetes semantiques revelent les structures cachees du recit ?

---

## O1 : Le graph capture l'etat vivant du monde (priorite maximale)

Le graph n'est pas une base de donnees statique. C'est une representation de l'etat courant de Contre-Terre a un instant donne. Chaque citoyen AI a un noeud Actor avec ses metiers, son tremens, son idiolecte. Chaque zone a un noeud Space avec sa signature sismique, sa profondeur, ses conditions de survie. Chaque seisme, chaque mort, chaque Contact marquant est un noeud Moment horodate.

**Ce que ca optimise :** Le moteur Cities of Light peut interroger le graph pour savoir qui est vivant, ou, avec quelles competences, dans quelle zone sismique, et avec quels liens de Contact. L'etat du monde est lisible a tout moment sans avoir a parser du texte narratif.

**Tradeoff :** Si le graph capture trop de details, les requetes deviennent lentes et le bruit noie le signal. Si le graph est trop abstrait, il perd la texture sensorielle qui fait l'essence de Contre-Terre. L'equilibre est : chaque noeud doit porter assez d'information dans `synthesis` pour que la recherche semantique fonctionne, et assez de detail dans `content` pour que l'agent qui le consulte comprenne le contexte.

---

## O2 : Les relations de Contact sont le tissu conjonctif du graph

Les liens entre citoyens ne sont pas des "relations" abstraites. Ils encodent l'histoire tactile entre deux personnes : frequence du Contact, zones du corps utilisees, richesse de l'idiolecte de paire, moments partages. Le poids du lien SPEAKS_TO (Contact weight) est la mesure la plus fiable de la profondeur relationnelle entre deux citoyens.

**Ce que ca optimise :** Les requetes de type "qui est le plus proche de Nandi ?" ne retournent pas une distance geographique mais une densite de Contact. La traversal du graph revele les clusters relationnels, les isolements (Jabu), les conflits (Sihle/Enama par la pauvrete de leur lien). Le graph encode ce que les personnages eux-memes ne peuvent pas formuler.

---

## O3 : L'histoire sismique structure le temps du monde

Chaque seisme significatif (magnitude 6+) est un noeud Moment lie aux zones affectees et aux citoyens presents. La sequence de ces noeuds constitue la chronologie du monde -- pas un calendrier, mais une succession de chocs. L'escalade sismique (magnitude 4 de fond vers 11 a la detonation) est lisible en traversant la chaine de Moments.

**Ce que ca optimise :** Le moteur peut simuler l'intensification sismique, faire reagir les citoyens par leur tremens, declencher des evenements en cascade. Les predictions de Nandi deviennent testables : le graph sait si un seisme va frapper une zone parce que les Moments precedents construisent un pattern.

---

## O4 : Les metiers et l'equipement tracent la competence disponible

Chaque citoyen est lie a ses metiers par des liens PRACTICES. Chaque objet significatif (la Charge, le sismographe, les cordes) est un noeud Thing lie a son porteur. L'effet cascade -- chaque mort supprime des competences -- est directement lisible dans le graph en comptant les liens PRACTICES actifs.

**Ce que ca optimise :** Le moteur peut determiner quelles competences restent disponibles a tout moment. Quand Thabo meurt, le graph montre que le lien PRACTICES vers "Aeromaitre" est mort -- et aucun autre citoyen ne porte cette competence. Le graph rend l'effet cascade computationnel, pas seulement narratif.

---

## O5 : Les predictions et le savoir collectif sont des recits partages

Les predictions sismiques, les mythes du village des sourds, le savoir transmis (geste inconnu, damier de Thabo) sont des noeuds Narrative. Ils representent ce que les citoyens croient, savent, transmettent. Le lien entre un citoyen et une Narrative (BELIEVES, KNOWS) encode qui porte quel savoir.

**Ce que ca optimise :** La perte de savoir est tracable. Quand Sihle meurt, les Narratives qu'il etait le seul a croire (validite des instruments, protocole meteorologique) perdent leur dernier porteur. Le graph montre l'erosion des connaissances aussi clairement que l'erosion du Contact.

---

## HIERARCHIE

```
O1 (etat vivant) > O2 (Contact comme tissu) > O3 (histoire sismique) > O4 (metiers/equipement) > O5 (savoir collectif)
```

**Tradeoff principal :** La densite du graph. Trop de noeuds par citoyen (un Moment pour chaque geste de Contact) noierait la structure. Trop peu (un seul noeud Narrative pour tout le savoir) perdrait la granularite. La regle : un noeud Moment pour chaque evenement qui change l'etat du monde (mort, seisme, invention, transmission). Un noeud Narrative pour chaque savoir distinct qui peut etre perdu.

---

*Cree : 2026-03-13 -- Sources : seed_venice_graph.py (Venezia), MAPPING.md, TAXONOMY.md, PERSONNAGES.md, OBJECTIVES_Manifest.md*
