# ALGORITHM -- World Geography

**Module :** `universe/world_geography`
**Univers :** Cities of Light -- 3e univers (Contre-Terre)

---

## Structure de donnees des zones et mecaniques de navigation

Ce document definit la structure de donnees de chaque zone geographique, le systeme de connexions entre zones, et les mecaniques par lesquelles les seismes modifient le reseau.

---

## Structure d'une zone

Chaque zone est definie par la structure suivante :

```
zone:
  id: string                    # identifiant unique (ex: "surface_archipel_sud")
  name: string                  # nom lisible (ex: "Archipel du Sud")
  depth: integer                # profondeur relative (0 = surface, 6 = grotte finale)
  base_magnitude: float         # magnitude sismique de fond (ex: 4.0)
  temperature_range: [min, max] # fourchette en Celsius (ex: [40, 45])
  contact_dialect_modifier:     # modificateur du Contact dans cette zone
    gesture_amplitude: float    # 1.0 = normal, <1 = comprime, >1 = amplifie
    gesture_speed: float        # 1.0 = normal, <1 = lent, >1 = rapide
    resolution: float           # 1.0 = standard, >1 = haute definition
    pain_threshold: float       # 0.0 = pas de douleur, 1.0 = Contact impossible
    available_modes: string[]   # modes de Contact possibles dans cette zone
  fauna: string[]               # organismes presents
  connections: connection[]     # liens vers d'autres zones
  habitability_score: float     # 0.0 (terminal) a 1.0 (vie normale)
  light_source: string          # source de lumiere dominante
  air_quality: float            # 1.0 = normal, 0.0 = irrespirable
  character: string             # "personnalite" de la zone
```

---

## Definitions des zones principales

### Zones de surface (depth: 0)

**Archipel du Sud (desert)**
```
id: "surface_desert_sud"
depth: 0
base_magnitude: 4.0
temperature_range: [40, 45]
contact_dialect_modifier:
  gesture_amplitude: 1.2    # gestes amples (basses longues)
  gesture_speed: 0.8        # rythme lent (ondes profondes)
  resolution: 1.0
  pain_threshold: 0.0
  available_modes: [arm_locks, shoulder, grips, identity, world]
fauna: [vegetation_racines_profondes, sources_souterraines, tubercules]
connections: [surface_piemont_sud]
habitability_score: 0.9
light_source: "soleil"
air_quality: 1.0
character: "indifferent"
```

**Archipels du Nord-Est (Nandi)**
```
id: "surface_archipel_nordest"
depth: 0
base_magnitude: 4.5
temperature_range: [30, 38]
contact_dialect_modifier:
  gesture_amplitude: 0.7    # gestes brefs (hautes seches)
  gesture_speed: 1.4        # rythme rapide (claquements)
  resolution: 1.0
  pain_threshold: 0.0
  available_modes: [arm_locks, shoulder, grips, identity, world]
fauna: [vegetation_adaptee_seches]
connections: [surface_desert_sud]  # route caravaniere
habitability_score: 0.85
light_source: "soleil"
air_quality: 1.0
character: "sec, nerveux"
```

### Piemont (depth: 1)

```
id: "piemont_volcanique"
depth: 1
base_magnitude: 5.0
temperature_range: [30, 35]
contact_dialect_modifier:
  gesture_amplitude: 0.9
  gesture_speed: 1.1
  resolution: 1.0
  pain_threshold: 0.0
  available_modes: [arm_locks, shoulder, grips, identity, world]
fauna: [filaments_bioluminescents_debut, organismes_paroi]
connections: [surface_desert_sud, cavernes_entree]
habitability_score: 0.7
light_source: "batons_chimiques + bioluminescence_faible"
air_quality: 0.95
character: "indifferent"
```

### Cavernes d'entree (depth: 2)

```
id: "cavernes_entree"
depth: 2
base_magnitude: 5.5
temperature_range: [33, 40]
contact_dialect_modifier:
  gesture_amplitude: 0.9
  gesture_speed: 1.0
  resolution: 1.1
  pain_threshold: 0.0
  available_modes: [arm_locks, shoulder, grips, identity, world]
fauna: [filaments_bioluminescents, mousse_sismique, organismes_plats]
connections: [piemont_volcanique, village_sourds, faille_verticale]
habitability_score: 0.5
light_source: "bioluminescence_bleue"
air_quality: 0.9
character: "vivant"
```

### Village des sourds (depth: 2, special)

```
id: "village_sourds"
depth: 2
base_magnitude: 3.0  # amortissement de 40% sur la magnitude 5 ambiante
temperature_range: [35, 40]
contact_dialect_modifier:
  gesture_amplitude: 0.5    # gestes economes
  gesture_speed: 0.9
  resolution: 2.0           # haute definition (3 doigts)
  pain_threshold: 0.0
  available_modes: [grips_haute_resolution, identity, hydraulique, world, front]
fauna: [bioluminescence_domestiquee, micro_ecosysteme_hydraulique]
connections: [cavernes_entree, tunnel_sortie_profond]
habitability_score: 0.65
light_source: "bioluminescence_canalisee_cycle_6h"
air_quality: 0.9  # ventilation naturelle par failles
character: "hospitalier"
```

### Faille verticale (depth: 3)

