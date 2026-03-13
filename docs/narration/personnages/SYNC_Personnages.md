# SYNC : Personnages

**Module :** `narration/personnages`
**Derniere mise a jour :** 2026-03-11
**Mis a jour par :** Claude (agent, voice)

---

## Etat courant

La documentation du module `narration/personnages` vient d'etre creee (2026-03-11). Elle couvre les 7 personnages du roman Contre-Terre a travers 8 documents : OBJECTIVES, PATTERNS, BEHAVIORS, ALGORITHM, VALIDATION, IMPLEMENTATION, HEALTH, SYNC.

---

## Maturite

**STATUS : DESIGNING**

### Ce qui est canonique (v1)

- **Structure des 7 personnages** : noms, metiers, ordre de mort, elements — figes
- **Gestes-signatures** : documentes a partir des 4 chapitres ecrits — stables
- **Cascade de competences** : 15 metiers / 7 personnes — figee
- **Dynamiques de paires** : Senzo-Nandi, Sihle-Enama, Thabo-Inyoni — etablies
- **Mecanique de la mort linguistique** : un mort = un idiolecte perdu — principe actif
- **4 premiers chapitres** : les comportements des 7 personnages y sont etablis et coherents

### Ce qui est en cours de design

- **Idiolectes de paire** : chaque duo a un vocabulaire Contact distinct — esquisse mais pas systematise
- **Chapitres V-VIII** : non ecrits. Les comportements des personnages dans ces chapitres sont planifies (SQUELETTE.md) mais pas encore incarnes en prose
- **Arc de Nandi Ch. V-VIII** : la progression fragile → leader → detonatrice est planifiee mais pas ecrite
- **Le geste inconnu** : transmis par la vieille femme (Ch. III), doit trouver son sens au Ch. VIII — non resolu

### Ce qui est propose (v2 / futur)

- Systematiser tous les idiolectes de paire (21 paires possibles, 5 actives)
- Developper le Contact-fantome de Nandi (Ch. VIII)
- Explorer le post-mortem de chaque idiolecte (comment les survivants compensent)

---

## Etat par personnage

### Senzo (mort Ch. IV)

| Dimension | Statut | Notes |
|-----------|--------|-------|
| Fiche personnage | COMPLET | PERSONNAGES.md + BEHAVIORS documentees des 4 chapitres |
| Geste-signature | COMPLET | Regarde/marche, nuque Nandi, poing ouvert, arc descendant, 3eme option |
| Idiolecte Contact | COMPLET | Paume entiere, lent, intime/commandement |
| Arc narratif | COMPLET | Chef stable → decide → meurt en protegeant. 4 chapitres. |
| Scene de mort | ECRITE | Ch. IV, Sc. 5. Glissement, tire la corde, mur tombe. Puissant. |
| Inventaire du manque | ECRIT | Ch. IV, Sc. 6. Idiolecte perdu, metiers perdus, cercle de deuil. |

### Nandi (meurt Ch. VIII, derniere)

| Dimension | Statut | Notes |
|-----------|--------|-------|
| Fiche personnage | COMPLET | La plus documentee. Presente dans chaque chapitre. |
| Geste-signature | COMPLET | Pieds nus, tremens, vomit, main au sol |
| Idiolecte Contact | COMPLET | Variable (doux/grip total), suit le tremens, sol/poignet |
| Arc narratif Ch. I-IV | ECRIT | Fragile → predictrice → reprend le geste de Senzo |
| Arc narratif Ch. V-VIII | PLANIFIE | Leader par defaut → sent mag.11 → seule → detone |
| Geste inconnu | EN COURS | Recu Ch. III. Sens prevu pour Ch. VIII. Non resolu. |
| Scene de mort | A ECRIRE | Ch. VIII. Detonation. Derniere. Contact avec la Terre. |

### Enama (meurt Ch. VI)

| Dimension | Statut | Notes |
|-----------|--------|-------|
| Fiche personnage | COMPLET | Conflit avec Sihle, biologie, racines, intuition |
| Geste-signature | COMPLET | Mains au sol, racines, Contact-monde, parle a voix haute |
| Idiolecte Contact | BON | Grip fort, rapide, urgence. Le Contact-monde (main sur roche) est unique. |
| Arc narratif Ch. I-IV | ECRIT | Antagoniste de Sihle → pas d'avis pour la premiere fois (Ch. IV) |
| Arc narratif Ch. V-VI | PLANIFIE | Cause mort Sihle → culpabilite → sacrifice dans la lave. Invente dernier geste. |
| Scene de mort | A ECRIRE | Ch. VI. Sacrifice volontaire. Geste nouveau invente a la mort. |

### Sihle (meurt Ch. V)

| Dimension | Statut | Notes |
|-----------|--------|-------|
| Fiche personnage | COMPLET | Rationnel, donnees, sismographe, antagoniste d'Enama |
| Geste-signature | COMPLET | Sismographe, yeux fermes, 2 doigts avant-bras, notes marge |
| Idiolecte Contact | COMPLET | Technique, froid, minimal. 2 doigts. |
| Arc narratif Ch. I-IV | ECRIT | Conflit avec Enama → doute au village → ignore par Senzo → s'assoit sans toucher |
| Arc narratif Ch. V | PLANIFIE | Conflit explose → separation du groupe → tombe. Main d'Enama lache. |
| Scene de mort | A ECRIRE | Ch. V. Chute causee par Enama. Contact ultime entre antagonistes. |

