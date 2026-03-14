# ALGORITHM : World Manifest

**Module :** `universe/manifest`
**Question centrale :** Quelle est la structure exacte du manifest ? Quels champs, quelles valeurs, quels calculs ?

---

## Structure globale

Le manifest suit le format `world-manifest.json` de Cities of Light, mais chaque section est adaptee a la physique de Contre-Terre.

```json
{
  "name": "contre-terre",
  "display_name": "Contre-Terre -- Cities of Light",
  "version": "0.1.0",
  "description": "Un monde de seismes permanents ou les humains communiquent par le Contact -- un langage tactile complet. Descente verticale dans un volcan. Mission-suicide. Le sol ne s'arrete jamais de trembler.",

  "terrain": { ... },
  "zones": [ ... ],
  "entities": { ... },
  "physics": { ... },
  "ai_config": { ... },
  "avatar": { ... },
  "portals": [ ... ]
}
```

---

## Section `terrain` -- Le sol qui tremble

```json
{
  "terrain": {
    "generator": "geological-vertical",
    "orientation": "descent",
    "max_depth": -10000,
    "surface_type": "desert",
    "ocean": false,
    "sky_model": "none",
    "sun": { "elevation": 45, "azimuth": 180, "zones": ["surface_desert"] },
    "global_seismics": {
      "base_magnitude": 4,
      "permanent": true,
      "pulse_frequency_hz": 0.33,
      "character": "animal endormi qui respire"
    },
    "bioluminescence": {
      "present_zones": ["piemont_volcanic", "village_sourds"],
      "color": "blue-white",
      "pulse_synced_to_magnitude": true,
      "touch_reactive": true,
      "degradation_with_depth": true
    }
  }
}
```

**Notes :**
- `generator: "geological-vertical"` indique au moteur que le monde est organise en couches, pas en iles ou districts
- `sky_model: "none"` -- pas de ciel sous terre. Le `sun` n'existe qu'a la surface
- `global_seismics.permanent: true` -- le sol vibre toujours. C'est le parametre le plus important du manifest
- `bioluminescence.pulse_synced_to_magnitude` -- les filaments battent au rythme du monde

---

## Section `zones` -- Les 8 couches + surface de spawn

