# IMPLEMENTATION -- World Geography

**Module :** `universe/world_geography`
**Univers :** Cities of Light -- 3e univers (Contre-Terre)

---

## Ou vit le contenu geographique -- sources, structure, format

Ce document cartographie les fichiers sources du systeme geographique, le format de donnees des zones, et les liens vers les autres modules du 3e univers.

---

## Sources de verite

### Sources primaires (worldbuilding roman)

| Fichier | Contenu geographique | Role |
|---------|---------------------|------|
| `MONDE.md` | Systeme sismique, tremens, architecture, profondeur/temperature, faune, Archipels | Fondation des parametres physiques |
| `STRUCTURE.md` | 8 chapitres = 8 couches geologiques | Correspondance zones/recit |
| `SQUELETTE.md` | Mecanismes par couche, scenes detaillees | Reference operationnelle |
| `CONTACT.md` | 5 modes du Contact, dialectes regionaux, degradation par zone | Dialect modifiers |
| `PERSONNAGES.md` | Origines des personnages (archipels) = calibration du tremens | Lien Archipels/citoyens |

### Documentation existante (doc chain worldbuilding)

| Fichier | Role pour world_geography |
|---------|--------------------------|
| `docs/worldbuilding/geographie/ALGORITHM_Geographie.md` | Parametres physiques par couche (temperature, air, lumiere, spectre, roche) |
| `docs/worldbuilding/geographie/PATTERNS_Geographie.md` | Decisions de design (verticalite, 8 couches, elements-tueurs, Archipels) |
| `docs/worldbuilding/geographie/VALIDATION_Geographie.md` | 14 invariants narratifs (descente irreversible, temperature croissante, etc.) |
| `docs/worldbuilding/seismique/ALGORITHM_Seismique.md` | Echelle de magnitudes, mecaniques du tremens, frequences par couche |
| `docs/worldbuilding/contact/ALGORITHM_Contact.md` | 5 modes, zones du corps, Contact-corde, dialectes regionaux |

---

## Format de donnees des zones

### Schema YAML de reference

Les zones sont definies en YAML. Le schema canonique est documente dans `ALGORITHM_World_Geography.md`. Voici le format compact :

```yaml
zones:
  - id: "surface_desert_sud"
    name: "Desert du Sud"
    depth: 0
    base_magnitude: 4.0
    temperature_range: [40, 45]
    contact_dialect_modifier:
      gesture_amplitude: 1.2
      gesture_speed: 0.8
      resolution: 1.0
      pain_threshold: 0.0
      available_modes: ["arm_locks", "shoulder", "grips", "identity", "world"]
    fauna: ["vegetation_racines_profondes", "sources_souterraines"]
    connections:
      - target: "piemont_volcanique"
        type: "terrain"
        stability: 0.9
        width: null  # open terrain
        seismic_vulnerability: 0.1
        reversible: true
    habitability_score: 0.9
    light_source: "soleil"
    air_quality: 1.0
    character: "indifferent"
```

### Mapping vers le schema Mind

Les zones sont mappees au schema Mind universel comme suit :

| Concept geographique | Mind node_type | Champs |
|---------------------|---------------|--------|
| Zone | `space` | `content` = description sensorielle, `synthesis` = resume zone |
| Connexion entre zones | `link` | `type` = "passage", proprietes dans content |
| Citoyen dans une zone | `link` | `type` = "habite" ou "traverse" |
| Evenement sismique | `moment` | `content` = description, `synthesis` = magnitude + zone |
| Faune/flore | `thing` | `type` = "organisme", `content` = proprietes |

Les zones sont des noeuds `space`. Les connexions sont des `link` entre `space`. Les citoyens qui habitent ou traversent une zone sont relies par des `link` de type "habite" ou "traverse".

---

## Graphe des connexions (etat initial)

```
surface_archipel_nordest ──── surface_desert_sud
                                      |
                               piemont_volcanique
                                      |
                               cavernes_entree ──── village_sourds
                                      |
                               faille_verticale
                                      |
                              cavernes_profondes
                                      |
                              zones_volcaniques
                                      |
                                grotte_finale
```

Le graphe est orientable mais pas oriente : les connexions sont bidirectionnelles, sauf quand elles sont marquees `reversible: false` (dans ce cas, elles ne vont que vers la profondeur).

### Connexions irreversibles

| De | Vers | Raison |
|----|------|--------|
| faille_verticale | cavernes_profondes | Passage vertical, pas de remontee |
| cavernes_profondes | zones_volcaniques | Chaleur empechant le retour |
| zones_volcaniques | grotte_finale | Boyau a sens unique |

---

## Relations avec les autres modules du 3e univers

| Module | Nature de la dependance |
|--------|------------------------|
| `universe/seismic_physics` | La `base_magnitude` de chaque zone est derivee du modele sismique. Les evenements sismiques qui modifient les connexions sont calcules par ce module. |
| `universe/contact_engine` | Le `contact_dialect_modifier` de chaque zone est lu par le moteur de Contact pour adapter les gestes. Les `available_modes` determinent quels types de Contact sont possibles. |
| `universe/citizen_model` | Le `habitability_score` determine quelles zones un citoyen peut habiter. Le `base_magnitude` determine l'intensite du tremens. L'`air_quality` determine les effets d'hypoxie. |
| `universe/narrative_engine` | Les zones sont les "lieux" du recit. Les transitions entre zones sont des moments narratifs. Les modifications de connexions par seismes sont des evenements de plot. |
| `universe/manifest` | Le world manifest reference les zone_id pour ancrer les scenes. |
| `universe/graph_schema` | Les zones sont des noeuds `space` dans le graphe Mind. |

---

## Fichiers a creer (non encore crees)

| Fichier | Contenu | Priorite |
|---------|---------|----------|
| `zones.yaml` | Definitions YAML de toutes les zones | Haute -- quand le systeme sera implemente |
| `connections.yaml` | Definitions YAML de toutes les connexions | Haute |
| `seismic_events.yaml` | Regles de modification des connexions par seismes | Moyenne |
| `navigation.py` | Logique de deplacement et de verification de connexite | Moyenne |

---

*Ce document sera mis a jour au fur et a mesure que le systeme est implemente.*
