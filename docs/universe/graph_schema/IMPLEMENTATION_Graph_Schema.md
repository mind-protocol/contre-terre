# IMPLEMENTATION — Graph Schema

> Ou le code vit. Patterns Cypher. Structure du script de seeding. Points d'ancrage.

---

## Backend : FalkorDB

Contre-Terre utilise FalkorDB (comme Venezia). Le graph se nomme `contre_terre`. Les node_types sont des labels FalkorDB : `Actor`, `Space`, `Moment`, `Narrative`, `Thing`. Les liens sont tous de type `link`, semantique dans les proprietes.

**Configuration :**
- Host : variable d'environnement `FALKORDB_HOST` (default: `localhost`)
- Port : variable d'environnement `FALKORDB_PORT` (default: `6379`)
- Graph name : `contre_terre`

---

## Patterns Cypher

### Creation d'un citoyen

```cypher
MERGE (a:Actor {id: 'citizen:nandi'})
ON CREATE SET
    a.name = 'Nandi',
    a.type = 'CITIZEN',
    a.synthesis = 'Nandi. Predictrice des seismes, Explosiviste backup. Tremens extreme. Pieds nus, lit le sol. Porteuse du geste inconnu.',
    a.content = '...',
    a.status = 'active',
    a.weight = 0.9,
    a.energy = 0,
    a.created_at_s = 1741872000,
    a.updated_at_s = 1741872000
```

### Creation d'une zone

```cypher
MERGE (s:Space {id: 'space:deaf_village'})
ON CREATE SET
    s.name = 'Village des sourds',
    s.type = 'SETTLEMENT',
    s.synthesis = 'Village des sourds -- derniere communaute humaine. Magnitude 6, amortissement 40%. Contact haute-resolution 3 doigts. Bioluminescence domestiquee.',
    s.content = '...',
    s.status = 'active',
    s.weight = 1.0,
    s.energy = 0,
    s.created_at_s = 1741872000,
    s.updated_at_s = 1741872000
```

### Lien Contact entre deux citoyens

```cypher
MATCH (a:Actor {id: 'citizen:senzo'}), (b:Actor {id: 'citizen:nandi'})
MERGE (a)-[l:link {type: 'SPEAKS_TO'}]->(b)
ON CREATE SET l.weight = 0.9, l.created_at_s = 1741872000
```

Direction inverse :
```cypher
MATCH (a:Actor {id: 'citizen:nandi'}), (b:Actor {id: 'citizen:senzo'})
MERGE (a)-[l:link {type: 'SPEAKS_TO'}]->(b)
ON CREATE SET l.weight = 0.85, l.created_at_s = 1741872000
```

### Lien citoyen → zone

```cypher
MATCH (a:Actor {id: 'citizen:nandi'}), (s:Space {id: 'space:surface_desert'})
MERGE (a)-[l:link {type: 'INHABITS'}]->(s)
ON CREATE SET l.weight = 1, l.created_at_s = 1741872000
```

### Lien citoyen → metier

```cypher
MATCH (a:Actor {id: 'citizen:nandi'}), (n:Narrative {id: 'metier:predictrice'})
MERGE (a)-[l:link {type: 'PRACTICES'}]->(n)
ON CREATE SET l.weight = 0.8, l.created_at_s = 1741872000
```

### Creation d'un evenement sismique

```cypher
MERGE (m:Moment {id: 'seisme:magnitude_7_ch2'})
ON CREATE SET
    m.name = 'Seisme magnitude 7 -- Ch. II',
    m.type = 'SEISMIC_EVENT',
    m.synthesis = 'Premier gros seisme. Magnitude 7. Ch. II. Contact d urgence declenche. Le sol se met a danser.',
    m.content = '...',
    m.status = 'occurred',
    m.weight = 1.5,
    m.energy = 0,
    m.created_at_s = 1741872000,
    m.updated_at_s = 1741872000
```

### Mort d'un citoyen (transaction composite)

```cypher
// 1. Creer le Moment de mort
MERGE (m:Moment {id: 'mort:senzo'})
ON CREATE SET
    m.name = 'Mort de Senzo',
    m.type = 'DEATH',
    m.synthesis = 'Mort de Senzo. Ch. IV. Glissement de terrain dans la faille. Perte du leader, du cartographe, de l idiolecte de la nuque.',
    m.weight = 2.0,
    m.created_at_s = 1741872000

// 2. Desactiver le citoyen
MATCH (a:Actor {id: 'citizen:senzo'})
SET a.status = 'dead', a.updated_at_s = 1741872000

// 3. Lier mort → citoyen
MATCH (m:Moment {id: 'mort:senzo'}), (a:Actor {id: 'citizen:senzo'})
MERGE (m)-[l:link {type: 'ABOUT'}]->(a)
SET l.weight = 1.0

// 4. Lier mort → zone
MATCH (m:Moment {id: 'mort:senzo'}), (s:Space {id: 'space:vertical_fault'})
MERGE (m)-[l:link {type: 'LOCATED_AT'}]->(s)
SET l.weight = 1.0

// 5. Lier les temoins
MATCH (m:Moment {id: 'mort:senzo'}), (a:Actor {id: 'citizen:nandi'})
MERGE (a)-[l:link {type: 'WITNESSED'}]->(m)
SET l.weight = 1.0
// Repeter pour chaque temoin
```

