# IMPLEMENTATION : World Manifest

**Module :** `universe/manifest`
**Question centrale :** Ou vit le manifest, comment il se connecte au moteur Cities of Light, quel est le flux de donnees ?

---

## Fichier principal

```
contre-terre/
  world-manifest.json          <-- Le manifest (ce module le documente)
```

Le manifest est un fichier JSON unique a la racine du projet, suivant la convention Cities of Light. Le moteur le charge au demarrage du monde. C'est le contrat entre le projet Contre-Terre (contenu, worldbuilding, regles) et le moteur Cities of Light (rendu, simulation, interactions).

---

## Fichiers de donnees references par le manifest

```
contre-terre/
  world-manifest.json
  data/
    citizens.json              <-- Definitions des citoyens (7 FULL + ACTIVE + AMBIENT)
    zones-detail.json          <-- Donnees complementaires par zone (optionnel)
  physics/
    constants.json             <-- Constantes physiques (sismiques, thermiques, Contact)
  prompts/
    citizen-base.md            <-- Prompt de base pour les citoyens AI (Contact-first)
```

### `data/citizens.json`

Contient les definitions de chaque citoyen AI avec les champs specifiques a Contre-Terre :

```json
[
  {
    "id": "senzo",
    "name": "Senzo",
    "tier": "FULL",
    "metiers": ["chef_expedition", "cartographe"],
    "natal_spectrum": { "frequency": "mid-dry", "character": "claquements reguliers" },
    "tremens_sensitivity": 0.35,
    "idiolect": {
      "pressure": "firm",
      "rhythm": "steady",
      "warmth": "high",
      "signature_gesture": "nuque_de_nandi",
      "preferred_zone": "epaule"
    },
    "contact_resolution": "full",
    "death_chapter": 4
  }
]
```

Chaque citoyen FULL doit inclure : `metiers`, `natal_spectrum`, `tremens_sensitivity`, `idiolect`, `contact_resolution`, `death_chapter`.

Les citoyens ACTIVE et AMBIENT ont un schema reduit : `name`, `tier`, `natal_spectrum` (optionnel), `role` (villageois, consortium, etc.).

### `physics/constants.json`

Contient les constantes de simulation :

```json
{
  "seismic": {
    "magnitude_floor": 4.0,
    "magnitude_ceiling": 11.0,
    "tremens_recalc_interval_ms": 60000,
    "cataclysm_base_probability_per_tick": 0.05,
    "depth_magnitude_coefficient": 0.0005
  },
  "contact": {
    "direct_max_range_m": 0.5,
    "corde_max_range_m": 50.0,
    "monde_max_range_m": 10.0,
    "pain_temperature_threshold_c": 55,
    "forced_contact_diameter_m": 0.6
  },
  "environment": {
    "temperature_gradient_per_1000m": 12.0,
    "oxygen_gradient_per_1000m": -10.0,
    "bioluminescence_depth_cutoff_m": -3000
  }
}
```

### `prompts/citizen-base.md`

Le prompt de base pour les citoyens AI de Contre-Terre. Remplace le prompt generique de Venezia. Contenu attendu :

- Tu communiques par le Contact (pas par la voix)
- Tu sens le sol trembler en permanence
- Ton corps reagit aux changements de frequence (tremens)
- Tu as des metiers -- des competences que tu exerces
- Chaque personne a une signature tactile unique -- ton idiolecte
- La descente est irreversible

---

## Connexion au moteur Cities of Light

### Flux de chargement

```
1. Moteur lit world-manifest.json
2. Moteur valide le schema (sections obligatoires : terrain, zones, entities, physics)
3. Moteur charge les fichiers references (data/citizens.json, physics/constants.json)
4. Moteur instancie le terrain selon terrain.generator ("geological-vertical")
5. Moteur cree les zones avec leurs profils sismiques
6. Moteur spawn les entites a la position de spawn
7. Moteur demarre le physics tick (avec tick_modifiers_by_depth)
8. Moteur connecte le graph mind (physics.graph_name = "contre_terre")
```

### Points d'integration specifiques a Contre-Terre

| Composant moteur | Champ manifest | Adaptation necessaire |
|------------------|----------------|----------------------|
| Voice system | `entities.tier_config.*.contact_*` | Remplacer voice par Contact |
| Zone loader | `zones[].depth` + `threshold_exit` | Charger verticalement, pas horizontalement |
| Mood system | `entities.tier_config.*.tremens_simulated` | Remplacer mood par tremens |
| Light renderer | `terrain.bioluminescence` + `zones[].environment.light_source` | Lumiere reactive, pas celeste |
| Avatar renderer | `avatar.metier_styles` | Identite par metier, pieds au sol |
| Portal system | `portals[]` | Un seul portail, surface uniquement |
| Tick scheduler | `physics.tick_modifiers_by_depth` | Tick accelere en profondeur |

### Extensions moteur requises

Le moteur Cities of Light standard (tel que Venezia l'utilise) ne gere pas nativement :

1. **Sismicite permanente** -- il faut un module `seismic_engine` qui genere des vibrations de fond continues et des cataclysmes aleatoires
2. **Tremens** -- il faut un module `tremens_calculator` qui calcule l'etat physiologique de chaque citoyen en fonction de la zone courante
3. **Contact-range** -- le systeme de voix doit etre remplace (ou wrappe) par un systeme de portee tactile
4. **Verticalite** -- le zone loader doit gerer la profondeur comme dimension principale (pas x/z)
5. **Irreversibilite** -- le threshold system doit empecher la remontee apres franchissement

Ces extensions sont declarees dans le manifest via `physics.seismic_engine` et les champs `contact.*` par zone.

---

## Relations avec les autres modules

| Module | Relation | Fichier |
|--------|----------|---------|
| `worldbuilding/seismique` | Fournit les constantes sismiques | `physics/constants.json` |
| `worldbuilding/contact` | Definit les modes et portees de Contact | `entities.tier_config`, `zones[].contact` |
| `worldbuilding/geographie` | Definit les couches et leurs proprietes | `zones[]` |
| `narration/personnages` | Definit les 7 citoyens FULL | `data/citizens.json` |
| `narration/metiers` | Definit les 15 metiers et styles avatar | `avatar.metier_styles` |
| `docs/MAPPING.md` | Mapping vers le schema mind | `physics.graph_name` |

---

## Processus de mise a jour

Quand un aspect du worldbuilding change (nouvelle constante sismique, nouveau mode de Contact, modification d'une zone), le processus est :

1. Modifier le fichier source du worldbuilding (ex: `ALGORITHM_Seismique.md`)
2. Mettre a jour le manifest (`world-manifest.json`) pour refleter le changement
3. Mettre a jour les fichiers de donnees si necessaire (`physics/constants.json`, `data/citizens.json`)
4. Valider contre les invariants (`VALIDATION_Manifest.md`)
5. Mettre a jour le SYNC

Le manifest est le point de convergence : il traduit le worldbuilding narratif en specification technique pour le moteur.

---

*Sources : world-manifest.json (Venezia, reference), IMPLEMENTATION des modules existants, MAPPING.md*
