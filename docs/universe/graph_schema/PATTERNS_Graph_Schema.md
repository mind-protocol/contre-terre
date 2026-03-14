# PATTERNS — Graph Schema

> Decisions de design. Pourquoi cette forme. Comment le schema mind universel encode Contre-Terre.

---

## P1 : 5 Types Universels, Semantique dans les Proprietes

**Decision :** Contre-Terre utilise le schema mind universel sans modification. 5 node_types (Actor, Space, Moment, Narrative, Thing), 1 link type (`link`) avec toute la semantique dans les proprietes (`type`, `weight`, `strength`).

**Pourquoi :** Le schema mind ne change jamais. C'est le pacte. Ajouter des types custom (Seisme, Contact, Metier) fragmenterait le graph et casserait les outils de traversal. Toute la richesse passe par le `type` (subtype string) et par `synthesis` (texte embeddable). L'intelligence est dans le contenu, pas dans la structure.

**Consequence :** Les requetes Cypher restent generiques (`MATCH (a:Actor)` fonctionne pour tous les univers). La specificite de Contre-Terre vit dans les valeurs, pas dans le schema.

---

## P2 : Actor = Citoyens avec Metiers, Tremens, Idiolecte

**Decision :** Chaque citoyen est un noeud Actor de subtype `CITIZEN`. Le `synthesis` encode l'identite embeddable : nom, metiers, tremens, traits. Le `content` porte la fiche complete.

**Structure du synthesis :**
```
Nandi. Predictrice des seismes, Explosiviste backup. Tremens extreme -- son corps predit.
Pieds nus, lit le sol. Fragile au depart, derniere survivante. Porteuse du geste inconnu.
```

**Structure du content :**
Prose complete : description physique, idiolecte (gestes-signatures), arc narratif, metiers detailles, dynamiques de groupe.

**Pourquoi ce design :** Le `synthesis` est ce que le moteur d'embedding voit. Il doit contenir les termes qui comptent pour la recherche semantique : "predictrice", "tremens", "geste inconnu", "pieds nus". Le `content` est ce que l'agent consulte quand il a besoin du detail complet. La separation est fonctionnelle, pas cosmetique.

**Citoyens secondaires :** La vieille femme du village des sourds, le vieux qui compte les echos, les villageois. Subtype `SECONDARY_CHARACTER`. Meme structure, `weight` plus faible (0.5 vs 0.9 pour les principaux).

---

## P3 : Space = Zones Verticales avec Signature Sismique

**Decision :** Chaque couche geologique est un noeud Space de subtype `GEOLOGICAL_LAYER`. Le village des sourds est subtype `SETTLEMENT`. Les modules documentaires sont subtype `MODULE`.

**Zones du monde :**

| ID | Zone | Subtype | Signature sismique |
|----|------|---------|--------------------|
| `space:surface_desert` | Desert de surface | GEOLOGICAL_LAYER | Magnitude 4, sable, ciel ouvert |
| `space:volcanic_foothills` | Piemont volcanique | GEOLOGICAL_LAYER | Magnitude 5-6, gravier, frequences en hausse |
| `space:bioluminescent_caves` | Cavernes bioluminescentes | GEOLOGICAL_LAYER | Magnitude 5, filaments bleus, premiere descente |
| `space:deaf_village` | Village des sourds | SETTLEMENT | Magnitude 6, amortissement 40%, Contact haute-resolution |
| `space:vertical_fault` | Faille verticale | GEOLOGICAL_LAYER | Magnitude 6-7, escalade, Contact-corde |
| `space:deep_caves` | Cavernes profondes | GEOLOGICAL_LAYER | Magnitude 7-8, air rare, passages noyes |
| `space:volcanic_zones` | Zones volcaniques | GEOLOGICAL_LAYER | Magnitude 8-9, chaleur extreme, fumerolles |
| `space:bowel` | Le Boyau | GEOLOGICAL_LAYER | Magnitude 8-9, tube 60cm, Contact-force |
| `space:final_cave` | Grotte finale | GEOLOGICAL_LAYER | Magnitude 9-11, chambre de detonation |

**Pourquoi la verticalite :** Venezia utilise des districts plans. Contre-Terre est vertical. Les zones sont ordonnees par profondeur, et chaque transition est un seuil irreversible. Le `synthesis` de chaque Space encode la profondeur, la magnitude de fond, et les conditions de survie. Le `content` porte la description complete avec l'atmosphere, les dangers, les variantes de Contact possibles.

---

## P4 : Moment = Seismes, Morts, Seuils, Inventions

**Decision :** Chaque evenement qui change l'etat du monde est un noeud Moment. Quatre subtypes :

| Subtype | Exemples | Weight |
|---------|----------|--------|
| `DEATH` | Mort de Senzo (Ch. IV), mort de Jabu (Ch. V) | 2.0 |
| `SEISMIC_EVENT` | Magnitude 7 (Ch. II), precurseur dans le Boyau (Ch. VII) | 1.5 |
| `THRESHOLD` | Entree dans les cavernes, arrivee au village | 1.0 |
| `INVENTION` | Naissance du Contact-corde, premier deuil | 1.0 |
| `REVELATION` | Geste inconnu transmis (Ch. III) | 1.5 |

