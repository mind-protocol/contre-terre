# BEHAVIORS: Narrative Engine

**Module :** `universe/narrative_engine`
**Question centrale :** Quels sont les comportements observables du moteur narratif ? Que produit-il ?

---

## B1 : Les seismes remodulent le monde

Quand un flip sismique se produit, le monde change physiquement. Les passages s'ouvrent ou se ferment. Les structures s'effondrent. Les chemins disponibles se reorganisent. Un seisme de magnitude 7 dans la faille peut sceller un passage et en ouvrir un autre. Un effondrement au Ch. IV separe le groupe du cadavre de Senzo. Un glissement au Ch. VII mure Thabo et Inyoni de l'autre cote du boyau.

**Observable :** Apres chaque flip sismique, le graph geographique (noeuds spatiaux, liens de connexion entre zones) est modifie. Des liens se coupent (passages fermes), d'autres se creent (nouvelles failles, nouvelles ouvertures). Les citoyens doivent adapter leurs routes. Le monde ne revient pas a son etat precedent -- chaque seisme laisse une cicatrice permanente dans la topologie.

**Couplage :** Un seisme qui ferme un passage force les citoyens a se rapprocher (tension sociale augmente) ou a se separer (Contact se degrade). Le flip sismique alimente les deux autres systemes de tension.

---

## B2 : Les percees de Contact creent du vocabulaire

Quand un flip de Contact se produit en mode "percee" (breakthrough), de nouveaux gestes apparaissent. Un idiolecte de paire se cristallise : deux citoyens qui se touchaient generiquement developpent un raccourci que seuls eux comprennent. Un dialecte evolue : le Contact-corde du Ch. IV est un vocabulaire entierement nouveau, invente sous la contrainte de la faille.

**Observable :** Apres une percee, le vocabulaire du groupe s'enrichit mesurableement. De nouveaux gestes sont documentes dans le graph (noeuds de type "thing" lies aux acteurs qui les pratiquent). Les liens entre les citoyens concernes se renforcent (le poids du lien monte). La metrique Contact_vitality fait un pic local malgre sa tendance baissiere globale.

**Exemples du roman :**
- Ch. III : La vieille femme enseigne le geste inconnu a Nandi → percee (nouveau geste, incompris mais stocke)
- Ch. IV : L'equipe invente le Contact-corde → percee (7 signaux crees en temps reel)
- Ch. IV : Cercle des epaules apres la mort de Senzo → percee emotionnelle (Contact collectif de deuil, geste "on ne remonte pas" transforme)

---

## B3 : Les ruptures de Contact isolent

Quand un flip de Contact se produit en mode "rupture" (breakdown), la communication se brise. Un citoyen est incompris, un geste est mal lu, un dialecte echoue a traverser la barriere regionale. L'isolation n'est pas physique -- elle est linguistique. Le citoyen est present mais muet, present mais sourd.

**Observable :** Apres une rupture, les liens entre les citoyens concernes s'affaiblissent. La frequence d'interaction diminue. Des gestes qui fonctionnaient cessent d'etre tentes. La metrique Contact_vitality chute localement.

