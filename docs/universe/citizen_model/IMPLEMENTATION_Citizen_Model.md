# IMPLEMENTATION — Citizen Model

> Schema JSON, seeding, et integration. Ou le modele vit dans le code.

---

## Schema JSON — Citoyen

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Contre-Terre Citizen",
    "type": "object",
    "required": ["id", "name", "archipel_origin", "tremens_sensitivity", "physical_state", "metiers", "contact_vocabulary", "zone", "alive"],
    "properties": {
        "id": {
            "type": "string",
            "description": "Identifiant unique du citoyen"
        },
        "name": {
            "type": "string",
            "description": "Nom du citoyen (convention zulu pour le roman)"
        },
        "archipel_origin": {
            "type": "string",
            "enum": ["archipel_subduction", "archipel_volcanique", "archipel_cotier", "archipel_plateau", "archipel_rift", "archipel_dorsale", "archipel_fosse"],
            "description": "Archipel de naissance (1 des 7 du Consortium)"
        },
        "tremens_sensitivity": {
            "type": "number",
            "minimum": 0.0,
            "maximum": 1.0,
            "description": "Sensibilite au tremens : 0 = insensible, 1 = predicteur pur"
        },
        "physical_state": {
            "type": "object",
            "required": ["feet", "hands", "skin", "inner_ear", "general"],
            "properties": {
                "feet": { "type": "string", "enum": ["intact", "worn", "damaged", "destroyed"] },
                "hands": { "type": "string", "enum": ["intact", "calloused", "cut", "burned", "destroyed"] },
                "skin": { "type": "string", "enum": ["intact", "abraded", "burned", "scarred"] },
                "inner_ear": { "type": "string", "enum": ["intact", "strained", "damaged", "deaf"] },
                "general": { "type": "string", "enum": ["healthy", "fatigued", "exhausted", "critical"] }
            }
        },
        "metiers": {
            "type": "array",
            "minItems": 1,
            "maxItems": 3,
            "items": {
                "type": "object",
                "required": ["id", "name", "perception_channel", "active"],
                "properties": {
                    "id": { "type": "integer", "minimum": 1, "maximum": 15 },
                    "name": { "type": "string" },
                    "perception_channel": { "type": "string" },
                    "active": { "type": "boolean", "default": true }
                }
            }
        },
        "contact_vocabulary": {
            "type": "object",
            "required": ["base_gestures", "personal_idiolect", "learned_variants"],
            "properties": {
                "base_gestures": {
                    "type": "array",
                    "items": { "type": "string" },
                    "minItems": 4,
                    "description": "Gestes universels du Contact"
                },
                "personal_idiolect": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["gesture", "meaning", "body_zone"],
                        "properties": {
                            "gesture": { "type": "string" },
                            "meaning": { "type": "string" },
                            "body_zone": { "type": "string", "enum": ["shoulder", "arm", "wrist", "hand", "nape", "forehead", "palm", "ground"] }
                        }
                    }
                },
                "learned_variants": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "Variantes Contact apprises (Contact-corde, haute-resolution, etc.)"
                }
            }
        },
        "pair_idiolects": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["partner_id", "gestures", "status"],
                "properties": {
                    "partner_id": { "type": "string" },
                    "gestures": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["gesture", "meaning"],
                            "properties": {
                                "gesture": { "type": "string" },
                                "meaning": { "type": "string" },
                                "origin_chapter": { "type": "integer" }
                            }
                        }
                    },
                    "status": { "type": "string", "enum": ["active", "orphaned", "dead"] }
                }
            }
        },
        "zone": {
            "type": "object",
            "required": ["current_archipel", "depth_level", "sub_zone"],
            "properties": {
                "current_archipel": { "type": "string" },
                "depth_level": { "type": "integer", "minimum": 0, "maximum": 7 },
                "sub_zone": { "type": "string" }
            }
        },
        "relationships": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["citizen_id", "contact_history", "bond_nature"],
                "properties": {
                    "citizen_id": { "type": "string" },
                    "contact_history": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["chapter", "type", "body_zone", "significance"],
                            "properties": {
                                "chapter": { "type": "integer" },
                                "type": { "type": "string", "enum": ["standard", "intimate", "conflict", "urgency", "grief", "phantom"] },
                                "body_zone": { "type": "string" },
                                "significance": { "type": "string" }
                            }
                        }
                    },
                    "bond_nature": { "type": "string", "enum": ["intimate", "colleague", "conflict", "minimal", "absent", "pedagogic", "silent"] }
                }
            }
        },
        "alive": { "type": "boolean" },
        "death": {
            "type": ["object", "null"],
            "properties": {
                "chapter": { "type": "integer" },
                "cause": { "type": "string" },
                "element": { "type": "string", "enum": ["landslide", "fall", "drowning", "lava", "burial", "explosion"] },
                "metiers_lost": { "type": "array", "items": { "type": "string" } },
                "idiolects_killed": { "type": "array", "items": { "type": "string" } },
                "vocabulary_lost": { "type": "array", "items": { "type": "string" } }
            }
        }
    }
}
```

---

## Seeding de la Population Initiale

### Etape 1 : Les 7 Archipels

Les 7 archipels du Consortium sont les sources de la population. Chaque archipel a un profil geologique qui influence la distribution des metiers :

```
archipels = [
    { name: "archipel_subduction",  size: 12, affinities: [8, 9, 1] },     # ecouteur, predicteur, meteo
    { name: "archipel_volcanique",  size: 11, affinities: [15, 6, 4] },    # aeromaître, geologue, mineur
    { name: "archipel_cotier",      size: 10, affinities: [2, 14, 13] },   # ocean, speleo, cuisinier
    { name: "archipel_plateau",     size: 10, affinities: [7, 12, 10] },   # cartographe, chef, survie
    { name: "archipel_rift",        size: 9,  affinities: [3, 6, 15] },    # biologiste, geologue, aeromaître
    { name: "archipel_dorsale",     size: 9,  affinities: [8, 4, 1] },     # ecouteur, mineur, meteo
    { name: "archipel_fosse",       size: 9,  affinities: [2, 14, 11] },   # ocean, speleo, grimpeuse
]
# Total : 70 citoyens (ajustable 50-80)
```

### Etape 2 : Generation des Citoyens

Pour chaque archipel, generer N citoyens selon les regles d'`ALGORITHM_Citizen_Model.md` :
1. Nom : genere selon conventions zulu (le roman utilise cette convention)
2. Metiers : 1-3, biaises vers les affinites de l'archipel
3. Tremens : derive des metiers (predicteur = haute, ecouteur = moyenne, autres = distribution normale)
4. Contact de base : gestes universels + 2-5 gestes personnels
5. Variantes Contact : selon l'archipel (chaque archipel a son dialecte)

### Etape 3 : Relations et Idiolectes de Paire

1. Pour chaque paire de citoyens du meme archipel : 30% de chance d'idiolecte de paire (1-3 gestes)
2. Pour les paires inter-archipel : 5% de chance (les contacts sont rares entre archipels)
3. Les 7 personnages du roman ont des idiolectes de paire pre-definis (voir `PERSONNAGES.md`)

### Etape 4 : Validation

Apres seeding, verifier tous les invariants de `VALIDATION_Citizen_Model.md` :
- [ ] Chaque citoyen a 1-3 metiers
- [ ] Chaque citoyen a le vocabulaire Contact de base
- [ ] Tremens coherent avec metiers sismiques
- [ ] Chaque metier porte par au moins 2 citoyens dans la population totale
- [ ] Idiolectes de paire symetriques
- [ ] Zones coherentes

---

## Integration avec le Graph Mind

### Mapping au Schema Universel

Les citoyens sont mappes au schema Mind comme suit (cf. `docs/MAPPING.md`) :

| Concept citoyen | node_type Mind | type (subtype) |
|----------------|---------------|----------------|
| Citoyen | `actor` | `citizen` |
| Metier | `thing` | `metier` |
| Geste Contact | `thing` | `gesture` |
| Idiolecte de paire | `narrative` | `pair_idiolect` |
| Archipel | `space` | `archipel` |
| Relation | `link` | `contact_history` |
| Mort | `moment` | `death` |

Le champ `content` d'un node `actor/citizen` contient le JSON complet du citoyen. Le champ `synthesis` contient un resume embeddable : nom, metiers, tremens, zone, statut.

### Fichiers de Donnees

| Fichier | Contenu | Format |
|---------|---------|--------|
| `data/citizens.json` | Population complete (50-80 citoyens) | JSON array |
| `data/metiers.json` | Les 15 metiers avec perception_channel | JSON array |
| `data/archipels.json` | Les 7 archipels avec affinites | JSON array |
| `data/contact_base.json` | Gestes universels du Contact | JSON array |

Ces fichiers suivent le pattern de Venezia (`data/*.json`) mais avec un schema radicalement different : pas de `wealth`, `social_class`, `guild`, `contracts` — remplace par `tremens`, `metiers`, `contact_vocabulary`, `pair_idiolects`.

---

## Dependances

```
PERSONNAGES.md ──────→ citizens.json (les 7 personnages du roman)
METIERS.md ──────────→ metiers.json (les 15 metiers)
CONTACT.md ──────────→ contact_base.json (gestes universels)
MONDE.md ────────────→ archipels.json (les 7 archipels, geologie)
ALGORITHM_Contact.md → schema Contact du citoyen
```

---

*Schema derive de : `PERSONNAGES.md`, `METIERS.md`, `CONTACT.md`, `ALGORITHM_Citizen_Model.md`, format reference Venezia*
