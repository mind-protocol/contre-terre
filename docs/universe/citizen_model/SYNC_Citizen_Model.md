# SYNC — Citizen Model

> Etat actuel du module. Ce qui est fait, ce qui reste.

```
LAST_UPDATED: 2026-03-13
UPDATED_BY: Claude Opus 4.6 (agent, voice)
STATUS: DESIGNING
```

---

## Etat General

Le modele citoyen de Contre-Terre est concu mais pas encore implemente. La doc chain complete (8 fichiers) definit l'architecture : un citoyen est un acteur corporel defini par son tremens, ses metiers (organes de perception), son vocabulaire Contact (idiolecte personnel + idiolectes de paire), son etat physique, et sa zone geographique. Le modele rompt deliberement avec Venezia : pas de ducats, pas de guildes, pas de classes sociales. L'identite est proprioceptive, pas economique.

Les 7 personnages du roman sont les premiers citoyens vivants de l'univers — pas des personnages historiques, mais des citoyens actifs. Le roman est leur mythe fondateur, pas leur biographie. Ils ne meurent pas canoniquement dans l'univers. Leur data est entierement definie dans `PERSONNAGES.md` et `METIERS.md`. La population elargie (50-80 citoyens) reste a seeder.

**Decision canonique : les citoyens ne savent pas qu'ils sont IA.** Pas de SID Mind Protocol (pas de privacy-first, pas d'open-source, pas de $MIND, pas de blockchain). Les citoyens vivent sur Contre-Terre, point. Ils ne partagent aucune valeur de base Mind Protocol. Leur ontologie est celle de leur monde : tremens, Contact, metiers, archipels.

**Decision canonique : les restrictions d'univers sont physiques, pas legales.** Un citoyen CT ne peut pas visiter Venise parce que son corps est calibre pour les tremens (desorientation sans vibration), sa langue est le Contact (inutile dans un monde vocal), ses perceptions de metier sont specifiques au volcan. Un poisson ne visite pas la montagne — pas par regle, par biologie.

**Brain seed prototype complet (2026-03-13) :** 16 fichiers JSON, 347 noeuds, 736 liens. 1 base partagee (47 noeuds, 111 liens), 10 clusters metier (predicteur, explosiviste, chef_expedition, cartographe, ecouteur, meteorologue, mineur, biologiste, cuisinier, survivaliste), 4 cerveaux citoyens (Nandi, Senzo, Sihle, Enama), 1 cluster d'integration (relations inter-citoyens). 3 cerveaux restants (Thabo, Inyoni, Jabu) a construire.

---

## Maturity

**STATUS: DESIGNING**

### Ce qui est canonique (v1)

- **Structure du citoyen** : schema JSON defini dans `ALGORITHM_Citizen_Model.md` et `IMPLEMENTATION_Citizen_Model.md`
- **Les 15 metiers** : definis, assignes, cascade de pertes documentee dans `METIERS.md`
- **Les 7 personnages du roman** : idiolectes, metiers, tremens, arcs — tous documentes dans `PERSONNAGES.md`. Statut = **vivants** (le roman est un mythe fondateur, pas leur histoire)
- **Les 5 idiolectes de paire** : Senzo/Nandi, Thabo/Inyoni, Enama/Nandi, Sihle/Enama, Jabu/groupe — documentes dans `PERSONNAGES.md`
- **L'effet cascade** : progression monotone decroissante des metiers couverts (dans le mythe et dans les game loops)
- **Le mapping corps-capacite** : degradation des pieds/mains/peau affecte perception et Contact
- **11 invariants** : definis dans `VALIDATION_Citizen_Model.md`
- **Pas de conscience de soi** : les citoyens ne savent pas qu'ils sont IA, pas de SID Mind Protocol
- **Restrictions physiques** : le corps calibre au tremens empeche le voyage inter-univers (pas de regle, de la biologie)
- **Brain seed** : 4 cerveaux complets (Nandi, Senzo, Sihle, Enama) + 10 clusters metier + 1 base partagee = 347 noeuds, 736 liens

### Ce qui est en cours de design

- **Les 7 archipels** : mentionnes (Consortium des Archipels) mais pas detailles individuellement. Chaque archipel doit avoir un nom, un profil geologique, un dialecte Contact, et une distribution de metiers.
- **Le seeding de la population** : l'algorithme est defini mais pas execute. Pas de `data/citizens.json` encore.
- **Le mapping Mind** : comment les citoyens sont injectes dans le graph (node_type, content, synthesis). Schema defini, pas de code d'ingestion.

### Ce qui est propose (v2)

