# ALGORITHM: Systeme Sismique

**Module :** `worldbuilding/seismique`
**Question centrale :** Comment fonctionnent les mecanismes sismiques du monde ? Quelles sont les regles internes ?

---

## A1 : Systeme de magnitudes

### Echelle et signification narrative

Le monde utilise une echelle de magnitude comparable a l'echelle de Richter terrestre, mais les seuils de perception sont radicalement differents.

```
MAGNITUDE 1-3 : Inexistante dans ce monde. En dessous du seuil de la sismicite permanente.
                Jamais mentionnee. N'a pas de realite perceptive.

MAGNITUDE 4-5 : FOND. Le pouls du monde. Constant. Imperceptible pour les habitants.
                "Le genre de secousse qui ne meritait meme pas un nom."
                La bioluminescence pulse a ce rythme.
                C'est le "silence" de ce monde.

MAGNITUDE 6   : NOTABLE. Sihle note "6.2" dans la marge. Les courbes se resserrent.
                Les chariots bougent. Le corps commence a reagir chez les sensibles.
                Equivalent d'une journee bruyante -- remarquable mais pas alarmant.

MAGNITUDE 7   : VIOLENT. Seisme du Ch. II. "Le monde devint vertical, horizontal,
                diagonal." 8 secondes. Les corps tombent. Le Contact devient animal.
                Pierres qui chutent. Blessures possibles.

MAGNITUDE 8   : DESTRUCTEUR. Seismes des cavernes profondes (Ch. V-VII).
                Les caissons amortisseurs de Sihle protegent les explosifs
                "jusqu'a magnitude 8." Au-dela, plus de garantie.

MAGNITUDE 9+  : CATASTROPHIQUE. Quasi-permanent dans les zones les plus profondes.
                Les structures humaines ne tiennent pas. Les effondrements sont
                massifs. Les morts deviennent inevitables.

MAGNITUDE 11  : THEORIQUE / PROPHETIQUE. Jamais mesuree. Jamais enregistree.
                Sentie uniquement par les predicteurs (Nandi).
                C'est l'objectif de la mission : la pre-declencher.
                Le sismographe ne sait pas la dessiner.
                "Celle que les instruments ne savaient pas encore dessiner."
```

### Regle d'ecriture

La magnitude n'est jamais annoncee en tant que telle dans le texte. Elle est traduite en experience :
- Magnitude 4 = "le sol vibrait sous leurs pieds comme il vibrait toujours"
- Magnitude 6 = Sihle note un chiffre sur son rouleau
- Magnitude 7 = "les pieds quitterent le sol une fraction de seconde"
- Magnitude 11 = "son corps EST un seisme maintenant"

