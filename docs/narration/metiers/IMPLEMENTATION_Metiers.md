# IMPLEMENTATION : Localisation du Contenu des Metiers

## Ou se trouve quoi dans le projet

---

## Fichiers source (worldbuilding)

| Fichier | Contenu metiers | Statut |
|---------|----------------|--------|
| `METIERS.md` | Liste des 15 metiers, notes sur Aeromaitre et Ecouteur/Predicteur, assignations partielles | Incomplet — les assignations sont en retard sur SQUELETTE.md |
| `SQUELETTE.md` | Table complete des assignations (personnage → metiers), cascade de competences, chronologie des morts | Source de verite pour les assignations |
| `PERSONNAGES.md` | Fiches personnages, ordre de disparition, dynamiques de groupe | Source de verite pour les personnalites |

### Hierarchie des sources

Quand les fichiers se contredisent, l'ordre de priorite est :

```
1. Chapitres ecrits (texte final)         → autorite maximale
2. SQUELETTE.md (assignations completes)   → autorite de reference
3. PERSONNAGES.md (personnalites)          → autorite sur les arcs
4. METIERS.md (descriptions des metiers)   → autorite sur les definitions
```

Si METIERS.md dit "Thabo est Speleologue" mais SQUELETTE.md dit "Thabo est Geologue", SQUELETTE.md fait autorite.

---

## Chapitres ecrits (prose)

### Chapitre I — Surface du Desert (`chapitre_01.md`)

