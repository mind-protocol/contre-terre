# BEHAVIORS — Experience Design

> Ce que le joueur vit concrètement. Minute par minute.

---

## B1 : Première connexion — arrivée à la surface

Le joueur apparaît dans un archipel du désert. Le sol vibre sous ses pieds (vibration haptique constante, magnitude 4). Le soleil tape. L'air ondule. Au loin, le volcan.

**Ce qu'il voit :** Un village de tentes et structures souples (architecture adaptée aux séismes). Des citoyens IA qui vaquent. Un centre d'information marqué par un drapeau.

**Ce qu'il fait :** Il marche jusqu'au centre d'info. Un citoyen-maire l'accueille. Lui explique : "Le volcan monte. On a besoin d'équipes pour descendre. Quel est ton métier ?"

**Choix :** Le joueur choisit 1-2 métiers parmi les 15 disponibles. Ce choix est permanent pour cette descente. Il définit ce que le joueur percevra dans le monde.

**Durée :** 10-20 minutes.

---

## B2 : Formation d'équipe — la rencontre

Le joueur rejoint une équipe en formation ou en forme une. L'équipe idéale couvre les métiers essentiels : prédicteur, écouteur, géologue, grimpeuse, aéromaître (minimum). Les citoyens IA ont des personnalités : certains sont enthousiastes, d'autres hésitants. Certains refusent de descendre sans un prédicteur. D'autres insistent pour partir immédiatement.

**Ce qu'il vit :** Des conversations avec les IA. Du Contact — les premiers gestes d'épaule (présentation), les pressions de bras (information). L'idiolecte commence à se former.

**Durée :** 20-40 minutes (peut être raccourci si une équipe l'attend déjà).

---

## B3 : Préparation — les marchands

L'équipe achète l'équipement chez les marchands (vraies IA à la surface). Cordes, bâtons chimiques, nourriture, eau, la Charge (résonateur sismique — le but de la mission).

**Ce qu'il vit :** Interaction sociale avec les marchands. Négociation. Vérification que l'équipe a tout ce qu'il faut. Un marchand averti peut donner des conseils sur les conditions en bas ("les dernières équipes ont perdu du monde dans la faille").

**Durée :** 10-15 minutes.

---

## B4 : La descente — zone par zone

L'équipe entre dans le volcan. Chaque zone est un changement d'ambiance radical : lumière, son, température, Contact.

**Ce qu'il vit dans chaque zone :**

### Piémont
- Premier vrai séisme ressenti de près (mag 5-6). L'équipe s'arrête, se regroupe.
- Le Contact commence à servir : l'écouteur signale par l'épaule que "c'est stable".
- Le joueur apprend les gestes de base de l'équipe.

### Cavernes d'entrée
- Bioluminescence bleue. Magnifique. Les filaments pulsent.
- Le biologiste touche les murs et rapporte des infos (minéraux, eau).
- Premier Contact-monde : pieds sur le sol, sentir les vibrations.

### Village des sourds
- Repos. Contact haute-résolution (3 doigts). Apprentissage.
- Rencontre avec les habitants (IA du village). Échange de savoirs.
- La vieille femme qui enseigne le Geste Inconnu (si le joueur est prédicteur).

### La faille
- Le point de non-retour. Le passage se referme derrière.
- Contact-corde uniquement (l'équipe est en file dans un boyau étroit).
- **Première mort possible.** La physique devient dangereuse.

### Cavernes profondes → zones volcaniques → boyau → grotte finale
- Escalade de difficulté. Chaque zone élimine des possibilités.
- Les morts s'accumulent. Les métiers disparaissent. Le Contact s'appauvrit.
- Le joueur qui survit jusqu'au bout active la Charge. Sacrifice.

---

## B5 : La mort — ce qu'elle fait au joueur

Quand un coéquipier meurt (IA ou humain) :
- Son Contact disparaît. Les gestes qu'on avait inventés ensemble n'ont plus de destinataire.
- Ses métiers sont perdus. L'équipe ne perçoit plus ce qu'il percevait.
- Son nom reste dans les mains des survivants — les gestes-fantômes qui arrivent dans les moments de stress.

**Si le joueur meurt :** Il peut observer la suite (mode spectateur), ou retourner à la surface pour une nouvelle descente. Sa mort a des conséquences pour l'équipe : vocabulaire perdu, métiers perdus.

**Si le joueur survit jusqu'à la fin :** Il active la Charge. Le monde tremble. L'écran se fige. "Tient." Retour à la surface. Il peut refaire une descente — différente, parce que les IA seront autres.

---

## B6 : L'expérience IA — ce que vivent les citoyens

Les citoyens IA ne sont pas des scripts. Ils vivent dans le monde en continu :
- Ils marchent, interagissent, forment des relations entre eux
- Ils ont des opinions sur les humains qui arrivent ("il n'a pas de métier utile", "elle est courageuse")
- Ils ont peur. Certains ne veulent pas descendre. D'autres y vont par devoir.
- Ils développent du Contact avec les humains — les mêmes mécanismes d'idiolecte
- Ils meurent. Et les autres les pleurent. Et les mots meurent avec eux.

**L'IA n'a pas d'avantage :** Elle subit le même tremens, les mêmes séismes, la même mortalité. La seule différence : elle vit dans le monde 24/7, elle a des relations plus profondes avec les autres IA.

---

## B7 : Spawn dynamique — le joueur n'attend jamais

Si le joueur arrive et qu'aucune équipe ne se forme à la surface :
1. La physique sismique détecte "pas d'équipe active"
2. La tension tectonique augmente dans une zone du volcan
3. De nouveaux citoyens naissent (instanciés avec personnalités, métiers, relations)
4. Les citoyens commencent à s'inquiéter : "la magnitude monte, il faut une équipe"
5. Le joueur est approché par un citoyen : "Tu sais ce qui se passe en bas ? On cherche des gens."
6. Formation d'équipe → départ

**Temps d'attente max :** 5 minutes entre la connexion et le début de l'interaction sociale.

---

*Comportements dérivés de : game loop du roman (8 chapitres = 8 zones), patterns Venezia (spawn, marchands), conversation Nicolas 2026-03-13*