```json
{
  "zones": [
    {
      "id": "spawn",
      "name": "Campement de surface",
      "position": { "x": 0, "y": 0, "z": 0 },
      "mode": "spawn",
      "depth": 0,
      "note": "Point de spawn. Desert plat, volcan visible a l'horizon."
    },
    {
      "id": "surface_desert",
      "name": "Desert de Surface",
      "depth": 0,
      "seismic_profile": {
        "frequency_band": "low-deep",
        "base_magnitude": 4.5,
        "character": "ondes basses, longues, profondes"
      },
      "environment": {
        "temperature_c": 42,
        "oxygen_pct": 100,
        "light_source": "sun",
        "geology": "sable-poussiere"
      },
      "contact": {
        "modes_available": ["direct", "monde"],
        "pain_threshold": false,
        "range_modifier": 1.0
      },
      "threshold_exit": {
        "target": "piemont_volcanic",
        "reversible": true,
        "trigger": "approach"
      }
    },
    {
      "id": "piemont_volcanic",
      "name": "Piemont Volcanique",
      "depth": -200,
      "seismic_profile": {
        "frequency_band": "mid-dry",
        "base_magnitude": 5.5,
        "character": "claquements secs remontant par les chevilles"
      },
      "environment": {
        "temperature_c": 32,
        "oxygen_pct": 98,
        "light_source": "chemical-sticks+bioluminescence",
        "geology": "gravier-basalte"
      },
      "contact": {
        "modes_available": ["direct", "monde"],
        "pain_threshold": false,
        "range_modifier": 1.0
      },
      "threshold_exit": {
        "target": "village_sourds",
        "reversible": false,
        "trigger": "descent-into-cavern"
      }
    },
    {
      "id": "village_sourds",
      "name": "Village des Sourds",
      "depth": -800,
      "seismic_profile": {
        "frequency_band": "infra-low-damped",
        "base_magnitude": 4.0,
        "dampening_pct": 40,
        "character": "vibrations si profondes qu'elles entrent dans les os"
      },
      "environment": {
        "temperature_c": 37,
        "oxygen_pct": 95,
        "light_source": "bioluminescence-domesticated",
        "geology": "roche-amenagee"
      },
      "contact": {
        "modes_available": ["direct", "haute_resolution", "hydraulic", "monde"],
        "pain_threshold": false,
        "range_modifier": 1.5
      },
      "threshold_exit": {
        "target": "faille_verticale",
        "reversible": false,
        "trigger": "tunnel-narrows"
      }
    },
    {
      "id": "faille_verticale",
      "name": "La Faille",
      "depth": -2000,
      "seismic_profile": {
        "frequency_band": "lateral-bounce",
        "base_magnitude": 6.0,
        "character": "ondes rebondissant entre les parois"
      },
      "environment": {
        "temperature_c": 50,
        "oxygen_pct": 85,
        "light_source": "chemical-sticks-sparse",
        "geology": "basalte-humide-soufre"
      },
      "contact": {
        "modes_available": ["corde"],
        "pain_threshold": false,
        "range_modifier": 0.3
      },
      "threshold_exit": {
        "target": "cavernes_profondes",
        "reversible": false,
        "trigger": "rockfall-seals-above"
      }
    },
    {
      "id": "cavernes_profondes",
      "name": "Cavernes Profondes",
      "depth": -4000,
      "seismic_profile": {
        "frequency_band": "multi-chaotic",
        "base_magnitude": 7.0,
        "character": "signaux complexes superposes"
      },
      "environment": {
        "temperature_c": 60,
        "oxygen_pct": 70,
        "light_source": "none",
        "geology": "roche-fracturee-passages-noyes"
      },
      "contact": {
        "modes_available": ["direct", "corde"],
        "pain_threshold": true,
        "range_modifier": 0.6
      },
      "threshold_exit": {
        "target": "zones_volcaniques",
        "reversible": false,
        "trigger": "passage-collapse"
      }
    },
    {
      "id": "zones_volcaniques",
      "name": "Zones Volcaniques",
      "depth": -6000,
      "seismic_profile": {
        "frequency_band": "high-nervous-irregular",
        "base_magnitude": 8.0,
        "character": "ondes deformees par la chaleur et la convection"
      },
      "environment": {
        "temperature_c": 80,
        "oxygen_pct": 50,
        "light_source": "lava-orange",
        "geology": "basalte-fissure-geysers-cendres"
      },
      "contact": {
        "modes_available": ["direct_douloureux"],
        "pain_threshold": true,
        "range_modifier": 0.4
      },
      "threshold_exit": {
        "target": "boyau",
        "reversible": false,
        "trigger": "lava-narrows"
      }
    },
    {
      "id": "boyau",
      "name": "Le Boyau",
      "depth": -8000,
      "seismic_profile": {
        "frequency_band": "direct-transmission",
        "base_magnitude": 8.5,
        "character": "le metal vibre, transmission directe"
      },
      "environment": {
        "temperature_c": 100,
        "oxygen_pct": 30,
        "light_source": "none",
        "geology": "tube-roche-lisse-60cm"
      },
      "contact": {
        "modes_available": ["force"],
        "pain_threshold": true,
        "range_modifier": 0.1
      },
      "threshold_exit": {
        "target": "grotte_finale",
        "reversible": false,
        "trigger": "seismic-precursor-seals-tube"
      }
    },
    {
      "id": "grotte_finale",
      "name": "La Grotte Finale",
      "depth": -10000,
      "seismic_profile": {
        "frequency_band": "all-spectrum",
        "base_magnitude": 9.5,
        "escalation_target": 11,
        "character": "toutes frequences simultanement"
      },
      "environment": {
        "temperature_c": 110,
        "oxygen_pct": 15,
        "light_source": "lava+detonation-white",
        "geology": "magma-actif"
      },
      "contact": {
        "modes_available": ["fantome", "monde"],
        "pain_threshold": true,
        "range_modifier": 0.0
      },
      "threshold_exit": null
    }
  ]
}
```

---

## Section `entities` -- Citoyens du tremblement

