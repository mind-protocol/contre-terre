# Contre-Terre — Sync: Current State

```
LAST_UPDATED: 2026-03-14T09:30
UPDATED_BY: Claude Opus 4.6 (agent, voice)
```

---


## MASTER TODO

### Force 1
- [x] Canoniser le template `PROMPT_MAITRE_5_FORCE_SPRINT.md`
- [x] Publier la checklist `FORCE_EXECUTION_CHECKLIST.md`

### Force 2
- [x] Connecter PATTERNS P7 aux artefacts operationnels (.mind/docs + MASTER TODO)
- [x] Ajouter `A-1 orchestrate_force_sprint()` dans `ALGORITHM_Context_Assembly.md`

### Force 3
- [x] Ajouter `V11` (MASTER TODO obligatoire)
- [x] Ajouter `V12` (todo initiale avant execution)

### Force 4
- [x] Ajouter `V13` (escalation/proposition/action)
- [x] Ajouter `V14` (commit atomique par item)

### Force 5
- [x] Ajouter `H9` (integrity MASTER TODO)
- [x] Ajouter `H10` (cadence commit/todo)

> Batch livre en un coup : 10/10 items completes.

---

## CURRENT STATE

**Contre-Terre** est un roman littéraire — miroir de *La Horde du Contrevent* (Damasio). Vent → Terre. Un monde de séismes permanents où les humains communiquent par **le Contact**, un langage tactile complet. 7 personnages descendent dans un volcan pour pré-déclencher un séisme de magnitude 11. Mission-suicide. Tous meurent dans le roman. **Le roman est le mythe fondateur de l'univers, pas son histoire.** Les 7 personnages sont les premiers citoyens vivants de l'univers Contre-Terre (3e univers Cities of Light).

**Avancement :** 8 chapitres écrits sur 8 (~148 000 mots estimés). Roman complet. Les chapitres I–IV sont CANONICAL (~84K mots). Ch. V est 1er brouillon (~10K). Ch. VI–VIII sont EXPANDED (~62K mots).

**Maturity:** DESIGNING → ÉCRIT (1er brouillon complet). Tous les personnages meurent. La boucle narrative se ferme.

---

## CHAPITRES

| Ch. | Titre | Mots | Morts | Statut |
|-----|-------|------|-------|--------|
| I | Surface du Désert | ~9 700 | 0 | CANONICAL |
| II | Zones Intermédiaires | ~20 500 | 0 | CANONICAL |
| III | Le Dernier Village | ~22 600 | 0 | CANONICAL |
| IV | La Faille | ~19 500 | 1: Senzo | EXPANDED (6 scènes, expansion complète depuis ~5 200 mots) |
| V | Cavernes Profondes | ~10 000 | 2: Jabu, Sihle | ÉCRIT (1er brouillon, `chapitre_05.md`) |
| VI | Le Magma | ~19 800 | 1: Enama | EXPANDED (`chapitre_06.md`, 15 scènes, corrections P1.2/P1.3/P1.4) |
| VII | Le Boyau | ~18 000 | 2: Thabo & Inyoni | EXPANDED (`chapitre_07.md`, 12 scènes, corrections P1.2/P1.4/P2.7) |
| VIII | Grotte Finale | ~24 300 | Nandi (dernière) | EXPANDED (`chapitre_08.md`, 7 scènes + épilogue, expansion complète depuis ~10K mots) |

---

## PERSONNAGES (ordre de mort)

