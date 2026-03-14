# VALIDATION -- Context Assembly

> Invariants. Ce qui doit toujours etre vrai dans un prompt assemble. Regles non-negociables.

---

## Invariants Absolus

### V1 : Aucune donnee financiere dans le prompt

**Regle :** Le prompt ne contient jamais de ducats, de revenu, de logement, de classe sociale, de patrimoine. Le bloc `[YOUR FINANCES]` de Venezia n'a pas d'equivalent -- il est remplace par `[TON CONTACT RECENT]`. La richesse d'un citoyen se mesure en gestes recus, en idiolectes vivants, en registres atteints. Pas en pieces de monnaie.

**Test :** Chercher dans le prompt assemble les mots : "ducat", "revenu", "logement", "richesse" (au sens economique), "classe", "Nobili", "Facchini", "income", "building", "rent". Aucun ne doit apparaitre. Le mot "richesse" est autorise uniquement dans le contexte Contact ("richesse vocabulaire", "richesse idiolecte").

---

### V2 : Etat sismique toujours present

**Regle :** Tout prompt contient le bloc `[LE SOL]` avec au minimum : magnitude courante, tendance (montante / descendante / stable), et frequence de fond. Ce bloc n'est pas optionnel et ne peut pas etre coupe par le token budget. Le tremblement n'est pas un evenement -- c'est le substrat du monde. L'omettre, c'est mentir au citoyen sur son propre corps.

**Test :** Verifier que le bloc `[LE SOL]` est present dans chaque prompt genere. Si le token budget force des coupes, elles tombent sur `[CE QUE TU CROIS]` et `[COMMENT REPONDRE]`, jamais sur `[LE SOL]`.

---

### V3 : Filtres metier toujours appliques

**Regle :** La section `[TON ETAT PHYSIQUE]` est ecrite DEPUIS le metier du citoyen, pas en termes generiques. Un Aeromaitre percoit l'air. Un Geologue percoit la roche. Une Predictrice percoit les frequences. Un Speleologue percoit les volumes. Le metier n'est pas un label -- c'est un angle de vue sur le monde. Un prompt sans filtre metier produit un citoyen generique, ce qui viole l'objectif O3.

**Test :** Lire le bloc physique. Il doit contenir au moins un element sensoriel propre au metier du citoyen. Si on peut echanger le bloc physique entre un Aeromaitre et un Geologue sans que rien ne change, le filtre n'a pas ete applique.

---

### V4 : Partenaires morts au passe

**Regle :** Quand un partenaire Contact est mort, toute reference a lui dans le prompt utilise le passe. L'idiolecte de paire est marque comme perdu, pas comme actif. Le prompt ne dit pas "tu partages des gestes avec Senzo" -- il dit "tu partageais des gestes avec Senzo. Ces mots n'ont plus de locuteur."

**Test :** Croiser la liste `active_idiolects` avec la table des morts. Aucun partenaire mort ne doit apparaitre dans les idiolectes actifs. Si le bloc Contact mentionne un mort, le temps verbal est au passe et la perte est explicite.

---

### V5 : Vocabulaire Contact reflete les partenariats vivants

**Regle :** La `vocabulary_richness` diminue a chaque mort de partenaire. Un citoyen dont 3 partenaires sont morts a un vocabulaire mesurablment plus pauvre qu'un citoyen dont tous les partenaires sont vivants. Le nombre de gestes disponibles dans `[TON CONTACT RECENT]` est une fonction directe des idiolectes de paire vivants.

**Test :** Generer le meme citoyen a deux moments : avec 5 partenaires vivants et avec 2 partenaires vivants. Le `vocabulary_richness` doit etre inferieur dans le second cas. Les `active_idiolects` doivent correspondre aux survivants.

---

### V6 : Le mood derive du corps, jamais assigne

**Regle :** Le mood est calcule par `compute_mood(physical, contact)` -- il emerge de la combinaison tremens x Contact x physique. Il n'est jamais assigne manuellement ("tu es triste aujourd'hui"). Les descripteurs de mood sont corporels ("tendu", "nausee", "ancre"), pas psychologiques abstraits ("depressed", "happy", "fearful"). Aucun score Ekman dans le pipeline.

