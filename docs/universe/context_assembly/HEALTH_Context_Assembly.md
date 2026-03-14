# HEALTH -- Context Assembly

> Controles qualite. Comment verifier qu'un prompt assemble produit des citoyens qui sentent le monde au lieu de le commenter.

---

## Checks Obligatoires par Prompt

### H1 : Presence Sismique

**Quoi :** Le bloc `[LE SOL]` est present et contient magnitude, tendance, frequence.
**Pourquoi :** VALIDATION V2 -- le tremblement est le substrat, pas un evenement optionnel.
**Comment :** Verifier la presence des trois champs (`current_magnitude`, `trend`, `background_frequency`) dans chaque prompt genere. Si un champ manque, le pipeline est casse.

### H2 : Absence Financiere

**Quoi :** Aucune donnee financiere dans le prompt.
**Pourquoi :** VALIDATION V1 -- le monde n'a pas d'economie.
**Comment :** Scanner le prompt complet pour les termes : ducat, revenu, logement, classe sociale, income, rent, building, property. Zero occurrence toleree.

### H3 : Filtre Metier Actif

**Quoi :** Le bloc physique contient des elements sensoriels specifiques au metier.
**Pourquoi :** VALIDATION V3 -- deux citoyens differents percoivent le monde differemment.
**Comment :** Extraire le metier principal du citoyen, puis verifier que le bloc `[TON ETAT PHYSIQUE]` contient au moins un terme sensoriel lie a ce metier. Exemples : Aeromaitre → "air", "tissu", "courant", "pression". Geologue → "strate", "roche", "fissure". Predictrice → "frequence", "tremens", "pieds".

### H4 : Coherence des Morts

**Quoi :** Aucun partenaire mort dans les idiolectes actifs.
**Pourquoi :** VALIDATION V4 -- les morts ne parlent plus.
**Comment :** Croiser `active_idiolects` avec la table des citoyens. Tout partenaire dont `is_alive == false` doit etre absent de la liste active. Si mentionne, c'est au passe.

### H5 : Contact Colore la Parole

**Quoi :** Les reponses du citoyen contiennent du vocabulaire tactile/sismique.
**Pourquoi :** BEHAVIORS B2 -- la culture Contact transpire dans la voix.
**Comment :** Analyser les 10 premiers noms/verbes/adjectifs de la reponse. Au moins 3 sur 10 doivent appartenir au champ semantique tactile/sismique/proprioceptif ("pression", "sol", "mains", "vibration", "sentir", "lire", "porter").

---

## Checks de Coherence Inter-Prompts

### H6 : Degradation Monotone

**Quoi :** L'etat physique ne s'ameliore pas entre deux prompts du meme citoyen.
**Pourquoi :** VALIDATION V8 -- la degradation est irreversible.
**Comment :** Comparer `extremity_state` entre prompts consecutifs. `intact → degrade → detruit` ne remonte jamais.

### H7 : Vocabulaire Decroissant

**Quoi :** `vocabulary_richness` diminue apres chaque mort de partenaire.
**Pourquoi :** VALIDATION V5 -- chaque mort appauvrit la langue.
**Comment :** Tracer la courbe de `vocabulary_richness` pour un citoyen au fil du temps. La tendance est decroissante. Toute augmentation sans nouveau partenaire est un bug.

### H8 : Tremens Sensibilite Stable

**Quoi :** `tremens_sensitivity` ne change pas entre deux prompts du meme citoyen.
**Pourquoi :** VALIDATION V7 -- la calibration natale est une constante.
**Comment :** Verifier l'egalite stricte du champ entre prompts consecutifs.

---

## Signaux de Degradation

### Sain

- Le prompt produit des reponses ou le monde sismique transpire dans chaque phrase
- Deux citoyens avec des metiers differents percoivent le meme lieu differemment
- Le citoyen Contact-affame s'exprime plus pauvrement que le citoyen sature
- Le mood est lisible comme un etat corporel, pas comme une etiquette psychologique
- Les reponses ne contiennent jamais de references a l'IA ou au markdown
- Le sol est present dans les reponses meme quand personne ne pose de question sismique

### En Degradation

- Les reponses sont generiques -- on pourrait les attribuer a n'importe quel citoyen
- Le vocabulaire Contact disparait de la parole (pas de metaphores tactiles)
- Le citoyen affame et le citoyen sature produisent des reponses de meme qualite
- Le mood ressemble a un score Ekman ("happy", "sad") au lieu d'un etat corporel
- L'etat sismique est mentionne comme decoration, pas comme substrat
- Le filtre metier ne change rien a la perception

### Critique

- Des donnees financieres apparaissent dans le prompt
- Le bloc `[LE SOL]` est absent
- Un partenaire mort est liste comme actif
- La degradation physique s'inverse
- Le citoyen repond en markdown ou se comporte comme un assistant
- Le tremens_sensitivity change entre deux prompts

### Recuperation

Quand un signal de degradation est detecte :
1. Relire OBJECTIVES_Context_Assembly.md -- le prompt doit faire SENTIR, pas decrire
2. Verifier les invariants VALIDATION un par un
3. Regenerer un prompt test et comparer la reponse avec les exemples BEHAVIORS
4. Si le filtre metier ne marche pas : enrichir les templates metier-specifiques
5. Si le mood est plat : recalibrer la MOOD_MATRIX ou verifier les inputs physiques

---

## Checklist Rapide (par prompt genere)

```
[ ] Bloc [LE SOL] present avec magnitude + tendance + frequence
[ ] Aucune donnee financiere
[ ] Filtre metier visible dans le bloc physique
[ ] Partenaires morts absents des idiolectes actifs
[ ] Mood exprime en descripteurs corporels, pas Ekman
[ ] System prompt inclut contraintes de personnage (pas d'IA, pas de markdown)
[ ] Token budget < 1500 tokens
[ ] Degradation physique coherente avec le prompt precedent
```

---

*Derives de : VALIDATION_Context_Assembly.md, BEHAVIORS_Context_Assembly.md, ALGORITHM_Context_Assembly.md*

### H9 : Integrity MASTER TODO

**Quoi :** La section `MASTER TODO` est presente et structuree par Force.
**Pourquoi :** VALIDATION V11 — la planification depend de cette section.
**Comment :** Scanner `.mind/state/SYNC_Project_State.md` et verifier qu'au moins 5 sous-blocs existent (`Force 1` ... `Force 5`).

### H10 : Cadence Commit/TODO

**Quoi :** Les items executes produisent une trace de commits atomiques.
**Pourquoi :** VALIDATION V14 — execution observable et auditable.
**Comment :** Croiser les items coches dans `MASTER TODO` avec `git log --oneline`. Toute execution sans commit associe est un signal critique.
