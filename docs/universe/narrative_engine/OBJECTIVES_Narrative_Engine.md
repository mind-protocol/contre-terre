# OBJECTIVES: Narrative Engine

**Module :** `universe/narrative_engine`
**Question centrale :** Qu'est-ce que le moteur narratif de Contre-Terre doit optimiser ? Quels sont ses objectifs hierarchises ?

---

## O1 : Les seismes comme moteurs narratifs (priorite maximale)

Les seismes ne sont pas du decor. Ils sont les evenements centraux du recit -- les moments ou le monde agit sur les personnages et force des decisions. Dans le moteur ngram, un moment est un noeud qui accumule de l'energie jusqu'a un seuil (tension_threshold), puis "flip" -- il se realise, il se produit. Dans Contre-Terre, les seismes SONT ces moments. La pression tectonique monte, la tension s'accumule dans le graph, et quand le seuil est franchi, le sol tremble. La magnitude du seisme correspond a l'energie accumulee au moment du flip.

**Cible d'optimisation :** Chaque seisme narrativement significatif (magnitudes 6+) doit etre le resultat d'une accumulation de tension mesurable dans le graph, pas un evenement aleatoire. La magnitude correspond au niveau d'energie au moment du flip. Les seismes de fond (magnitude 4-5) sont le bruit de base du systeme -- la generation_rate permanente qui maintient le monde vivant.

---

## O2 : La vitalite du Contact comme metrique de sante

La sante du monde ne se mesure pas en stabilite sismique -- le sol tremble toujours. Elle se mesure en vitalite du Contact : la frequence, la richesse et la diversite des interactions tactiles entre citoyens. Un monde ou les citoyens se touchent, communiquent, inventent de nouveaux gestes est un monde vivant. Un monde ou le Contact se degrade -- moins de locuteurs, vocabulaire appauvri, zones intimes fermees -- est un monde qui meurt.

**Cible d'optimisation :** La metrique Contact_vitality agrege la frequence d'interaction, la taille du vocabulaire actif (idiolectes de paire), la diversite des zones corporelles utilisees, et le nombre de locuteurs vivants. Cette metrique doit baisser de maniere monotone au fil du roman (chaque mort la diminue irreversiblement) tout en ayant des pics locaux (un moment de Contact intense entre survivants).

---

## O3 : Les cycles tension-relachement mappes sur les cycles de magnitude

Le roman ne suit pas une escalade lineaire. Il oscille : tension → seisme → bref relachement → nouvelle tension. Ce rythme doit etre encode dans le moteur. Les constantes ngram (generation_rate, decay_rate, tension_threshold) gouvernent la frequence et l'amplitude de ces cycles. Le decay_rate empeche la tension de monter indefiniment entre les seismes. Le generation_rate la maintient en mouvement. Le tension_threshold determine quand le flip se produit.

**Cible d'optimisation :** Les cycles doivent correspondre au rythme narratif du roman : Ch. I-II cycles courts et frequents (monde actif, seismes reguliers), Ch. III-IV ralentissement (village = zone amortie, faille = silence qui accumule), Ch. V-VII acceleration (cavernes profondes, magnitude croissante, cycles comprimes), Ch. VIII climax (tension maximale → un seul flip → magnitude 11).

---

## O4 : Emergence de recits collectifs depuis le Contact individuel

Les grandes histoires de Contre-Terre ne sont pas ecrites d'avance. Elles emergent de la confluence de centaines d'interactions individuelles. Quand un citoyen enseigne un geste a un autre, quand un predicteur sent une vague avant qu'elle n'arrive, quand un groupe decouvre un passage -- ces micro-evenements s'accumulent dans des noeuds narratifs (narrative nodes) qui, par backflow, irradient vers les acteurs et modifient leur comportement. Un recit collectif nait quand suffisamment de citoyens sont lies aux memes moments.

**Cible d'optimisation :** Les noeuds narratifs les plus energetiques a un instant donne refletent les histoires que le monde "raconte". L'expedition vers la magnitude 11 est un noeud narratif qui se construit moment apres moment, mort apres mort. Sa completion est le roman lui-meme.

---

## HIERARCHIE

```
O1 (seismes = moments) > O2 (Contact vitality) > O3 (cycles tension-relachement) > O4 (emergence collective)
```

**Tradeoff principal :** Si le moteur optimise trop pour les seismes, le Contact devient un sous-produit. Si le Contact domine, les seismes deviennent decoratifs. L'equilibre est : les seismes creent les conditions (destruction, separation, urgence) qui forcent le Contact a s'adapter (nouveaux gestes, nouvelles contraintes, degradation). La sismicite est le substrat ; le Contact est la reponse vivante.

---

*Sources : `physics/constants.json` (Venezia), `ALGORITHM_Seismique.md`, `PATTERNS_Seismique.md`, `ALGORITHM_Contact.md`, `OBJECTIVES_Contact_Engine.md`*
