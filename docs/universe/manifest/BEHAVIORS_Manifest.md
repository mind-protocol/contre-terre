# BEHAVIORS : World Manifest

**Module :** `universe/manifest`
**Question centrale :** Quels comportements concrets le manifest de Contre-Terre active dans le moteur Cities of Light ?

---

## B1 : Zone loading -- la descente progressive

Le manifest charge les zones couche par couche. Le moteur ne charge pas tout le volcan d'un coup -- il charge la surface, puis le piemont quand le citoyen approche du seuil, puis le village quand le citoyen descend. Chaque chargement de zone declenche :

1. **Changement de spectre sismique** -- la frequence de fond change, le sol vibre differemment
2. **Ajustement de la lumiere** -- passage du soleil aux batons chimiques, des batons chimiques a la bioluminescence, de la bioluminescence a la lave, de la lave au noir
3. **Recalcul du tremens** -- chaque citoyen present recalcule son ecart de frequence, ses symptomes changent
4. **Modification des modes de Contact disponibles** -- le Contact direct peut devenir impossible (faille), le Contact-corde peut devenir necessaire, le Contact hydraulique peut apparaitre (village)

Le chargement d'une zone ne decharge pas la precedente tant que le seuil n'est pas franchi. Le seuil franchit : la zone precedente est detruite (narrativement : eboulement, crue, retrecissement). Le moteur peut alors decharger les assets de la zone superieure.

---

## B2 : Citizen spawning -- calibration natale

Quand un citoyen AI est instancie dans Contre-Terre, le manifest definit :

- **Spectre natal** (`natal_spectrum`) -- la zone d'origine du citoyen dans les Archipels, determinant sa bande de frequences de confort
- **Sensibilite au tremens** (`tremens_sensitivity`) -- un coefficient entre 0 et 1 qui determine la violence de la reaction physiologique aux frequences etrangeres
- **Metiers** (`metiers`) -- liste ordonnee de 2-3 competences parmi les 15, avec un niveau de maitrise pour chacune
- **Idiolecte** (`idiolect`) -- signature tactile unique : pression, vitesse, chaleur, zone preferee du corps
- **Contact resolution** (`contact_resolution`) -- capacite maximale de communication : full (5 modes), functional (3 modes), basal (1 mode : presence)

Le spawning place le citoyen a la surface du desert. Il ne peut pas spawner sous terre. La descente est un parcours, pas un teletransport. Le manifest encode la position de spawn comme unique : `{ zone: "surface_desert", position: { x: 0, y: 0, z: 0 } }`.

---

## B3 : Physics config -- le sol qui ne s'arrete jamais

Le manifest configure trois couches de physique simultanees :

### Physique sismique
- `base_magnitude` -- la magnitude de fond (4-5 en surface, 8-9+ dans le volcan)
- `frequency_profile` -- le spectre sismique local (basses profondes, claquements secs, infra-basses, etc.)
- `cataclysm_probability` -- la probabilite d'un evenement sismique majeur par tick de simulation
- `tremens_recalc_interval` -- la frequence de recalcul du tremens des citoyens

### Physique du Contact
- `contact_modes_available` -- les modes de Contact possibles dans cette zone
- `contact_pain_threshold` -- la temperature a partir de laquelle le Contact direct cause de la douleur
- `contact_range_modifier` -- modificateur de portee selon les conditions (brouillard sismique, chaleur, etroitesse)
- `bioluminescence_reactivity` -- est-ce que les murs reagissent au toucher dans cette zone

### Physique environnementale
- `temperature` -- temperature ambiante en degres
- `oxygen_level` -- pourcentage d'oxygene disponible (100% en surface, critique en profondeur)
- `light_source` -- source de lumiere dominante (soleil, batons chimiques, bioluminescence, lave, aucune)
- `geology` -- type de roche (sable, basalte, roche amenagee, tube lisse, magma)

Ces trois couches interagissent. La temperature affecte le Contact (peau qui brule). La sismicite affecte la bioluminescence (les filaments pulsent plus fort). L'oxygene affecte le tremens (l'hypoxie amplifie les hallucinations).

---

## B4 : Contact range -- la portee du toucher

Le manifest definit la portee du Contact pour chaque tier et chaque zone. Ce parametre remplace le `radius` + `voice` de Venezia.

| Tier | Contact Range (direct) | Contact Range (corde) | Contact Range (monde) |
|------|------------------------|------------------------|------------------------|
| FULL | 0.5m | 15m (longueur de corde) | 2m (sol autour des pieds) |
| ACTIVE | 1m | 30m | 5m |
| AMBIENT | 5m (vibrations sentie) | 50m (tension de corde) | 10m |

**Par zone :**
- **Surface** -- Contact direct normal, pas de corde necessaire
- **Faille** -- Contact direct impossible, Contact-corde uniquement
- **Village** -- Contact haute resolution (3 doigts), Contact hydraulique (+20m par rigole)
- **Boyau** -- Contact force (0m : les corps se touchent en permanence dans le tube de 60cm)
- **Grotte finale** -- Contact-fantome (portee : memoire, pas distance)

---

## B5 : Avatar config -- metier comme identite visuelle

Le manifest definit l'apparence des citoyens non par classe sociale mais par metier. Le moteur utilise `metier_styles` pour rendre chaque citoyen visuellement identifiable par sa competence dominante.

**Comportement attendu :**
- L'Aeromaitre a un tissu qui reagit aux mouvements d'air dans la simulation
- Le Seismo-auditeur porte un rouleau de papier avec des courbes (le sismographe) visible sur le torse
- La Grimpeuse a des mains animees qui comptent (32 sangles, toujours)
- La Predictrice est pieds nus -- ses pieds reagissent au sol (tremens visible)
- La Biologiste a les mains terreuses -- elles touchent les murs, les filaments, les racines

L'avatar ne flotte pas (contrairement a Venezia ou `float_bob: true`). Les pieds sont au sol. Toujours. Le Contact passe par le sol autant que par les mains. Un avatar qui flotte serait coupe du monde.

---

## B6 : Narrative tick -- le temps du volcan

Le manifest configure un `tick_interval_ms` pour le moteur de physique narrative (le graph mind). Venezia utilise 300000ms (5 minutes). Contre-Terre doit utiliser un tick plus court pour refletez l'urgence du monde :

- **Surface :** tick de 300000ms (5 min) -- rythme calme, la magnitude 4 est le silence
- **Zones profondes :** tick de 60000ms (1 min) -- le monde s'accelere avec la profondeur
- **Grotte finale :** tick de 10000ms (10 sec) -- la magnitude 11 approche, chaque seconde compte

Le tick controle la frequence de recalcul des etats (tremens, Contact, sismicite) et la probabilite d'evenements (seismes, effondrements, crues).

---

*Sources : world-manifest.json (Venezia), ALGORITHM_Seismique.md, ALGORITHM_Contact.md, ALGORITHM_Geographie.md, PATTERNS_Geographie.md*
