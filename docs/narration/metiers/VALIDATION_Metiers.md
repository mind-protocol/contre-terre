# VALIDATION : Invariants du Systeme des Metiers

## Regles de coherence que chaque chapitre doit respecter

---

## V1 : Aucun mort ne peut exercer son metier

**Invariant :** Un personnage mort ne peut pas etre mentionne en train d'exercer sa competence, sauf en hallucination (Ch. VIII, Contact-fantome).

**Verification :** Apres chaque mort, scanner le texte pour toute mention du metier perdu comme s'il etait encore actif.

**Exemples de violations :**
- Apres Ch. IV : "Senzo consulta la carte" → VIOLATION
- Apres Ch. V : "Sihle nota un chiffre dans la marge" → VIOLATION
- Exception : "Nandi hallucina Thabo qui testait l'air" → AUTORISE (Ch. VIII, Contact-fantome)

---

## V2 : La perte doit etre ressentie

**Invariant :** Apres chaque mort, au moins une scene doit montrer le groupe confronte a l'absence de la competence perdue.

**Verification :** Pour chaque mort, identifier la scene ou le groupe echoue/improvise parce que le metier manque.

**Attendu :**
- Senzo mort (Ch. IV) → Scene ou personne ne sait quelle route prendre (Ch. V)
- Sihle mort (Ch. V) → Scene ou les donnees sismiques manquent, personne ne sait lire les signes (Ch. VI)
- Jabu mort (Ch. V) → Scene ou l'eau est un probleme et personne ne le gere (Ch. VI)
- Enama morte (Ch. VI) → Scene ou la nourriture/survie est un probleme sans solution (Ch. VII)
- Thabo mort (Ch. VII) → Scene ou l'air est dangereux et personne ne le detecte (Ch. VIII)
- Inyoni morte (Ch. VII) → Scene ou Nandi doit manipuler les explosifs seule (Ch. VIII)

---

## V3 : Chaque metier doit etre montre avant la mort de son porteur

**Invariant :** Un metier qui n'a jamais ete montre en action ne peut pas etre ressenti comme une perte par le lecteur.

**Verification :** Pour chaque metier, identifier au moins une scene de demonstration dans les chapitres precedant la mort du personnage.

**Etat actuel (Ch. I-IV ecrits) :**