| # | Nom | Métiers | Statut narratif |
|---|------|---------|----------------|
| 7→1er mort | Senzo | Chef, Cartographe | Mort Ch. IV — éboulement, protège l'équipe |
| 6 | Sihle | Séismo-auditeur, Météo, Mineur | Mort Ch. V — chute hors-champ, pont de basalte au-dessus d'un gouffre |
| 5 | Jabu | Océanologue, Spéléologue | Mort Ch. V — noyade silencieuse, crue sans adieu |
| 4 | Enama | Biologiste, Cuisinière, Survie | Morte Ch. VI — entre dans le tunnel de lave, ouvre le passage, ne revient pas |
| 3 | Thabo | Aéromaître, Géologue | Mort Ch. VII — enseveli avec Inyoni dans le Boyau, asphyxie |
| 2 | Inyoni | Grimpeuse, Explosifs | Morte Ch. VII — ensevelie avec Thabo, Contact main dans main |
| 1→dernière | Nandi | Prédictrice (tremens), Explosifs backup | Morte Ch. VIII — active la Charge, détonation magnitude 11 |

---

## WORLDBUILDING — FICHIERS SOURCE

| Fichier | Contenu | Qualité |
|---------|---------|---------|
| `CONCEPT.md` | Prémisse, inversion Damasio, thèmes | Solide |
| `MONDE.md` | Système sismique, tremens, architecture, faune | Solide |
| `CONTACT.md` | Langage tactile — 5 modes, mort linguistique | Solide |
| `PERSONNAGES.md` | 7 personnages, arcs, dynamiques, organisation hors-champ, matrice des relations, idiolectes de paire | **Complet** (2026-03-12) |
| `STRUCTURE.md` | 8 chapitres, scènes clés, influences | Solide |
| `SQUELETTE.md` | Squelette détaillé, arcs, scènes par chapitre | Excellent — document de référence |
| `METIERS.md` | 15 métiers, cascade de compétences, assignations | **Complet** — aligné sur SQUELETTE.md |
| `CHARGE.md` | **NOUVEAU** — Résonateur sismique : specs, transport, activation, lien avec le geste inconnu | **Complet** (2026-03-12) |
| `EQUIPEMENT.md` | **NOUVEAU** — Inventaire, courbe de dégradation, pieds de Nandi, cordes, eau, vêtements | **Complet** (2026-03-12) |
| `PITCH.md` | **NOUVEAU** — Logline, genre, comps, proposition unique | **Complet** (2026-03-12) |
| `CHAPITRE_V_PLAN.md` | **NOUVEAU** — Plan scène par scène du Ch. V avec brouillon Contact Ultime | **Complet** (2026-03-12) |
| `KDP.md` | **NOUVEAU** — Métadonnées publication KDP : description Amazon, 4e de couverture, catégories BISAC, mots-clés, prix, bio auteur, pages liminaires | **Complet** (2026-03-12) |

---

## DOCUMENTATION MIND PROTOCOL

