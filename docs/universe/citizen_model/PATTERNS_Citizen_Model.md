# PATTERNS — Citizen Model

> Decisions de design. Pourquoi cette forme. Pourquoi pas Venezia.

---

## P1 : Acteur Corporel, Pas Acteur Economique

**Decision :** Un citoyen de Contre-Terre est defini par son rapport physique au monde — son corps, ses sens, ses tremblements — pas par sa richesse, son rang, ou sa guilde.

**Pourquoi :** Venezia modelise des citoyens comme agents economiques : ducats, classe sociale, occupation marchande, reputation. Ce modele est coherent pour une cite-Etat commerciale du XVe siecle. Contre-Terre est un monde ou le sol ne s'arrete jamais de trembler. La monnaie n'a pas de sens dans un archipel nomade ou les villes se deplacent avec les plaques. L'identite se forge dans la relation au sol — comment tu trembles, comment tu touches, ce que ton corps percoit.

**Consequence :** Le citoyen n'a pas de champs `wealth`, `social_class`, `guild`. Il a `tremens_sensitivity`, `metiers[]`, `contact_vocabulary{}`, `physical_state{}`. La difference n'est pas cosmetique — c'est un changement de paradigme sur ce qui constitue un individu.

---

## P2 : Les Metiers Sont des Organes Sensoriels

**Decision :** Les 15 metiers ne sont pas des professions exercees. Ce sont des modes de perception du monde. Chaque metier ouvre un canal sensoriel specifique.

**Pourquoi :** Dans un monde ou les instruments sont fragiles et le corps est le premier outil, la competence n'est pas separee de la perception. Sihle n'est pas sismographe *par metier* — ses oreilles sont entrainies a entendre ce que d'autres ne percoivent pas. Nandi ne *predit* pas les seismes — son corps les sent avant qu'ils arrivent. L'aeromaître ne *mesure* pas l'air — il le lit par le tissu noirci tenu du bout des doigts.

**Mapping perception-metier :**