| Metier | Montre ? | Scene(s) |
|--------|----------|----------|
| Chef (#12, Senzo) | OUI | Ch. I-IV, multiples scenes |
| Cartographe (#7, Senzo) | OUI | Ch. II, IV |
| Seismo-auditeur (#8, Sihle) | OUI | Ch. I, II, IV |
| Meteorologue (#1, Sihle) | NON | A montrer Ch. V avant sa mort |
| Mineur (#4, Sihle) | PARTIEL | Ch. I (caissons). A renforcer. |
| Ocean (#2, Jabu) | OUI | Ch. III |
| Speleologue (#14, Jabu) | PARTIEL | Ch. II (batons chimiques). A renforcer. |
| Biologiste (#3, Enama) | OUI | Ch. II |
| Cuisiniere (#13, Enama) | OUI | Ch. I |
| Survivaliste (#10, Enama) | NON | A montrer Ch. V ou VI |
| Aeromaitre (#15, Thabo) | OUI | Ch. I, II, III, IV |
| Geologue (#6, Thabo) | NON | A montrer avant Ch. VII |
| Grimpeuse (#11, Inyoni) | OUI | Ch. I, II, IV |
| Explosiviste (#5, Inyoni) | NON | A montrer avant Ch. VII |
| Predictrice (#9, Nandi) | OUI | Ch. I, II, III, IV |
| Explosiviste backup (#5b, Nandi) | NON | A montrer avant Ch. VIII |

**Metiers non encore montres et devant l'etre :**
1. Meteorologue (Sihle) — dans Ch. V, avant sa mort
2. Survivaliste (Enama) — dans Ch. V ou debut Ch. VI
3. Geologue (Thabo) — dans Ch. V ou VI
4. Explosiviste (Inyoni) — dans Ch. V ou VI
5. Explosiviste backup (Nandi) — scene d'apprentissage dans Ch. V, VI ou VII

---

## V4 : Les assignations doivent etre coherentes entre fichiers

**Invariant :** Les metiers assignes dans SQUELETTE.md, METIERS.md, et le texte des chapitres doivent etre identiques.

**Verification :** Croiser les trois sources.

**Etat actuel :**

| Personnage | SQUELETTE.md | METIERS.md | Chapitres | Coherent ? |
|-----------|-------------|-----------|-----------|------------|
| Senzo | Chef, Cartographe | Leader + ? | Chef, Cartographe (implicite) | METIERS.md incomplet |
| Sihle | Seismo-auditeur, Meteo, Mineur | ? | Seismo-auditeur (explicite) | METIERS.md vide |
| Jabu | Ocean, Speleologue | Ocean (?), + ? | Ocean (explicite) | METIERS.md incomplet |
| Enama | Biologiste, Cuisiniere, Survivaliste | ? | Biologiste, Cuisiniere (explicite) | METIERS.md vide |
| Thabo | Aeromaitre, Geologue | Speleologue (?), + ? | Aeromaitre (explicite) | METIERS.md errone (dit Speleo) |
| Inyoni | Grimpeuse, Explosiviste | ? | Grimpeuse (explicite) | METIERS.md vide |
| Nandi | Predictrice, Explosiviste backup | Predictrice, + ? | Predictrice (explicite) | METIERS.md incomplet |

**Issue identifiee :** METIERS.md assigne "Speleologue (?)" a Thabo alors que SQUELETTE.md assigne Speleologue a Jabu et Geologue a Thabo. C'est une incoherence. SQUELETTE.md fait autorite.

---

## V5 : Le metier dedouble (#5 Explosiviste) respecte la hierarchie principal/backup

**Invariant :** Inyoni est toujours presentee comme l'explosiviste principale. Nandi est toujours le backup. Jamais l'inverse.

**Verification :** Dans toute scene impliquant les explosifs :
- Si Inyoni est vivante, c'est elle qui manipule la charge
- Nandi observe, apprend, assiste — elle ne manipule pas seule
- Apres la mort d'Inyoni (Ch. VII), Nandi prend le relais avec une hesitation visible

---

## V6 : L'ordre des morts respecte la gradation de degradation

**Invariant :** L'ordre des morts ne doit pas etre modifie sans recalculer l'ensemble de la cascade.

**Verification :** L'ordre est :
1. Senzo (Ch. IV) — perte de direction
2. Sihle + Jabu (Ch. V) — perte de perception instrumentale et de navigation
3. Enama (Ch. VI) — perte de survie
4. Thabo + Inyoni (Ch. VII) — perte de perception atmospherique et d'expertise mission
5. Nandi (Ch. VIII) — accomplissement et fin

Modifier cet ordre (par exemple, tuer Thabo avant Sihle) changerait la dramaturgie : l'air disparaitrait avant les instruments, ce qui inverserait la resolution du conflit raison/intuition.

---

## V7 : Le Contact reflete la perte de metiers

**Invariant :** Quand un metier meurt, le Contact perd non seulement l'idiolecte du personnage mais aussi le vocabulaire professionnel que son metier avait genere.

**Verification :** Apres chaque mort, verifier que :
- Les gestes specifiques au metier ne sont plus utilises par le groupe
- Si un autre personnage tente le geste, il est approximatif ou different
- Le Contact retrecit proportionnellement aux metiers perdus

**Exemples :**
- Apres Senzo : plus de consultation de carte (geste de derouler le tissu cartographique)
- Apres Sihle : plus de Contact technique au poignet pour demander des donnees
- Apres Thabo : plus de geste "l'air circule" (main a plat, mouvement lateral)

---

## V8 : La predictrice ne remplace personne

**Invariant :** Nandi ne "reprend" pas les metiers des morts. Elle reprend les gestes de Contact de Senzo (heritage linguistique), mais elle n'apprend pas la cartographie, la biologie, ou la geologie.

**Verification :** Nandi ne doit jamais etre montree en train d'exercer un metier qui n'est pas le sien (prediction, explosifs backup) — sauf dans l'approximation et l'erreur.

**Exception :** Le geste *On ne remonte pas* de Senzo est un emprunt linguistique, pas un metier. Nandi reprend le mot, pas la fonction.

---

## V9 : L'ironie geologique est respectee pour chaque mort

**Invariant :** Chaque personnage meurt par ou a travers l'element de son expertise.

**Verification :**

| Personnage | Expertise | Mort | Ironie | Verifie |
|-----------|----------|------|--------|---------|
| Senzo | Route, carte | Glissement de terrain | La route le tue | OUI (Ch. IV ecrit) |
| Sihle | Instruments, mesure | Chute dans le vide | Le vide = absence de donnees | A VERIFIER (Ch. V) |
| Jabu | Ocean, eau | Noyade | L'eau le tue | A VERIFIER (Ch. V) |
| Enama | Biologie, survie | Lave | Le vivant brulant la tue | A VERIFIER (Ch. VI) |
| Thabo | Air, roche | Ensevelissement | La roche ecrase, l'air disparait | A VERIFIER (Ch. VII) |
| Inyoni | Grimpe, explosifs | Ensevelissement | La montagne refuse qu'elle monte | A VERIFIER (Ch. VII) |
| Nandi | Prediction, explosifs | Detonation | Elle DEVIENT le seisme | A VERIFIER (Ch. VIII) |
