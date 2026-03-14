# PATTERNS: Narrative Engine

**Module :** `universe/narrative_engine`
**Question centrale :** Pourquoi le moteur narratif est concu comme il l'est ? Quelles decisions de design, et pourquoi ?

---

## P1 : Trois systemes de tension paralleles, un seul moteur physique

**Decision :** Le moteur ne simule pas "la tension" comme un chiffre unique. Il maintient trois systemes de tension distincts qui alimentent tous le meme moteur ngram. Chaque systeme a ses propres sources, ses propres seuils, et ses propres types de flip.

### Systeme 1 : Tension sismique (pression geologique)

**Source :** Accumulation tectonique naturelle. Chaque zone geologique genere de la tension a son propre rythme (les zones volcaniques profondes plus vite que la surface desertique). La generation_rate est modulee par la profondeur.

**Seuil de flip :** Quand la tension d'une zone depasse son tension_threshold local, un seisme se produit. La magnitude correspond a l'energie accumulee. Apres le flip, la tension chute (mais jamais a zero -- le fond magnitude 4 est irreductible).

**Moments produits :** Seismes classiques, glissements, effondrements, bangs acoustiques, eruptions. Les 10 types de cataclysmes documentes dans PATTERNS_Seismique.md sont les differentes formes que prend le flip sismique.

### Systeme 2 : Tension de Contact (densite communicative)

**Source :** Frequence et intensite des interactions tactiles entre citoyens. Un groupe qui communique beaucoup accumule de la tension de Contact -- pas parce que la communication est mauvaise, mais parce que la densrite d'information cree une pression vers la cristallisation. Trop de donnees sans synthese = tension.

**Seuil de flip :** Quand la tension de Contact depasse le seuil, deux issues : percee (breakthrough) ou rupture (breakdown). Percee = nouveau vocabulaire, nouveau geste, idiolecte de paire. Rupture = malentendu, incomprehension, isolation.

**Moments produits :** Creation d'idiolectes, percees dialectales (la vieille femme enseigne le geste inconnu), ruptures (Sihle refuse le Contact intuitif d'Enama, separation du groupe au Ch. V).

### Systeme 3 : Tension sociale (conflits relationnels)

**Source :** Divergences entre citoyens -- desaccords epistemologiques (Sihle vs Enama), tensions de leadership (qui decide apres Senzo ?), conflits de metier (l'aeromaitre vs le predicteur sur l'air de la faille). Chaque desaccord non resolu ajoute de la tension.

**Seuil de flip :** Quand la tension sociale depasse le seuil, le groupe se transforme : scission, reconciliation, sacrifice, ou reorganisation des roles. La mort d'un membre est souvent le flip -- elle resolve la tension en supprimant un pole du conflit.

**Moments produits :** Separation du groupe (Ch. V), transfert de leadership, cercles de Contact (Ch. IV, scene des epaules), sacrifices (Enama dans le magma).

**Pourquoi trois et pas un :** Un seul systeme de tension produirait un monde monotone -- "tension monte, quelque chose se passe". Trois systemes permettent des interferences : un seisme peut interrompre un conflit social, une percee de Contact peut prevenir un seisme (le geste inconnu de Nandi calibre la Charge). Les systemes se couplent sans se confondre.

### L'adaptation depuis Venezia : du sang au seisme

Le moteur ngram de Venezia operait avec un grand-livre du sang (blood-ledger) structure autour de trois axes de tension : economique (ressources, dette, echange), narrative (moments, recits, completions), et sociale (relations, conflits, alliances). Contre-Terre SUPPRIME l'axe economique. Il n'y a pas de monnaie, pas de dette, pas de marche dans un monde ou sept personnes descendent dans un volcan pour mourir. L'axe economique est remplace par l'axe sismique : la pression tectonique devient la "dette" que le monde accumule et que les seismes "remboursent". Le cycle accumulation → flip → relachement est structurellement identique au cycle emprunt → crise → remboursement du blood-ledger -- mais la source de tension est geologique, pas sociale. L'energie, le decay, et la tension sont les memes primitives ; seul le substrat change.

---

## P2 : Les seismes ne sont pas aleatoires -- ils emergent

**Decision :** Aucun seisme n'est genere par un de aleatoire. Chaque seisme est le resultat d'une accumulation mesurable de tension dans le graph. Le moteur ne lance pas "un seisme de magnitude 7 maintenant" -- il observe que la tension de la zone Piemont a depasse 0.7, et le flip produit un seisme dont la magnitude correspond a l'energie accumulee.

