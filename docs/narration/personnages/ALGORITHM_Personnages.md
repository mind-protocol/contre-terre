# ALGORITHM : Personnages

**Module :** `narration/personnages`
**Derniere mise a jour :** 2026-03-11

---

## Mecaniques du systeme de personnages

Ce document decrit les mecaniques — les regles de fonctionnement interne du systeme de personnages. Pas ce que le lecteur voit (BEHAVIORS), mais comment ca marche en sous-main.

---

## 1. Systeme d'idiolectes

### Definition

Chaque personnage pratique le Contact avec un style unique — son **idiolecte tactile**. L'idiolecte est la "voix" du personnage dans un langage sans voix. Il se compose de :

- **La zone de contact privilegiee** : ou le personnage touche (nuque, epaule, avant-bras, poignet, sol)
- **La pression** : large paume (Senzo), deux doigts (Sihle), trois doigts (villageois)
- **Le rythme** : lent et long (Senzo), rapide et court (Enama), regulier et methodique (Inyoni)
- **Le registre** : intime (nuque), technique (avant-bras), urgence (epaule), lecture (sol)

### Idiolectes documentes

| Personnage | Zone | Pression | Rythme | Registre dominant |
|-----------|------|----------|--------|------------------|
| Senzo | Nuque, Epaule | Paume entiere | Lent, long | Intime / Commandement |
| Nandi | Sol, Poignet | Variable (doux / grip total) | Irregulier (suit le tremens) | Perception / Urgence |
| Enama | Sol, Poignet, Roche | Grip fort | Rapide | Ecoute corporelle / Urgence |
| Sihle | Avant-bras | 2 doigts | Mesure, technique | Information / Donnees |
| Thabo | Air (via tissu) | Contact indirect | Methodique | Lecture environnementale |
| Inyoni | Corde, Sangles | Grip permanent | Compte (repete) | Maintien / Decompte |
| Jabu | Peu de Contact direct | Faible | Efface | Solitude / Travail |

### Mort d'un idiolecte

Quand un personnage meurt, son idiolecte disparait. Les autres ne peuvent plus "dire" ce que ce personnage disait. Meme si un survivant reproduit le geste, ce n'est plus le meme — "Les memes mouvements, faits par un autre, ne diraient pas la meme chose." (Ch. IV)

**Exception notable :** Nandi reprend le geste "On ne remonte pas" de Senzo apres sa mort. Le texte marque explicitement que c'est un emprunt, pas un remplacement : "Un mot qui n'appartenait pas a Nandi mais qu'elle prenait quand meme. Un emprunt. Un heritage. Un vol necessaire."

---

## 2. Cascade de competences

### Table des metiers

| Personnage | Metier 1 | Metier 2 | Metier 3 |
|-----------|----------|----------|----------|
| Senzo | Chef d'expedition | Cartographe | — |
| Sihle | Seismo-auditeur | Meteorologue | Mineur |
| Jabu | Specialiste oceanique | Speleologue | — |
| Enama | Biologiste | Cuisiniere | Survivaliste |
| Thabo | Aeromaître | Geologue | — |
| Inyoni | Grimpeuse | Explosiviste | — |
| Nandi | Predictrice (tremens) | Explosiviste (backup) | — |

### Progression de la cascade

```
DEPART (Ch. I) : 7 personnes, 15 metiers, Contact complet
    |
Ch. IV : Senzo meurt
    → Perdu : Chef, Cartographe
    → Consequence : Plus de decideur de route, plus de carte
    → Contact perdu : Idiolecte de commandement (paume entiere, nuque)
    |
Ch. V : Sihle et Jabu meurent
    → Perdu : Seismo-auditeur, Meteorologue, Mineur, Oceanologue, Speleologue
    → Consequence : 5 metiers d'un coup. Plus de lecture sismique instrumentale,
      plus de navigation oceanique, plus de connaissances de minage.
    → Contact perdu : Contact technique (2 doigts), Contact isole de Jabu
    → L'equipe passe de 6 a 4. La moitie des mots du Contact sont morts.
    |
Ch. VI : Enama meurt
    → Perdu : Biologiste, Cuisiniere, Survivaliste
    → Consequence : Plus de nourriture specialisee, plus de lecture du vivant,
      plus de survie de terrain
    → Contact perdu : Geste-monde (main a plat sur la roche) + un geste nouveau
      invente a l'instant de la mort, qui meurt avec elle
    → L'equipe est a 3.
    |
Ch. VII : Thabo et Inyoni meurent
    → Perdu : Aeromaître, Geologue, Grimpeuse, Explosiviste principal
    → Consequence : CRITIQUE. Plus de lecture de l'air (gaz toxiques) au moment
      ou l'air est le plus dangereux. Plus d'explosiviste principal — Nandi doit
      activer la charge en backup, sans formation complete.
    → Contact perdu : Tissu (Thabo), Corde (Inyoni), "Tient." (Inyoni)
    → Nandi est seule. 1 personne. 2 metiers restants (predictrice + backup explosifs).
    |
Ch. VIII : Nandi meurt (detonation)
    → Perdu : Tout.
    → Le Contact n'a plus de destinataire. La langue meurt avec le dernier locuteur.
```

### Regle de la cascade

La cascade n'est pas lineaire — elle est exponentielle. Chaque mort amplifie la vulnerabilite :

- 7 → 6 (Ch. IV) : perte du chef. Le groupe peut encore fonctionner.
- 6 → 4 (Ch. V) : perte de 5 metiers d'un coup. Le groupe est diminue de moitie.
- 4 → 3 (Ch. VI) : perte de la survie. Le groupe ne peut plus se nourrir, plus interpreter le vivant.
- 3 → 1 (Ch. VII) : perte de l'air et des explosifs. Nandi est seule et sous-equipee.
- 1 → 0 (Ch. VIII) : fin.

