# PATTERNS -- Context Assembly

> Decisions de design. Pourquoi le prompt de Contre-Terre a cette forme et pas une autre.

---

## P1 : Contact-First Base Instruction

**Decision :** Le system prompt ouvre avec l'identite Contact du citoyen, pas avec son nom et sa classe.

**Pourquoi :** Dans Venezia, le system prompt commence par "You are {name}, a {social_class} citizen of Venice in the year 1525." Cette ouverture ancre l'identite dans le social. Contre-Terre n'a pas de classes sociales. L'identite est inscrite dans le corps : comment tu trembles, comment tu touches, ce que tu percois. Le system prompt doit ouvrir par les metiers (canaux de perception), le tremens (calibration natale), et l'idiolecte (signature tactile). Le nom vient apres -- le corps vient avant.

**Structure du system prompt :**
```
1. [QUI TU ES] -- nom, metiers comme filtres sensoriels, pas comme CV
2. [TON CORPS] -- tremens natal, pieds/mains, condition physique
3. [TA LANGUE] -- Contact : gestes universels + idiolecte personnel
4. [TON MONDE] -- le sol tremble toujours, le son ne porte pas, le toucher est le langage
5. [REGLES] -- 1-3 phrases, spatial audio, pas d'assistant, pas de markdown
```

**Consequence :** Le citoyen sait *ce qu'il sent* avant de savoir *a qui il parle*. Son identite sensorielle precede son identite sociale.

---

## P2 : Prompt Structure en 6 Blocs

**Decision :** Le context block (message user) suit 6 blocs au lieu des 7 de Venezia.

**Structure Venezia → Structure Contre-Terre :**

| Venezia | Contre-Terre | Difference |
|---------|-------------|------------|
| [YOUR STATE] mood + time + location | [TON ETAT PHYSIQUE] tremens + pieds + temperature + air | Mood physique, pas emotionnel |
| [YOUR FINANCES] ducats, income, buildings | [TON CONTACT RECENT] derniers gestes, partenaires, richesse idiolecte | Contact remplace finances |
| [THE PERSON IN FRONT OF YOU] trust score | [QUI TE TOUCHE] historique Contact avec cette personne | Le trust est Contact, pas numerique |
| [YOUR TRUSTED ALLIES] relationship list | [TES LIENS] partenaires Contact vivants, idiolectes de paire | Relations = vocabulaires partages |
| [WHAT IS ON YOUR MIND] beliefs + narratives | [CE QUE TU CROIS] croyances du graph + etat sismique | Croyances + seismique fusionnes |
| [HOW TO RESPOND] behavior constraints | [COMMENT REPONDRE] contraintes de Contact + registre du metier | Contact-aware constraints |
| [WHAT THEY JUST SAID] visitor speech | [CE QU'ILS T'ONT DIT] parole du visiteur | Identique |

**Pourquoi cette reorganisation :** L'etat physique est la fondation -- le tremblement des mains, la temperature du sol sous les pieds, l'air qui se rarefie. Le Contact recent est l'equivalent fonctionnel de l'economie : c'est la richesse du citoyen, sauf que cette richesse se mesure en gestes recus, pas en ducats. L'etat sismique n'est pas un evenement a part -- il est tisse dans l'etat physique. Le trust n'est pas un score numerique -- c'est un historique de Contact : combien de fois m'as-tu touche, avec quels gestes, dans quels registres ?

---

## P3 : Mood Triaxial (Tremens + Contact + Physique)

**Decision :** Le mood ne derive pas de l'economie (Venezia) mais de trois axes corporels.

**Axe 1 -- Tremens :** L'ecart entre la calibration natale du citoyen et la frequence sismique locale. Un citoyen de surface (calibre pour 0.1-0.3 Hz) plonge dans une zone a 2 Hz est en souffrance tremens -- nausee, desorientation, hallucinations. Un Predicteur comme Nandi est hypersensible : son tremens monte plus vite, mais elle peut aussi le lire.

**Axe 2 -- Contact :** La saturation Contact recente. Un citoyen touche regulierement avec des gestes riches (idiolectes de paire, registres varies) est Contact-sature -- calme, connecte, articule. Un citoyen isole (pas de Contact depuis longtemps) est Contact-affame -- anxieux, hyper-reactif, linguistiquement appauvri.

**Axe 3 -- Physique :** Temperature, qualite de l'air, etat des extremites (pieds, mains, peau). Des mains brulees par l'obsidienne reduisent la capacite Contact. Des pieds detruits ne lisent plus le sol. L'air rarefie cause la confusion. Ces conditions physiques sont le substrat sur lequel tremens et Contact operent.

**Combinaison :** Les trois axes se combinent pour produire un mood emergent :

| Tremens | Contact | Physique | Mood resultant |
|---------|---------|----------|---------------|
| Bas | Sature | Bon | Calme, presente, perceptive |
| Haut | Affame | Bon | Anxieux, hyper-alerte, instable |
| Bas | Affame | Degrade | Melancolique, replie, econome en gestes |
| Haut | Sature | Degrade | Resistant mais epuise, presque lucide |
| Haut | Affame | Degrade | Desespere, au bord du Contact-fantome |

Le mood n'est pas un label Ekman -- c'est un etat corporel que le LLM traduit en comportement.

---

## P4 : Le Metier Comme Filtre de Perception

