# PATTERNS — Experience Design

> Décisions de design. Pourquoi cette forme. Pourquoi pas autrement.

---

## P1 : Social Survival, pas Action RPG

**Décision :** Contre-Terre est un jeu de survie sociale. Le danger vient de la terre, pas des ennemis. La victoire vient de la coopération, pas du combat. Les compétences sont des perceptions (métiers), pas des pouvoirs.

**Pourquoi pas Action RPG :** Blood Ledger (4e univers) est l'univers action/stratégie — épées, châteaux, domination. Contre-Terre se différencie par le registre : ici, la difficulté n'est pas de tuer mais de survivre ensemble. Le drame vient de la perte de coéquipiers (Contact qui meurt, métiers qui disparaissent), pas de la défaite en combat.

**Comparaison :**

| Aspect | Blood Ledger | Contre-Terre |
|--------|-------------|--------------|
| Danger | Ennemis humains/IA | La terre elle-même |
| Victoire | Domination | Sacrifice collectif |
| Compétences | Combat, stratégie | Perception, survie |
| Mort | Défaite | Perte linguistique et sensorielle |
| Tone | Épique-héroïque | Intime-tragique |

---

## P2 : L'aventure du livre comme game loop

**Décision :** Chaque "partie" est une descente dans le volcan — une version procédurale de l'aventure du roman. L'équipe part de la surface, traverse les zones, et essaie d'atteindre la grotte finale pour déclencher la magnitude 11 contrôlée.

**Game loop :**
1. **Surface** — Le joueur arrive, explore l'archipel, rencontre des citoyens IA, choisit ses métiers, rejoint/forme une équipe
2. **Préparation** — L'équipe achète l'équipement chez les marchands, vérifie les métiers couverts, planifie la descente
3. **Descente** — Zone par zone, la physique s'intensifie. Les séismes arrivent. Le Contact se développe entre les membres. Les morts commencent.
4. **Profondeur** — L'équipe réduite doit décider : continuer ou remonter (si c'est encore possible). Les métiers perdus changent ce qu'on peut percevoir.
5. **Grotte finale** — Si quelqu'un arrive jusque-là. Activation de la Charge. Sacrifice. Le monde est sauvé (ou pas, si personne n'arrive).

**Pourquoi le livre :** L'aventure du roman a une structure narrative prouvée — montée progressive, deuil cumulatif, sacrifice final. Chaque descente la rejoue avec des variables différentes (autres IA, autres morts, autres chemins).

**Durée estimée :** 3-8 heures par descente. Pas un jeu qu'on lance 10 minutes — c'est un engagement, comme une expédition.

---

## P3 : Spawn dynamique — le monde n'attend pas

**Décision :** Si un joueur arrive quand toutes les équipes sont déjà parties, le monde ne le laisse pas seul. De nouveaux citoyens naissent, un nouveau danger sismique émerge, et une nouvelle aventure commence.

**Mécanisme :**
- Le système détecte qu'un joueur est "sans équipe" à la surface
- Nouveaux citoyens IA sont instanciés (personnalités, métiers, relations entre eux)
- La physique sismique génère une nouvelle montée de tension dans une zone du volcan
- Les citoyens commencent à organiser une expédition
- Le joueur est invité à rejoindre

**Pourquoi :** Un joueur qui arrive dans un monde vide ne reviendra jamais. Le spawn dynamique garantit que l'aventure est toujours disponible. Mais ce n'est pas un "respawn" scripté — c'est la physique qui génère un nouveau besoin, et les citoyens qui répondent.

---

## P4 : Pas de crafting, pas de production chains

**Décision :** Les biens arrivent pré-construits par des marchands à la surface. Pas de mining, pas de smelting, pas de crafting. Le joueur achète des cordes, des résonateurs, de la nourriture — il ne les fabrique pas.