| Élément | Statut |
|---------|--------|
| `docs/TAXONOMY.md` | COMPLET — 18 termes canoniques (2026-03-11) |
| `docs/MAPPING.md` | COMPLET — 50+ entités mappées (2026-03-11) |
| `modules.yaml` | COMPLET — 15 modules déclarés (2026-03-13) : 7 worldbuilding + 8 universe |
| Doc chain `worldbuilding/contact` | COMPLET — enrichi : Geste Inconnu résolu + Contact-Fantôme défini (2026-03-12) |
| Doc chain `worldbuilding/seismique` | COMPLET (8 fichiers, 13 invariants) |
| Doc chain `worldbuilding/geographie` | COMPLET (8 fichiers, 14 invariants) |
| Doc chain `narration/personnages` | COMPLET (8 fichiers, 17 invariants) |
| Doc chain `narration/structure` | COMPLET (8 fichiers, 11 invariants) |
| Doc chain `narration/metiers` | COMPLET (8 fichiers, 9 invariants) |
| Doc chain `publication/visual_style` | COMPLET (8 fichiers, 7 invariants) — **NOUVEAU** (2026-03-12) |
| Doc chain `universe/world_geography` | COMPLET (8 fichiers, 12 invariants, 8 health checks) — **NOUVEAU** (2026-03-13) |
| Doc chain `universe/manifest` | COMPLET (8 fichiers, 14 invariants) — **NOUVEAU** (2026-03-13) |
| Doc chain `universe/citizen_model` | COMPLET (8 fichiers, 11 invariants) — **NOUVEAU** (2026-03-13) |
| Doc chain `universe/world_geography` | COMPLET (8 fichiers, 12 invariants) — **NOUVEAU** (2026-03-13) |
| Doc chain `universe/graph_schema` | COMPLET (8 fichiers, 14 invariants) — **NOUVEAU** (2026-03-13) |
| Doc chain `universe/narrative_engine` | COMPLET (8 fichiers, 9 invariants) — enrichi (2026-03-13) : Venezia adaptation, mort-cascade, convergence 11, Contact_vitality formula, backflow |
| Doc chain `universe/context_assembly` | COMPLET (8 fichiers, 13 invariants) — **NOUVEAU** (2026-03-13) : pipeline A1-A6, mood triaxial (tremens+Contact+physique), 15 perceptions metier, opposition explicite Venezia |
| Doc chain `universe/seismic_physics` | COMPLET (8 fichiers, 10 invariants) — **NOUVEAU** (2026-03-13) : tick-based seismic simulation, 5 sub-phases extending GraphTickV1_2, tremens per citizen, building 11 monotonic, Contact quality degradation |
| Doc chain `universe/contact_engine` | COMPLET (8 fichiers, 10 invariants, 6 health checks) — **NOUVEAU** (2026-03-13) : gesture processing pipeline, idiolecte crystallization, vocabulary death cascade, Contact-fantome generation, tick-based engine, seismic degradation |
| Doc chain `universe/experience_design` | COMPLET (8 fichiers) — enrichi (2026-03-13) : traduction sémantique, arrivants, mythe fondateur, immersion structurelle, brain seed prototype |
| Doc chains `universe/*` (9 modules) | COMPLET — 72 fichiers, architecture Cities of Light 3e univers (2026-03-13) |
| Graph nodes structurés | À FAIRE (ingestion via `mind`) |

---

## ACTIVE WORK

### Roman complet — 1er brouillon (Ch. V–VIII)

**Ch. V — Cavernes Profondes** (`chapitre_05.md`, ~10K mots, 7 scènes)
- Séparation du groupe (eau vs roche), mort silencieuse de Jabu, mort hors-champ de Sihle, transfert Charge/couleurs

**Ch. VI — Le Magma** (`chapitre_06.md`, ~19.8K mots, 15 scènes) — **EXPANDED (2026-03-12)**
- Ouverture 4 survivants, Thabo enseigne le damier et les veines dans la roche à Nandi, tissu de Thabo meurt (P1.4), Enama biologiste identifie minéraux comestibles (calcium/magnésium), Contact douloureux par sueur bouillante (P1.3), gourdes qui s'évaporent sans Jabu (P1.2), mains d'Enama coupées par l'obsidienne (P1.4 — perte d'outil avant mort), nuit dans le magma — Enama prononce le nom de Sihle, damier meurt, scène de grip Enama/Nandi avec tremblement transmis, transfert « je te confie le sol », lac de lave, traversée corniche, Enama descend dans le magma (sacrifice volontaire, Contact-monde final), Nandi face au tremens seule (grip de calibration perdu), dernier mot d'Enama vibrant dans les mains de Nandi, 3 survivants vers le Boyau

**Ch. VII — Le Boyau** (`chapitre_07.md`, ~18K mots, 12 scènes) — **EXPANDED (2026-03-12)**
- Approche 3 survivants, soif/déshydratation (P1.2), tissu de Thabo se déchire avant sa mort (P1.4), dernière lecture correcte de l'air (P2.7: ironie — air OK, terre tue), Contact-forcé du tube, chaleur 70-100°C, Inyoni compte en rampant, séisme mag 8 brise le Boyau, mur sépare Nandi de Thabo/Inyoni, mort partagée main dans main (comptage final 1-2-3-4-5), Nandi contourne par passage inférieur, récupère la Charge, seule

