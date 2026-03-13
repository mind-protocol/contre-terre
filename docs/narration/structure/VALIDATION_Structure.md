# VALIDATION: Structure Narrative

**Module :** `narration/structure`
**Source de verite :** `STRUCTURE.md`, `SQUELETTE.md`
**Derniere mise a jour :** 2026-03-11

---

## Invariants structurels

Ces regles sont non-negociables. Si un chapitre viole un invariant, le chapitre est casse.

---

### V1 : 8 chapitres, 8 couches, 7 morts

Le roman a exactement 8 chapitres. Chaque chapitre correspond a une couche geologique. 7 personnages meurent — un par un ou par paires — selon l'ordre defini dans le squelette.

**Verification :** Compter les chapitres. Compter les morts. Verifier la correspondance chapitre-couche.

| Ch. | Couche | Morts | Cumul survivants |
|-----|--------|-------|-----------------|
| I | Surface | 0 | 7 |
| II | Piemont | 0 | 7 |
| III | Village | 0 | 7 |
| IV | Faille | 1 (Senzo) | 6 |
| V | Cavernes | 2 (Jabu, Sihle) | 4 |
| VI | Volcanique | 1 (Enama) | 3 |
| VII | Chambre | 2 (Thabo, Inyoni) | 1 |
| VIII | Grotte finale | 1 (Nandi) | 0 |

**Si un personnage meurt dans un chapitre different de celui prevu, l'invariant est viole.**

---

### V2 : Ordre des morts inalterable

L'ordre des morts est structurel, pas narratif. Chaque mort est causee par un element geologique specifique et remplit une fonction precise dans l'arc du Contact.

| Ordre | Personnage | Element | Fonction structurelle |
|-------|-----------|---------|----------------------|
| 1er | Senzo | Terre (glissement) | Le decideur tombe. Plus de route choisie. |
| 2e | Jabu | Eau (noyade) | L'effacement discret. Le specialiste de l'eau meurt par l'eau. |
| 3e | Sihle | Vide (chute) | La raison tombe. Le conflit se resout par la mort. |
| 4e | Enama | Feu (lave) | Le choix. La culpabilite tue plus que le volcan. |
| 5e-6e | Thabo & Inyoni | Pierre (ensevelissement) | La mort partagee. Le Contact survit entre eux. |
| 7e | Nandi | Tout (detonation) | La mission. La boucle se ferme. |

**Modifier cet ordre detruit la cascade de competences et l'arc d'erosion du Contact.**

---

### V3 : Jamais d'exposition

Aucune phrase du roman ne doit expliquer le monde au lecteur. Pas de "Dans ce monde, les humains communiquent par le toucher car..." Pas de flashback explicatif. Pas de dialogue pedagogique. Le monde s'enseigne par l'usage.

**Verification :** Pour chaque passage, se demander : "Est-ce qu'un personnage penserait ou dirait ca naturellement ?" Si la reponse est non — si le passage n'existe que pour informer le lecteur — c'est de l'exposition. Supprimer.

