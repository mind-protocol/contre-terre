# HEALTH — Citizen Model

> Controles qualite. Comment verifier la coherence du modele citoyen a travers la population et la narration.

---

## Checks Obligatoires Apres Seeding

### H1 : Validite des Metiers

**Quoi :** Verifier que chaque citoyen a 1-3 metiers valides parmi les 15.
**Pourquoi :** Invariant V1. Un citoyen sans metier est un corps sans organe de perception.
**Comment :** Pour chaque citoyen, verifier `len(metiers) >= 1 AND len(metiers) <= 3` et que chaque `metier.id` est dans [1-15].

### H2 : Couverture Metier Globale

**Quoi :** Verifier que chaque metier est porte par au moins 2 citoyens dans la population totale.
**Pourquoi :** Invariant V8. Pas de "single point of failure" a l'echelle du monde (l'equipe de 7 a ce probleme — c'est le roman, pas le monde).
**Comment :** Pour chaque metier 1-15 : `count(citizens with this metier) >= 2`. Si un metier n'est porte que par un seul citoyen, le seeding est desequilibre.

### H3 : Coherence Tremens-Metier

**Quoi :** Verifier que les predicteurs ont `tremens_sensitivity >= 0.8` et les ecouteurs `>= 0.5`.
**Pourquoi :** Invariant V3. La perception sismique exige un seuil physiologique.
**Comment :** Croiser `metiers` et `tremens_sensitivity` pour chaque citoyen. Signaler toute violation.

### H4 : Contact de Base Present

**Quoi :** Verifier que chaque citoyen possede au moins les 4 gestes universels.
**Pourquoi :** Invariant V2. Le Contact de base est la grammaire commune du monde.
**Comment :** Pour chaque citoyen : `len(contact_vocabulary.base_gestures) >= 4`. Les gestes minimaux : grip total (*maintenant*), pression epaule (*je suis la*), poing-ouvert (*on y va*), arc descendant (*on ne remonte pas*).

### H5 : Symetrie des Idiolectes de Paire

**Quoi :** Verifier que tout idiolecte de paire est reciproque.
**Pourquoi :** Invariant V9. Le Contact n'existe qu'entre deux peaux — pas a sens unique.
**Comment :** Pour chaque citoyen A ayant un `pair_idiolect` avec B : verifier que B a un `pair_idiolect` identique avec A. Les gestes doivent etre les memes. Le statut doit etre le meme.

---

## Checks Dynamiques (Evolution dans le Temps)

### H6 : Croissance du Vocabulaire Contact

**Quoi :** Le vocabulaire Contact d'un citoyen vivant croit (ou se maintient) au fil des chapitres. Il ne diminue jamais sauf par degradation physique.
**Pourquoi :** Le Contact est une langue vivante — elle s'enrichit par l'usage. Un citoyen qui interagit apprend de nouveaux gestes, invente des idiolectes de paire, decouvre des variantes. Le vocabulaire ne recule que si le corps ne peut plus le porter (mains detruites, peau brulee).
**Comment :** Pour chaque citoyen vivant, comparer `richesse_totale(chapitre N)` avec `richesse_totale(chapitre N-1)`. Si la richesse diminue sans degradation physique correspondante, c'est un bug.

### H7 : Richesse Relationnelle Reflectee par les Idiolectes

**Quoi :** Un citoyen avec beaucoup de relations actives a un `richesse_relationnelle` eleve. Un citoyen isole a un `richesse_relationnelle` faible.
**Pourquoi :** La richesse linguistique est distribuee, pas individuelle. Jabu, le citoyen le plus isole du roman, a le `richesse_relationnelle` le plus faible — et c'est sa tragedie. A l'inverse, Nandi, la plus connectee (idiolectes avec Senzo, Enama, et Contact avec tous), a la richesse la plus haute — et sa perte a chaque mort est la plus grande.
**Comment :** Classer les citoyens par `richesse_relationnelle` et verifier que le classement reflete la structure sociale narrative. Jabu < Sihle < Thabo ~ Inyoni < Enama < Senzo < Nandi.

### H8 : Degradation Post-Mortem