### Thabo (meurt Ch. VII)

| Dimension | Statut | Notes |
|-----------|--------|-------|
| Fiche personnage | BON | Aeromaître, tissu, methodique. Moins developpe que les 4 principaux. |
| Geste-signature | COMPLET | Tissu, froncement = "Je note", plie en rituel |
| Idiolecte Contact | PARTIEL | Contact indirect via tissu. Peu de Contact direct documente. |
| Arc narratif Ch. I-IV | ECRIT | Competent, fiable, discret. Le vieux souffle sur son tissu. |
| Arc narratif Ch. V-VII | PLANIFIE | Detecte baisse O2 (Ch. V), gaz toxiques (Ch. VI), boyau (Ch. VII) |
| Scene de mort | A ECRIRE | Ch. VII. Enseveli avec Inyoni. Contact survit entre eux. |
| **Alerte** | ATTENTION | Peu de scenes de premier plan. A renforcer dans Ch. V-VII. |

### Inyoni (meurt Ch. VII)

| Dimension | Statut | Notes |
|-----------|--------|-------|
| Fiche personnage | BON | Grimpeuse, explosifs, compte, "Tient.", Contact-corde |
| Geste-signature | COMPLET | Compte, serre, "Tient.", noeuds, corde |
| Idiolecte Contact | BON | Corde comme medium. Grip permanent. Decompte-priere. |
| Arc narratif Ch. I-IV | ECRIT | Sangles → Contact-corde inventé (Ch. IV) → 47 fibres |
| Arc narratif Ch. V-VII | PLANIFIE | Boyau (Ch. VII), mort partagee avec Thabo |
| Scene de mort | A ECRIRE | Ch. VII. Ensevelie avec Thabo. Derniere mort a deux. |

### Jabu (meurt Ch. V)

| Dimension | Statut | Notes |
|-----------|--------|-------|
| Fiche personnage | MINIMAL | Le moins developpe. Delibere mais a risque. |
| Geste-signature | BON | Hamacs, seul, ne se plaint pas, gourdes |
| Idiolecte Contact | FAIBLE | Peu de Contact documente. Position isolee. |
| Arc narratif Ch. I-IV | ECRIT | Efface, discret, seul. Prepare la mort solitaire. |
| Arc narratif Ch. V | PLANIFIE | Suit le groupe eau → noyade apres separation |
| Scene de mort | A ECRIRE | Ch. V. Noyade. Le specialiste de l'eau meurt par l'eau. |
| **Alerte** | ATTENTION | Risque de mort sans impact si Ch. V ne donne pas une scene forte. |

---

## Tensions ouvertes

| Tension | Statut | Chapitres | Notes |
|---------|--------|-----------|-------|
| Sihle vs Enama | ACTIVE | I-V (V = resolution) | Se resout par la mort de Sihle et la culpabilite d'Enama |
| Le geste inconnu de la vieille femme | OUVERTE | III → VIII | Nandi le porte. Sens non defini. L'auteur doit trancher. |
| Qui mene apres Senzo ? | RESOLUE implicitement | V-VIII | Personne. Le volcan mene. |
| Contact-fantome de Nandi | A ECRIRE | VIII | Hallucinations des mains des morts |
| Idiolectes de paire non systematises | OUVERTE | — | 21 paires possibles, ~5 actives. A approfondir ? |
| Assignations metiers METIERS.md | MINEURE | — | SQUELETTE.md est plus complet, METIERS.md a des "?" |

---

## Actions a venir

| Priorite | Action | Agent suggeré |
|----------|--------|---------------|
| 1 | Ecrire Ch. V (morts Sihle + Jabu) | groundwork |
| 2 | Renforcer presence de Thabo dans Ch. V-VI avant sa mort | groundwork |
| 3 | Donner a Jabu une scene forte en Ch. V avant sa noyade | groundwork |
| 4 | Resoudre le sens du geste inconnu de la vieille femme | voix ou architecte |
| 5 | Systematiser les idiolectes de paire | voice |
| 6 | Aligner METIERS.md avec SQUELETTE.md | steward |

---

## Handoff

**Pour l'agent suivant (groundwork) :** Les 4 premiers chapitres sont ecrits et les personnages y sont solidement etablis. Pour ecrire le Ch. V, s'appuyer sur SQUELETTE.md (plan detaille) et BEHAVIORS (gestes-signatures a maintenir). Points critiques : la scene de mort de Sihle doit inclure le Contact ultime Enama-Sihle (main qui saisit puis lache), la scene de mort de Jabu doit avoir un impact malgre son effacement, et les inventaires du manque (idiolectes perdus, metiers perdus) doivent suivre chaque mort.

**Pour l'humain (Nicolas) :** La doc chain personnages est en place. Les alertes principales sont : Jabu et Thabo ont peu de presence de premier plan dans les chapitres ecrits — il faut les renforcer avant leurs morts respectives. Le geste inconnu de la vieille femme (Ch. III) attend une decision sur son sens au Ch. VIII. Les idiolectes de paire (vocabulaire Contact unique entre chaque duo de personnages) sont esquisses mais pas systematises — c'est une question ouverte : faut-il les developper formellement ou les laisser emerger de l'ecriture ?
