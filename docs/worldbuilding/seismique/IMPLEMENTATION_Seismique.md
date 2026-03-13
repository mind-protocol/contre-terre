# IMPLEMENTATION: Systeme Sismique

**Module :** `worldbuilding/seismique`
**Question centrale :** Ou vit le contenu sismique dans les fichiers du projet ?

---

## Sources de verite

### Worldbuilding (regles du monde)

| Fichier | Contenu sismique | Role |
|---------|------------------|------|
| `MONDE.md` | Systeme sismique complet : types de cataclysmes, echelles, architecture, tremens, Echelle de Capitulation, profondeur/temperature, faune/flore | **Source de verite primaire** pour les regles du monde sismique |
| `CONCEPT.md` | Premisse ("monde de seismes permanents"), inversion Damasio (vent → terre) | Source du concept generateur |
| `METIERS.md` | Ecouteur de seismes (#8), Predicteur (#9), Aeromaitre (#15) | Definition des metiers lies au sismique |

### Narration (comment le sismique est ecrit)

| Fichier | Contenu sismique | Role |
|---------|------------------|------|
| `SQUELETTE.md` | Courbe d'escalade sismique par chapitre, morts par element geologique, arc Sihle/Enama/Nandi | **Plan de reference** pour l'escalade narrative |
| `STRUCTURE.md` | Chapitres = couches geologiques, boyau, village sourd | Structure narrative liee au sismique |
| `PERSONNAGES.md` | Arcs de Nandi (tremens), Sihle (instruments), Enama (corps) | Personnages porteurs du theme sismique |

### Prose (texte ecrit)

| Fichier | Contenu sismique | Statut |
|---------|------------------|--------|
| `chapitre_01.md` | Magnitude 4-5 de fond, premier pressentiment de Nandi, architecture mobile, sismographe de Sihle | CANONICAL |
| `chapitre_02.md` | Premier seisme magnitude 7, tremens de Nandi (premier vomissement), bioluminescence, infra-basses, embranchement en Y (Sihle vs Enama), silence sismique avant glissement | CANONICAL |
| `chapitre_03.md` | Village des sourds (amortissement 40%), echo sismique du vieux, tremblement volontaire de la vieille femme, bioluminescence domestiquee, avertissement ("les intervalles raccourcissent") | CANONICAL |
| `chapitre_04.md` | Seismes lateraux dans la fissure, faille en mouvement, Contact-corde sous seisme, silence sismique = piege, glissement de terrain, effondrement du mur (mort de Senzo) | CANONICAL |
| `chapitre_05.md` | a ecrire | -- |
| `chapitre_06.md` | a ecrire | -- |
| `chapitre_07.md` | a ecrire | -- |
| `chapitre_08.md` | a ecrire | -- |

---

## Documentation (ce fichier et la chaine complete)

| Fichier | Contenu |
|---------|---------|
| `docs/worldbuilding/seismique/OBJECTIVES_Seismique.md` | Ce que le systeme sismique optimise narrativement |
| `docs/worldbuilding/seismique/PATTERNS_Seismique.md` | Decisions de design du systeme sismique |
| `docs/worldbuilding/seismique/BEHAVIORS_Seismique.md` | Manifestations du sismique par chapitre |
| `docs/worldbuilding/seismique/ALGORITHM_Seismique.md` | Mecaniques internes (magnitudes, tremens, profondeur) |
| `docs/worldbuilding/seismique/VALIDATION_Seismique.md` | Invariants de coherence |
| `docs/worldbuilding/seismique/IMPLEMENTATION_Seismique.md` | Ce fichier |
| `docs/worldbuilding/seismique/HEALTH_Seismique.md` | Controles qualite |
| `docs/worldbuilding/seismique/SYNC_Seismique.md` | Etat actuel |

### Taxonomie

| Fichier | Termes sismiques definis |
|---------|------------------------|
| `docs/TAXONOMY.md` | `tremens`, `magnitude`, `Echelle de Capitulation`, `ecouteur`, `predicteur`, `aeromaitre`, `bioluminescence`, `bangs`, `village des sourds` |

---

## Carte des references croisees

### Le sismique dans les autres modules

Le systeme sismique irrigue tous les autres modules du projet. Il n'est pas autonome -- il est le substrat sur lequel tout le reste repose.

```
seismique ──────► contact
    │               Le Contact existe PARCE QUE le sol tremble.
    │               Le tremens et la sensibilite sismique nourrissent
    │               la finesse du Contact (Nandi, village des sourds).
    │
    ├──────────► geographie
    │               Chaque zone = un spectre sismique.
    │               La descente = traversee de bandes de frequences.
    │               L'architecture est une reponse sismique.
    │
    ├──────────► personnages
    │               Nandi (predictrice/tremens), Sihle (sismographe/ecouteur),
    │               Enama (corps/intuition), Thabo (aeromaitre/air sismique).
    │               Les morts sont causees par des elements geologiques.
    │
    ├──────────► structure
    │               Chapitres = couches geologiques.
    │               Courbe d'escalade sismique = courbe narrative.
    │               Chaque mort = un type de cataclysme.
    │
    └──────────► metiers
                    3 metiers directement sismiques :
                    Ecouteur (#8), Predicteur (#9), Aeromaitre (#15).
                    L'effet cascade des morts amplifie la perte sismique.
```

---

## Passages cles a reference rapide

### Magnitude 4 de fond (le pouls du monde)

> "Le sol vibrait sous leurs pieds comme il vibrait toujours, comme il avait vibre la veille et l'avant-veille et tous les jours depuis que les jours existaient. Magnitude 4, peut-etre 5. Le genre de secousse qui ne meritait meme pas un nom. Un bruit de fond. Le pouls du monde."
-- Ch. I, Sc. 1

### Premier tremens de Nandi

> "Nandi sentit le sol changer. Pas un seisme. Pas encore. Quelque chose avant le seisme. Un inflechissement dans la frequence, un leger desaccord entre la vibration qu'elle attendait et celle qui arrivait. Comme une note fausse dans un orchestre que personne d'autre n'entendait."
-- Ch. I, Sc. 1

### Le micro-silence (pre-seisme)

> "Le micro-silence. L'infime suspension de la vibration de fond, la fraction de seconde ou le sol retient son souffle. Comme un coeur qui saute un battement."
-- Ch. II, Sc. 2

### Seisme magnitude 7

> "Pas comme dans le desert, ou les secousses roulaient sous le sable, longues et sourdes, presque paresseuses. Ici la roche n'amortissait rien. L'onde remonta directement par le basalte, rigide, brutale, et elle frappa les pieds comme un coup de marteau sous la plante."
-- Ch. II, Sc. 2

### Glissement vs seisme

> "Pas un seisme. Un glissement. La difference etait celle entre un coup de poing et un coup de couteau -- le seisme frappe et relache, le glissement coupe et ne s'arrete plus."
-- Ch. IV, Sc. 5

### Le sol retenu (silence = piege)

> "Le sol n'etait pas silencieux. Le sol etait retenu. Comme une respiration bloquee. Comme un cri qui monte dans la gorge et qui ne sort pas."
-- Ch. IV, Sc. 5

### Sismographe insuffisant

> "Le vieux regarda le sismographe. Longtemps. [...] Et le vieux secoua la tete. [...] Ce n'est pas assez."
-- Ch. III, Sc. 4

### Bioluminescence sismique

> "Des filaments lumineux, tenus, bleutes, couraient le long de la roche comme un reseau de veines. [...] une matiere organique qui pulsait faiblement au rythme de la vibration de fond. Magnitude 4. Le mur pulsait a magnitude 4. Comme un coeur qui battait au rythme du monde."
-- Ch. II, Sc. 3

---

*Cree : 2026-03-11 -- Source : arborescence du projet, contenu des fichiers*
