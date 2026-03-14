# ALGORITHM — Graph Schema

> Procedures. Comment le graph est peuple, mis a jour, et maintenu.

---

## A1 : Procedure de Seeding Initial

Le seeding cree l'etat du monde au debut du roman (Ch. I). Inspire du pattern de `seed_venice_graph.py` (Venezia), adapte aux specificites de Contre-Terre.

### Etape 1 — Creer les zones (Space nodes)

9 zones geographiques. Chaque zone est un noeud Space avec `type`, `synthesis` (nom + description embeddable + signature sismique), `content` (description complete), `status: 'active'`, `weight` proportionnel a l'importance narrative.

```
Pour chaque zone dans ZONES:
    MERGE (s:Space {id: zone.id})
    SET s.name, s.type = 'GEOLOGICAL_LAYER' ou 'SETTLEMENT',
        s.synthesis, s.content, s.status = 'active',
        s.weight, s.energy = 0,
        s.created_at_s = now
```

Ordre de creation : surface → profondeur (la verticalite est l'ordre naturel).

### Etape 2 — Creer les citoyens (Actor nodes)

7 personnages principaux + 2-3 secondaires. Chaque citoyen est un noeud Actor avec `synthesis` construit selon le pattern : nom, metiers, tremens, traits cles.

```
Pour chaque citoyen dans CITIZENS:
    synthesis = build_citizen_synthesis(citoyen)
    content = build_citizen_content(citoyen)
    MERGE (a:Actor {id: citoyen.id})
    SET a.name, a.type = 'CITIZEN' ou 'SECONDARY_CHARACTER',
        a.synthesis, a.content, a.status = 'active',
        a.weight = 0.9 (principal) ou 0.5 (secondaire),
        a.energy = 0, a.created_at_s = now
```

Le `build_citizen_synthesis` condense : nom, metiers (par nom), trait tremens, arc en une phrase, gestes-signatures cles.

Le `build_citizen_content` porte la fiche complete : description, personnalite, dynamiques, idiolecte, historique.

### Etape 3 — Lier les citoyens aux zones

Chaque citoyen commence dans la zone de surface.

```
Pour chaque citoyen:
    MATCH (a:Actor {id: citoyen.id}), (s:Space {id: 'space:surface_desert'})
    MERGE (a)-[l:link {type: 'INHABITS'}]->(s)
    SET l.weight = 1, l.created_at_s = now
```

### Etape 4 — Creer les liens de Contact initiaux

Les relations de Contact existent avant le debut du roman. Le poids est base sur la matrice des relations de PERSONNAGES.md :

```
Pour chaque paire (A, B) dans RELATIONS:
    weight_ab = contact_weight(A, B)  # derive de la matrice
    weight_ba = contact_weight(B, A)  # potentiellement different

    MERGE (a)-[l:link {type: 'SPEAKS_TO'}]->(b)
    SET l.weight = weight_ab, l.created_at_s = now

    MERGE (b)-[l:link {type: 'SPEAKS_TO'}]->(a)
    SET l.weight = weight_ba, l.created_at_s = now
```

Poids initiaux derives de la matrice :

| Paire | Weight A→B | Weight B→A | Justification |
|-------|-----------|-----------|---------------|
| Senzo → Nandi | 0.9 | 0.85 | Dialecte le plus riche, intime |
| Thabo → Inyoni | 0.7 | 0.7 | Test-et-tient, symetrique |
| Enama → Nandi | 0.6 | 0.55 | Grip de calibration, Contact-terre |
| Sihle → Enama | 0.3 | 0.4 | Conflit, Contact pauvre |
| Jabu → (tous) | 0.1-0.15 | 0.1-0.15 | Quasi-absent |

### Etape 5 — Creer les liens metiers (PRACTICES)

```
Pour chaque citoyen:
    Pour chaque metier du citoyen:
        MATCH (a:Actor {id: citoyen.id})
        MERGE (n:Narrative {id: 'metier:' + metier.id})
        ON CREATE SET n.name = metier.nom, n.type = 'METIER',
                      n.synthesis = metier.description_courte
        MERGE (a)-[l:link {type: 'PRACTICES'}]->(n)
        SET l.weight = 0.8
```

### Etape 6 — Creer les noeuds d'equipement (Thing nodes)

```
Pour chaque objet dans EQUIPMENT:
    MERGE (t:Thing {id: objet.id})
    SET t.name, t.type, t.synthesis, t.content,
        t.status = 'intact', t.weight, t.created_at_s = now

    MATCH (a:Actor {id: objet.porteur}), (t:Thing {id: objet.id})
    MERGE (a)-[l:link {type: 'CARRIES'}]->(t)
    SET l.weight = 1, l.created_at_s = now
```

### Etape 7 — Creer les Narratives (savoirs et systemes)

```
Pour chaque concept dans NARRATIVES:
    MERGE (n:Narrative {id: concept.id})
    SET n.name, n.type, n.synthesis, n.content,
        n.status = 'active', n.weight, n.created_at_s = now
```

Lier les citoyens aux savoirs qu'ils portent via BELIEVES.

### Etape 8 — Creer l'historique sismique initial

Seeder quelques Moments sismiques historiques (avant le debut du roman) pour etablir le pattern d'escalade :

```
Pour chaque seisme_historique:
    MERGE (m:Moment {id: seisme.id})
    SET m.name, m.type = 'SEISMIC_EVENT', m.synthesis, m.content,
        m.weight = 1.5, m.created_at_s = seisme.timestamp

    # Lier aux zones affectees
    MERGE (m)-[l:link {type: 'AFFECTS'}]->(s:Space {id: zone.id})
    SET l.weight = seisme.intensite_locale
```

---

## A2 : Procedure de Mise a Jour (Evenements)

### Nouveau Contact

Quand deux citoyens interagissent via le Contact :

```
1. MATCH les deux noeuds Actor
2. Verifier qu'un lien SPEAKS_TO existe dans les deux directions
3. Incrementer le weight du lien (capped a 1.0)
4. Mettre a jour updated_at_s
```

Le poids augmente vite au debut (chaque Contact compte) et sature (la relation a un plafond). Formule : `new_weight = min(1.0, old_weight + 0.05 * quality)` ou `quality` est 0.5 (banal) a 1.0 (marquant).

### Nouveau Seisme

```
1. Creer un noeud Moment (type: SEISMIC_EVENT)
2. Lier aux zones affectees (AFFECTS) avec poids = intensite locale
3. Lier aux citoyens presents (FELT) avec poids = 1.0
4. Si predit par un citoyen: creer lien PREDICTS retroactif
5. Mettre a jour le PRECEDES avec le seisme precedent
```

### Mort d'un Citoyen

La procedure la plus lourde. Change l'etat du monde.

```
1. Creer un noeud Moment (type: DEATH)
2. Passer le status du citoyen a 'dead'
3. Lier le Moment a la zone (LOCATED_AT) et au citoyen (endpoint)
4. Lier les citoyens temoins (WITNESSED)
5. Les liens SPEAKS_TO du mort deviennent historiques (ne pas supprimer -- le poids reste, le status indique la mort)
6. Transferer les objets (CARRIES) au nouveau porteur si applicable
7. Mettre a jour les metiers : verifier si PRACTICES perd son dernier porteur actif
```

### Changement de Zone

Quand l'expedition descend :

```
1. Pour chaque citoyen actif:
    a. Supprimer le lien INHABITS vers l'ancienne zone
    b. Creer un lien INHABITS vers la nouvelle zone
2. Creer un Moment (type: THRESHOLD) pour le passage
3. Lier le Moment aux deux zones (ancienne et nouvelle)
```

### Transmission de Savoir

Quand un citoyen transmet un savoir (Inyoni → Nandi pour la Charge, Thabo → Nandi pour le damier) :

```
1. MATCH le citoyen recepteur et la Narrative
2. Creer un lien BELIEVES (recepteur → Narrative)
3. Weight = 0.5 au debut (savoir recu mais pas encore maitrise)
4. Creer un Moment (type: INVENTION ou REVELATION) pour tracer l'evenement
```

---

## A3 : Construction du Synthesis

Le `synthesis` est le champ le plus critique -- c'est ce que les embeddings voient. Regles de construction :

**Pour un Actor (citoyen) :**
```
{nom}. {metier_1}, {metier_2}. {trait_tremens}. {geste_signature_cle}. {arc_en_une_phrase}.
```
Max 500 caracteres. Les mots importants doivent etre presents : nom, metiers, tremens, geste.

**Pour un Space (zone) :**
```
{nom} -- {subtype}. Magnitude {mag}, {conditions}. Contact: {variante_contact_locale}.
```
Max 400 caracteres. Signature sismique + conditions de survie + type de Contact.

**Pour un Moment (evenement) :**
```
{nom}. {type}. Ch. {num}. {description_courte}. Consequence: {impact_principal}.
```
Max 300 caracteres. Type + chapitre + impact.

**Pour une Narrative (savoir) :**
```
{nom}. {type}. {definition_courte}. Porteurs: {liste_citoyens}.
```
Max 400 caracteres. Definition + qui le sait.

**Pour un Thing (objet) :**
```
{nom}. {type}. Porteur: {citoyen}. Etat: {status}. {role_narratif_court}.
```
Max 300 caracteres. Etat + porteur + role.

---

*Procedures derivees de : seed_venice_graph.py (Venezia), MAPPING.md, PERSONNAGES.md, METIERS.md, EQUIPEMENT.md*