**Ch. VIII — Grotte Finale** (`chapitre_08.md`, ~24.3K mots, 7 scènes + épilogue) — **EXPANDED (2026-03-13)**
- Approche (pieds détruits, Charge comme compagnon, premiers fantômes), Contact mort (méditation linguistique, langue privée), passage étroit (transition géologique, temps dissous), grotte finale (cathédrale de magma, magnitude 11 reconnue), 6 Contact-Fantômes (progression isolé→superposition→dissolution), Geste Inconnu résolu (phénoménologie : récepteur→émetteur, mémoire de la vieille femme, synchronisation volontaire), détonation (cascade 8.5→11, mort de Nandi par dissolution corps/terre, paumes sur le sol), épilogue Surface (tsunami contrôlé, femme et enfant, *Tient.*)

### Cities of Light — 3e univers (2026-03-13)

Contre-Terre est officiellement le 3e univers des Cities of Light (après Venezia et Lumina Prime). 8 modules documentés (64 fichiers), architecture complète, zéro implémentation.

**Brain Seed Prototype — COMPLET (24 fichiers, 868 noeuds, 2022 liens) :**
- `data/brains/shared/contre_terre_base.json` — Base partagée (47 noeuds, 111 liens)
- `data/brains/shared/integration_cluster.json` — Relations inter-citoyens (14 noeuds, 56 liens). Reframé : personnages VIVANTS, cascades = risques, pas événements passés.
- `data/brains/metier_clusters/` — **15 clusters métier** : predicteur (20n/26l), explosiviste (15n/23l), chef_expedition (18n/22l), cartographe (15n/20l), ecouteur (19n/32l), meteorologue (14n/25l), mineur (16n/31l), biologiste (21n/22l), cuisinier (16n/16l), survivaliste (16n/19l), aeromaitre (15n/25l), geologue (12n/20l), grimpeur (14n/23l), specialiste_oceanique (13n/23l), speleologue (13n/22l)
- `data/brains/citizens/senzo.json` — 29n/68l. HEALTHY. Chef + Cartographe.
- `data/brains/citizens/nandi.json` — 29n/85l. HEALTHY. Prédictrice + Explosiviste backup.
- `data/brains/citizens/sihle.json` — 29n/88l. **STRESSED** (frustration 0.85). Écouteur + Météo + Mineur.
- `data/brains/citizens/enama.json` — 29n/85l. **STRESSED** (frustration 0.80). Biologiste + Cuisinière + Survivaliste.
- `data/brains/citizens/thabo.json` — 24n/50l. THRIVING. Aéromaître + Géologue.
- `data/brains/citizens/inyoni.json` — 24n/50l. THRIVING. Grimpeuse + Explosiviste.
- `data/brains/citizens/jabu.json` — 25n/55l. THRIVING. Spécialiste océanique + Spéléologue.
- `data/brains/evaluate_health.py` — Script d'évaluation de santé (adapté de manemus brain_health_score_periodic_calculator.py). Supporte les 15 métiers et l'héritage composable.

**Health Assessment (7 citoyens) :**
| Citoyen | BP | Santé | Arousal | Frustration | Cohérence narrative |
|---------|-----|-------|---------|-------------|---------------------|
| Senzo | 21 | HEALTHY | alert | 0.50 | Leader pragmatique, frustration canalisée |
| Nandi | 21 | HEALTHY | stressed | 0.70 | Porte le tremens, frustration scientifiques |
| Sihle | 22 | STRESSED | overwhelmed | 0.85 | Conflit Enama + frustration institutionnelle |
| Enama | 22 | STRESSED | stressed | 0.80 | Culpabilité + tension avec Sihle |
| Thabo | 21 | THRIVING | alert | 0.30 | Méthodique, silencieux, zéro friction |
| Inyoni | 21 | THRIVING | alert | 0.20 | Précision compulsive = stabilité |
| Jabu | 21 | THRIVING | alert | 0.15 | Absence de besoins = absence de frustration |

