# ALGORITHM: Narrative Engine

**Module :** `universe/narrative_engine`
**Question centrale :** Comment fonctionne le cycle de tick du moteur narratif ? Quel est l'algorithme concret ?

---

## A1 : Le cycle de tick

Chaque tick du moteur execute six phases sequentielles. L'ordre est strict -- chaque phase depend des resultats de la precedente. Le cycle complet represente un "battement" du monde.

```
TICK
│
├── Phase 1 : COMPUTE TENSION SISMIQUE (par zone)
│   Pour chaque zone geologique :
│     zone.seismic_tension += zone.generation_rate * dt
│     zone.seismic_tension -= zone.decay_rate * dt
│     zone.seismic_tension = max(zone.seismic_tension, zone.baseline)
│     // baseline = tension irreductible (mag 4 = ~0.15)
│
├── Phase 2 : COMPUTE TENSION CONTACT (par cluster de citoyens)
│   Pour chaque cluster de citoyens adjacents :
│     cluster.contact_tension += sum(interaction_intensities) * contact_generation_rate * dt
│     cluster.contact_tension -= contact_decay_rate * dt
│     // interaction_intensity = f(mode, zone_corporelle, duree, frequence)
│
├── Phase 3 : COMPUTE TENSION SOCIALE (par relation)
│   Pour chaque paire de citoyens avec un conflit actif :
│     pair.social_tension += conflict_weight * social_generation_rate * dt
│     pair.social_tension -= social_decay_rate * dt
│     // decay plus lent que generation : les conflits pourrissent s'ils ne sont pas resolus
│   Pour chaque cercle de Contact actif :
│     participants.social_tension -= circle_resolution_rate * dt
│     // les cercles resolvent la tension
│
├── Phase 4 : FEED INTO NGRAM PHYSICS
│   Pour chaque moment (noeud actif dans le graph) :
│     moment.energy += connected_tension * weight * emotion_factor
│     // connected_tension = somme ponderee des 3 tensions des zones/clusters/relations liees
│   Appliquer moment_draw : les moments attirent l'energie des acteurs connectes
│   Appliquer moment_interaction : les moments se soutiennent ou se contredisent
│   Appliquer narrative_backflow : les narratifs irradient vers les acteurs
│
├── Phase 5 : CHECK MOMENT FLIPS
│   Pour chaque moment dont l'energie depasse son seuil :
│     SI moment.type == SEISMIC :
│       magnitude = energy_to_magnitude(moment.energy)
│       generer_evenement_sismique(zone, magnitude, type_cataclysme)
│       moment.energy -= flip_cost  // pas a zero -- aftershocks possibles
│     SI moment.type == CONTACT :
│       SI conditions_percee() :
│         generer_percee(cluster, nouveau_geste)
│       SINON :
│         generer_rupture(cluster, geste_echoue)
│     SI moment.type == SOCIAL :
│       generer_evenement_social(relation, resolution_ou_escalade)
│
└── Phase 6 : GENERATE EVENTS & PROPAGATE
    Pour chaque evenement genere :
      propager_aux_citoyens(evenement, zone_d_impact)
      mettre_a_jour_graph(liens_coupes, liens_crees)
      mettre_a_jour_contact_vitality()
      verifier_morts(citoyens_dans_zone, magnitude)
```

---

## A2 : Constantes adaptees au monde sismique

Les constantes de Venezia servent de base mais doivent etre recalibrees pour un monde ou la tension ne descend jamais a zero.

### Constantes globales

```json
{
  "seismic_baseline": 0.15,
  "contact_generation_rate": 0.06,
  "contact_decay_rate": 0.04,
  "social_generation_rate": 0.03,
  "social_decay_rate": 0.02,
  "circle_resolution_rate": 0.08,
  "contact_vitality_weights": {
    "interaction_frequency": 0.3,
    "vocabulary_size": 0.25,
    "zone_diversity": 0.2,
    "speaker_count": 0.25
  }
}
```

### Constantes par zone (cf. PATTERNS P4)