**Cas limites acceptes :**
- Un personnage qui explique quelque chose a un autre personnage qui ne sait pas (la vieille femme enseigne a Nandi = OK)
- Un personnage qui pense a ce qu'il sait dans un contexte ou c'est naturel (Sihle lit son sismographe = OK)
- Le contexte qui revele le fonctionnement (magnitude 7 → le Contact change = le lecteur comprend le lien sans qu'on le dise)

---

### V4 : Un a deux POV par chapitre, Nandi toujours presente

Chaque chapitre est ecrit depuis un ou deux points de vue internes. Jamais d'omniscience. Nandi est POV dans chaque chapitre — elle est le fil conducteur sensoriel.

**Verification :** Identifier le(s) POV de chaque chapitre. Verifier que le texte ne contient pas d'information qu'aucun POV ne peut connaitre.

**Exemples de violations :**
- "Sihle pensait que..." dans un chapitre ou Sihle n'est pas POV → violation
- "La roche etait composee de basalte a 73%..." quand personne ne le sait → violation
- "A la surface, le monde continuait..." quand tout le monde est sous terre → violation

---

### V5 : Le Contact retrecit

Le nombre de gestes de Contact DOIT diminuer a mesure que les personnages meurent. C'est l'erosion linguistique — la colonne vertebrale du roman.

**Verification quantitative :**

| Chapitres | Idiolectes vivants | Gestes disponibles | Registre |
|-----------|-------------------|-------------------|----------|
| I-III | 7 | Complet | Riche, nuance, explore |
| IV | 6 (perte Senzo) | -1 chef | L'epaule et la nuque de Senzo manquent |
| V | 4 (perte Jabu, Sihle) | -3 cumul | Le technique (Sihle) et le discret (Jabu) manquent |
| VI | 3 (perte Enama) | -4 cumul | Le corporel (Enama) manque |
| VII | 1 (perte Thabo, Inyoni) | -6 cumul | Le tissu (Thabo) et le comptage (Inyoni) manquent |
| VIII | 0 vivant (Nandi seule) | Le Contact n'a plus de destinataire | Fantome |

**Un chapitre qui introduit PLUS de Contact qu'il n'en perd est suspect.** L'exception est le Contact-corde (Ch. IV) qui est un nouveau medium, pas un enrichissement — le Contact-corde est plus pauvre que le Contact direct.

---

### V6 : Chaque mort supprime des competences

La cascade de competences est structurelle. 15 metiers pour 7 personnes signifie que chaque mort brise 2-3 expertises.

**Verification :**

| Mort | Competences perdues | Consequence narrative |
|------|--------------------|-----------------------|
| Senzo | Chef, Cartographe | Plus de route decidee. La carte est inutile. |
| Jabu | Oceanique, Speleologue | L'eau et les grottes ne sont plus lues. |
| Sihle | Seismo-auditeur, Meteo, Mineur | Plus de mesure instrumentale. |
| Enama | Biologiste, Cuisiniere, Survie | Plus d'ecoute corporelle du sol. Plus de nourriture. |
| Thabo | Aeromaitre, Geologue | L'air n'est plus lu. La roche non plus. |
| Inyoni | Grimpeuse, Explosiviste | Plus de corde, plus de charge — Nandi doit faire en backup. |

**Apres chaque mort, le texte ne doit JAMAIS montrer l'equipe exercant la competence du mort comme si de rien n'etait.** Si Thabo est mort, personne ne teste l'air avec un tissu. Si Sihle est mort, personne ne lit le sismographe.

---

### V7 : La voix est toujours une transgression

Chaque fois qu'un personnage utilise sa voix (parle a voix haute), le texte marque cet acte comme inhabituel, couteux, transgressif. La voix n'est jamais le mode par defaut.

**Verification :** Toute ligne de dialogue vocal doit etre accompagnee d'une reaction du groupe (surprise, malaise, silence apres). Si le dialogue est traite comme normal, l'invariant est viole.

---

### V8 : Ouverture sensorielle, fermeture en seuil

Chaque chapitre ouvre par les sens (le corps entre dans la couche) et ferme par un seuil (le groupe quitte la couche).

**Verification :**
- Premiere phrase : contient-elle une sensation physique (toucher, vibration, temperature, son) ?
- Derniere phrase : marque-t-elle un passage, une transition, une perte ?

---

### V9 : Pas d'ellipse temporelle

Le temps narratif est continu. La descente ne s'interrompt pas entre les chapitres. Pas de "trois jours plus tard" au debut d'un chapitre. Le lecteur descend avec l'equipe, sans pause.

**Cas limite :** Le temps sous terre est incertain ("ce qui ressemblait a trois heures"). L'incertitude temporelle est un effet du monde souterrain, pas une ellipse narrative.

---

### V10 : La premiere et la derniere phrase du roman

**Premiere phrase :** "Senzo posa sa main sur l'epaule de Nandi. Trois pressions. Lentes."
Cette phrase est canonique. Elle ouvre le Contact, le monde, et la relation Senzo-Nandi.

**Derniere phrase :** Doit contenir le silence. Pour la premiere fois, rien ne tremble. La boucle se ferme — le monde qui tremblait depuis la premiere phrase cesse de trembler.

**Invariant :** La derniere phrase est le negatif de la premiere. Le Contact (premiere phrase) est devenu silence (derniere phrase). Le tremblement (omnipresent) est devenu immobilite.

---

### V11 : Le geste inconnu traverse le roman

Le geste transmis par la vieille femme au chapitre III est plante, porte par Nandi pendant cinq chapitres, et compris au chapitre VIII. Il ne doit JAMAIS etre explique avant le VIII. Nandi le porte sans le comprendre.

**Verification :** Le geste peut etre mentionne (Nandi y pense, ses mains se souviennent) mais jamais decode avant le chapitre final.

---

## Matrice de verification

| Invariant | Verifiable par | Frequence |
|-----------|---------------|-----------|
| V1 (8/8/7) | Comptage | A la fin |
| V2 (ordre des morts) | Tableau | A chaque mort ecrite |
| V3 (zero exposition) | Relecture critique | A chaque chapitre |
| V4 (POV) | Identification narrateur | A chaque scene |
| V5 (erosion Contact) | Comptage des gestes | A chaque chapitre |
| V6 (cascade competences) | Verification absence | Apres chaque mort |
| V7 (voix = transgression) | Relecture dialogue | A chaque occurrence |
| V8 (ouverture/fermeture) | Premiere/derniere phrase | A chaque chapitre |
| V9 (pas d'ellipse) | Transition entre chapitres | A chaque jonction |
| V10 (premiere/derniere) | Verification | A la fin |
| V11 (geste inconnu) | Tracking | Continu |