**Pourquoi :** La previsibilite est le coeur du conflit epistemologique du roman. Nandi sent les seismes venir (son tremens est un pre-symptome) PARCE QU'ILS SONT DETERMINISTES. Si les seismes etaient aleatoires, la prediction serait impossible et l'Echelle de Capitulation n'aurait pas de sens. Le moteur encode la these du roman : le corps peut savoir avant l'instrument parce que la terre suit des lois -- des lois que le corps ressent et que l'instrument ne sait pas encore mesurer.

**Ce que ca empeche :** Les seismes-surprise sans fondement narratif. Chaque seisme du roman doit etre retracable a une accumulation de tension.

---

## P3 : Le decay empeche la stagnation et l'explosion

**Decision :** La tension dans chaque systeme decroit naturellement (decay_rate) si rien ne l'alimente. Mais le generation_rate permanent la maintient en mouvement. L'equilibre entre generation et decay definit le rythme du monde.

**Pourquoi :** Sans decay, la tension ne ferait que monter -- le monde exploserait. Sans generation, la tension finirait par mourir -- le monde stagnerait. Le decay est ce qui permet les cycles : accumulation → flip → relachement → re-accumulation. Le homeostasis_target (0.3 dans Venezia) definit le niveau de tension "au repos" du monde -- pour Contre-Terre, ce repos n'est pas le silence mais la magnitude 4 permanente.

---

## P4 : La profondeur module toutes les constantes

**Decision :** Les constantes ngram ne sont pas fixes pour tout le monde. Elles varient par zone geologique. Plus on descend, plus la generation_rate augmente (plus de pression tectonique), plus le tension_threshold baisse (moins d'accumulation necessaire pour un flip), et plus le decay_rate diminue (la tension ne se dissipe pas dans la roche profonde).

**Pourquoi :** La descente dans le volcan est une escalade narrative. Le moteur doit encoder cette escalade structurellement, pas par des regles ad hoc. Les memes lois physiques produisent des comportements radicalement differents en surface et en profondeur -- exactement comme dans le roman.

| Zone | generation_rate | decay_rate | tension_threshold | Comportement |
|------|----------------|------------|-------------------|--------------|
| Surface (desert) | 0.04 | 0.06 | 0.8 | Cycles lents, seismes rares |
| Piemont | 0.06 | 0.05 | 0.7 | Cycles reguliers |
| Cavernes | 0.08 | 0.04 | 0.65 | Cycles frequents |
| Faille | 0.10 | 0.02 | 0.6 | Tension qui monte vite, se dissipe peu |
| Zones volcaniques | 0.14 | 0.02 | 0.5 | Seismes quasi-permanents |
| Grotte finale | 0.20 | 0.01 | 0.4 | Tension insoutenable → magnitude 11 |

---

## P5 : La mort est un flip irrevocable

**Decision :** La mort d'un citoyen est un moment flip dans le systeme social ET dans le systeme Contact. Le flip est irrevocable : le noeud meurt, ses liens se coupent, son vocabulaire disparait. Contrairement a un seisme (qui libere la tension et permet un nouveau cycle), une mort ne cree pas de nouveau cycle -- elle supprime un pole du systeme.

**Pourquoi :** Le roman est une mission-suicide. Sept personnes descendent, sept meurent. Le moteur doit rendre chaque mort structurellement significative : pas seulement la perte d'un personnage, mais la perte d'une partie du systeme de tension lui-meme. Apres la mort de Sihle, le pole "instrument" de la tension epistemologique disparait. Le systeme se simplifie -- et se simplifie vers la catastrophe.

---

## DECISIONS NON PRISES

| Question ouverte | Impact | Priorite |
|-----------------|--------|----------|
| Constantes exactes par zone (les valeurs du tableau P4 sont indicatives) | Calibration du rythme narratif | Haute |
| Couplage entre les 3 systemes de tension (comment un seisme affecte-t-il la tension sociale ?) | Richesse des interactions | Haute |
| Poids relatif des 3 systemes dans la metrique globale | Balance du moteur | Moyenne |
| Gestion des zones de transition (entre deux couches geologiques) | Fluidite de la simulation | Basse |

---

*Sources : `physics/constants.json` (Venezia), `PATTERNS_Seismique.md`, `ALGORITHM_Seismique.md`, phases ngram (generation, moment_draw, moment_flow, moment_interaction, narrative_backflow, completion)*
