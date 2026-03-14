# VALIDATION — Citizen Model

> Invariants. Ce qui doit toujours etre vrai pour un citoyen de Contre-Terre.

---

## Invariants Structurels

### V1 : Tout citoyen a au moins un metier

**Regle :** Aucun citoyen ne peut exister sans au moins un metier parmi les 15. Le metier est un organe de perception — un citoyen sans metier serait un corps sans sens. Meme les citoyens "non-specialises" ont un metier de base (cuisinier, survivaliste, chef).

**Test :** Pour chaque citoyen dans la population : `len(citizen.metiers) >= 1 AND len(citizen.metiers) <= 3`. La limite a 3 est documentee dans `METIERS.md` — les 7 personnages du roman couvrent 15 metiers a eux seuls parce que chacun en cumule 2-3.

---

### V2 : Tout citoyen a le vocabulaire Contact de base

**Regle :** Chaque citoyen possede les gestes universels du Contact dans son `contact_vocabulary.base_gestures`. Ces gestes sont la grammaire commune — l'epaule dit l'urgence, le bras dit l'information, la main dit l'emotion. Un citoyen peut avoir un idiolecte riche ou pauvre, mais la base est non-negociable.

**Test :** Pour chaque citoyen : `len(citizen.contact_vocabulary.base_gestures) >= MINIMUM_BASE_GESTURES`. Le minimum correspond aux gestes universels documentes dans `ALGORITHM_Contact.md` : grip total 5 doigts (*maintenant*), pression d'epaule (*je suis la*), poing-ouvert (*on y va*), arc descendant (*on ne remonte pas*).

---

### V3 : La sensibilite tremens est coherente avec les metiers sismiques

**Regle :** Les metiers de perception sismique exigent un seuil de sensibilite tremens :
- Predicteur des seismes (#9) : `tremens_sensitivity >= 0.8`
- Ecouteur de seismes (#8) : `tremens_sensitivity >= 0.5`
- Aucune contrainte pour les autres metiers

**Test :** Pour chaque citoyen ayant le metier Predicteur : `tremens_sensitivity >= 0.8`. Pour chaque citoyen ayant le metier Ecouteur : `tremens_sensitivity >= 0.5`. Violation = incoherence du modele. Un ecouteur insensible au tremens est un oxymoron.

**Corollaire :** La haute sensibilite tremens n'implique pas le metier. Un citoyen peut avoir `tremens_sensitivity: 0.85` sans etre predicteur — il souffre du tremens sans avoir appris a le lire. La sensibilite est physiologique ; le metier est un apprentissage.

---

### V4 : La degradation physique affecte les capacites

**Regle :** Un citoyen dont le `physical_state` se degrade perd des capacites de maniere tracable :

| Etat physique | Capacite affectee |
|---------------|------------------|
| `feet: damaged` | Prediction par le sol reduite |
| `feet: destroyed` | Prediction par le sol impossible |
| `hands: cut` | Contact fin desactive (idiolectes de paire complexes) |
| `hands: burned` | Tout Contact douloureux |
| `hands: destroyed` | Contact impossible |
| `inner_ear: damaged` | Ecoute sismique reduite |
| `inner_ear: deaf` | Ecoute sismique impossible, Contact-corde illisible |
| `skin: burned` | Tout Contact = douleur |

**Test :** Verifier qu'aucun citoyen avec `hands: destroyed` n'initie un Contact. Verifier qu'aucun citoyen avec `feet: destroyed` ne "lit le sol". La degradation n'est pas un score — c'est une perte d'outil. Le texte doit la refleter.

---

### V5 : La mort tue l'idiolecte

**Regle :** Quand un citoyen meurt, tous ses `pair_idiolects` passent a `status: orphaned` chez le partenaire survivant. Aucun geste de l'idiolecte de paire ne peut etre utilise normalement apres la mort. Si un survivant reprend un geste du mort, le texte doit marquer l'heritage comme imparfait ("Pas le meme").

**Test :** Apres chaque mort dans la simulation :
1. Tous les `pair_idiolects` impliquant le mort sont marques `orphaned`
2. Le `personal_idiolect` du mort est enregistre dans `death.vocabulary_lost`
3. La couverture metier du groupe est recalculee

---

### V6 : L'effet cascade est monotone decroissant

**Regle :** Le nombre de metiers couverts par le groupe ne peut que diminuer ou rester stable apres une mort. Il ne peut jamais augmenter (pas d'apprentissage de nouveaux metiers en cours de mission).

**Test :** `metiers_couverts(chapitre N) <= metiers_couverts(chapitre N-1)` pour tout N > 1. La seule "exception" est le transfert de competence — Nandi recoit le metier Explosiviste en "backup" d'Inyoni — mais ce transfert est pre-existant, pas acquis en mission.

---

### V7 : Un citoyen mort ne communique plus

**Regle :** Un citoyen avec `alive: false` ne produit plus de Contact. La seule exception est le Contact-fantome (Ch. VIII) : Nandi *hallucine* le Contact des morts. Le modele doit marquer ces interactions comme `type: phantom`, pas comme du Contact reel.

**Test :** Aucune `contact_history` entry avec un citoyen mort comme emetteur ne doit avoir `type` different de `phantom`. Un mort qui "parle" en Contact reel est un bug.

---

## Invariants de Coherence

### V8 : Distribution des metiers dans la population

**Regle :** Dans une population de 50-80 citoyens, chaque metier est porte par au moins 2 citoyens. Pas de "single point of failure" a l'echelle de la population entiere (meme si l'equipe de 7 a ce probleme — c'est volontaire pour le roman).

**Test :** Pour chaque metier parmi les 15 : `count(citizens with metier X) >= 2`.

---

### V9 : Les idiolectes de paire sont symetriques

**Regle :** Si le citoyen A a un `pair_idiolect` avec le citoyen B, alors B a le meme `pair_idiolect` avec A. Les gestes sont les memes, le statut est le meme. Un idiolecte de paire est bilateral par definition — il n'existe qu'entre deux peaux.

**Test :** Pour chaque `pair_idiolect` de A referancant B : verifier qu'un `pair_idiolect` identique existe chez B referancant A. Asymetrie = bug.

---

### V10 : La zone est coherente avec la profondeur

**Regle :** La zone d'un citoyen doit etre coherente avec son `depth_level`. Un citoyen a `depth_level: 7` ne peut pas etre dans la zone "surface du desert". Les zones suivent la descente du roman :

| depth_level | sub_zone possible |
|-------------|------------------|
| 0 | surface, desert, archipel |
| 1 | zones intermediaires |
| 2 | dernier village |
| 3 | la faille |
| 4 | cavernes profondes |
| 5 | zone volcanique |
| 6 | boyau |
| 7 | grotte finale |

**Test :** `citizen.zone.depth_level` correspond a `citizen.zone.sub_zone`. Incoherence = bug de localisation.

---

### V11 : La richesse Contact decroit avec les morts

**Regle :** La somme de `richesse_relationnelle` de tous les citoyens vivants decroit apres chaque mort. L'arc narratif est une contraction linguistique — pas une expansion.

**Test :** `sum(richesse_relationnelle, alive citizens, chapitre N) < sum(richesse_relationnelle, alive citizens, chapitre N-1)` pour tout N ou une mort se produit.

---

*Invariants derives de : `METIERS.md`, `PERSONNAGES.md`, `CONTACT.md`, `ALGORITHM_Citizen_Model.md`*
