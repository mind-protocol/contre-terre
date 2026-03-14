# VALIDATION : World Manifest

**Module :** `universe/manifest`
**Question centrale :** Quels invariants le manifest doit respecter pour que Contre-Terre soit coherent ?

---

## Invariants absolus (violation = erreur)

### V1 : Chaque zone a un profil sismique

Aucune zone ne peut exister sans `seismic_profile`. Le tremblement est constitutif du monde -- une zone sans sismicite est un trou dans la physique. Meme le village des sourds (amortissement 40%) a une sismicite residuelle.

**Test :** Pour chaque objet dans `zones[]`, verifier que `seismic_profile` existe et contient `frequency_band`, `base_magnitude`, et `character`.

**Contre-exemple interdit :** `{ "id": "cavernes_profondes", "depth": -4000 }` sans `seismic_profile` -- le moteur ne saurait pas comment faire trembler le sol.

---

### V2 : Chaque citoyen FULL a une sensibilite tremens

Tout citoyen de tier FULL doit avoir un `natal_spectrum` et un `tremens_sensitivity` definis. Le tremens n'est pas optionnel -- c'est la reaction du corps au monde. Un citoyen sans tremens serait un corps deconnecte de la terre.

**Test :** Pour chaque entite dans `data/citizens.json` de tier FULL, verifier que `natal_spectrum` (avec `frequency` et `character`) et `tremens_sensitivity` (float 0-1) sont presents.

**Seuils :**
- `tremens_sensitivity` entre 0.1 (tres adapte) et 1.0 (Nandi -- maximale)
- `natal_spectrum.frequency` dans l'ensemble {"low-deep", "mid-dry", "high-sharp", "infra-low"}

---

### V3 : Le Contact range remplace le voice range

Le manifest ne doit contenir AUCUNE reference a `voice`, `voice_indicator`, ou `voice_range`. Ces concepts n'existent pas a Contre-Terre. Toute communication passe par le Contact.

**Test :** Le JSON du manifest ne contient aucune cle `voice`. Les tiers d'entites utilisent `contact_range`, `contact_resolution`, et `contact_modes` exclusivement.

**Motivation :** Un citoyen qui "parle" casserait l'immersion. Le Contact est le seul canal. Meme les cris de douleur ne sont pas des mots -- ce sont des vibrations du corps que le Contact lit.

---

### V4 : Les transitions entre zones sont irreversibles (sauf surface)

Chaque `threshold_exit` doit avoir `reversible: false` sauf pour la premiere transition (surface <-> piemont). La descente est un aller simple. Le manifest ne permet pas de remonter.

**Test :** Pour chaque zone de profondeur < 0 (sous la surface), verifier que `threshold_exit.reversible == false`. Seul `surface_desert` peut avoir une sortie reversible.

**Motivation :** L'irreversibilite est le principe structurant du roman. Permettre le retour detruirait la tension narrative. Le moteur doit encoder cette contrainte dans la geometrie des zones.

---

### V5 : La magnitude augmente avec la profondeur

La `base_magnitude` de chaque zone doit etre superieure ou egale a celle de la zone precedente, a l'exception du village des sourds (amortissement). L'escalade sismique est inexorable.

**Test :** Trier les zones par `depth` (decroissant). Verifier que `seismic_profile.base_magnitude` est monotoniquement croissante, avec une exception autorisee pour `village_sourds` (magnitude amortie < magnitude du piemont).

**Seuils :**
```
surface_desert: 4.5
piemont_volcanic: 5.5
village_sourds: 4.0 (dampened -- exception)
faille_verticale: 6.0
cavernes_profondes: 7.0
zones_volcaniques: 8.0
boyau: 8.5
grotte_finale: 9.5 (escalation_target: 11)
```

---

### V6 : Chaque zone definit les modes de Contact disponibles

Le manifest doit lister explicitement quels modes de Contact fonctionnent dans chaque zone. Un citoyen ne peut pas utiliser un mode non declare pour sa zone courante.

**Test :** Pour chaque zone, verifier que `contact.modes_available` est un tableau non vide. Les valeurs autorisees sont : `"direct"`, `"corde"`, `"hydraulic"`, `"monde"`, `"haute_resolution"`, `"direct_douloureux"`, `"force"`, `"fantome"`, `"presence"`.

