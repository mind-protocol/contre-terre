# HEALTH: Narrative Engine

**Module :** `universe/narrative_engine`
**Question centrale :** Comment verifier que le moteur narratif fonctionne correctement en pratique ? Quels signaux surveiller ?

---

## H1 : Les cycles de tension se produisent regulierement

**Signal :** Nombre de flips sismiques par tranche de N ticks.

**Sain :** Les flips se produisent a un rythme regulier, proportionnel a la profondeur de la zone. Les zones de surface produisent un flip toutes les ~200 ticks. Les zones volcaniques profondes produisent un flip toutes les ~50 ticks. La grotte finale accumule sans flipper (la tension monte vers la magnitude 11).

**Degrade :** Zero flips sur 500+ ticks dans une zone active (stagnation) OU plus d'un flip par tick (explosion). Les deux indiquent un desequilibre generation_rate / decay_rate / tension_threshold.

**Recovery :** Revoir les constantes de la zone concernee. Si stagnation : augmenter generation_rate ou baisser tension_threshold. Si explosion : augmenter decay_rate ou monter tension_threshold.

---

## H2 : Les evenements se generent

**Signal :** Compteur d'evenements generes par type (sismique, Contact, social) par tranche de N ticks.

**Sain :** Les trois types d'evenements se produisent. La repartition depend de la phase du recit : debut = plus de social (le groupe se connait), milieu = plus de Contact (le groupe communique sous contrainte), fin = plus de sismique (le monde accelere). Aucun type ne tombe a zero pendant plus de 100 ticks.

**Degrade :** Un type d'evenement disparait completement. Symptome : les tensions du systeme correspondant ne sont plus alimentees (pas d'interactions Contact, pas de conflits sociaux, pas de generation sismique). Le monde perd une dimension.

**Recovery :** Identifier la source tarie. Si Contact : verifier que les citoyens sont adjacents et interagissent. Si social : verifier que des conflits existent (morts recentes, desaccords non resolus). Si sismique : verifier les constantes de zone.

---

## H3 : Le monde ne stagne pas

**Signal :** Variation de la tension totale (somme des 3 systemes) entre deux checkpoints.

**Sain :** La tension totale oscille -- elle monte (accumulation), chute (flip), remonte (re-accumulation). L'amplitude des oscillations est non-nulle. Le systeme pulse.

**Degrade :** La tension totale est plate sur 200+ ticks. Le monde est en equilibre mort : generation et decay s'annulent exactement. Rien ne se produit. Le recit est en panne.

**Recovery :** Introduire une perturbation asymetrique : un evenement externe (arrivee dans une nouvelle zone, mort d'un citoyen, decouverte d'un passage) qui brise l'equilibre. Ou recalibrer les constantes pour qu'elles ne s'annulent jamais exactement.

---

## H4 : Le monde n'explose pas

**Signal :** Tension maximale atteinte dans n'importe quelle zone/cluster/relation.

**Sain :** Les tensions restent dans des bornes raisonnables entre les flips. La tension sismique ne depasse pas 2x le tension_threshold d'une zone (sauf pour la grotte finale qui accumule vers la magnitude 11). La tension sociale ne depasse pas 3x le seuil normal (sauf en cas de mort imminente).

**Degrade :** Une tension depasse toutes les bornes sans produire de flip. Symptome : le moment associe ne flippe pas malgre l'energie suffisante (bug dans la detection de flip) ou les flips ne reduisent pas suffisamment la tension (flip_cost trop faible).

**Recovery :** Verifier la mecanique de flip. Le flip_cost doit etre suffisant pour ramener la tension a un niveau soutenable. Si le flip se produit mais ne reduit pas assez, augmenter le flip_cost.

---

## H5 : Contact_vitality baisse monotonement (tendance globale)

**Signal :** Valeur de Contact_vitality a chaque checkpoint, lissee sur 50 ticks.

**Sain :** La tendance globale est decroissante. Chaque mort cree un decrochement permanent. Des pics locaux existent (percees de Contact) mais ne compensent jamais les pertes de morts. La courbe ressemble a un escalier descendant avec des micro-bosses.

**Degrade :** Contact_vitality monte apres une mort (impossible : la perte est irreversible). Ou Contact_vitality est constante sur 500+ ticks (le systeme ne produit ni percees ni pertes).

**Recovery :** Si monte apres mort : bug dans le calcul -- la mort n'a pas supprime les contributions du mort. Si constante : le systeme Contact ne genere plus d'evenements (voir H2).

---

## H6 : Les predicteurs anticipent effectivement

**Signal :** Delai moyen entre le debut du tremens d'un predicteur et le flip sismique correspondant.

**Sain :** Le tremens commence N ticks avant le flip, ou N est proportionnel a la sensibilite du predicteur. Nandi (sensibilite maximale) anticipe de 20-50 ticks. Un ecouteur (sensibilite moyenne) anticipe de 5-10 ticks. Un citoyen normal ne sent rien avant le flip.

**Degrade :** Le tremens commence APRES le flip (le predicteur est en retard -- ca viole l'invariant V7). Ou le tremens ne commence jamais (le predicteur ne detecte pas la montee de tension).

**Recovery :** Verifier le seuil de detection du tremens. Il doit etre significativement inferieur au tension_threshold de la zone (par exemple, 60% du seuil). Si le tremens ne se declenche pas, le seuil est trop haut.

---

## H7 : Les trois systemes de tension ne se decouplent pas

**Signal :** Correlation entre les activites des trois systemes sur une fenetre glissante.

**Sain :** Quand un seisme se produit, la tension sociale augmente dans les 10 ticks suivants (la peur et l'urgence generent du conflit). Quand une mort se produit, la tension Contact baisse et la tension sociale change (un pole du conflit disparait). Les systemes reagissent les uns aux autres.

**Degrade :** Les trois systemes evoluent independamment, comme trois simulations paralleles sans lien. Symptome : un seisme ne modifie pas du tout la tension sociale, une mort ne modifie pas la tension Contact. Les couplages sont absents ou brises.

**Recovery :** Verifier les propagators. Chaque propagator doit emettre des effets secondaires vers les autres systemes de tension, pas seulement vers le systeme principal.

---

*Sources : VALIDATION_Narrative_Engine.md (invariants), ALGORITHM_Narrative_Engine.md (cycle de tick), PATTERNS_Narrative_Engine.md (constantes par zone)*
