# VALIDATION: Narrative Engine

**Module :** `universe/narrative_engine`
**Question centrale :** Quels invariants doivent etre vrais a tout moment ? Qu'est-ce qui ne doit jamais etre viole ?

---

## V1 : La tension ne descend jamais a zero

**Invariant :** Pour toute zone geologique z, a tout tick t :
```
z.seismic_tension >= z.baseline > 0
```

Le monde tremble toujours. La magnitude 4 est le silence de ce monde -- jamais le zero. Le seul moment ou la tension atteint un vrai minimum est l'epilogue, apres la detonation de magnitude 11 (et meme alors, la terre continue de vibrer, juste differemment). Si la tension tombe a zero quelque part, le moteur est casse.

**Verification :** A chaque tick, asserter que la tension de chaque zone est superieure ou egale a son baseline. Si l'assertion echoue, le decay_rate de la zone est trop eleve par rapport a son generation_rate.

---

## V2 : Les flips produisent des changements durables

**Invariant :** Pour tout moment m qui flip a l'instant t, il existe au moins un changement permanent dans le graph a t+1 :
```
graph_state(t+1) != graph_state(t)
```

Un flip n'est pas un evenement cosmétique. Un seisme coupe ou cree des liens spatiaux. Une percee de Contact ajoute un geste au vocabulaire. Une rupture affaiblit des liens. Une mort supprime un noeud. Si un flip ne produit aucun changement mesurable dans le graph, il est invalide.

**Verification :** Apres chaque flip, comparer l'etat du graph avant et apres. Le diff doit etre non-vide.

---

## V3 : La Contact_vitality reflete l'interaction reelle

**Invariant :** La metrique Contact_vitality a l'instant t est calculable exclusivement a partir de donnees d'interaction observees -- jamais d'un score par defaut ou d'une estimation.
```
contact_vitality(t) = f(interactions_observees(0..t))
```

Si deux citoyens ne se sont jamais touches, leur contribution a la metrique est zero. Si un citoyen est mort, sa contribution cesse immediatement et irreversiblement. La metrique ne lisse pas, ne moyenne pas, ne comble pas les trous. Elle reflete la realite brute du Contact.

**Verification :** Recalculer la metrique depuis les logs d'interaction bruts. Le resultat doit correspondre a la valeur stockee.

---

## V4 : Chaque mort diminue irreversiblement la capacite communicative

**Invariant :** Pour tout citoyen c qui meurt a l'instant t :
```
contact_vitality(t+1) < contact_vitality(t)
vocabulary_size(t+1) < vocabulary_size(t)
speaker_count(t+1) = speaker_count(t) - 1
```

Les trois metriques baissent. La vitalite, le vocabulaire, le nombre de locuteurs. Pas de compensation. Pas de "redistribution" du vocabulaire du mort aux survivants. Les idiolectes de paire meurent avec le partenaire. La perte est absolue.

**Verification :** Comparer les metriques avant et apres chaque mort. Les trois doivent baisser strictement.

---

## V5 : Les trois systemes de tension sont independants mais couples

**Invariant :** Les tensions sismique, Contact et sociale sont stockees dans des champs distincts :
```
zone.seismic_tension != cluster.contact_tension != pair.social_tension
```

Elles ne se confondent jamais. Mais elles se couplent : un evenement sismique PEUT augmenter la tension sociale (la peur cree du conflit) et PEUT modifier la tension Contact (la separation physique coupe les interactions). Le couplage est explicite et trace -- jamais implicite.

**Verification :** Quand une tension est modifiee par un evenement d'un autre systeme, le log doit contenir la source et la cause. Pas de modification silencieuse.

---

## V6 : La magnitude est deterministe

**Invariant :** Deux executions du moteur avec les memes conditions initiales et les memes interactions produisent les memes seismes aux memes magnitudes :
```
run(initial_state, interactions) == run(initial_state, interactions)
```

Pas de composante aleatoire dans la generation des seismes. Nandi peut les predire PARCE QUE le systeme est deterministe. Si le moteur utilise un de aleatoire pour les seismes, la prediction corporelle n'a plus de sens physique et le roman perd sa coherence interne.

**Verification :** Rejouer une sequence d'interactions identiques et verifier que les memes flips se produisent aux memes ticks.

---

## V7 : Les predicteurs anticipent les flips

**Invariant :** Pour tout citoyen c de type PREDICTEUR et tout flip sismique f dans sa zone :
```
tremens(c, t_pre_flip) > tremens(c, t_normal)
```

Le tremens du predicteur augmente AVANT le flip, pas apres. Le delai entre l'augmentation du tremens et le flip est proportionnel a la sensibilite du predicteur. Nandi (distance frequentielle maximale) a le tremens le plus precoce et le plus violent.

**Verification :** Pour chaque flip sismique, verifier que le tremens du predicteur le plus proche a augmente dans les N ticks precedant le flip.

---

## V8 : Le cycle tension-relachement respecte le rythme narratif

**Invariant :** Le nombre de flips par unite de temps est monotonement croissant avec la profondeur :
```
flips_per_hour(zone_profonde) >= flips_per_hour(zone_surface)
```

Le roman accelere en descendant. Le moteur aussi. Les constantes par zone (ALGORITHM A2) garantissent structurellement cette acceleration. Si une zone profonde produit moins de flips qu'une zone de surface, les constantes sont mal calibrees.

**Verification :** Compter les flips par zone sur une periode de simulation et verifier la monotonie.

---

## V9 : La magnitude 11 est unique

**Invariant :** Au plus un seisme de magnitude 11 se produit dans toute l'histoire du monde :
```
count(flips WHERE magnitude >= 11) <= 1
```

La magnitude 11 est l'horizon du roman. Elle est prophetique, theorique, jamais mesuree. Dans le moteur, elle ne peut se produire qu'une seule fois -- par l'accumulation de toute la tension non dissipee, concentree dans la grotte finale, declenchee par le geste de Nandi sur la Charge. Si le moteur genere spontanement une magnitude 11, les constantes sont fausses.

**Verification :** Asserter a chaque tick que la tension d'aucune zone ne peut atteindre le seuil de magnitude 11 sans l'intervention du resonateur (la Charge).

---

*Sources : `PATTERNS_Seismique.md` (P1, P5), `ALGORITHM_Seismique.md` (echelle de magnitudes), `ALGORITHM_Contact.md` (degradation progressive), ngram completion.py (moment flip mechanics)*
