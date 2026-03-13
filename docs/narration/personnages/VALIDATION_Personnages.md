# VALIDATION : Personnages

**Module :** `narration/personnages`
**Derniere mise a jour :** 2026-03-11

---

## Invariants du systeme de personnages

Un invariant est une regle qui doit etre vraie dans chaque scene, chaque chapitre, chaque page. Si un invariant est viole, le texte est incoherent.

---

## Invariants structurels

### V01 : Decompte des vivants

A tout moment du recit, le nombre de personnages vivants doit correspondre au schema suivant :

| Chapitres | Personnages vivants | Nombre |
|-----------|-------------------|--------|
| I - III | Senzo, Nandi, Enama, Sihle, Thabo, Inyoni, Jabu | 7 |
| IV (apres mort Senzo) | Nandi, Enama, Sihle, Thabo, Inyoni, Jabu | 6 |
| V (apres morts Sihle + Jabu) | Nandi, Enama, Thabo, Inyoni | 4 |
| VI (apres mort Enama) | Nandi, Thabo, Inyoni | 3 |
| VII (apres morts Thabo + Inyoni) | Nandi | 1 |
| VIII (apres mort Nandi) | (aucun) | 0 |

**Verification :** dans chaque scene, les personnages presents doivent etre un sous-ensemble des vivants. Un personnage mort ne peut pas apparaitre sauf en hallucination explicitement marquee (Ch. VIII uniquement pour le Contact-fantome).

### V02 : Ordre des morts inviolable

L'ordre est : Senzo (IV) → Sihle (V) → Jabu (V) → Enama (VI) → Thabo (VII) → Inyoni (VII) → Nandi (VIII).

Sihle et Jabu meurent dans le meme chapitre. Thabo et Inyoni meurent dans le meme chapitre, ensemble. Aucune permutation n'est autorisee.

### V03 : Cause de mort coherente avec l'element

| Personnage | Cause | Element | Verification |
|-----------|-------|---------|-------------|
| Senzo | Glissement de terrain | Terre | La terre le prend |
| Sihle | Chute (causee par Enama) | Vide | Tombe dans le vide |
| Jabu | Noyade apres separation | Eau | L'eau le prend |
| Enama | Marche dans la lave (sacrifice) | Feu | Le feu la prend / elle choisit le feu |
| Thabo + Inyoni | Ensevelissement | Pierre | La pierre les referme |
| Nandi | Detonation | Tout | Tous les elements |

### V04 : 15 metiers distribues sur 7 personnes

La table des metiers (ALGORITHM) est la reference. Aucun metier ne peut etre attribue a un personnage qui ne le possede pas. Aucun personnage ne peut exercer un metier qu'il n'a pas.

---

## Invariants comportementaux

### V05 : Gestes-signatures constants

Chaque personnage maintient ses gestes-signatures tant qu'il est vivant. Ils ne changent pas sans raison narrative explicite.

| Personnage | Geste | Invariant |
|-----------|-------|-----------|
| Nandi | Pieds nus | Toujours. Jamais de chaussures. Dans chaque scene ou elle marche. |
| Thabo | Tissu tendu | A chaque passage, a chaque entree. Le tissu est toujours present. |
| Inyoni | Compte | Tout. Sangles, fibres, doigts, personnes. Le decompte est constant. |
| Inyoni | "Tient." | Repete en serrant. Le mot est present dans chaque scene ou elle serre. |
| Sihle | Sismographe | Toujours sur lui. Harnais de poitrine. Courbes visibles. |
| Senzo | Main sur nuque de Nandi | Exclusif. Personne d'autre ne touche la nuque de Nandi. |
| Enama | Mains au sol quand elle "ecoute" | Rituel repete a chaque embranchement, chaque doute. |
| Jabu | Seul, a l'ecart | Position isolee dans le groupe. Deuxieme chariot, seul. |

### V06 : Zone de Contact coherente par personnage

Chaque personnage touche dans sa zone privilegiee. Sihle ne touche pas la nuque. Senzo ne pose pas deux doigts sur l'avant-bras. Les idiolectes ne se melangent pas sans raison narrative (le seul melange autorise est le "vol" d'un geste apres une mort — cf. Nandi reprenant le geste de Senzo).