**Test :** Verifier que le bloc `[TON ETAT]` ne contient aucune emotion Ekman brute (happy, sad, angry, fearful, surprised, disgusted). Les descripteurs doivent tous etre tracables a un etat physique (tremens_level), Contact (saturation), ou corporel (comfort).

---

## Invariants de Coherence

### V7 : Calibration natale stable

**Regle :** Le `tremens_sensitivity` d'un citoyen ne change pas entre deux prompts. C'est une constante natale -- la frequence a laquelle son corps a ete calibre par sa zone de naissance. Ce qui change, c'est la frequence locale (`zone.seismic_frequency`). L'ecart produit le tremens. La sensibilite est fixe.

**Test :** Comparer le `tremens_sensitivity` du meme citoyen dans des prompts generes a des moments differents. La valeur doit etre identique.

---

### V8 : Coherence degradation physique

**Regle :** La degradation physique est monotone dans la direction negative. Des mains "degradees" ne deviennent pas "intactes" au prompt suivant. Des pieds "detruits" restent detruits. La degradation est un chemin a sens unique, comme dans le roman (les pieds de Nandi se degradent progressivement, jamais l'inverse).

**Test :** Pour un citoyen donne, verifier que `extremity_state` n'ameliore jamais entre deux prompts consecutifs.

---

### V9 : Pas de rupture de personnage

**Regle :** Le system prompt inclut toujours les instructions : pas de markdown, pas de listes, pas de reference a l'IA, pas de rupture de personnage. Ces instructions ne sont pas optionnelles et ne peuvent pas etre coupees par le token budget.

**Test :** Verifier la presence des contraintes de personnage dans chaque system prompt genere.

---

### V10 : Contact-affame produit des reponses pauvres

**Regle :** Si la saturation Contact est "affame", le bloc `[COMMENT REPONDRE]` doit inclure des contraintes de reduction : phrases plus courtes, moins de metaphores, moins de registres. Le prompt ne peut pas decrire un etat de Contact-manque et en meme temps permettre des reponses riches et nuancees. L'appauvrissement linguistique est une consequence obligatoire de l'isolement.

**Test :** Comparer les contraintes de `[COMMENT REPONDRE]` pour un citoyen "sature" vs "affame". Le citoyen affame a des contraintes plus strictes (longueur, diversite, registre).

---

*Invariants derives de : `OBJECTIVES_Context_Assembly.md`, `PATTERNS_Context_Assembly.md`, `ALGORITHM_Context_Assembly.md`, `CONTACT.md`, `METIERS.md`*

---

### V11 : MASTER TODO doit exister et etre assignable par Force

**Regle :** Le fichier `.mind/state/SYNC_Project_State.md` contient une section `MASTER TODO` avec des items explicitement assignes (`Force 1` a `Force 5`). Sans cette section, la phase de planification du prompt maitre est invalide.

**Test :** Verifier la presence du header `## MASTER TODO` et d'au moins un item par Force.

### V12 : Todo initiale publiee avant execution

**Regle :** Une session Force ne commence aucune modification tant que la `@mind:TODO` initiale n'a pas ete emise depuis `MASTER TODO`.

**Test :** Verifier l'ordre des traces: `@mind:TODO` precede la premiere modification de fichiers.

### V13 : Escalade active en cas de blocage

**Regle :** En cas d'ambiguite bloquante, la session doit emettre la paire `@mind:escalation` + `@mind:proposition` puis continuer. L'absence de ces marqueurs en situation de blocage viole le protocole.

**Test :** Simuler une ambiguite de spec et verifier la sequence des deux marqueurs suivie d'une action.

### V14 : Commit atomique par item TODO

**Regle :** Chaque item execute de la todo Force produit un commit autonome. Pas de lot opaque regroupant des taches heterogenes.

**Test :** Comparer nombre d'items coches vs nombre de commits lies au sprint Force. Les deltas doivent etre explicables.