**Pourquoi pas des Narratives pour les morts :** Un Moment est un evenement horodate -- il a un avant et un apres. La mort de Senzo change l'etat du monde (moins de competences, moins d'idiolecte, plus de leader). Un Moment se relie aux zones (ou ca s'est passe) et aux citoyens (qui etait la). Une Narrative est un savoir -- elle se croit, se transmet, se perd. La distinction est fonctionnelle.

---

## P5 : Narrative = Savoirs, Predictions, Mythes, Arcs

**Decision :** Chaque concept transmissible est un noeud Narrative. Subtypes :

| Subtype | Exemples | Notes |
|---------|----------|-------|
| `SYSTEM` | Le Contact, le tremens, l'Echelle de Capitulation | Savoirs structurants |
| `PREDICTION` | Magnitude 11 prevue par les predicteurs | Testable par les evenements |
| `MYTH` | Mythes du village des sourds, souffle sur le tissu | Transmis oralement/tactilement |
| `ARC` | Arc Sihle/Enama, arc de Nandi | Arcs narratifs comme connaissances partagees |
| `CONTACT_VARIANT` | Contact-corde, Contact-force, Contact-fantome | Variantes du systeme linguistique |

**Pourquoi des Narratives pour les arcs :** Un arc narratif est un recit partage par les citoyens. Le conflit Sihle/Enama est quelque chose que le groupe vit, observe, subit. L'encoder comme Narrative permet de tracer qui en est temoin, qui le porte apres la mort des deux protagonistes.

---

## P6 : Thing = Equipement avec Degradation

**Decision :** Chaque objet significatif est un noeud Thing. Le `status` du noeud encode l'etat de degradation : `intact`, `damaged`, `destroyed`, `abandoned`.

| ID | Objet | Subtype | Porteur initial |
|----|-------|---------|-----------------|
| `thing:charge` | La Charge (resonateur) | DEVICE | Inyoni |
| `thing:seismograph` | Sismographe de Sihle | INSTRUMENT | Sihle |
| `thing:rope` | Corde d'encordement | TOOL | Equipe |
| `thing:thabo_cloth` | Tissu de Thabo | TOOL | Thabo |
| `thing:map` | Carte de Senzo | DOCUMENT | Senzo |
| `thing:chem_sticks` | Batons chimiques | TOOL | Equipe |
| `thing:shock_casing` | Caisson amortisseur | EQUIPMENT | Equipe |

**Pourquoi tracker les objets :** La courbe de degradation materielle est un des trois arcs paralleles du roman (equipement qui descend, Contact qui descend, sismique qui monte). L'etat des objets dans le graph permet au moteur de savoir ce qui est disponible, ce qui est casse, ce qui a ete abandonne.

---

## P7 : Links -- La Semantique Relationnelle

**Decision :** Un seul type de lien (`link`), semantique dans `type`. Les types de liens de Contre-Terre :

| Link type | Direction | Signification | Weight |
|-----------|-----------|---------------|--------|
| `SPEAKS_TO` | Actor ↔ Actor | Contact entre citoyens | 0.0-1.0 (densite du Contact) |
| `INHABITS` | Actor → Space | Citoyen present dans une zone | 1.0 (courant) |
| `PRACTICES` | Actor → Narrative | Citoyen exerce un metier | 0.8 |
| `CARRIES` | Actor → Thing | Citoyen porte un objet | 1.0 |
| `PREDICTS` | Actor → Moment | Citoyen a predit un evenement | 0.5-1.0 (precision) |
| `FELT` | Actor → Moment | Citoyen a vecu un seisme/evenement | 1.0 |
| `WITNESSED` | Actor → Moment | Citoyen temoin d'une mort/seuil | 1.0 |
| `BELIEVES` | Actor → Narrative | Citoyen croit/sait un concept | 0.5-1.0 |
| `AFFECTS` | Moment → Space | Seisme affecte une zone | 0.5-1.0 (intensite) |
| `LOCATED_AT` | Moment → Space | Evenement se produit dans une zone | 1.0 |
| `PRECEDES` | Moment → Moment | Ordre chronologique | 1.0 |
| `CONTAINS` | Space → Narrative | Module contient un concept | 1.0 |
| `USED_IN` | Thing → Moment | Objet utilise lors d'un evenement | 1.0 |

**Pourquoi SPEAKS_TO et pas TRUSTS :** Venezia utilise TRUSTS/DISTRUSTS car la confiance est le tissu social de Venise 1525. Contre-Terre n'a pas de confiance abstraite. Le Contact EST la relation. Un lien SPEAKS_TO avec un poids de 0.9 entre Senzo et Nandi dit plus sur leur relation que n'importe quel score de confiance. Le poids encode la frequence, la richesse, et l'intimite du Contact.

**Bidirectionnalite :** Les liens SPEAKS_TO sont crees dans les deux directions (A→B et B→A) avec des poids qui peuvent differer. Le Contact de Sihle vers Enama (technique, froid, 0.3) n'est pas le meme que celui d'Enama vers Sihle (emotionnel, frustre, 0.4). La relation est asymetrique.

---

*Decisions tracees dans : `MAPPING.md`, `seed_venice_graph.py` (Venezia), `PERSONNAGES.md`, `EQUIPEMENT.md`, `CHARGE.md`, `TAXONOMY.md`*