### V07 : Le tremens de Nandi reagit a chaque changement de frequence

Chaque fois que le sol change de registre sismique (nouvelle zone, nouvelle couche, nouveau milieu), Nandi doit avoir une reaction physique : nausee, vomissement, mâchoires serrees, yeux injectes. Le tremens n'est pas intermittent — il est systematique.

### V08 : Enama ne touche jamais le sismographe de Sihle

L'antagonisme Enama/Sihle se manifeste aussi par l'evitement de l'objet de l'autre. Enama ne regarde pas le sismographe ("Elle n'avait jamais regarde son sismographe"). Sihle ne pose pas les mains au sol pour "ecouter."

---

## Invariants narratifs

### V09 : Pas de parole inutile

Le monde de Contre-Terre est un monde ou la voix est un luxe inutile. Les personnages ne parlent pas — ils utilisent le Contact. Toute parole vocale doit etre marquee comme exceptionnelle. La seule instance dans les chapitres ecrits est Enama qui dit "La terre parle" (Ch. II) — et le texte marque explicitement le choc de cette transgression.

**Regle :** Si un personnage parle a voix haute, le texte doit noter que c'est anormal et pourquoi il le fait quand meme.

### V10 : Le Contact s'apprend par immersion, jamais par explication

Aucun personnage n'explique le Contact. Le lecteur l'apprend en le voyant utilise. "Trois pressions. Lentes. D'un cote a l'autre. Dans leur Contact, ca voulait dire : Suis-moi." (Ch. I) — la traduction suit l'usage, elle ne le precede pas.

**Regle :** Pas de scene d'exposition type "Le Contact est un langage tactile qui fonctionne comme suit..."

### V11 : Les morts ne reviennent pas (sauf Contact-fantome)

Les personnages morts disparaissent du recit. Pas de flashbacks. Pas de souvenirs detailles. La seule exception prevue est le Contact-fantome au Ch. VIII : Nandi hallucine les mains des morts. Cette exception doit etre clairement marquee comme hallucination.

### V12 : Apres une mort, l'inventaire du manque

Chaque scene de mort doit etre suivie (pas forcement immediatement, mais dans le meme chapitre) par un moment ou les survivants decouvrent ce qu'ils ne peuvent plus dire/faire. La mort de Senzo → "Les gestes que Senzo avait [...] n'existent plus." La mort de Sihle → plus de lecture instrumentale. Etc.

### V13 : Nandi est la derniere survivante

Non-negociable. Nandi meurt en dernier. Seule. Elle active la charge. Le Contact meurt avec elle.

### V14 : Le sacrifice d'Enama est volontaire

Enama ne meurt pas par accident. Elle choisit la lave. La culpabilite de la mort de Sihle est le moteur explicite de son sacrifice. Toute scene de mort d'Enama qui la montrerait comme accidentelle violerait cet invariant.

---

## Invariants de coherence inter-fichiers

### V15 : Coherence avec SQUELETTE.md

Le squelette est la source de verite pour la structure. Les scenes de mort, l'ordre des chapitres, les elements associes doivent correspondre exactement a SQUELETTE.md.

### V16 : Coherence avec METIERS.md

Les attributions de metiers dans SQUELETTE.md priment sur celles de METIERS.md (qui sont incompletes). Toute mention de competence dans la prose doit etre coherente avec la table canonique de l'ALGORITHM.

### V17 : Coherence avec CONTACT.md

Les gestes de Contact decrits dans la prose doivent etre coherents avec le systeme decrit dans CONTACT.md (5 modes, zones, registres). Les innovations (Contact-corde, Contact-monde) doivent etre marquees comme telles.

---

## Grille de verification rapide

Pour chaque scene ecrite, verifier :

- [ ] Le bon nombre de personnages vivants est present
- [ ] Aucun personnage mort n'apparait (sauf hallucination Ch. VIII)
- [ ] Les gestes-signatures des personnages presents sont coherents
- [ ] Les zones de Contact sont respectees
- [ ] Le tremens de Nandi reagit si le sol change
- [ ] Pas de parole vocale non-justifiee
- [ ] Le Contact est montre, pas explique
- [ ] Les metiers exerces correspondent aux attributions
