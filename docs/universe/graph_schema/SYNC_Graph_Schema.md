# SYNC — Graph Schema

**Module :** `universe/graph_schema`

---

## Maturity

**STATUS : DESIGNING**

Le module `universe/graph_schema` definit comment le graph FalkorDB de Contre-Terre encode l'etat du monde -- citoyens, zones, Contact, seismes, equipement -- en utilisant le schema mind universel (5 node types, 1 link type). La documentation est complete. Le script de seeding et les fichiers de donnees n'ont pas encore ete generes.

### Ce qui est decide (canonical)

- **Schema mind strict** : 5 types (Actor, Space, Moment, Narrative, Thing), 1 lien (`link`). Aucun type custom. Toute semantique dans `type` (string) et `synthesis`/`content`
- **Actor = citoyen** : 7 principaux (subtype CITIZEN, weight 0.9) + 2-3 secondaires (SECONDARY_CHARACTER, weight 0.5). Synthesis encode nom + metiers + tremens + arc
- **Space = zones verticales** : 9 zones geographiques ordonnees par profondeur. Chaque zone a sa signature sismique, ses conditions de survie, ses variantes de Contact
- **Moment = evenements qui changent l'etat du monde** : morts (DEATH), seismes (SEISMIC_EVENT), seuils (THRESHOLD), inventions, revelations. Immutables une fois crees
- **Narrative = savoirs transmissibles** : metiers (15), systemes (Contact, tremens), arcs (Sihle/Enama, Nandi), variantes Contact, mythes
- **Thing = equipement** : 7 objets avec degradation (intact -> damaged -> destroyed -> abandoned). La Charge est le fil rouge materiel
- **Liens Contact** : SPEAKS_TO bidirectionnel, poids asymetriques derives de la matrice PERSONNAGES.md. Senzo-Nandi (0.9/0.85), Jabu-tous (0.1-0.15)
- **Procedure de mort** : atomique -- Moment DEATH + desactivation Actor + transfert objets + metiers orphelins detectables. Les liens SPEAKS_TO des morts ne sont jamais supprimes
- **Conventions d'ID** : `citizen:{prenom}`, `space:{nom_snake_case}`, `mort:{prenom}`, `metier:{nom}`, `thing:{nom}`

### Ce qui est en design (open)

- **Citoyens secondaires** : la vieille femme et le vieux du village sont documentes dans MAPPING.md mais leurs fiches Actor detaillees ne sont pas encore ecrites
- **Historique sismique pre-roman** : combien de Moments SEISMIC_EVENT faut-il seeder avant le Ch. I ? Assez pour montrer le pattern d'escalade, pas assez pour noyer le graph
- **Poids initiaux des Narratives** : les liens BELIEVES entre citoyens et savoirs n'ont pas encore de poids calibres. Le savoir de Nandi sur le geste inconnu est-il 0.3 (recoit sans comprendre) ou 0.5 (recoit avec intuition) ?
- **Metriques de degradation equipement** : a quel tick le sismographe passe de `intact` a `damaged` ? Le roman ne donne pas de moments precis pour chaque degradation

### Ce qui est propose (v2)

- **Graph dynamique temps reel** : le graph s'adapte en temps reel aux actions des citoyens AI dans Cities of Light, pas seulement aux evenements narratifs scriptes
- **Contact-monde dans le graph** : encoder les interactions humain-terre comme des liens Actor -> Space avec un type specifique, distincts des liens INHABITS
- **Poids temporels** : les liens SPEAKS_TO pourraient decroitre si deux citoyens n'interagissent pas pendant longtemps (atrophie du Contact), pas seulement augmenter

---

## Etat des fichiers