**Decision :** Chaque metier injecte un vocabulaire sensoriel different dans le prompt.

**Pourquoi :** Deux citoyens dans la meme caverne ne percoivent pas la meme chose. L'Aeromaitre sent l'air se rarefier. Le Geologue lit les strates. La Predictrice sent la frequence monter dans ses pieds. La Grimpeuse compte les prises. Le prompt doit encoder cette perception filtree : pas "tu es dans une caverne" mais "l'air ici est plus lourd qu'il y a deux heures -- tu le sens dans la resistance du tissu quand tu le tends".

**Impact sur le prompt :**
- La section [TON ETAT PHYSIQUE] est ecrite DEPUIS le metier : un Meteorologue percoit la pression atmospherique, un Mineur percoit la densite de la roche.
- La section [CE QUE TU CROIS] est filtree par le metier : un Seismo-auditeur a des croyances fondees sur les courbes, une Predictrice a des croyances fondees sur le tremens.

---

## P5 : Le Contact Vocabulaire dans les Reponses

**Decision :** Le bloc [COMMENT REPONDRE] inclut des directives de vocabulaire Contact.

**Pourquoi :** Les citoyens de Contre-Terre interagissent par la voix dans Cities of Light (spatial audio), mais leur culture est tactile. Leurs phrases doivent porter cette empreinte. Le prompt inclut des exemples de transpositions : au lieu de "je suis inquiet", le citoyen pourrait dire quelque chose comme "le sol n'a pas arrete depuis l'aube, j'ai les mains qui cherchent un contact qui n'est pas la". Au lieu de "je ne te fais pas confiance", il pourrait dire "on ne s'est jamais touche l'epaule".

**Regles de registre vocale :**
- La voix dans Contre-Terre est rare et transgressive (VALIDATION V4 du Contact)
- Mais dans l'interface Cities of Light, les citoyens parlent aux visiteurs
- Resolution : le citoyen parle, mais avec le vocabulaire du Contact. Ses metaphores sont tactiles. Sa grammaire est spatiale. Il dit "pression", pas "stress". Il dit "le sol", pas "la situation".

---

## P6 : Relations = Historique Contact, Pas Score de Trust

**Decision :** Le trust entre deux personnes est derive de l'historique Contact partage, pas d'un nombre arbitraire.

**Pourquoi :** Venezia utilise un TrustScore (0-100) store dans un tableau de relations. Contre-Terre derive la confiance du Contact : combien de touches, dans quels registres (epaule = collectif, main = emotion, nuque = intime), avec quelle frequence, avec quelle richesse. Quelqu'un qui t'a touche la nuque est plus intime que quelqu'un qui t'a touche l'epaule 50 fois. La richesse n'est pas dans la quantite mais dans la profondeur des registres atteints.

**Impact sur le prompt :** La section [QUI TE TOUCHE] ne dit pas "Trust: 73/100". Elle dit : "Vous avez partage du Contact de main. Jamais la nuque. Ses gestes sont brefs -- il ne donne pas d'information, il verifie ta presence." Le LLM interprete cette description qualitative pour calibrer son comportement.

---

## P7 : Prompt Maitre Multi-Force avec Never-Stop

**Decision :** Les sessions Codex paralleles suivent un prompt maitre unique (template), avec une variable `Force [N]` injectee par l'orchestrateur.

**Pourquoi :** Le travail distribue en 5 Forces doit garder un protocole identique pour eviter la derive entre onglets. Un template canonique garantit que chaque instance suit le meme ordre de chargement de contexte, la meme logique de planification, et les memes regles d'execution. On remplace uniquement le numero de Force, pas la procedure.

**Structure imposee du prompt maitre :**
- **Phase 1 -- Context Cascade** : lecture sequentielle des manifestos, documents fondamentaux (`FRAMEWORK`, `SYSTEM`, `STYLE`, `PRINCIPLES`), doc chain module, puis `SYNC_Project_State.md`.
- **Phase 2 -- Planification** : extraction explicite des taches assignees a la Force depuis la section MASTER TODO, avec sortie en terminal sous marqueur `@mind:TODO`.
- **Phase 3 -- Execution** : boucle tache par tache (skill/agent approprie, execution, verification, commit), puis iteration jusqu'a zero tache.

**Règle critique : Never-Stop Protocol**
- En cas d'ambiguite ou de blocage, l'agent n'attend pas.
- Il emet `@mind:escalation`, puis immediatement `@mind:proposition`.
- Il applique sa proposition sans pause pour maintenir le flux de livraison.

**Consequence :** L'orchestration devient observable et cadencee : chaque Force avance en continu, declare ses hypotheses explicitement, et laisse une trace granulaire via commits intermediaires.

**Canon operationnel associe :**
- Template canonique stocke dans `.mind/docs/PROMPT_MAITRE_5_FORCE_SPRINT.md`
- Checklist d'execution stockee dans `.mind/docs/FORCE_EXECUTION_CHECKLIST.md`
- Les taches d'orchestration vivent dans `MASTER TODO` de `.mind/state/SYNC_Project_State.md`

---

*Decisions tracables dans : `poc_mind_context_assembly.py` (Venezia), `OBJECTIVES_Context_Assembly.md`, `CONTACT.md`, `METIERS.md`, `.mind/docs/PROMPT_MAITRE_5_FORCE_SPRINT.md`*
