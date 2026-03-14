# VALIDATION — Experience Design

> Invariants. Ce qui DOIT être vrai pour que l'expérience fonctionne.

---

## Invariants absolus

### V1 : Le joueur ne doit jamais attendre plus de 5 minutes sans interaction sociale

Si le joueur est seul et sans équipe, le spawn dynamique s'active. Un citoyen IA vient lui parler dans les 5 minutes. L'attente silencieuse tue les jeux.

### V2 : Aucun événement n'est scripté

Pas de triggers ("quand le joueur entre dans la zone X, le séisme Y arrive"). Les séismes résultent de la tension accumulée. Les morts résultent des conditions physiques. Les rencontres résultent des mouvements des citoyens. La physique est le seul auteur.

### V3 : L'humain n'a aucun avantage sur l'IA

Mêmes règles, même mortalité, même tremens, même Contact. Si l'humain est prédicteur, il ressent la même nausée que l'IA prédictrice. Pas de "mode héros". Pas de respawn privilégié.

### V4 : Les métiers sont des perceptions, pas des stats

Un prédicteur ne voit pas "+15% chance de séisme dans 30s". Il sent une nausée montante, un tremblement dans les pieds, une urgence dans le corps. L'information est proprioceptive, jamais numérique.

### V5 : La mort d'un coéquipier change réellement ce que le joueur peut faire

Pas un message "votre coéquipier est mort". Le vocabulaire Contact partagé disparaît. Le métier n'est plus couvert (l'aéromaître est mort → personne ne lit l'air → on ne sait pas si une poche de gaz approche). La perte est fonctionnelle, pas cosmétique.

---

## Invariants structurels

### V6 : Pas de monnaie dans le volcan

L'argent n'existe qu'à la surface (marchands). Sous terre, il n'y a que le Contact, les métiers, et l'équipement qu'on porte. Pas de loot, pas de drops, pas de chest.

### V7 : La descente est mécaniquement irréversible après la faille

Avant la faille : on peut remonter. Après : le passage se ferme (physiquement, pas arbitrairement — effondrement, crue, chaleur). L'engagement est réel.

### V8 : L'équipe doit avoir un prédicteur OU un écouteur

Pas d'obligation stricte de composition, mais sans perception sismique, l'équipe est aveugle. Les citoyens IA refuseront probablement de partir sans — c'est leur décision, pas une règle du jeu.

### V9 : Le Contact est le seul langage sous terre

Pas de chat textuel sous terre. Pas de voice chat magique. Le Contact (menu radial ou VR) est la seule façon de communiquer avec les IA. Les humains entre eux peuvent parler (voice chat), mais les IA ne comprennent que le Contact.

### V10 : La physique self-calibrating ne fabrique jamais d'événements

Elle ajuste la vitesse d'accumulation de tension. Elle ne crée pas de séismes artificiels. La différence est critique : le séisme qui tue un coéquipier est un vrai événement physique, pas un script déguisé.

---

## Invariants économiques

### V11 : Le compute par joueur doit rester sous $X/heure (à déterminer)

L'abonnement doit couvrir le coût de compute. Si un joueur coûte $5/heure en LLM calls et paie $15/mois, le modèle est mort. L'autopilot et les réactions pré-calculées sont des nécessités économiques, pas des optimisations.

### V12 : Le spawn dynamique ne doit pas multiplier les citoyens sans contrôle

Chaque citoyen actif coûte du compute. Le spawn dynamique crée le minimum nécessaire pour une équipe (4-6 IA). Les citoyens "idle" à la surface ont un compute minimal (~1 appel LLM/5 min).

---

## Invariants d'anti-nausée

### V13 : Le tremblement visuel ne doit JAMAIS être un screen-shake

Le tremblement se manifeste par : particules flottantes, vibrations haptiques, sons basse fréquence, avatar qui vacille, surfaces qui ondulent. PAS par la caméra qui secoue. Le motion sickness tue le jeu plus vite que l'ennui.

---

*Invariants dérivés de : conversation Nicolas 2026-03-13, patterns anti-nausée VR, économie compute LLM*