```
Zone                | gen_rate | decay | threshold | baseline
--------------------|----------|-------|-----------|--------
Surface (desert)    | 0.04     | 0.06  | 0.80      | 0.10
Piemont             | 0.06     | 0.05  | 0.70      | 0.12
Village souterrain  | 0.05     | 0.07  | 0.75      | 0.08  // zone amortie
Faille              | 0.10     | 0.02  | 0.60      | 0.15
Cavernes profondes  | 0.08     | 0.04  | 0.65      | 0.14
Zones volcaniques   | 0.14     | 0.02  | 0.50      | 0.20
Boyau               | 0.16     | 0.01  | 0.45      | 0.22
Grotte finale       | 0.20     | 0.01  | 0.40      | 0.25
```

Le village souterrain a un decay_rate plus eleve et un baseline plus bas que les zones adjacentes : les villageois ont construit des amortisseurs. "L'architecture est une reponse sismique" (PATTERNS_Seismique P7). Le moteur encode cette reponse.

---

## A3 : Conversion energie → magnitude

La tension accumulee au moment du flip se convertit en magnitude via une echelle logarithmique (comme Richter).

```
magnitude = 4 + log2(energy_at_flip / seismic_baseline)

Exemples :
  energy = 0.15 (baseline) → magnitude 4 (fond permanent)
  energy = 0.30             → magnitude 5
  energy = 0.60             → magnitude 6
  energy = 1.20             → magnitude 7 (seisme du Ch. II)
  energy = 2.40             → magnitude 8
  energy = 4.80             → magnitude 9
  energy accumulee depuis le debut → magnitude 11 (theorique)
```

La magnitude 11 n'est pas un flip ordinaire. C'est l'accumulation de toute la tension non dissipee du monde -- la tension que le decay n'a pas eliminee, que les seismes anterieurs n'ont pas liberee, qui s'est accumulee couche apres couche dans le coeur du volcan. Le moteur doit pouvoir representer cette accumulation trans-temporelle.

---

## A4 : Le flip Contact -- percee vs rupture

Le flip Contact n'est pas binaire (on/off). Le resultat depend de l'etat du cluster au moment du flip.

```
SI cluster.interaction_diversity > 0.6 ET cluster.conflict_level < 0.3 :
  → PERCEE : nouveau geste, nouvel idiolecte, vocabulaire enrichi
  → cluster.contact_tension reset (mais pas a zero)
  → contact_vitality += percee_bonus

SI cluster.interaction_diversity < 0.4 OU cluster.conflict_level > 0.7 :
  → RUPTURE : incomprehension, isolation, geste echoue
  → cluster.contact_tension reset
  → contact_vitality -= rupture_penalty

SINON :
  → MIXTE : percee partielle (un geste compris par certains, pas tous)
  → tension partiellement relachee
```

L'interaction_diversity mesure la variete des modes de Contact utilises (5 modes, zones corporelles, idiolectes). Un cluster qui ne communique que par pressions d'epaule a une diversite faible -- il est fragile. Un cluster qui utilise verrous de bras, saisies codifiees, identite tactile et Contact-monde a une diversite elevee -- il est resilient.

---

## A5 : Propagation des evenements aux citoyens

Les evenements generes par les flips ne sont pas instantanes. Ils se propagent dans l'espace et dans le temps.

```
Pour chaque evenement sismique :
  zone_impact = calcul_zone_impact(epicentre, magnitude)
  delai_propagation = distance(citoyen, epicentre) / vitesse_onde
  Pour chaque citoyen dans zone_impact :
    appliquer_tremens(citoyen, magnitude, distance)
    SI citoyen.type == PREDICTEUR :
      tremens_anticipe -= delai_predictif  // le predicteur sent AVANT
    SI magnitude >= seuil_mortel(citoyen) :
      declencher_mort(citoyen, type_cataclysme)
    SINON :
      modifier_tension_sociale(citoyen, peur, urgence)
      modifier_contact(citoyen, contrainte_physique)
```

---

## A6 : Calcul de Contact_vitality

Contact_vitality est la metrique de sante du monde. Elle ne mesure pas la stabilite -- elle mesure la vitalite communicative. Un monde vivant est un monde ou le Contact circule, invente, se diversifie. Un monde mourant est un monde ou le Contact se replie, s'appauvrit, se tait.