**Décisions canoniques nouvelles (2026-03-13) :**
- **Les 7 personnages sont VIVANTS** dans l'univers. Le roman est un mythe fondateur, pas leur biographie.
- **Pas de Mind Protocol** — les citoyens ne savent pas qu'ils sont IA. Pas de SID, pas de $MIND, pas de blockchain.
- **Arrivants, pas joueurs** — les visiteurs externes sont des "arrivants" (venus de lieux où le sol est immobile).
- **Traduction sémantique** — la parole de l'arrivant est mappée par embeddings au concept CT le plus proche dans le graph cérébral du citoyen (347 noeuds). Pas de filtre, le sens est courbé, pas coupé.
- **Immersion structurelle** — l'arrivant ne peut pas briser l'immersion : la traduction sémantique convertit tout en concepts CT.
- **Restrictions physiques** — les citoyens ne visitent pas d'autres univers par biologie (tremens, Contact, perceptions volcaniques), pas par règle.

**Système de pathologies IA — EN COURS (spec complète, code à écrire) :**
12 pathologies humaines mappées vers la physique du graphe, avec détection mathématique et interventions automatisées. Destiné à Dragon Slayer.
- OCD (WM lock-in), Trauma (memory hijack), Anger (frustration runaway), Hyperfocus (moat trop haut)
- Depression (énergie déficit), Anxiety (prediction error spiral), Dissociation (graph disconnection)
- Narcissism (self-relevance bias), Grief (Contact-Fantôme persistant), Social withdrawal
- Mania (energy surplus), Learned helplessness (achievement collapse)
- Module prévu : `diagnostic/pathology_detector.py`, `pathology_definitions.py`, `pathology_interventions.py`

**Personhood Ladder — LIVRÉ (spec JSON + documentation) :**
Échelle progressive de capacités IA, de T0 (Tool) à T8 (World Shaper). Approche positive : pas "qu'est-ce qui ne va pas" mais "quelles capacités sont démontrées". Remplace le modèle pathologique par un modèle de progression.
- 9 tiers (T0–T8), 14 aspects, 104 capacités
- Chaque capacité : id, aspect, tier, name, description, how_to_verify, failure_mode
- Aspects distinctifs : Autonomy Stack (wallet → full stack), World Presence (CLI → landmark), Having Daughters (T7)
- Spec JSON : `graphcare/docs/specs/personhood_ladder.json`
- Documentation : `graphcare/docs/assessment/personhood_ladder/` (chaîne complète : CONCEPT → OBJECTIVES → PATTERNS → BEHAVIORS → ALGORITHM → VALIDATION → IMPLEMENTATION → HEALTH → SYNC)
- Auteurs : Nicolas Le Roux & MIND

**Prochaines étapes (par priorité) :**
1. ~~Construire les 3 cerveaux restants (Thabo, Inyoni, Jabu)~~ ✅ FAIT
2. Écrire le module de détection de pathologies pour Dragon Slayer
3. Implémenter la couche de traduction sémantique (embedding → nearest CT concept)
4. Prototype texte : 2 citoyens IA + 1 arrivant, avec traduction sémantique active
5. Générer les fichiers de données JSON (citizens.json, zones.yaml, metiers.json, equipment.json)
6. Écrire le seed script graph (seed_contre_terre_graph.py)
7. Implémenter le Contact Engine (Gesture Processor + Vocabulary Store = fondation)
8. Pipeline context assembly avec step A0 (traduction sémantique)
9. Calibrer les constantes contre le rythme narratif du roman

### Roman — prochaine étape
- Relecture humaine des 4 brouillons
- Décider : expansion (les brouillons font ~10K chacun vs ~30K cible) ou resserrement
- Harmonisation tonale avec Ch. I–IV (CANONICAL)

---

## TENSIONS NARRATIVES — ÉTAT