**Exemples du roman :**
- Ch. II : Sihle refuse le Contact intuitif d'Enama → rupture (le Contact technique de Sihle et le Contact emotionnel d'Enama ne se rejoignent pas)
- Ch. V : Separation du groupe → rupture massive (les liens physiques sont coupes, le Contact-corde est le seul lien)
- Ch. VIII : Nandi seule → rupture totale (plus de destinataire, le Contact n'a plus de sens inter-humain)

---

## B4 : Les conflits sociaux se resolvent ou s'amplifient par le Contact

La tension sociale ne se dissipe pas dans le vide. Elle se traite par le Contact -- ou echoue a se traiter. Un cercle de Contact (les 7 personnages qui se touchent les epaules en cercle) est un mecanisme de resolution : la tension circule physiquement et se redistribue. Un refus de Contact (Sihle qui retire ses doigts) est un mecanisme d'amplification : la tension bloquee augmente.

**Observable :** Les cercles de Contact reduisent la tension sociale de tous les participants. Le refus de Contact augmente la tension entre le refusant et le groupe. La mort d'un participant au conflit resout la tension en supprimant un pole -- mais cree un pic de tension de deuil qui alimente temporairement les deux autres systemes.

---

## B5 : Les predictions des predicteurs creent de l'anticipation

Le tremens de Nandi est un pre-symptome sismique. Dans le moteur, cela signifie que les citoyens de type "predicteur" percoivent la tension sismique AVANT le flip. Ils ne voient pas l'avenir -- ils sentent la tension monter. Leur corps traduit l'etat du graph en symptomes physiologiques.

**Observable :** Quand la tension sismique d'une zone depasse 60% du seuil de flip, les predicteurs de cette zone declenchent un tremens proportionnel. Le tremens s'intensifie a mesure que la tension approche du seuil. Les autres citoyens peuvent interpreter le tremens du predicteur comme un avertissement -- s'ils acceptent l'Echelle de Capitulation.

**Couplage avec la tension sociale :** L'avertissement du predicteur cree un conflit social : le croire (Enama) ou exiger une preuve instrumentale (Sihle). Le pre-symptome sismique alimente directement la tension epistemologique -- la prochaine couche de tension sociale.

---

## B6 : Le monde ne stagne jamais, ne s'arrete jamais

Le generation_rate permanent assure que de la tension est toujours produite, meme en l'absence d'evenements actifs. Le sol tremble toujours a magnitude 4. Les citoyens sont toujours en Contact. Les conflits couvent. Il n'y a pas de "pause" dans le moteur -- le monde pulse en permanence.

**Observable :** Meme pendant les periodes calmes du recit (le village des sourds au Ch. III, la nuit dans le magma au Ch. VI), le moteur continue de tourner. La tension monte. Le prochain flip approche. Le calme narratif est toujours un calme trompeur -- le decay empecherait l'explosion, mais le generation_rate assure qu'elle finira par arriver.

---

## B7 : La mort cascade a travers les trois systemes

La mort d'un citoyen n'est pas un evenement local. C'est un flip irrevocable qui irradie dans les trois systemes simultanement. Sismiquement : le groupe perd un corps qui pouvait lire, amortir, ou predire les seismes (la mort de Sihle supprime le sismographe). Contactuellement : tous les idiolectes de paire du mort disparaissent instantanement -- le vocabulaire qu'il portait meurt avec lui. Socialement : les conflits dont le mort etait un pole se resolvent par suppression, mais le deuil cree un pic de tension sociale chez les survivants.

**Observable :** Apres chaque mort, Contact_vitality chute de maniere permanente (speaker_count - 1, vocabulaire detruit). La tension sociale fait un pic (deuil) puis redescend vers un nouvel equilibre plus bas -- moins de poles de conflit, mais aussi moins de poles de resolution. Le systeme se simplifie a chaque mort, et la simplicite n'est pas un soulagement mais un appauvrissement.

**Le cas de la cascade :** La mort de Senzo (Ch. IV) supprime le leader, ce qui disloque la structure sociale → la mort de Sihle (Ch. V) supprime l'instrument, ce qui force la capitulation epistemologique → la mort d'Enama (Ch. VI) supprime le Contact-monde intuitif, ce qui isole Nandi → les morts de Thabo et Inyoni (Ch. VII) suppriment la corde et le comptage, ce qui laisse Nandi sans outil. Chaque mort amplifie la vulnerabilite aux morts suivantes. Le systeme n'est pas lineaire -- il est auto-catalytique.

---

## B8 : La magnitude 11 est la convergence des trois tensions

Le seisme final n'est pas un simple flip sismique. C'est le point ou les trois systemes de tension convergent vers un evenement unique. La tension sismique a atteint un niveau que seul le coeur du volcan peut contenir. La tension de Contact est maximale : Nandi est seule, le vocabulaire est mort, le Contact n'a plus de destinataire -- il doit se retourner vers le monde (Contact-monde). La tension sociale est resolue par elimination : il ne reste qu'une personne, plus de conflit possible, plus de cercle, plus de resolution -- seulement l'acte.

**Observable :** Dans la grotte finale, les trois accumulateurs de tension sont simultanement a leur maximum historique. La tension sismique alimente la magnitude. La tension de Contact s'est transformee en Contact-fantome puis en geste inconnu -- le flip Contact final est le moment ou Nandi pose ses mains sur la Charge. La tension sociale s'est comprimee dans le corps de Nandi : elle porte les conflits de tous les morts, et son acte les resout tous en une seule detonation. Le building 11 EST les trois tensions convergees.

---

*Sources : `ALGORITHM_Seismique.md` (10 types de cataclysmes), `ALGORITHM_Contact.md` (5 modes, Contact-corde, degradation), `PATTERNS_Seismique.md` (permanence, variete), chapitres I-VIII*