| Metier | Personnage | Scenes | Manifestation |
|--------|-----------|--------|--------------|
| Chef (#12) | Senzo | Sc. 1 | Signal de depart (poing/main ouverte), position en tete, regard vers le volcan |
| Cartographe (#7) | Senzo | — | Non montre Ch. I |
| Seismo-auditeur (#8) | Sihle | Sc. 1 | Sismographe sur les genoux, yeux fermes, lecture des courbes |
| Cuisiniere (#13) | Enama | Sc. 1 | Coupe des racines, ecrase des tubercules, prepare la bouillie |
| Aeromaitre (#15) | Thabo | Sc. 1 | Tissu tendu face au vent, observe les fibres |
| Grimpeuse (#11) | Inyoni | Sc. 1 | Serre 32 sangles, compte en serrant, mots du Contact comme priere |
| Predictrice (#9) | Nandi | Sc. 1 | Pieds nus, sent le changement de frequence, main au sol, tremens |
| Mineur (#4) | Sihle | Sc. 1 | Mention des caissons amortisseurs qu'il a concus |

### Chapitre II — Zones Intermediaires (`chapitre_02.md`)

| Metier | Personnage | Scenes | Manifestation |
|--------|-----------|--------|--------------|
| Chef (#12) | Senzo | Sc. 1-5 | Revient vers Nandi, poing d'arret (magnitude 7), choisit la gauche |
| Cartographe (#7) | Senzo | Sc. 4 | Deroule la carte a l'embranchement, les lignes disent "droite" |
| Seismo-auditeur (#8) | Sihle | Sc. 1-4 | Note "6.2", montre le sismographe, Contact technique au poignet |
| Biologiste (#3) | Enama | Sc. 3 | Touche les filaments bioluminescents, Contact-monde |
| Aeromaitre (#15) | Thabo | Sc. 1, 3 | Tissu devant la faille (courant aspirant), frotte les fibres |
| Grimpeuse (#11) | Inyoni | Sc. 2, 3 | Tient debout pendant magnitude 7, detache/repartit chargements |
| Predictrice (#9) | Nandi | Sc. 1-5 | Vomit (recalibrage), sent le micro-silence, pieds qui lisent le sol |
| Speleologue (#14) | Jabu | Sc. 3 | Allume le baton chimique |

### Chapitre III — Le Dernier Village (`chapitre_03.md`)

| Metier | Personnage | Scenes | Manifestation |
|--------|-----------|--------|--------------|
| Chef (#12) | Senzo | Sc. 1, 2, 6 | Contact avec la vieille femme, signal de depart, *On ne remonte pas* |
| Aeromaitre (#15) | Thabo | Sc. 1, 6 | Tissu inerte (changement d'air), recoit le souffle du vieux sur le tissu |
| Ocean (#2) | Jabu | Sc. 6 | Remplit les gourdes au-dela du necessaire |
| Grimpeuse (#11) | Inyoni | Sc. 6 | Verifie les sangles (32 + 24 charges), compte les doigts de l'enfant |
| Predictrice (#9) | Nandi | Sc. 1, 3, 5 | Sent les frequences du village, apprend vite le Contact local, recoit le geste inconnu |
| Biologiste (#3) | Enama | Sc. 3, 4 | Traduit le Contact du vieux pour l'equipe |
| Seismo-auditeur (#8) | Sihle | Sc. 2, 3, 4 | Note l'amortissement de 40%, tend le sismographe au vieux |

### Chapitre IV — La Faille (`chapitre_04.md`)

| Metier | Personnage | Scenes | Manifestation |
|--------|-----------|--------|--------------|
| Chef (#12) | Senzo | Sc. 1-5 | Choisit la fissure (troisieme voie), donne le signal de descente, tire la corde, meurt en protegeant |
| Cartographe (#7) | Senzo | Sc. 2 | Deroule la carte, "la carte etait blanche" — Terra incognita |
| Seismo-auditeur (#8) | Sihle | Sc. 2, 4 | Pointe la droite (donnees), sismographe dans le noir |
| Aeromaitre (#15) | Thabo | Sc. 1 | Tissu aspire devant la faille — "l'air monte, ca descend" |
| Grimpeuse (#11) | Inyoni | Sc. 1, 3, 4 | Deroule la corde, noeuds a 8 torsions, premiere dans la faille, Contact-corde, filtre vibrations |
| Predictrice (#9) | Nandi | Sc. 3, 5, 6 | Sent par les os, alerte sur le piege (sol retenu), reprend le geste de Senzo |

---

## Chapitres a ecrire (Ch. V-VIII)

### Metiers a montrer dans les chapitres restants

**Ch. V — Cavernes Profondes :**
- Meteorologue (Sihle) : prevision atmospherique. OBLIGATOIRE avant sa mort.
- Speleologue (Jabu) : navigation souterraine experte. RENFORCER avant sa mort.
- Survivaliste (Enama) : technique de survie en milieu extreme. A montrer.
- L'absence de cartographe et de leader : les consequences de la mort de Senzo.

**Ch. VI — Zones Volcaniques :**
- Geologue (Thabo) : evaluation des roches, identification des risques. A montrer.
- Aeromaitre (Thabo) : detection des gaz toxiques. EXPLICITE dans le SQUELETTE.
- Explosiviste (Inyoni) : manipulation des charges. A montrer.
- L'absence de cuisinier et de survivaliste : consequences de la mort d'Enama.

**Ch. VII — Interieur du Volcan :**
- Aeromaitre (Thabo) : teste l'air du boyau avant d'entrer. CONFIRME dans SQUELETTE.
- Explosiviste backup (Nandi) : scene d'apprentissage/observation. A montrer avant la mort d'Inyoni.
- L'absence de geologue et de grimpeuse apres la mort de Thabo/Inyoni.

**Ch. VIII — Grotte Finale :**
- Predictrice (Nandi) : tremens au maximum, corps-sismographe. Omnipresent.
- Explosiviste backup (Nandi) : activation de la charge. Scene finale.
- Contact-fantome : hallucinations des metiers perdus (Thabo teste l'air, Senzo montre la route).

---

## Relations entre fichiers

```
METIERS.md (definitions)
    ↓ alimente
SQUELETTE.md (assignations + chronologie)
    ↓ structure
chapitre_XX.md (prose)
    ↓ incarne
BEHAVIORS_Metiers.md (gestes-signatures)
    ↓ verifie
VALIDATION_Metiers.md (invariants)
```

Les modifications doivent remonter la chaine : si un chapitre change l'assignation d'un metier, SQUELETTE.md doit etre mis a jour, puis METIERS.md, puis cette doc chain.