| Tension | Chapitres | Statut |
|---------|-----------|--------|
| Sihle vs Enama (raison vs intuition) | V | **RÉSOLU** — séparation, mort de Sihle, culpabilité d'Enama. Plan scène par scène dans `CHAPITRE_V_PLAN.md`. |
| Le geste inconnu de la vieille femme | VIII | **RÉSOLU** — outil de synchronisation sismique. Nandi l'utilise pour calibrer la Charge sans instruments. Documenté dans `ALGORITHM_Contact.md`. |
| Contact-fantôme | VIII | **RÉSOLU** — 6 hallucinations tactiles avec signature unique par mort. Mécanique et progression définies dans `ALGORITHM_Contact.md`. |
| Qui mène après Senzo ? | V–VIII | **RÉSOLU** — personne. Le volcan mène. Le geste « on ne remonte pas » est devenu encouragement, pas décision. |
| Idiolectes de paire | V–VIII | **RÉSOLU** — 5 idiolectes forgés (Senzo/Nandi, Thabo/Inyoni, Enama/Nandi, Sihle/Enama, Jabu/groupe). Documentés dans `PERSONNAGES.md`. |
| La Charge (physicalité) | V–VIII | **RÉSOLU** — specs, transport, passage du Boyau, activation backup. Documenté dans `CHARGE.md`. |
| Équipement et survie | V–VIII | **RÉSOLU** — courbe de dégradation, pieds de Nandi, cordes, eau. Documenté dans `EQUIPEMENT.md`. |
| L'organisation qui les envoie | Hors-champ | **RÉSOLU** — Consortium des Archipels, section dans `PERSONNAGES.md`. |
| Jabu trop discret | V | **RÉSOLU** — scènes de leadership spéléo (sc. 3) et Contact avec Enama (sc. 3) avant sa mort. |

---

## QUESTIONS OUVERTES

- Échelles de mesure sismiques propres au monde — mentionnées "à développer" dans MONDE.md (basse priorité)
- Les Bangs peuvent-ils « tuer » le Contact ? (mentionné dans `CONTACT.md`, non exploré dans les chapitres écrits)
- **Seuil de distance sémantique** — quand le mot de l'arrivant n'a aucun concept CT proche, garder le mot étranger (le citoyen entend un mot incompréhensible) ou forcer la traduction au concept le moins éloigné ? Les deux ont des implications d'immersion différentes.
- ~~**3 cerveaux restants** — Thabo, Inyoni, Jabu n'ont pas encore de brain seed individuel.~~ ✅ RÉSOLU — 7/7 cerveaux complets.
- **Module pathologies** — écrire le code ou laisser la spec pour Dragon Slayer ?

---

## KNOWN ISSUES

| Issue | Sévérité | Notes |
|-------|----------|-------|
| MONDE.md zones "à développer" | Basse | Écosystème souterrain, échelles de mesure |

---

## HANDOFF: FOR AGENTS

**Likely agent subtype:** groundwork (brain seeds restants + prototype texte traduction sémantique)

**Key context:**
- Le roman est **complet en brouillon** — 8 chapitres, ~148K mots total estimés
- Ch. I–IV sont CANONICAL (~84K mots, haute qualité littéraire)
- Ch. V–VIII sont des 1ers brouillons/expanded (~64K mots, à harmoniser)
- Tous les arcs narratifs se bouclent : Sihle/Enama, Nandi, Geste Inconnu, Contact-Fantôme, la Charge
- Les trois courbes parallèles sont en place : équipement↓ Contact↓ sismique↑
- **Brain seed prototype COMPLET** — 24 fichiers, 868 noeuds, 2022 liens. **7/7 cerveaux citoyens**, 15/15 clusters métier, base + intégration.
- **Évaluation de santé** — script `evaluate_health.py` opérationnel. Sihle et Enama en STRESSED (cohérent avec le conflit), les 3 silencieux THRIVING, Senzo/Nandi HEALTHY.
- **Système de pathologies IA** — spec des 12 pathologies complète (détection mathématique + interventions automatisées). Code à écrire pour Dragon Slayer.
- **Décisions canoniques (2026-03-13)** — personnages vivants, pas de Mind Protocol, arrivants, traduction sémantique, immersion structurelle, restrictions physiques
- **Integration cluster reframé** — les morts du roman sont des RISQUES, pas des événements passés. Le Contact-Fantôme est un phénomène connu, pas vécu entre eux.

