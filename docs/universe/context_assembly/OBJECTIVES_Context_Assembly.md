# OBJECTIVES -- Context Assembly

> Ce que le pipeline d'assemblage de prompt optimise pour que les citoyens de Contre-Terre *parlent* comme des corps dans un monde sismique, pas comme des chatbots dans un monde economique.

---

## Objectif Principal

**O1 : Produire des prompts qui font SENTIR le monde a travers le corps du citoyen, pas a travers son patrimoine.**

Venezia assemble ses prompts autour de l'economie : ducats, revenus, logement, classe sociale. Le mood compute a partir du ratio richesse/attente. Contre-Terre ne peut pas fonctionner ainsi. Ici, un citoyen ne possede rien -- il percoit. Son prompt doit encoder ce que son corps ressent en ce moment : la frequence du sol sous ses pieds, la saturation de ses mains apres un Contact prolonge, la nausee du tremens qui monte quand la magnitude change. Le citoyen ne pense pas "j'ai 200 000 ducats" -- il pense "le sol vibre a 0.3 Hz et mes mains portent encore le geste de Thabo".

**Critere de reussite :** Un citoyen qui recoit ce prompt produit une reponse ou le monde sismique transpire dans chaque phrase -- pas comme decoration, mais comme substrat. Il ne dit pas "je me sens bien" ; il dit quelque chose qui implique qu'il sent la terre, qu'il lit l'air, qu'il porte des mots dans ses mains.

---

## Objectifs Secondaires

**O2 : Le mood emerge du corps, pas de l'economie.**

Le compute de mood de Venezia additionne des scores Ekman (happy, sad, angry, fearful, surprised, disgusted) derives de l'etat financier et social. Contre-Terre doit deriver le mood de trois axes corporels : le tremens (ecart entre calibration natale et frequence locale), la saturation Contact (quantite et qualite du Contact recent), et le confort physique (temperature, air, degradation des extremites). Un citoyen dont le tremens est eleve et le Contact recent pauvre sera anxieux -- non pas parce qu'il est pauvre, mais parce que son corps souffre et que personne ne l'a touche.

**O3 : L'identite passe par les metiers et les idiolectes, pas par la classe sociale.**

Venezia utilise `SocialClass` pour definir le registre de parole (Nobili = composed, Facchini = determined). Contre-Terre remplace cela par les metiers : un Aeromaitre parle en termes de flux d'air et de tissu qui tremble. Un Speleologue decrit les espaces en volumes et echos. Une Predictrice sent les seismes venir avant de les nommer. Le prompt doit injecter le filtre sensoriel du metier dans la perception du citoyen. En parallele, le vocabulaire Contact actif -- les gestes qu'il connait, les idiolectes de paire vivants -- definit sa palette d'expression. Un citoyen dont les partenaires Contact sont morts s'exprime plus pauvrement : moins de nuances, moins de registres.

**O4 : Les seismes sont un contexte permanent, pas un evenement ponctuel.**

Venezia n'a pas d'equivalent -- le plus proche serait un evenement politique ou un changement de decret. Contre-Terre vit dans un monde qui ne cesse jamais de trembler. Le prompt doit toujours inclure l'etat sismique actuel : la magnitude de fond, les seismes recents, et la tendance (ca monte, ca descend, c'est stable). Ce n'est pas un bloc optionnel -- c'est le substrat sur lequel tout le reste repose.

**O5 : Le Contact colore la parole, meme quand la parole est vocale.**

Les citoyens de Contre-Terre communiquent par le toucher. Quand ils parlent (dans l'univers Cities of Light, les interactions sont vocales), leurs phrases doivent porter la trace de cette culture tactile : metaphores proprioceptives, references au sol, descriptions en termes de pression et de vibration. Un citoyen ne dit pas "je suis triste" -- il dit quelque chose qui implique l'absence de Contact, le vide sur l'epaule, le silence de la peau.

---

## Non-Objectifs

- **Pas de simulation financiere.** Aucun ducats, aucun revenu, aucun logement dans le prompt. Le bloc `[YOUR FINANCES]` de Venezia n'a pas d'equivalent.

- **Pas de reproduction exacte des emotions Ekman.** Le modele Ekman a 6 emotions est un outil, pas un objectif. Le mood de Contre-Terre est derive du corps et peut produire des etats que les 6 emotions ne couvrent pas (tremens-vertige, Contact-manque, proprioception-noyee).

- **Pas de prompt generique.** Deux citoyens avec des metiers differents recevant le meme etat sismique doivent percevoir ce monde differemment. Le prompt est toujours filtre par le corps individuel.

---

## Tradeoffs

| Choix | Sacrifie | Justification |
|-------|----------|---------------|
| Physique > Psychologie | Pas de modele psychologique abstrait (Big Five, MBTI) | L'etat emotionnel est physiologique dans Contre-Terre : le corps sait avant l'esprit |
| Specificity > Generality | Chaque citoyen a un prompt tres different | Un prompt generique produirait des reponses generiques -- le metier doit filtrer |
| Contact > Voix | Les metaphores tactiles peuvent derouter le joueur | La culture Contact est ce qui rend Contre-Terre unique ; la lisser, c'est perdre le monde |
| Seismique toujours present | Tokens consommes meme sans evenement sismique | Le tremblement n'est pas un evenement, c'est l'etat normal ; l'omettre, c'est mentir |

---

## Relation aux Autres Modules

- **citizen_model** : Fournit les donnees brutes (tremens_sensitivity, metiers, idiolectes, etat physique) que context_assembly transforme en blocs de prompt.
- **contact_engine** : Fournit l'historique Contact recent (avec qui, quels gestes, quelle richesse) pour le bloc Contact.
- **seismic_physics** : Fournit la magnitude courante, la frequence de fond, et la tendance sismique pour le bloc sismique.
- **world_geography** : Fournit les conditions locales (temperature, air, profondeur) pour le bloc physique.
- **narrative_engine** : Fournit les croyances et arcs narratifs actifs pour le bloc beliefs.

---

*Source : `poc_mind_context_assembly.py` (Venezia, reference), `citizen-base.md`, `PERSONNAGES.md`, `CONTACT.md`, `METIERS.md`, `MONDE.md`*