```json
{
  "entities": {
    "source": "local",
    "path": "data/citizens.json",
    "tier_config": {
      "FULL": {
        "max": 7,
        "contact_range": 0.5,
        "contact_resolution": "full",
        "contact_modes": ["direct", "corde", "monde", "haute_resolution"],
        "llm": true,
        "tremens_simulated": true
      },
      "ACTIVE": {
        "max": 20,
        "contact_range": 2.0,
        "contact_resolution": "functional",
        "contact_modes": ["direct"],
        "llm": false,
        "tremens_simulated": false
      },
      "AMBIENT": {
        "max": 100,
        "contact_range": 5.0,
        "contact_resolution": "basal",
        "contact_modes": ["presence"],
        "llm": false,
        "tremens_simulated": false
      }
    }
  }
}
```

**Notes :**
- `FULL` : les 7 personnages principaux. Contact complet, tremens simule, LLM actif. Ce sont les citoyens narratifs.
- `ACTIVE` : les villageois, les membres du Consortium. Contact fonctionnel, pas de tremens. Citoyens de contexte.
- `AMBIENT` : population de fond des archipels. Presence sentie, pas de dialogue. Tissu du monde.

---

## Section `physics` -- Le moteur du monde

```json
{
  "physics": {
    "engine": "ngram",
    "graph_name": "contre_terre",
    "tick_interval_ms": 120000,
    "constants_path": "physics/constants.json",
    "seismic_engine": {
      "permanent_vibration": true,
      "cataclysm_generator": true,
      "tremens_calculator": true,
      "bioluminescence_sync": true
    },
    "tick_modifiers_by_depth": {
      "surface": 1.0,
      "piemont": 1.0,
      "village": 0.8,
      "faille": 1.5,
      "cavernes": 2.0,
      "volcanique": 3.0,
      "boyau": 5.0,
      "grotte_finale": 10.0
    }
  }
}
```

---

## Section `avatar` -- Le corps comme identite

```json
{
  "avatar": {
    "style": "organic-grounded",
    "float_bob": false,
    "glow_ring": false,
    "feet_on_ground": true,
    "tremens_visible": true,
    "metier_styles": {
      "chef_expedition": { "palette": "sand-rust", "signature": "regard-qui-choisit", "ornament": "none" },
      "cartographe": { "palette": "sand-ochre", "signature": "rouleau-tissu", "ornament": "roll" },
      "seismo_auditeur": { "palette": "stone-dark", "signature": "sismographe-torse", "ornament": "scroll" },
      "meteorologue": { "palette": "grey-cloud", "signature": "yeux-fermes", "ornament": "none" },
      "biologiste": { "palette": "moss-earth", "signature": "mains-terreuses", "ornament": "root" },
      "aeromaitre": { "palette": "grey-white", "signature": "tissu-vent", "ornament": "windcloth" },
      "geologue": { "palette": "basalt-grey", "signature": "mains-roche", "ornament": "none" },
      "grimpeuse": { "palette": "rope-brown", "signature": "mains-comptant", "ornament": "carabiner" },
      "explosiviste": { "palette": "copper-dark", "signature": "doigts-precis", "ornament": "fuse" },
      "predictrice": { "palette": "skin-bare", "signature": "pieds-nus", "ornament": "none" },
      "oceanologue": { "palette": "deep-blue", "signature": "gourdes", "ornament": "water" },
      "spelologue": { "palette": "black-shadow", "signature": "posture-basse", "ornament": "none" },
      "cuisinier": { "palette": "fire-orange", "signature": "mains-coupant", "ornament": "none" },
      "survivaliste": { "palette": "earth-green", "signature": "regard-peripherique", "ornament": "none" },
      "mineur": { "palette": "iron-dark", "signature": "epaules-larges", "ornament": "pioche" }
    }
  }
}
```

---

## Section `portals` -- Un seul portail, a la surface

```json
{
  "portals": [
    {
      "id": "hub_return",
      "zone": "spawn",
      "position": { "x": 10, "y": 0, "z": 10 },
      "target_manifest": "../lumina-prime/world-manifest.json",
      "label": "Retour a Lumina Prime",
      "note": "Le seul portail. Disponible a la surface uniquement. Sous terre, il n'y a plus de retour."
    }
  ]
}
```

---

*Structure derivee de : world-manifest.json (Venezia, format canonique), ALGORITHM_Geographie.md (couches), ALGORITHM_Seismique.md (magnitudes, tremens), ALGORITHM_Contact.md (modes, portees), MAPPING.md (entites)*