```
id: "faille_verticale"
depth: 3
base_magnitude: 6.0
temperature_range: [45, 55]
contact_dialect_modifier:
  gesture_amplitude: 0.0    # Contact direct impossible
  gesture_speed: 0.0
  resolution: 0.0
  pain_threshold: 0.3
  available_modes: [corde]  # Contact-corde uniquement
fauna: []
connections: [cavernes_entree, cavernes_profondes]
habitability_score: 0.25
light_source: "batons_chimiques + filaments_epars"
air_quality: 0.8
character: "hostile"
```

### Cavernes profondes (depth: 4)

```
id: "cavernes_profondes"
depth: 4
base_magnitude: 7.0
temperature_range: [55, 65]
contact_dialect_modifier:
  gesture_amplitude: 0.8    # gestes reduits par la fatigue
  gesture_speed: 0.7        # ralenti par l'hypoxie
  resolution: 0.6           # imprecis (tremblements, delire)
  pain_threshold: 0.4
  available_modes: [arm_locks, shoulder, grips, identity]  # Contact-monde degrade
fauna: [extremophiles_rares]
connections: [faille_verticale, zones_volcaniques]
habitability_score: 0.15
light_source: "noir_quasi_total"
air_quality: 0.5
character: "chaotique"
```

### Zones volcaniques (depth: 5)

```
id: "zones_volcaniques"
depth: 5
base_magnitude: 8.0
temperature_range: [70, 90]
contact_dialect_modifier:
  gesture_amplitude: 0.5
  gesture_speed: 1.3        # gestes courts et rapides (la peau brule)
  resolution: 0.3
  pain_threshold: 0.8       # Contact = douleur
  available_modes: [grips_brefs, identity_reduit]
fauna: []  # trop chaud
connections: [cavernes_profondes, grotte_finale]
habitability_score: 0.05
light_source: "lave_orange + fumerolles"
air_quality: 0.3  # CO2, gaz toxiques
character: "cruel"
```

### Grotte finale (depth: 6)

```
id: "grotte_finale"
depth: 6
base_magnitude: 9.0+  # montee vers 11
temperature_range: [100, 300+]
contact_dialect_modifier:
  gesture_amplitude: 0.0
  gesture_speed: 0.0
  resolution: 0.0
  pain_threshold: 1.0
  available_modes: [fantome, monde]  # Contact-fantome + Contact-monde
fauna: []
connections: [zones_volcaniques]
habitability_score: 0.01
light_source: "lave + detonation"
air_quality: 0.1
character: "terminal"
```

---

## Structure d'une connexion

```
connection:
  target_zone_id: string       # zone de destination
  passage_type: string         # "tunnel", "faille", "riviere", "boyau", "puits"
  stability: float             # 0.0 (effondre) a 1.0 (stable)
  width: float                 # largeur en metres (0.6 = boyau)
  seismic_vulnerability: float # probabilite de modification par seisme
  reversible: boolean          # peut-on revenir par ce passage?
```

---

## Navigation entre zones

### Algorithme de deplacement

```
1. INTENTION    Le citoyen choisit une direction (ou suit un guide)
2. CONNEXION    Verifier : la connexion existe-t-elle? Est-elle stable?
3. TRANSITION   Appliquer les effets de transition :
                  a. Recalibrage sismique (tremens si ecart de frequence)
                  b. Changement de temperature (fatigue, douleur)
                  c. Modification du Contact (nouveau dialecte)
                  d. Changement d'air (essoufflement, delire)
4. ARRIVEE      Le citoyen est dans la nouvelle zone
5. SEUIL        Un evenement peut rendre le retour impossible :
                  - Eboulement derriere soi
                  - Passage vertical sans remontee
                  - Chaleur croissante empechant le retour
```

### Comment les seismes modifient les connexions

```
EVENEMENT SISMIQUE (magnitude M dans une zone Z)
    |
    ├── M < 6.0 : Pas d'effet sur les connexions
    |
    ├── 6.0 <= M < 7.0 : Effet mineur
    |   ├── Connexions avec stability < 0.3 → fermeture possible
    |   └── Connexions avec seismic_vulnerability > 0.8 → width modifiee (+/- 20%)
    |
    ├── 7.0 <= M < 8.0 : Effet modere
    |   ├── Connexions avec stability < 0.5 → fermeture probable
    |   ├── Nouvelles connexions possibles (probabilite faible)
    |   └── Passage de type "riviere" → risque de crue
    |
    ├── M >= 8.0 : Effet majeur
    |   ├── Toute connexion avec stability < 0.7 → fermeture
    |   ├── Nouvelles connexions (effondrement revelateur)
    |   └── Passages "boyau" → risque de scellement
    |
    └── M >= 9.0 : Reconfiquration
        ├── Fermetures multiples
        ├── Ouvertures multiples
        └── La carte est a refaire
```

### Regle fondamentale

La somme des connexions sortantes de toute zone doit toujours etre >= 1. Aucune zone ne devient completement isolee -- il reste toujours au moins un passage, meme dangereux. L'isolement total n'existe que pour la grotte finale apres la detonation (et a ce moment, la question ne se pose plus).

---

*Algorithmes derives de : `ALGORITHM_Geographie.md` (mecaniques par couche), `ALGORITHM_Seismique.md` (types de cataclysmes), `ALGORITHM_Contact.md` (dialectes)*