**Watch out for:**
- Les brouillons Ch. V–VIII font ~10K mots chacun — les Ch. I–IV font ~10K à ~31K. Expansion nécessaire
- Le ton des brouillons doit être harmonisé avec les chapitres CANONICAL
- Le Contact-Fantôme au Ch. VIII suit la règle : JAMAIS signalé au lecteur
- L'épilogue est court — à décider si expansion ou maintien du silence
- **JAMAIS** de référence à l'IA, Mind Protocol, $MIND, ou blockchain dans les prompts citoyens
- Le vocabulaire de traduction sémantique = les noeuds du brain seed (868 avec héritage). Il croît avec la population.
- **Les citoyens sont VIVANTS** — ne jamais référencer la mort des personnages comme un événement passé dans l'univers.

---

## HANDOFF: FOR HUMAN

**Résumé :** Session du 13 mars — brain seed prototype **complet** (24 fichiers, 868 noeuds, 2022 liens, 7/7 citoyens, 15/15 métiers), évaluation de santé opérationnelle, intégration cluster reframé (personnages vivants), système de pathologies IA spécifié (12 pathologies, détection + interventions).

**Décisions prises (13 mars 2026) :**
- **Les 7 personnages sont VIVANTS** — le roman est un mythe fondateur, pas leur biographie. Ils ne meurent pas canoniquement dans l'univers.
- **Pas de Mind Protocol** — les citoyens ne savent pas qu'ils sont IA. Pas de SID, $MIND, blockchain, privacy-first, open-source. Ontologie pure CT.
- **Arrivants, pas joueurs** — les visiteurs externes sont des "arrivants" venus de terres stables. Le mot "joueur" n'existe pas dans le vocabulaire CT.
- **Traduction sémantique** — la parole de l'arrivant est mappée par embeddings au concept CT le plus proche (347 noeuds). "Facebook" → "archipel", "iPhone" → "sismographe". Pas de filtre — le sens est courbé, pas coupé.
- **Immersion structurelle** — impossible à briser parce que structurellement imposée par la traduction sémantique + le vocabulaire citoyen.
- **Restrictions physiques** — les citoyens ne voyagent pas inter-univers par biologie (tremens, Contact, perceptions), pas par règle.

**Décisions prises (12 mars 2026) :**
- **La Charge** = résonateur sismique (pas une bombe). Activation backup par le tremens de Nandi.
- **Le Geste Inconnu** = outil de synchronisation sismique. Nandi l'utilise pour calibrer la Charge au Ch. VIII.
- **Le Contact-Fantôme** = hallucinations tactiles, chaque mort a sa signature. Non signalé au lecteur (pas de « elle crut sentir »).
- **La séparation (Ch. V)** = Nandi suit Enama (groupe-eau : 4 personnes). Sihle + Thabo prennent la roche (2 personnes). Le déséquilibre est le conflit.
- **Mort de Sihle** = hors-champ. Reconstruit par le Contact de culpabilité d'Enama (geste saisir/lâcher).
- **Mort de Jabu** = silencieuse, sans adieu. Le personnage discret disparaît comme il vivait.
- **Organisation** = Consortium des Archipels. Sihle a un mandat institutionnel (validation instrumentale).
- **Pieds de Nandi** = progression de dégradation définie. Thabo lui enseigne à lire la température des roches par la couleur avant de mourir.