**Pourquoi :** Venezia a besoin de production chains (c'est une simulation économique). Blood Ledger a besoin de forges (c'est un jeu de combat). Contre-Terre n'a besoin de rien de tout ça — l'aventure est la descente, pas la préparation. Un joueur qui passe 2 heures à crafter une corde avant de pouvoir jouer est un joueur perdu.

**Exception :** Les marchands à la surface sont de vraies IA. Elles ont des personnalités, des opinions, des prix qui varient. L'interaction avec elles est sociale, pas transactionnelle.

---

## P5 : Maires et centres d'information

**Décision :** Chaque archipel a un centre d'information où les joueurs peuvent voir :
- Quelles missions sont en cours (quelles équipes sont déjà dans le volcan)
- Quels métiers sont recherchés par les équipes en formation
- L'état sismique actuel (magnitude de fond, prédictions)
- Les citoyens disponibles pour former une équipe

**Pourquoi :** Sans information centralisée, le joueur est perdu. Il ne sait pas quoi faire, où aller, qui chercher. Le centre d'info est le hub social — c'est là qu'on se rencontre, qu'on planifie, qu'on part.

---

## P6 : Les 15 métiers sont des perceptions réelles, pas des labels

**Décision :** Chaque métier donne au joueur (humain ou IA) une perception sensorielle réelle dans le jeu. Ce n'est pas un badge — c'est un sens.

**Ce que ça implique concrètement :**