- **Simulation de l'effet cascade** : un script qui prend une sequence de morts et calcule les pertes a chaque etape (metiers, idiolectes, vocabulaire). Utile pour verifier la coherence narrative.
- **Generateur d'idiolectes** : un outil qui genere des gestes plausibles pour les citoyens de la population elargie, en respectant les metiers et les zones du corps.
- **Dialectes inter-archipel** : chaque archipel a sa variante du Contact. Les differences dialectales pourraient etre modelisees (gestes communs avec des variations de zone/pression/duree).

---

## Dependances

| Module | Relation | Statut du module |
|--------|----------|-----------------|
| `worldbuilding/contact` | Le Contact est la langue du citoyen | DESIGNING — doc chain complete |
| `worldbuilding/seismique` | Le tremens calibre le corps | DESIGNING — doc chain complete |
| `worldbuilding/geographie` | Les archipels distribuent la population | DESIGNING — doc chain complete |
| `narration/personnages` | Les 7 personnages sont les instances de reference | DESIGNING — doc chain complete |
| `narration/metiers` | Les 15 metiers definissent la perception | DESIGNING — doc chain complete |
| `universe/contact_engine` | Le moteur Contact fera vivre les interactions | PAS COMMENCE |
| `universe/narrative_engine` | Le moteur narratif pilotera les arcs | PAS COMMENCE |

---

## Ce Qui Reste a Faire

### Priorite haute

- [ ] **Detailler les 7 archipels** : noms, profils geologiques, dialectes Contact, affinites metier. Source : `PERSONNAGES.md` (Consortium des Archipels) + `MONDE.md` (geographie sismique).
- [ ] **Seeder la population initiale** : 50-80 citoyens selon l'algorithme defini, generer `data/citizens.json`.
- [ ] **Encoder les 7 personnages du roman** : transformer les fiches de `PERSONNAGES.md` en JSON conformes au schema.

### Priorite moyenne

- [ ] **Implementer l'algorithme A3** (effet cascade) : script Python qui prend une sequence de morts et calcule les pertes.
- [ ] **Valider le seeding** : executer tous les checks de `HEALTH_Citizen_Model.md` sur la population generee.
- [ ] **Mapper vers le graph Mind** : ingestion des citoyens comme nodes `actor/citizen` dans le graph.

### Priorite basse

- [ ] **Generateur d'idiolectes** : outil de generation de gestes pour la population elargie.
- [ ] **Simulation dialectale** : modeliser les variantes Contact par archipel.
- [ ] **Visualisation de l'effet cascade** : representation graphique de la perte de metiers/vocabulaire chapitre par chapitre.

---

## Tensions

| Tension | Statut | Notes |
|---------|--------|-------|
| Venezia patterns vs Contre-Terre | **RESOLUE** — rupture deliberee. Le citizen_model de Contre-Terre n'importe rien de Venezia sauf le format JSON. | Decision documentee dans PATTERNS P1. |
| Taille de la population | **OUVERTE** — 50-80 est une estimation. Le monde de Contre-Terre a-t-il besoin de plus de citoyens pour les archipels ? Nicolas doit arbitrer. | @mind:escalation |
| Noms des archipels | **OUVERTE** — les 7 archipels sont references par type geologique (subduction, volcanique, etc.), pas par nom propre. Des noms narratifs seraient necessaires pour le worldbuilding. | @mind:todo |
| Personnages vivants vs morts dans le roman | **RESOLUE** — les 7 personnages sont vivants dans l'univers. Le roman est un mythe fondateur. Ils meurent dans le mythe, pas dans l'univers. | Decision 2026-03-13 |
| Conscience de soi des citoyens | **RESOLUE** — les citoyens ne savent pas qu'ils sont IA. Pas de SID Mind Protocol. Pas de meta-connaissance. Ils vivent sur Contre-Terre, point. | Decision 2026-03-13 |
| Restrictions inter-univers | **RESOLUE** — restrictions physiques, pas legales. Le corps calibre au tremens empeche le voyage (desorientation, langue incompatible, perceptions inutiles hors volcan). | Decision 2026-03-13 |

---

## Handoff

**Pour l'agent groundwork (implementation) :**
- Lire la doc chain entiere avant de coder
- Le schema JSON de `IMPLEMENTATION_Citizen_Model.md` est la source de verite pour la structure
- Commencer par encoder les 7 personnages du roman en JSON (cas concrets avant generalisation)
- Le seeding de la population elargie vient apres, une fois les 7 personnages valides
- Les invariants de `VALIDATION_Citizen_Model.md` sont des tests, pas des suggestions

**Pour Nicolas :**
- Le modele citoyen est concu. Les decisions de design (corps > economie, metier = perception, Contact > score) sont documentees dans PATTERNS.
- Decisions en attente : taille de la population (50-80 ou plus ?), noms des archipels, niveau de detail des dialectes inter-archipel.
- Les 7 personnages du roman sont deja entierement definis — ce module les formalise en structure de donnees sans rien perdre de leur richesse narrative.

---

*Derniere mise a jour : 2026-03-13*