| Fichier | Statut | Notes |
|---------|--------|-------|
| `OBJECTIVES_Graph_Schema.md` | COMPLET | 5 objectifs hierarchises |
| `PATTERNS_Graph_Schema.md` | COMPLET | 7 decisions de design (types, liens, subtypes) |
| `BEHAVIORS_Graph_Schema.md` | COMPLET | 7 comportements observables du graph |
| `ALGORITHM_Graph_Schema.md` | COMPLET | 3 procedures (seeding, mise a jour, construction synthesis) |
| `VALIDATION_Graph_Schema.md` | COMPLET | 14 invariants (6 structurels, 6 semantiques, 2 schema) |
| `IMPLEMENTATION_Graph_Schema.md` | COMPLET | Patterns Cypher, structure script, hooks, conventions |
| `HEALTH_Graph_Schema.md` | COMPLET | 7 checks, 4 signaux de degradation, checklist |
| `SYNC_Graph_Schema.md` | COMPLET | Ce fichier |
| `scripts/seed_contre_terre_graph.py` | **A CREER** | Le script de seeding n'existe pas encore |
| `data/citizens.json` | **A CREER** | 7 principaux + secondaires a traduire depuis PERSONNAGES.md |
| `data/zones.json` | **A CREER** | 9 zones a traduire depuis PATTERNS P3 |
| `data/metiers.json` | **A CREER** | 15 metiers a traduire depuis METIERS.md |
| `data/equipment.json` | **A CREER** | 7 objets a traduire depuis PATTERNS P6 |
| `data/narratives.json` | **A CREER** | Savoirs, systemes, arcs a traduire depuis MAPPING.md |
| `data/contact_relations.json` | **A CREER** | Matrice des poids Contact a traduire depuis PERSONNAGES.md |

---

## Travail a faire

### Court terme (prochaine session)

1. **Generer les fichiers JSON** (`data/citizens.json`, `data/zones.json`, etc.) a partir des documents source
2. **Ecrire `seed_contre_terre_graph.py`** en suivant le pattern de `seed_venice_graph.py` et les procedures d'ALGORITHM A1
3. **Executer le seeding** sur FalkorDB et valider les 14 invariants de VALIDATION
4. **Verifier les checks HEALTH** sur le graph seede

### Moyen terme

5. **Calibrer les poids** : ajuster les poids Contact initiaux apres inspection du graph (les clusters relationnels emergent-ils correctement ?)
6. **Enrichir les citoyens secondaires** : fiches detaillees pour la vieille femme et le vieux du village
7. **Integrer avec le moteur** : connecter les hooks de mise a jour (on_contact, on_citizen_death, etc.) au moteur Cities of Light

### Long terme (v2)

8. Graph dynamique temps reel
9. Poids temporels (decroissance Contact)
10. Contact-monde comme liens explicites

---

## Dependances avec d'autres modules

| Module | Sens | Nature |
|--------|------|--------|
| `universe/manifest` | <-- | Structure du monde (zones, parametres physiques) |
| `universe/citizen_model` | <-- | Schema JSON des citoyens, seeding population |
| `universe/contact_engine` | --> | Lit/ecrit les liens SPEAKS_TO |
| `universe/seismic_physics` | --> | Lit/ecrit les Moments sismiques |
| `universe/narrative_engine` | --> | Lit les Narratives, ecrit les arcs |
| `universe/context_assembly` | --> | Traverse le graph pour assembler le contexte agent |
| `narration/personnages` | <-- | 7 personnages = templates Actor canoniques |
| `narration/metiers` | <-- | 15 metiers = templates Narrative |
| `worldbuilding/contact` | <-- | Mecaniques Contact = poids liens SPEAKS_TO |

---

## Handoff

**Pour agent groundwork :** Le travail immediat est la generation des fichiers JSON de donnees puis l'ecriture du script de seeding. Toute la spec est dans la doc chain -- ALGORITHM A1 donne l'ordre des etapes, IMPLEMENTATION donne les patterns Cypher, PATTERNS donne les subtypes et poids. Il s'agit de traduire la documentation en code executable.

**Pour agent architect :** Le module graph_schema est le socle de tous les autres modules `universe/`. Les modules contact_engine, seismic_physics, et narrative_engine dependront de la structure definie ici. Avant de commencer ces modules, le graph doit etre seede et valide.

**Pour humain :** La doc chain graph_schema est complete (8 fichiers). Les 7 personnages du roman fournissent les templates Actor canoniques. Le schema est strict (5 types mind, pas de custom). Les decisions de design (liens Contact bidirectionnels, Moments immutables, morts non-supprimees) sont documentees avec leurs justifications. Relecture souhaitee avant generation du script de seeding.

---

*Cree : 2026-03-13 -- Agent : Claude Opus 4.6*