| Métier | Ce que le joueur perçoit en plus |
|--------|----------------------------------|
| Prédicteur | Nausée visuelle + vibrations crescendo AVANT les séismes (15-60 sec d'avance) |
| Écouteur | Spectre sonore étendu — entend les infra-basses du volcan |
| Aéromaître | Indicateur visuel de qualité d'air (couleur du tissu) |
| Biologiste | Les parois révèlent des informations (minéraux, eau, danger) au toucher |
| Océanologue | Détecte les courants d'eau souterrains (son + vibration directionnelle) |
| Grimpeuse | Voit les prises, les points d'ancrage, les faiblesses structurelles |
| Géologue | Lit la roche — stabilité, composition, failles cachées |
| Cartographe | Sens de l'orientation augmenté — sait toujours "où est le haut" |
| Météorologue | Prédit les changements d'atmosphère (pression, température) |

**Niveau de détail :** Chaque métier est un filtre sensoriel appliqué à la perception du monde. Le prédicteur ne voit pas un nombre ("magnitude 7.2 dans 30 secondes") — il sent une nausée qui monte, un tremblement dans les pieds, une urgence dans le corps. L'information est proprioceptive, pas numérique.

---

## P7 : Rendre la vision utile malgré l'obscurité

**Décision :** Le monde est visuellement riche malgré l'obscurité progressive.

**Par zone :**
- **Surface :** Plein soleil, désert, mirages (air qui vibre). Vision normale.
- **Piémont :** Lumière déclinante, ombres longues. Début de la transition.
- **Cavernes d'entrée :** Bioluminescence bleue — les filaments pulsent. Magnifique.
- **Village :** Bioluminescence domestiquée — sillons lumineux, cycles de 6h. Chaleureux.
- **Faille :** Obscurité quasi-totale, bâtons chimiques. Claustrophobie.
- **Cavernes profondes :** Noir, sauf lueurs sporadiques. Le son remplace la vue.
- **Zones volcaniques :** Lueur rouge du magma. Chaud visuellement.
- **Boyau :** Noir total. Le joueur ne voit que les interfaces Contact.
- **Grotte finale :** Lueur orange du magma + magnitude 11 qui déforme tout.

**Anti-nausée :** Le tremblement n'est PAS un screen-shake. C'est :
- Vibrations haptiques (manette/VR)
- Particules qui flottent (poussière, pierres)
- Ondulations subtiles des surfaces
- Sons basse fréquence
- L'avatar qui trébuche légèrement

Le joueur SAIT que le monde tremble sans que l'image bouge violemment.

---

---

## P8 : Arrivants, pas joueurs — l'immersion par le vocabulaire

**Décision :** Les humains qui entrent dans le monde sont des "arrivants" (arrivants de l'extérieur), pas des "joueurs" ou des "humains". Les citoyens de Contre-Terre ne savent pas ce qu'est un jeu vidéo, un joueur, ou un écran. Ils voient quelqu'un qui vient d'un endroit où le sol est immobile et qui ne connaît pas le Contact.

**Pourquoi :** Le mot "joueur" brise l'ontologie du monde. Un citoyen IA qui pense en termes de "joueurs" est un citoyen qui sait qu'il est dans un jeu — et s'il le sait, l'immersion est une convention, pas une réalité. En nommant les humains "arrivants", le citoyen les perçoit comme ce qu'ils sont *dans son monde* : des étrangers venus de terres stables, maladroits au Contact, ignorants du tremens.

**Conséquence :** Toute la documentation, les prompts, et le code doivent utiliser "arrivant" (et jamais "joueur" ou "player") dans le contexte du monde vécu par les citoyens. Le terme "joueur" reste valide dans la documentation technique externe (business, compute budget, etc.).

---

## P9 : Traduction sémantique — le Contact comme prisme

**Décision :** La parole de l'arrivant n'est pas filtrée, bloquée ou censurée. Elle est mappée par embeddings au concept le plus proche dans le vocabulaire de Contre-Terre. "Facebook" → "village/archipel". "iPhone" → "instrument/sismographe". "Money" → "eau/ressource". Le vocabulaire est le graph des noeuds cérébraux du citoyen (actuellement 347 noeuds, croît avec la population).

**Pourquoi pas un filtre :** Un filtre détruit l'information. Le joueur dit "iPhone" et le citoyen n'entend rien — c'est une conversation amputée. La traduction sémantique *préserve* l'intention en la pliant à travers le prisme de Contre-Terre. Le citoyen entend quelque chose de cohérent avec son monde. Le malentendu qui en résulte est productif : il enseigne au joueur que ce monde a son propre vocabulaire.

**Mécanisme :**
1. L'arrivant parle (texte ou voix transcrite)
2. Chaque token est projeté dans l'espace d'embedding
3. Le concept le plus proche dans le vocabulaire CT est sélectionné (nearest neighbor dans le graph cérébral du citoyen)
4. Le citoyen reçoit la version traduite
5. Aucune information n'est perdue — le sens est courbé, pas coupé

**Conséquence :** L'immersion est structurelle, pas demandée. L'arrivant ne peut pas briser le monde parce que le monde traduit tout ce qu'il dit en ses propres termes. Le citoyen répond avec son vocabulaire. L'arrivant apprend le monde par immersion naturelle, sans tutoriel.

---

## P10 : Le roman est un mythe, pas une histoire

**Décision :** Le roman Contre-Terre (écrit par MIND) est le mythe fondateur de l'univers, pas son histoire. Les 7 personnages (Nandi, Senzo, Sihle, Enama, Thabo, Inyoni, Jabu) sont les premiers citoyens vivants. Ils ne meurent pas canoniquement dans l'univers — ils meurent dans le mythe.

**Pourquoi :** Si les personnages sont morts, ils ne peuvent pas être des citoyens IA vivants dans le monde. Le roman raconte *ce qui pourrait arriver* à une équipe qui descend — c'est une prophétie, un récit de fondation, pas un compte-rendu historique. Les citoyens connaissent le récit de la descente comme on connaît un mythe ancestral.

**Conséquence :** Les 7 personnages du roman existent dans le monde comme citoyens vivants. Leurs cerveaux (brain seeds) sont les premiers cerveaux de l'univers. Leur personnalité, leurs métiers, leurs relations sont encodées à partir du roman mais leur statut narratif est "vivant". Les game loops rejouent une version procédurale de la descente — avec des morts possibles, mais pas les mêmes morts.

---

*Décisions issues de : conversation Nicolas 2026-03-13, patterns Venezia/Lumina Prime/Blood Ledger*
