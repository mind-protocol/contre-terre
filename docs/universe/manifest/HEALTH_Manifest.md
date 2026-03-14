# HEALTH : World Manifest

**Module :** `universe/manifest`
**Question centrale :** Comment verifier que le manifest est sain, coherent, et pret pour le moteur ?

---

## Checks obligatoires avant publication du manifest

### H1 : Validation du schema JSON

Le manifest doit etre un JSON valide avec les sections obligatoires.

**Test :** Parser `world-manifest.json` sans erreur. Verifier la presence de : `name`, `display_name`, `version`, `terrain`, `zones`, `entities`, `physics`, `avatar`, `portals`.

**Frequence :** A chaque modification du manifest.

**Outil :** `python3 -c "import json; json.load(open('world-manifest.json'))"` + verification des cles.

---

### H2 : Toutes les zones ont une physique complete

Chaque zone doit definir son `seismic_profile`, son `environment` et sa configuration `contact`.

**Test :** Pour chaque element de `zones[]` :
- `seismic_profile` existe avec `frequency_band`, `base_magnitude`, `character`
- `environment` existe avec `temperature_c`, `oxygen_pct`, `light_source`, `geology`
- `contact` existe avec `modes_available` (tableau non vide), `pain_threshold`, `range_modifier`

**Frequence :** A chaque ajout ou modification de zone.

**Resultat attendu :** 9 zones (spawn + 8 couches), toutes avec physique complete.

---

### H3 : Tous les citoyens FULL ont une config Contact

Chaque citoyen de tier FULL dans `data/citizens.json` doit avoir ses parametres de Contact et de tremens.

**Test :** Pour chaque citoyen ou `tier == "FULL"` :
- `natal_spectrum` existe (frequency + character)
- `tremens_sensitivity` existe (float 0-1)
- `idiolect` existe (pressure, rhythm, warmth, signature_gesture, preferred_zone)
- `metiers` existe (tableau de 2-3 elements)
- `contact_resolution` == "full"

**Frequence :** A chaque modification de la liste de citoyens.

**Resultat attendu :** 7 citoyens FULL, tous avec config complete.

---

### H4 : Gradient de profondeur coherent

Les parametres physiques doivent suivre les gradients definis dans `ALGORITHM_Geographie.md`.

**Test :**
- Magnitude : croissante avec la profondeur (exception village)
- Temperature : croissante avec la profondeur a partir de la faille
- Oxygene : decroissante avec la profondeur
- Aucune inversion non justifiee

**Frequence :** A chaque modification des parametres de zone.

**Methode :** Trier les zones par `depth`, verifier les monotonies.

---

### H5 : Aucune reference a `voice`

Le manifest ne doit contenir aucun concept de communication vocale.

**Test :** `grep -i "voice" world-manifest.json` ne retourne aucun resultat. Idem pour `voice_indicator`, `voice_range`.

**Frequence :** A chaque modification du manifest.

**Motivation :** Meme une reference residuelle a `voice` dans un commentaire ou un champ oublie indiquerait un copier-coller depuis Venezia non adapte.

---

### H6 : Coherence manifest ↔ worldbuilding

Les valeurs du manifest doivent correspondre aux documents de worldbuilding.

**Tests par module :**

| Source | Verification |
|--------|-------------|
| `ALGORITHM_Seismique.md` (magnitudes par couche) | Les `base_magnitude` du manifest correspondent aux magnitudes documentees |
| `ALGORITHM_Geographie.md` (temperatures) | Les `temperature_c` correspondent au gradient defini |
| `ALGORITHM_Contact.md` (5 modes) | Les `modes_available` couvrent les modes documentes |
| `PATTERNS_Geographie.md` (8 couches) | Les 8 zones du manifest correspondent aux 8 couches |
| `METIERS.md` (15 metiers) | Les 15 `metier_styles` couvrent les 15 metiers |

**Frequence :** Avant chaque release du manifest.

---

### H7 : Portails valides

Le manifest ne doit avoir qu'un portail, a la surface.

**Test :**
- `portals.length == 1`
- `portals[0].zone == "spawn"`
- `portals[0].target_manifest` pointe vers un fichier existant

**Frequence :** Rarement (structure stable).

---

### H8 : Fichiers references existent

Tous les fichiers references dans le manifest doivent exister sur disque.

**Test :** Verifier l'existence de :
- `data/citizens.json`
- `physics/constants.json`
- `prompts/citizen-base.md`

**Frequence :** A chaque modification des paths dans le manifest.

---

## Signaux de degradation

### Le manifest s'eloigne du worldbuilding

**Symptome :** Les magnitudes du manifest ne correspondent plus aux magnitudes de `ALGORITHM_Seismique.md`. Les modes de Contact ne couvrent plus les modes documentes dans `ALGORITHM_Contact.md`.

**Cause probable :** Modifications du worldbuilding sans mise a jour du manifest, ou vice versa.

**Recovery :** Relire les doc chains worldbuilding (seismique, contact, geographie) et re-synchroniser le manifest. Le worldbuilding est la source de verite ; le manifest est la traduction technique.

---

### Le manifest copie Venezia sans adaptation

**Symptome :** Presence de champs `voice`, `social_class_styles`, `sky_model: "preetham"`, `float_bob: true`, `water_level`.

**Cause probable :** Generation initiale par copie du manifest de Venezia, adaptation incomplete.

**Recovery :** Passer les checks H5, V3, V7, V10. Supprimer tout champ specifique a Venezia. Remplacer par les equivalents Contre-Terre.

---

### Les zones manquent de physique

**Symptome :** Zones ajoutees avec uniquement `id`, `name`, `depth` -- sans `seismic_profile`, `environment`, `contact`.

**Cause probable :** Ajout de zone en mode prototype, sans remplir les champs obligatoires.

**Recovery :** Passer le check H2. Remplir chaque zone en consultant `ALGORITHM_Geographie.md` pour les parametres de la couche correspondante.

---

### Les citoyens n'ont pas de tremens

**Symptome :** Citoyens FULL sans `natal_spectrum` ou `tremens_sensitivity`.

**Cause probable :** Ajout de citoyen en mode minimal, oubli des parametres physiologiques.

**Recovery :** Passer le check H3. Definir le spectre natal en consultant `PERSONNAGES.md` pour l'origine geographique du personnage.

---

## Checklist rapide

Avant chaque release du manifest, verifier :

- [ ] JSON valide, toutes sections presentes (H1)
- [ ] 9 zones avec physique complete (H2)
- [ ] 7 citoyens FULL avec Contact + tremens (H3)
- [ ] Gradients coherents : magnitude, temperature, oxygene (H4)
- [ ] Aucun `voice` (H5)
- [ ] Valeurs alignees avec worldbuilding (H6)
- [ ] 1 portail, surface (H7)
- [ ] Fichiers references existent (H8)

---

*Sources : HEALTH des modules worldbuilding, VALIDATION_Manifest.md, world-manifest.json (Venezia)*