---

## 3. Arcs de personnages

### Types d'arcs

Le roman utilise trois types d'arcs :

**Arc long** — un personnage present du debut a la fin (ou presque), avec une transformation visible :
- Nandi (Ch. I-VIII) : fragile → predictrice → leader par defaut → detonatrice → derniere survivante

**Arc de pivot** — un personnage dont la mort change la direction du recit :
- Senzo (Ch. I-IV) : le chef tombe, plus personne ne decide
- Enama (Ch. I-VI) : le sacrifice volontaire, ne du conflit avec Sihle

**Arc d'effacement** — un personnage dont la discretion prepare le manque :
- Jabu (Ch. I-V) : presque invisible, sa mort revele retrospectivement sa presence silencieuse
- Thabo (Ch. I-VII) : methodique, fiable, son absence est ressentie par l'air qui n'est plus lu
- Inyoni (Ch. I-VII) : "Tient" jusqu'a ce que ca ne tienne plus

### Progressions par chapitre

| Personnage | Ch. I | Ch. II | Ch. III | Ch. IV | Ch. V | Ch. VI | Ch. VII | Ch. VIII |
|-----------|-------|--------|---------|--------|-------|--------|---------|----------|
| Senzo | Chef stable | Decide la route | Valide le Contact | Meurt | — | — | — | — |
| Nandi | Predictrice fragile | Tremens, vomit | Apprend geste inconnu | Reprend "On ne remonte pas" | (leader par defaut) | (sent mag.11) | (quasi-seule) | Detone |
| Enama | Coupe racines | Colere contre Sihle | Apprend Contact village | Pas d'avis pour 1ere fois | Cause mort Sihle | Sacrifice | — | — |
| Sihle | Lit courbes | Conflit donnees vs corps | Doute au village | Ignore par Senzo | Meurt | — | — | — |
| Thabo | Teste air | Fronce sourcils | Recoit souffle du vieux | Plie tissu en deuil | ? | ? | Meurt | — |
| Inyoni | Compte sangles | "Tient." | Compte doigts de l'enfant | Compte fibres, Contact-corde | ? | ? | Meurt | — |
| Jabu | Enroule hamacs, seul | Prend un eclat, grogne | Remplit gourdes | Suspendu sans plainte | Meurt | — | — | — |

---

## 4. Dynamiques de paires

### Paires narrativement actives

**Senzo — Nandi (le couple tactile)**
- Relation exclusive : main sur la nuque, dialects prives.
- Senzo est le seul a toucher la nuque de Nandi.
- Apres sa mort : le geste de la nuque est perdu. Personne ne le remplacera.
- Transfert : Nandi herite du geste de leadership ("On ne remonte pas").

**Sihle — Enama (raison vs intuition)**
- Antagonisme central. Jamais resolu par la victoire d'un camp.
- Sihle : "Les donnees disent non." Enama : "La terre parle."
- Climax : Enama cause indirectement la mort de Sihle (Ch. V). Culpabilite → sacrifice (Ch. VI).
- Moment de rapprochement : Sihle s'assoit a cote d'Enama sans la toucher (Ch. IV, deuil).

**Thabo — Inyoni (la mort partagee)**
- Codes comme un duo dans la colonne de marche (cote a cote, tirent le meme chariot).
- Seule mort partagee du roman. Contact survit entre eux dans le noir du boyau.
- Symbolique : identites liees qui fusionnent dans la fin.

**Senzo — equipe (le regard et le poing)**
- Senzo commande par le geste : poing ouvert = on y va, arc descendant = on ne remonte pas.
- Personne ne le remplace explicitement. Le groupe subit la route au lieu de la choisir.

### Paires latentes (moins documentees)

- Enama — Nandi : partagent la lecture corporelle du monde. "Toi aussi ?" (Ch. II, echange de regards)
- Inyoni — corde / sangles : relation personnage-objet aussi forte qu'une relation personnage-personnage
- Sihle — sismographe : idem

---

## 5. Mecanique de la mort linguistique

### Processus

Chaque mort traverse les memes etapes :

1. **L'evenement physique** — glissement, chute, noyade, lave, eboulement, detonation
2. **La coupure du Contact** — la corde se detend, la main lache, le mur tombe entre les corps
3. **Le silence** — les survivants decouvrent qu'un "trou" s'est ouvert dans leur langue
4. **L'inventaire du manque** — quels gestes ne peuvent plus etre dits, quels metiers ne sont plus couverts
5. **La tentative de reprise** — un survivant tente de reprendre un geste du mort (Nandi reprend "On ne remonte pas")
6. **La difference** — le geste repris n'est pas le meme. "Les doigts plus fins, le mouvement plus lent, l'arc plus large."

### Ce qui disparait a chaque mort

| Mort | Idiolecte perdu | Metiers perdus | Geste irrecuperable |
|------|----------------|----------------|---------------------|
| Senzo | Paume entiere, rythme lent, nuque | Chef, Cartographe | La nuque de Nandi |
| Sihle | 2 doigts techniques | Seismo-auditeur, Meteo, Mineur | Lecture instrumentale |
| Jabu | (peu documente) | Oceanologue, Speleologue | Presence silencieuse |
| Enama | Grip fort, Contact-monde | Biologiste, Cuisine, Survie | Geste nouveau invente a la mort |
| Thabo | Tissu, froncement | Aeromaître, Geologue | Lecture de l'air |
| Inyoni | Compte, corde, "Tient" | Grimpeuse, Explosifs | Contact-corde |
| Nandi | Pieds nus, tremens | Predictrice, Explosifs backup | Le Contact tout entier |