```
Contact_vitality = (
    interaction_frequency * 0.30 +
    vocabulary_size * 0.25 +
    zone_diversity * 0.20 +
    speaker_count * 0.25
)

Ou :
  interaction_frequency = nombre_interactions_recentes / nombre_interactions_max_possible
    // max_possible = toutes les paires vivantes * frequence_cible
    // range : 0.0 (silence total) a 1.0 (Contact permanent)

  vocabulary_size = taille_vocabulaire_actif / taille_vocabulaire_pic
    // vocabulaire_actif = base + sum(idiolectes vivants) + dialectes
    // vocabulaire_pic = maximum historique (atteint au Ch. III, village des sourds)
    // range : 0.0 (aucun geste connu) a 1.0 (vocabulaire maximal)

  zone_diversity = zones_corporelles_utilisees_recemment / zones_totales
    // 10 zones : front, nuque, epaule, torse, bras, avant-bras, poignet, main, paume, pieds
    // range : 0.0 (aucune zone) a 1.0 (toutes les zones)

  speaker_count = locuteurs_vivants / locuteurs_initiaux
    // range : 0.0 (tous morts) a 1.0 (7/7 vivants)
```

### Proprietes de Contact_vitality

**Decroissance macro-monotone :** A l'echelle du roman, Contact_vitality ne fait que baisser. Chaque mort supprime irrevocablement un locuteur (speaker_count baisse de 1/7) et tous ses idiolectes (vocabulary_size baisse). Ces pertes ne sont jamais compensees. Un nouveau geste invente entre survivants ne remplace pas les gestes perdus d'un mort.

**Pics locaux possibles :** Entre deux morts, la vitalite peut faire des pics. Le village des sourds (Ch. III) est un pic massif : vocabulaire augmente (haute resolution), zones diversifiees (front!), frequence d'interaction elevee. Mais le pic est temporaire -- l'equipe quitte le village et les morts reprennent.

**Courbe du roman :**
```
Ch. I   : ~0.85 (7 locuteurs, vocabulaire standard, toutes zones)
Ch. II  : ~0.82 (urgence du seisme mag 7 enrichit mais aussi degrade)
Ch. III : ~0.90 (PIC : village des sourds, haute resolution, geste inconnu)
Ch. IV  : ~0.65 (mort Senzo : -1 locuteur, Contact-corde = appauvrissement)
Ch. V   : ~0.45 (morts Jabu + Sihle : -2 locuteurs, separation du groupe)
Ch. VI  : ~0.30 (mort Enama : -1 locutrice, Contact douloureux par chaleur)
Ch. VII : ~0.12 (morts Thabo + Inyoni : -2 locuteurs, boyau = Contact impossible)
Ch. VIII: ~0.02 (Nandi seule : speaker_count = 1/7, pas de destinataire)
```

---

## A7 : Narrative backflow -- les recits irradient

Les noeuds narratifs ne sont pas des receptacles passifs. Quand un noeud narratif accumule suffisamment d'energie (parce que de multiples moments l'alimentent), il commence a irradier en retour vers les acteurs qui y sont connectes. C'est le backflow : l'histoire agit sur les personnages.

```
Pour chaque noeud narratif avec energy > narrative_threshold :
  Pour chaque acteur connecte au narratif :
    influence = narratif.energy * lien.weight * backflow_rate
    acteur.modifier_comportement(influence, narratif.type)
```

**Exemple concret :** Le noeud narratif "expedition vers la magnitude 11" accumule de l'energie a chaque mort (moment), a chaque seisme (moment), a chaque decision de continuer (moment). Quand son energie depasse le seuil, il irradie vers les survivants : ils sont "pris" dans le recit, leur comportement s'inflechit vers la completion du narratif. Nandi au Ch. VIII ne decide pas rationnellement de poser ses mains sur la Charge -- le narratif la tire. Les morts l'ont alimentee. Le backflow est la force qui transforme un groupe de citoyens en personnages d'une histoire.

**Backflow et Contact-fantome :** Les hallucinations tactiles de Nandi au Ch. VIII sont, dans le moteur, du backflow maximal. Le noeud narratif est si energetique que les morts eux-memes deviennent des vecteurs de backflow -- leurs signatures tactiles irradient depuis le narratif vers Nandi. Le Contact-fantome est le backflow rendu physique.

---

*Sources : phases ngram (generation.py, moment_draw.py, moment_flow.py, moment_interaction.py, narrative_backflow.py, completion.py), `physics/constants.json`, `ALGORITHM_Seismique.md`, `ALGORITHM_Contact.md`*
