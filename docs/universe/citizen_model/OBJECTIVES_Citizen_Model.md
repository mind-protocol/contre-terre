# OBJECTIVES — Citizen Model

> Ce que le modele citoyen optimise dans l'univers de Contre-Terre (3e univers Cities of Light).

---

## Objectif Principal

**O1 : Definir l'identite d'un citoyen par son corps, pas par son patrimoine.**

Un citoyen de Contre-Terre n'est pas un acteur economique. Il n'a pas de ducats, pas de classe sociale, pas de guilde. Son identite est inscrite dans quatre dimensions corporelles : comment il tremble (tremens), comment il touche (Contact), ce qu'il percoit (metiers), et avec qui il a partage du Contact (relations). Le modele citoyen doit capturer ces quatre axes sans jamais les reduire a des statistiques abstraites. Un citoyen est un corps dans un monde sismique — ce corps est sa carte d'identite.

---

## Objectifs Secondaires

**O2 : Faire des metiers des organes de perception, pas des competences.**

Les 15 metiers de Contre-Terre ne sont pas des professions — ce sont des facons de percevoir le monde. L'aeromaître ne "fait" pas de la qualite de l'air ; il *lit* l'air. La predictrice ne "calcule" pas les seismes ; son corps *sait* avant elle. Le modele citoyen doit encoder le metier comme un filtre sensoriel qui transforme ce que le citoyen percoit, pas comme une ligne de CV. Chaque metier ouvre un canal de perception et en ferme d'autres.

**O3 : Incarner le Contact comme langue vivante, individuelle et relationnelle.**

Chaque citoyen possede un vocabulaire Contact de base (gestes universels) et un idiolecte personnel (gestes propres). Mais le Contact vit surtout *entre* les gens : les idiolectes de paire — vocabulaires inventes par deux personnes qui n'existent qu'entre elles. Le modele doit capturer cette dimension relationnelle : la richesse linguistique d'un citoyen n'est pas individuelle, elle est le produit de ses relations. Perdre un partenaire, c'est perdre des mots.

**O4 : Rendre la degradation physique narrative, pas numerique.**

Les pieds, les mains, la peau — le corps d'un citoyen se degrade au contact de la terre sismique. Cette degradation n'est pas un score de vie qui diminue. C'est une perte d'outils : des mains brulee par l'obsidienne ne peuvent plus faire de Contact fin. Des pieds detruits ne lisent plus le sol. Le modele doit encoder l'etat physique comme une capacite narrative, pas comme des points de vie.

**O5 : Permettre la mort comme evenement linguistique et professionnel.**

Quand un citoyen meurt, le monde perd des mots (son idiolecte, ses idiolectes de paire) et des perceptions (ses metiers). L'effet cascade — documenté dans `METIERS.md` — est le ressort dramatique central. Le modele doit rendre cette perte calculable : apres la mort de X, quels metiers restent couverts ? Quels vocabulaires disparaissent ? Quels couples linguistiques sont brises ?

---

## Non-Objectifs

- **Pas un systeme economique.** Contre-Terre n'a pas de monnaie, pas de guildes, pas de marche. Le Consortium des Archipels est une alliance de circonstance, pas une structure economique permanente. Le modele citoyen ne doit pas importer les patterns de Venezia (ducats, classes sociales, contrats).

- **Pas un systeme de progression.** Les citoyens ne "montent en niveau". Leurs metiers sont acquis par l'apprentissage long (des annees), pas par l'experience accumulee en session. Le modele capture un etat, pas une trajectoire de progression.

- **Pas un avatar jouable.** Le modele citoyen sert la narration et la simulation d'un monde, pas l'interaction joueur-personnage. Les citoyens sont des acteurs dans un monde habite, pas des personnages controlables.

---

## Tradeoffs

| Choix | Sacrifie | Justification |
|-------|----------|---------------|
| Corps > Economie | Pas de systeme de ressources individuelles | L'identite dans Contre-Terre est proprioceptive, pas financiere |
| Perception > Competence | Les metiers ne produisent pas de "resultats" mesurables | Un metier est un canal sensoriel, pas un outil de production |
| Relation > Individu | Le Contact est plus riche entre deux personnes que pour une seule | La richesse linguistique est distribuee, pas individuelle |
| Degradation narrative > Points de vie | Pas de score de sante numerique | La perte d'un doigt change ce qu'on peut *dire*, pas combien de temps on *survit* |

---

## Relation aux Autres Modules

- **contact_engine** : Le Contact est la *langue* du citoyen. Le citizen_model stocke le vocabulaire ; le contact_engine le fait vivre en interaction.
- **seismic_physics** : Le tremens calibre le corps du citoyen. La sensibilite tremens determine la capacite de prediction et la vulnerabilite aux seismes.
- **world_geography** : La zone (archipel, profondeur) determine le dialecte Contact et les conditions de degradation physique.
- **narrative_engine** : Les arcs narratifs des citoyens (mort, perte, heritage) sont pilotes par les proprietes du modele citoyen.

---

*Source : `PERSONNAGES.md`, `METIERS.md`, `CONTACT.md`, `MONDE.md`*