**Coherences croisees :**
- `"corde"` ne peut apparaitre que dans les zones ou l'encordement est physiquement possible (faille, cavernes)
- `"hydraulic"` n'apparait que dans le village (rigole d'eau)
- `"haute_resolution"` n'apparait que dans le village (3 doigts, generation de sourds)
- `"force"` n'apparait que dans le boyau (60cm, impossible de ne pas se toucher)
- `"fantome"` n'apparait que dans la grotte finale (Nandi seule, hallucinations)

---

## Invariants structurels (violation = incoherence)

### V7 : Les pieds sont au sol

`avatar.float_bob` doit etre `false`. `avatar.feet_on_ground` doit etre `true`. Le Contact-monde passe par les pieds et les mains au sol. Un avatar qui flotte est coupe du monde sismique.

**Test :** Verifier `avatar.float_bob == false` et `avatar.feet_on_ground == true`.

---

### V8 : La temperature augmente avec la profondeur

L'`environment.temperature_c` de chaque zone doit suivre un gradient croissant avec la profondeur, a l'exception du piemont (entree cavernes = baisse depuis le desert).

**Test :** Les temperatures des zones profondes (faille et au-dela) doivent etre monotoniquement croissantes.

---

### V9 : L'oxygene decroit avec la profondeur

L'`environment.oxygen_pct` doit decroitre avec la profondeur. La surface est a 100%, la grotte finale est critique.

**Test :** Verifier que `oxygen_pct` est strictement decroissante a partir de la faille (profondeur -2000).

---

### V10 : Pas de `social_class_styles`

Le manifest ne doit contenir aucune reference a `social_class_styles`, `Patrician`, `Cittadino`, `Popolano`, `Ecclesiastic`, ou `Forestiero`. L'identite passe par les metiers.

**Test :** Le JSON du manifest ne contient aucune cle `social_class_styles`. Le champ `avatar.metier_styles` est present a la place.

---

### V11 : Un seul portail, a la surface

Le tableau `portals` ne doit contenir qu'un seul element, de zone `"spawn"`. Aucun portail sous terre.

**Test :** `portals.length == 1` et `portals[0].zone == "spawn"`.

---

## Invariants inter-modules (liens avec d'autres doc chains)

### V12 : Les zones correspondent aux 8 chapitres

Les 8 zones de profondeur (surface exclu) doivent correspondre aux 8 couches definies dans `PATTERNS_Geographie.md` (P2 : 8 couches = 8 chapitres).

**Verification :** Chaque chapitre (I-VIII) a une et une seule zone correspondante dans le manifest.

---

### V13 : Les 5 modes de Contact sont representes

Les modes de Contact declares dans l'ensemble de toutes les zones doivent couvrir les 5 modes fondamentaux definis dans `ALGORITHM_Contact.md` plus les extensions (corde, hydraulique, force, fantome, monde).

**Verification :** L'union de tous les `contact.modes_available` couvre au minimum : direct, corde, monde, haute_resolution, force, fantome.

---

### V14 : Les 15 metiers ont un style avatar

Chaque metier declare dans `METIERS.md` doit avoir un style correspondant dans `avatar.metier_styles`.

**Verification :** Les 15 cles de `metier_styles` correspondent aux 15 metiers du systeme de competences.

---

## Grille de verification rapide

| # | Invariant | Auto-verifiable | Critique |
|---|-----------|-----------------|----------|
| V1 | Chaque zone a un seismic_profile | Oui (JSON schema) | Oui |
| V2 | Chaque FULL a tremens | Oui (citizens.json) | Oui |
| V3 | Pas de voice | Oui (grep) | Oui |
| V4 | Transitions irreversibles | Oui (JSON) | Oui |
| V5 | Magnitude croissante | Oui (sort + compare) | Oui |
| V6 | Modes Contact par zone | Oui (JSON) | Oui |
| V7 | Pieds au sol | Oui (JSON) | Non |
| V8 | Temperature croissante | Oui (sort + compare) | Non |
| V9 | Oxygene decroissante | Oui (sort + compare) | Non |
| V10 | Pas de social_class | Oui (grep) | Non |
| V11 | Un seul portail | Oui (count) | Non |
| V12 | 8 zones = 8 chapitres | Manuel (cross-ref) | Oui |
| V13 | 5+ modes Contact | Oui (union) | Oui |
| V14 | 15 metiers ont un style | Oui (cross-ref) | Non |

---

*Invariants derives de : VALIDATION_Seismique.md, VALIDATION_Contact.md, VALIDATION_Geographie.md, PATTERNS_Manifest.md, world-manifest.json (Venezia)*