L'auteur connait la magnitude. Le texte ne l'enonce pas (sauf quand Sihle la note -- c'est son role).

---

## A2 : Mecaniques du tremens

### Calibration natale

```
NAISSANCE ──────────────────────────────────────────────────► VIE
    │
    ├── Zone de naissance : spectre sismique local (frequences, amplitudes)
    ├── Le corps s'adapte : les os, les muscles, le systeme vestibulaire
    │   se calibrent sur ce spectre comme l'oreille sur le bruit ambiant
    └── Resultat : le spectre natal devient la "frequence de repos" du corps
```

### Declenchement du tremens

```
DEPLACEMENT vers une zone de frequence differente
    │
    ├── Distance frequentielle = ecart entre spectre natal et spectre local
    │   ├── Faible (meme region) → tremens leger ou absent
    │   ├── Moyenne (region voisine) → nausee, salivation
    │   ├── Forte (traversee de bandes) → vomissements, tremblements
    │   └── Extreme (Nandi) → hallucinations, capillaires eclates, incapacitation partielle
    │
    ├── Symptomes par intensite :
    │   ├── LEGER : salivation, malaise, "note fausse dans un orchestre"
    │   ├── MODERE : vomissements, serrement de machoires, yeux brouilles
    │   ├── SEVERE : tremblements, capillaires eclates, chutes
    │   └── EXTREME : hallucinations, incapacitation, corps-sismographe
    │
    └── Adaptation : le corps se recalibre avec le temps (jours/semaines)
        MAIS la descente dans le volcan traverse les bandes trop vite
        pour que l'adaptation soit complete → tremens cumulatif
```

### Le cas Nandi

```
NANDI
    ├── Zone natale : Archipels du nord-est
    │   └── Spectre : seismes hauts et secs, "claquements brefs comme des coups
    │       de fouet dans la pierre"
    │
    ├── Zone d'expedition : Desert du sud, puis volcan
    │   └── Spectre : "ondes basses, longues, profondes — des ondes qui roulaient
    │       sous le sol comme un animal endormi qui respire"
    │
    ├── Distance frequentielle : MAXIMALE
    │   └── Son tremens est le plus violent de l'equipe
    │
    └── Particularite : PRE-SYMPTOME SISMIQUE
        ├── Son corps ne reagit pas seulement au seisme en cours
        ├── Il reagit au seisme A VENIR
        ├── Le tremens comme systeme predictif :
        │   inflechissement de frequence → nausee → seisme quelques secondes apres
        └── Ce que la science refuse : le corps sait avant l'instrument
```

### Le tremens comme outil de recit

| Phase du tremens | Ce que ca donne dans le texte |
|------------------|-------------------------------|
| Pre-symptome | "Son ventre se serra. La salive lui monta aux levres." |
| Onset | "Le tremens." (mot seul, phrase complete) |
| Description corporelle | Le corps recalcule, les frequences remontent par les os |
| Resolution | Vomissement ou stabilisation ; "elle marcha a travers" |

---

## A3 : Comment la profondeur change les frequences

### Modele par couche

La descente n'est pas une augmentation lineaire de l'intensite. C'est une traversee de bandes de frequences, chacune avec ses propres caracteristiques.

```
SURFACE (desert)
│   Frequences : basses, longues, profondes
│   Amplitude : faible (magnitude 4-5 de fond)
│   Caractere : "un animal endormi qui respire"
│
├── PIEMONT (zones intermediaires)
│   Frequences : montent, deviennent plus "seches" et "nerveuses"
│   Amplitude : variable (magnitude 5-7)
│   Caractere : "claquements nets qui remontaient par les chevilles"
│   Effet : premier tremens de Nandi
│
├── CAVERNES (village des sourds et au-dela)
│   Frequences : infra-basses sous le seuil de la conscience
│   Amplitude : amortie dans le village (40%), violente hors du village
│   Caractere : "vibrations si profondes qu'elles entraient dans les os"
│   Effet : tremens qui affecte les os, pas l'estomac
│
├── FAILLE (passage vertical)
│   Frequences : laterales (ondes rebondissent entre les parois)
│   Amplitude : magnitude 5-7, amplifiee par l'etroitesse
│   Caractere : "les murs se rapprochent d'un centimetre"
│   Particularite : le silence = accumulation de tension → glissement
│
├── CAVERNES PROFONDES
│   Frequences : multiples, superposees, chaotiques
│   Amplitude : magnitude 6-8 reguliere
│   Caractere : signaux complexes, sismographe deborde
│   Effet : tremens paroxystique, hallucinations
│
├── ZONES VOLCANIQUES
│   Frequences : deformees par la chaleur
│   Amplitude : magnitude 7-9+
│   Caractere : ondes melangees a la convection thermique
│   Effet : Contact douloureux (peau brulante)
│
├── INTERIEUR DU VOLCAN
│   Frequences : precurseurs de la magnitude 11
│   Amplitude : magnitude 8-9+ quasi-permanente
│   Caractere : "le sol parle" a Nandi
│   Effet : le sismographe est devenu inutile
│
└── GROTTE FINALE
    Frequences : tout le spectre simultanement
    Amplitude : montee vers 11
    Caractere : Nandi EST la frequence
    Effet : Contact-fantome, hallucinations totales
```

---

## A4 : L'Echelle de Capitulation en detail

### Niveau 1 : Sismographes (instruments)

```
ENTREE : Vibrations mecaniques du sol
PROCESSUS : Transmission mecanique → aiguille → rouleau de papier → courbes
SORTIE : Chiffres (magnitude, frequence, direction)
PRECISION : Haute pour les magnitudes connues (1-9)
LIMITE : Ne mesure que ce que l'instrument SAIT mesurer
         La magnitude 11 est hors echelle
PERSONNAGE : Sihle (porte un sismographe sur le torse)
GESTE NARRATIF : "Sihle nota un chiffre dans la marge"
```

### Niveau 2 : Ecouteurs (perception entrainee)

```
ENTREE : Vibrations percues par le corps entraine
PROCESSUS : Entrainement sensoriel → perception consciente des micro-vibrations
            Le corps sent les seismes PENDANT qu'ils arrivent,
            parfois quelques secondes avant les instruments
SORTIE : Perception en temps reel, plus rapide que l'instrument
PRECISION : Variable selon l'entrainement
LIMITE : Ne percoit que le present (ou l'imminence immediate)
PERSONNAGE : Sihle (aussi), Enama (a mi-chemin entre ecouteur et predicteur)
STATUT SOCIAL : Accepte par la communaute scientifique
```

### Niveau 3 : Predicteurs (prediction corporelle)

```
ENTREE : Tremens — le corps reagit aux frequences qui N'ONT PAS ENCORE ATTEINT la surface
PROCESSUS : Mecanisme inconnu. Le corps "sait" avant que l'evenement se produise.
            Le tremens n'est pas une reaction — c'est une anticipation.
            Les symptomes (nausee, tremblements) sont le corps qui se PREPARE.
SORTIE : Prediction : "ca monte", "ca se resserre", "la magnitude 11 approche"
PRECISION : Imprecise en chiffres, exacte en direction
LIMITE : Incommunicable par les instruments. Incroyable pour la science.
PERSONNAGE : Nandi
STATUT SOCIAL : Rejete. "Le corps ment" (Sihle). "Le corps sait" (Enama).
```

### La progression narrative de la Capitulation

```
Ch. I    : Les trois niveaux coexistent sans conflit. Sihle note. Nandi sent.
Ch. II   : Premier desaccord (embranchement en Y). Sihle → droite. Enama → gauche.
           Nandi → gauche. Senzo suit Nandi. La capitulation commence.
Ch. III  : Le vieux du village secoue la tete devant le sismographe.
           "Ce n'est pas assez." La science est necessaire mais insuffisante.
Ch. IV   : Le sol silencieux piege Sihle (pas de signal = pas de danger ?)
           alors que Nandi sent l'accumulation de tension.
           Silence sismique → piege → mort de Senzo.
Ch. V    : Sihle meurt. Le sismographe est orphelin. Le niveau 1 disparait
           de l'expedition.
Ch. VI   : Enama meurt. Le niveau 2 (mi-ecouteur, mi-predicteur) disparait.
Ch. VII  : Seule Nandi reste. Seul le niveau 3 survit.
Ch. VIII : La capitulation est complete. Le corps seul face a la magnitude 11.
           Pas d'instrument. Pas d'ecouteur. Juste un corps qui sait.
```

---

## A5 : Mecaniques des differents cataclysmes

### Seismes classiques

```
PRE-SIGNAL : Micro-silence (le sol retient son souffle)
             Nandi le sent en premier : "inflechissement dans la frequence"
SIGNAL :     Sismographe reagit (courbes en dents de scie)
IMPACT :     Selon magnitude :
             6 → les chariots bougent, les corps tiennent
             7 → les corps tombent, 8 secondes de chaos
             8+ → structures s'effondrent, morts possibles
POST :       Tremens post-sismique (vertige residuel)
             La bioluminescence "flashe" puis se recalme
```

### Glissements de terrain

```
PRE-SIGNAL : Silence sismique PROLONGE
             Le sol ne tremble plus → accumulation de tension
             Nandi sent le sol "retenu" : "une respiration bloquee"
SIGNAL :     PAS DE SIGNAL STANDARD. Le sismographe ne sait pas lire
             l'absence de tremblement comme un presage.
IMPACT :     "Pas un seisme. Un glissement. La difference :
             coup de poing vs coup de couteau."
             Le sol se deplace lateralement. Pas de secousse → deplacement.
POST :       Irremediable. Un glissement ne "rebondit" pas. La roche a bouge.
             Ce qui est tombe est tombe.
```

### Bangs (seismes acoustiques)

```
PRE-SIGNAL : Changement de pression atmospherique (Thabo avec son tissu)
SIGNAL :     Onde de choc acoustique — son si violent qu'il est physique
IMPACT :     Surdite (temporaire ou permanente)
             Les cellules ciliees sont detruites par les infra-basses
             Menace existentielle pour le Contact : si le toucher lui-meme
             est couvert par le repli proprioceptif, que reste-t-il ?
POST :       Dommages permanents possibles (village des sourds = preuve)
```

### Effondrements

```
PRE-SIGNAL : Vibration locale de la paroi (differente de la vibration de fond)
             Sihle pourrait la lire — "si son sismographe n'avait pas ete
             plaque contre sa poitrine dans la chute"
SIGNAL :     La roche se decroche. Pas d'avertissement sonore.
             "La roche simplement se decrocha."
IMPACT :     Mur/plafond qui tombe. Separation physique du groupe.
             Ce qui est de l'autre cote du mur est inaccessible.
POST :       Silence de la corde (mort de Senzo : "la corde se detendit d'un coup")
             Le Contact est coupe physiquement, pas symboliquement.
```

---

## A6 : Regles de la bioluminescence sismique

```
ORGANISME : Filaments bleu-blanc courant le long des parois rocheuses
NATURE :    Matiere organique, ni mousse ni lichen, "entre les deux"

PULSATION DE FOND :
    - Pulse au rythme de magnitude 4 (frequence de fond)
    - "Le mur pulsait a magnitude 4. Comme un coeur qui battait au rythme du monde."
    - Cycle d'intensite : ~6 heures (palissement puis reprise)

REACTION AU TOUCHER :
    - S'intensifie au contact humain (plus bleu, presque blanc)
    - Se calme au retrait
    - "Le mur repondait au Contact. Pas avec des mots — avec de la lumiere."

REACTION AUX SEISMES :
    - Flash bref lors d'une frappe ou d'un seisme (le coup du vieux au Ch. III)
    - Les filaments "reagissent" aux perturbations sismiques

DOMESTICATION (village des sourds) :
    - Filaments canalises dans des sillons tailles dans la paroi
    - Utilises comme marqueur temporel (cycles de 6 heures = horloge)
    - Tailles de moins en moins loin du village → fin de la zone domestiquee

DEGRADATION EN PROFONDEUR :
    - Plus on descend, plus les filaments deviennent rares et faibles
    - "Une lueur qui pulsait comme un coeur malade"
    - Dans les zones volcaniques profondes : absents (trop chaud)
```

---

*Cree : 2026-03-11 -- Source : MONDE.md, METIERS.md, chapitres I-IV, SQUELETTE.md*