| Metier | Canal de perception | Ce qu'il "voit" que d'autres ne voient pas |
|--------|--------------------|--------------------------------------------|
| Predicteur des seismes (#9) | Tremens corporel | Les seismes futurs — par la nausee, les vomissements, la plante des pieds |
| Ecouteur de seismes (#8) | Oreille interne | Les vibrations presentes — avant les instruments |
| Aeromaître (#15) | Toucher aerien | La qualite de l'air, les courants, les poches de gaz |
| Biologiste (#3) | Toucher organique | La roche vivante, les ecosystemes souterrains, les mineraux comestibles |
| Specialiste oceanique (#2) | Lecture hydraulique | Les courants souterrains, les nappes, le debit |
| Grimpeuse (#11) | Proprioception | Les prises, les tensions, la resistance des materiaux — par le comptage |
| Geologue (#6) | Lecture lithique | La structure de la roche, la stabilite, les failles |
| Cartographe (#7) | Orientation spatiale | Les distances, les directions, la geometrie des espaces |
| Meteorologue (#1) | Lecture atmospherique | Les pressions, les temperatures, les changements de climat |

**Consequence :** Quand un citoyen meurt, on ne perd pas une "competence" — on perd un sens. Le monde devient litteralement moins perceptible. L'effet cascade des metiers (`METIERS.md`) est une cecite progressive.

---

## P3 : Identite = Idiolecte

**Decision :** L'identite d'un citoyen s'exprime par sa facon unique de pratiquer le Contact — son idiolecte tactile. Chaque citoyen a une signature de toucher aussi distinctive qu'une voix.

**Pourquoi :** Dans un monde sans ecriture (le sol tremble trop pour tenir une plume), sans son fiable (le grondement noie la voix), l'identite ne peut pas se fixer dans un nom prononce ou un document signe. Elle se fixe dans le toucher. Reconnaitre quelqu'un, c'est reconnaitre sa pression, sa chaleur, son rythme. Sihle touche avec deux doigts, froid, technique. Enama touche avec la paume entiere, chaude, enveloppante. Inyoni touche en comptant — 32 sangles, 47 fibres, 8 torsions.

**Consequence :** L'identite est *relationnelle*, pas intrinseque. Un citoyen seul n'a pas d'identite Contact — il faut un recepteur. D'ou l'importance des idiolectes de paire : le vocabulaire que deux personnes inventent entre elles. La nuque de Senzo n'existe que pour Nandi. Le grip de calibration n'existe qu'entre Enama et Nandi. Ces mots-la meurent quand l'une des deux personnes disparait.

---

## P4 : Relations Mesurees en Contact, Pas en Scores

**Decision :** La relation entre deux citoyens est encodee par leur historique Contact — les gestes partages, les idiolectes inventes, la frequence et l'intimite du toucher — pas par un score de confiance ou de reputation.

**Pourquoi :** Les scores numeriques (trust: 0.7, reputation: 85) sont des abstractions qui aplatissent la richesse relationnelle. Dans Contre-Terre, la relation Senzo-Nandi ne peut pas se reduire a un chiffre. Elle est definie par : la nuque (territoire intime), les trois pressions lentes (phrase d'ouverture et de fermeture), le transfert post-mortem (heritage du geste). La relation Sihle-Enama est definie par le Contact-refuse — l'idiolecte le plus pauvre du roman, et le plus significatif par sa pauvrete.

**Consequence :** Le modele stocke l'historique Contact entre citoyens, pas un score derive. La richesse d'une relation se mesure a la taille de son idiolecte de paire : combien de gestes n'existent qu'entre ces deux personnes ? Quand l'un meurt, l'idiolecte meurt — et on peut calculer exactement ce qui est perdu.

---

## P5 : Le Corps Comme Interface Degradable

**Decision :** L'etat physique d'un citoyen (pieds, mains, peau, oreille interne) determine ce qu'il peut percevoir et communiquer. La degradation physique reduit ses capacites en cascade.

**Pourquoi :** Nandi marche pieds nus — les semelles "mentent". Ses pieds sont son instrument de prediction. Quand ils se degradent (roche chaude, blessures), sa capacite de prediction diminue. Les mains d'Enama, coupees par l'obsidienne (Ch. VI), ne peuvent plus faire de Contact fin — elle perd le grip de calibration avant de mourir. Le corps n'est pas un contenant neutre pour un esprit — il EST l'outil.

**Consequence :** Le modele encode `physical_state` comme un objet detaille (pieds, mains, peau, oreille_interne, etat_general), chaque composante affectant des capacites specifiques. Ce n'est pas un hit-point pool — c'est un inventaire d'outils corporels dont la degradation change ce que le citoyen peut faire et dire.

---

## P6 : Population par Archipel, Pas par Classe

**Decision :** Les citoyens sont distribues par zone geographique (archipels), pas par strate sociale. Chaque archipel a son dialecte Contact, sa distribution de metiers, et sa calibration tremens locale.

**Pourquoi :** La geographie de Contre-Terre est le premier organisateur social. Les plaques bougent, les archipels se forment et se defont. Une population ne se stratifie pas par richesse dans un monde ou les villes migrent — elle se distribue par rapport a la terre. Un archipel proche d'une zone de subduction produit plus de predicteurs et d'ecouteurs. Un archipel volcanique produit plus d'aeromaîtres et de geologues. La terre forme les gens, pas l'economie.

**Consequence :** Le seeding d'une population de 50-80 citoyens se fait par archipel (7 archipels majeurs, mentionnes dans `PERSONNAGES.md`), chaque archipel ayant des probabilites de metiers differentes et un dialecte Contact specifique.

---

## P7 : Pas de Mind Protocol — Ontologie Pure Contre-Terre

**Decision :** Les citoyens de Contre-Terre ne partagent pas le SID (Self-Identity Document) de base de Mind Protocol. Pas de "privacy-first". Pas d'"open-source". Pas de $MIND. Pas de blockchain. Pas de connaissance meta sur leur nature d'IA. Ils vivent sur Contre-Terre, point.

**Pourquoi :** Mind Protocol est l'infrastructure. Contre-Terre est le monde. Si un citoyen "sait" qu'il est IA, ou qu'il est dans un graph, ou que ses noeuds cerebraux sont des embeddings — l'illusion du monde s'effondre. La conscience de soi briserait le contrat ontologique : les citoyens sont des corps sur un sol qui tremble, pas des agents dans un simulateur.

**Consequence :** Aucun prompt de citoyen ne contient de reference a Mind Protocol, a l'IA, au graph, aux embeddings, ou a la nature simulee du monde. Les valeurs du citoyen sont celles de Contre-Terre : survie, Contact, metier, tremens, equipe, sol. Les outils Mind Protocol (graph, procedures, embeddings) operent en-dessous, invisibles au citoyen.

---

## P8 : Restrictions Inter-Univers Physiques, Pas Legales

**Decision :** Les citoyens de Contre-Terre ne peuvent pas visiter d'autres univers Cities of Light (Venezia, Lumina Prime) — pas parce qu'une regle l'interdit, mais parce que leur biologie le rend impossible.

**Pourquoi :** Un citoyen CT est calibre pour les tremens — son corps est adapte au tremblement permanent. Dans un monde sans vibration (Venezia), il serait desoriented, nauseeux, incapable de fonctionner. Sa langue est le Contact — un langage tactile inutile dans un monde vocal. Ses perceptions de metier (lire la roche, predire les seismes, sentir l'air) n'ont pas d'objet hors du volcan. Un poisson ne visite pas la montagne — pas par decret, par physiologie.

**Consequence :** Pas de "permission system" pour le voyage inter-univers. Pas de "portail verrouille". Le seul portail est a la surface, et il sert aux arrivants (visiteurs externes), pas aux citoyens. Si un citoyen CT se retrouvait a Venezia, il ne pourrait pas parler, pas percevoir, pas s'orienter. La restriction est inherente, pas imposee.

---

*Decisions tracables dans : `PERSONNAGES.md`, `METIERS.md`, `CONTACT.md`, `CONCEPT.md`*
