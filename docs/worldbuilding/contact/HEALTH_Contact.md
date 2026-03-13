# HEALTH — Le Contact

> Controles qualite. Comment verifier la coherence du Contact a travers les chapitres.

---

## Checks Obligatoires Avant Publication d'un Chapitre

### H1 : Comptage des Gestes

**Quoi :** Lister tous les gestes de Contact dans le chapitre.
**Pourquoi :** Detecter les incoherences (zone du corps ≠ registre, geste modifie sans raison).
**Comment :** Pour chaque geste, noter : qui → qui, zone du corps, type, signification, coherent avec ALGORITHM ?

### H2 : Registre des Idiolectes Actifs

**Quoi :** Verifier que seuls les personnages vivants utilisent leurs gestes propres.
**Pourquoi :** Apres une mort, les gestes du mort ne doivent plus apparaitre naturellement.
**Comment :** Croiser la liste des gestes du chapitre avec la table des morts. Signaler toute occurrence d'un geste d'un personnage mort qui n'est pas marquee comme heritage ou absence.

### H3 : Nombre de Survivants

**Quoi :** Le nombre de personnages est exact dans chaque scene.
**Pourquoi :** Bug narratif critique si le nombre est faux.
**Comment :** A chaque changement de scene, compter les personnages nommes ou impliques. Comparer avec la table VALIDATION V7.

### H4 : Pieds de Nandi

**Quoi :** Nandi est pieds nus, ou son etat de pieds est mentionne.
**Pourquoi :** Invariant V13. Ses pieds sont son instrument de prediction.
**Comment :** Chercher toute scene avec Nandi en mouvement. Verifier.

### H5 : Voix = Transgression

**Quoi :** Toute parole vocale est marquee comme evenement.
**Pourquoi :** Invariant V4.
**Comment :** Chercher les dialogues en tirets ou guillemets. Verifier la reaction des personnages.

---

## Checks de Coherence Inter-Chapitres

### H6 : Progression de la Degradation

**Quoi :** Le Contact du chapitre N est moins riche que le Contact du chapitre N-1 (apres Ch. IV).
**Pourquoi :** L'arc est une contraction. Invariant V15.
**Comment :** Comparer la diversite des gestes (nombre de types differents) entre chapitres successifs. La tendance doit etre decroissante.

**Metriques possibles :**
- Nombre de zones du corps utilisees dans le chapitre
- Nombre de locuteurs Contact distincts
- Nombre de gestes uniques (premiere occurrence)
- Ratio gestes "standards" vs gestes "propres" (les gestes propres diminuent)

### H7 : Continuite du Geste Inconnu

**Quoi :** Le geste de la vieille femme est mentionne ou ressenti par Nandi a intervalles reguliers.
**Pourquoi :** Fil rouge. Ne doit pas disparaitre du texte entre Ch. III et Ch. VIII.
**Comment :** Au moins une reference par chapitre (meme breve — "ses mains portaient encore le mot du village").

### H8 : Coherence des Dialectes Senzo-Nandi

**Quoi :** Apres la mort de Senzo, les gestes de leur dialecte prive ne sont plus utilises normalement.
**Pourquoi :** V2 — idiolecte mort avec le locuteur.
**Comment :** Lister les gestes du dialecte Senzo-Nandi (nuque, pressions specifiques). Verifier qu'ils n'apparaissent plus apres Ch. IV sauf en tant que manque, souvenir ou Contact-fantome.

### H9 : Le Contact-Corde Evolue

**Quoi :** Si des scenes de corde apparaissent apres Ch. IV, le vocabulaire-corde doit etre coherent avec celui invente au Ch. IV (et peut s'enrichir).
**Pourquoi :** Coherence interne du sous-systeme.
**Comment :** Croiser le vocabulaire-corde avec la table d'ALGORITHM.

---

## Signaux de Degradation (dans le processus d'ecriture)

### Sain

- Le Contact porte l'emotion des scenes — les moments forts passent par le toucher
- Le lecteur peut deviner le sens des gestes par le contexte
- Chaque mort change visiblement la texture du Contact dans le texte
- Les invariants VALIDATION sont respectes
- Les variantes du Contact emergent naturellement de l'environnement
- Le geste inconnu reste present en filigrane

### En Degradation

- Le Contact devient decoratif (ajoute apres coup, pas structurant)
- Des gestes contradictoires apparaissent (meme geste, sens differents sans raison)
- Un personnage mort continue d'etre "present" dans le Contact sans que ce soit marque
- Le Contact ne change pas entre les chapitres (stagnation)
- La voix est utilisee sans etre marquee comme transgression
- Le geste inconnu disparait du texte pendant plus d'un chapitre
- Le Contact-corde est utilise pour transmettre des emotions complexes (depasse ses limites)

### Critique

- Le Contact est explique au lecteur par exposition
- Le nombre de survivants est faux
- Un geste central change de signification sans justification
- Le chapitre VIII n'inclut pas le geste inconnu
- Nandi est chaussee sans raison narrative
- Le Contact du Ch. VIII est plus riche que celui du Ch. I

### Recuperation

Quand un signal de degradation est detecte :
1. Revenir aux fichiers source (CONTACT.md, ALGORITHM)
2. Relire le dernier chapitre ecrit pour re-ancrer le style
3. Verifier les invariants VALIDATION un par un
4. Si le probleme est un geste contradictoire : choisir une version et corriger l'autre
5. Si le probleme est une stagnation : relire BEHAVIORS B3 (courbe de degradation)

---

## Checklist Rapide (a utiliser avant chaque chapitre)

```
[ ] Nombre de survivants correct
[ ] Pieds de Nandi nus ou mentionnes
[ ] Aucune exposition didactique du Contact
[ ] Gestes des morts absents ou marques comme manque
[ ] Au moins 1 reference au geste inconnu (Ch. IV–VII)
[ ] Voix = transgression si utilisee
[ ] Contact moins riche qu'au chapitre precedent (apres Ch. IV)
[ ] Zones du corps coherentes avec les registres
[ ] Le Contact porte au moins 1 scene emotionnelle cle
```

---

*Derives de : VALIDATION_Contact.md, BEHAVIORS_Contact.md, chapitres I–IV*