---

## Structure du Script de Seeding

Le script de seeding suit le pattern de Venezia (`seed_venice_graph.py`) adapte a Contre-Terre.

```
scripts/
    seed_contre_terre_graph.py       # Script principal de seeding
data/
    citizens.json                     # 7 principaux + secondaires
    zones.json                        # 9 zones geographiques
    metiers.json                      # 15 metiers
    equipment.json                    # 7 objets significatifs
    narratives.json                   # Savoirs, systemes, arcs
    seismic_history.json              # Historique sismique pre-roman
    contact_relations.json            # Matrice des poids Contact
```

**Script principal :**
```python
# seed_contre_terre_graph.py
# Usage: python scripts/seed_contre_terre_graph.py [--clear] [--dry-run]

# Etapes dans l'ordre:
# [1/8] Creer les zones (Space)
# [2/8] Creer les citoyens (Actor)
# [3/8] Lier citoyens aux zones (INHABITS)
# [4/8] Creer les liens Contact (SPEAKS_TO bidirectionnels)
# [5/8] Creer les metiers (Narrative) et liens PRACTICES
# [6/8] Creer l'equipement (Thing) et liens CARRIES
# [7/8] Creer les Narratives (savoirs, systemes)
# [8/8] Creer l'historique sismique (Moment)
```

Le flag `--clear` ne supprime que les noeuds specifiques a Contre-Terre (type CITIZEN, GEOLOGICAL_LAYER, etc.) sans toucher l'infrastructure mind (agents, capabilities).

Le flag `--dry-run` affiche ce qui serait cree sans toucher FalkorDB.

---

## Hooks de Mise a Jour

Les mises a jour du graph sont declenchees par des evenements du moteur Cities of Light :

| Evenement | Hook | Action |
|-----------|------|--------|
| Contact entre 2 citoyens | `on_contact` | Incrementer weight SPEAKS_TO |
| Seisme | `on_seismic_event` | Creer Moment, lier zones, declencher tremens |
| Mort citoyen | `on_citizen_death` | Creer Moment DEATH, desactiver Actor, transferer objets |
| Changement de zone | `on_zone_change` | Mettre a jour INHABITS, creer Moment THRESHOLD |
| Transmission de savoir | `on_knowledge_transfer` | Creer lien BELIEVES |
| Degradation objet | `on_equipment_damage` | Mettre a jour Thing.status |

---

## Dependances Inter-Modules

```
universe/graph_schema
    ├── depends_on: universe/manifest (definit la structure du monde)
    ├── depends_on: universe/citizen_model (definit la structure des citoyens)
    ├── used_by: universe/contact_engine (lit/ecrit les liens SPEAKS_TO)
    ├── used_by: universe/seismic_physics (lit/ecrit les Moments sismiques)
    ├── used_by: universe/narrative_engine (lit les Narratives, ecrit les arcs)
    └── used_by: universe/context_assembly (traverse le graph pour assembler le contexte)
```

---

## Conventions de Nommage des IDs

| Type | Pattern | Exemples |
|------|---------|----------|
| Actor (principal) | `citizen:{prenom_lowercase}` | `citizen:nandi`, `citizen:senzo` |
| Actor (secondaire) | `character:{descripteur}` | `character:vieille_femme`, `character:vieux_echos` |
| Space (geologique) | `space:{nom_snake_case}` | `space:vertical_fault`, `space:deep_caves` |
| Space (habite) | `space:{nom_snake_case}` | `space:deaf_village` |
| Moment (mort) | `mort:{prenom}` | `mort:senzo`, `mort:jabu` |
| Moment (seisme) | `seisme:{description_courte}` | `seisme:magnitude_7_ch2` |
| Moment (seuil) | `seuil:{description}` | `seuil:entree_cavernes` |
| Narrative (systeme) | `systeme:{nom}` | `systeme:contact`, `systeme:tremens` |
| Narrative (metier) | `metier:{nom}` | `metier:predictrice`, `metier:aeromaitre` |
| Narrative (arc) | `arc:{nom}` | `arc:sihle_enama`, `arc:nandi` |
| Thing | `thing:{nom}` | `thing:charge`, `thing:seismograph` |

---

*References : seed_venice_graph.py (Venezia), MAPPING.md (conventions ID), database_config.yaml*