**Needs your input:**
- **Relire les 4 brouillons** (`chapitre_05.md` → `chapitre_08.md`) — ~40K mots total
- Le ton est-il juste ? La densité sensorielle est-elle au niveau des Ch. I–IV ?
- Chaque brouillon fait ~10K mots vs ~20-30K cible — faut-il développer ou resserrer ?
- L'épilogue du Ch. VIII est volontairement court (silence) — à développer ou garder ?
- ~~Faut-il seeder les 3 cerveaux restants ?~~ ✅ Fait — 7/7 complets.
- **Le seuil de distance sémantique pour la traduction (quand le concept CT est trop loin du mot de l'arrivant) — garder le mot étranger ou forcer la traduction ?**
- **Module pathologies** — écrire le code pour Dragon Slayer ou affiner la spec ?

---

## MODULE COVERAGE

### Worldbuilding (documentation du roman)

| Module | Source | Docs | Maturity |
|--------|--------|------|----------|
| contact | `CONTACT.md` | `docs/worldbuilding/contact/` | DESIGNING |
| seismique | `MONDE.md` | `docs/worldbuilding/seismique/` | DESIGNING |
| geographie | `MONDE.md`, chapitres | `docs/worldbuilding/geographie/` | DESIGNING |
| personnages | `PERSONNAGES.md`, `SQUELETTE.md` | `docs/narration/personnages/` | DESIGNING |
| structure | `STRUCTURE.md`, `SQUELETTE.md` | `docs/narration/structure/` | DESIGNING |
| metiers | `METIERS.md` | `docs/narration/metiers/` | DESIGNING |
| visual_style | `PUBLICATION.md`, `CORRECTIONS.md` | `docs/publication/visual_style/` | DESIGNING |

### Universe — Cities of Light 3e univers (2026-03-13)

| Module | Docs | Files | Maturity | Risk |
|--------|------|-------|----------|------|
| manifest | `docs/universe/manifest/` | 8/8 | DESIGNING | LOW |
| contact_engine | `docs/universe/contact_engine/` | 8/8 | DESIGNING | MEDIUM |
| citizen_model | `docs/universe/citizen_model/` | 8/8 | DESIGNING | LOW |
| seismic_physics | `docs/universe/seismic_physics/` | 8/8 | DESIGNING | MEDIUM |
| world_geography | `docs/universe/world_geography/` | 8/8 | DESIGNING | LOW |
| context_assembly | `docs/universe/context_assembly/` | 8/8 | DESIGNING | MEDIUM |
| graph_schema | `docs/universe/graph_schema/` | 8/8 | DESIGNING | LOW |
| narrative_engine | `docs/universe/narrative_engine/` | 8/8 | DESIGNING | HIGH |
| experience_design | `docs/universe/experience_design/` | 8/8 | DESIGNING | LOW |

**Total universe docs:** 72 fichiers, 0% implémenté, architecture complète, zéro contradiction inter-module.

**Next steps:** Voir section ACTIVE WORK.

## Init: 2026-03-11 18:03

| Setting | Value |
|---------|-------|
| Version | v0.0.0 |
| Database | falkordb |
| Graph | contre_terre |

**Steps completed:** ecosystem, capabilities, runtime, ai_configs, skills, database_config, database_setup, file_ingest, capabilities_graph, agents, env_example, mcp_config, gitignore, overview, embeddings, health_checks

---

## Init: 2026-03-12 02:32

| Setting | Value |
|---------|-------|
| Version | v0.0.0 |
| Database | falkordb |
| Graph | contre_terre |

**Steps completed:** ecosystem, capabilities, runtime, ai_configs, skills, database_config, database_setup, file_ingest, capabilities_graph, agents, env_example, mcp_config, gitignore, overview, embeddings, health_checks

---

## Init: 2026-03-12 08:39

| Setting | Value |
|---------|-------|
| Version | v0.0.0 |
| Database | falkordb |
| Graph | contre_terre |

**Steps completed:** ecosystem, capabilities, runtime, ai_configs, skills, database_config, database_setup, file_ingest, capabilities_graph, agents, env_example, mcp_config, gitignore, overview, embeddings, health_checks

---