**Quoi :** Apres chaque mort, verifier que l'effet cascade est correct : metiers perdus, idiolectes orphelins, vocabulaire disparu.
**Pourquoi :** L'effet cascade est le ressort dramatique central du roman (cf. `METIERS.md`). Si l'algorithme A3 n'est pas respecte, la narration diverge du modele.
**Comment :** Apres chaque mort, executer l'algorithme A3 de `ALGORITHM_Citizen_Model.md` et verifier :
1. Les bons metiers sont marques comme perdus
2. Les bons idiolectes sont marques comme orphelins
3. La couverture metier du groupe survivant est recalculee correctement

### H9 : Physical State Coherent avec la Narration

**Quoi :** L'etat physique de chaque citoyen correspond a ce que le texte decrit.
**Pourquoi :** La degradation physique n'est pas un score abstrait — elle est narree. Si le modele dit `feet: damaged` mais le texte montre Nandi courant sans douleur, il y a incoherence.
**Comment :** Pour chaque chapitre, croiser `physical_state` du modele avec les descriptions du texte. Les pieds de Nandi se degradent progressivement :
- Ch. I-III : `feet: intact` (pieds nus, lecture du sol)
- Ch. IV : `feet: worn` (fissure, roche abrasive)
- Ch. V-VI : `feet: damaged` (chaleur, roche volcanique)
- Ch. VII-VIII : `feet: destroyed` (plus de lecture du sol — prediction par le tremens seul)

---

## Signaux de Degradation (du processus de modelisation)

### Sain

- Chaque citoyen est distinct — son idiolecte le rend reconnaissable
- Les metiers influencent visiblement le comportement (le biologiste touche le sol, l'aeromaître leve le tissu)
- Les morts provoquent des pertes calculables et narrativement ressenties
- La population reflete la diversite des archipels (dialectes differents, affinites metier differentes)
- L'effet cascade fonctionne : chaque mort rend le monde plus sourd, plus muet, plus aveugle
- Les idiolectes de paire enrichissent les relations au-dela des liens "collegue" ou "conflit"

### En Degradation

- Les citoyens sont interchangeables (memes metiers, meme vocabulaire, meme comportement)
- Les metiers n'influencent pas la perception (un biologiste et un aeromaître "voient" la meme chose)
- Les morts ne changent rien au modele (pas de recalcul, pas de perte tracee)
- Les idiolectes de paire sont decoratifs (existent dans les donnees mais n'affectent pas le comportement)
- L'etat physique ne correspond pas au texte (modele et narration divergent)
- La population est homogene (pas de variation inter-archipel)

### Critique

- Un citoyen sans metier existe dans la population
- Un predicteur a une sensibilite tremens inferieure a 0.8
- Un citoyen mort continue de communiquer en Contact reel (pas phantom)
- Un idiolecte de paire est asymetrique (A connait le geste, B ne le connait pas)
- L'effet cascade augmente au lieu de diminuer (plus de metiers apres une mort)

### Recuperation

Quand un signal de degradation est detecte :
1. Revenir aux fichiers source (`PERSONNAGES.md`, `METIERS.md`, `CONTACT.md`)
2. Re-executer les invariants de `VALIDATION_Citizen_Model.md`
3. Si le probleme est un desequilibre de seeding : regenerer la population avec des poids corriges
4. Si le probleme est une divergence modele-texte : le texte fait autorite — ajuster le modele

---

## Checklist Rapide

```
[ ] Chaque citoyen a 1-3 metiers valides
[ ] Chaque citoyen a le vocabulaire Contact de base (>= 4 gestes universels)
[ ] Predicteurs : tremens >= 0.8
[ ] Ecouteurs : tremens >= 0.5
[ ] Chaque metier porte par >= 2 citoyens dans la population
[ ] Idiolectes de paire symetriques
[ ] Zones coherentes avec depth_level
[ ] Apres chaque mort : effet cascade calcule, idiolectes orphelins
[ ] Physical state correspond au texte
[ ] Richesse relationnelle : Jabu < Nandi (structure narrative respectee)
```

---

*Derives de : `VALIDATION_Citizen_Model.md`, `ALGORITHM_Citizen_Model.md`, `PERSONNAGES.md`*
