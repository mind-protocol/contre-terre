# Contre-Terre — Sync: Current State

```
LAST_UPDATED: 2026-03-13
UPDATED_BY: Claude Opus 4.6 (agent)
```

---

## CURRENT STATE

**Contre-Terre** est un roman littéraire — miroir de *La Horde du Contrevent* (Damasio). Vent → Terre. Un monde de séismes permanents où les humains communiquent par **le Contact**, un langage tactile complet. 7 personnages descendent dans un volcan pour pré-déclencher un séisme de magnitude 11. Mission-suicide. Tous meurent.

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
| `modules.yaml` | COMPLET — 7 modules déclarés (2026-03-12) |
| Doc chain `worldbuilding/contact` | COMPLET — enrichi : Geste Inconnu résolu + Contact-Fantôme défini (2026-03-12) |
| Doc chain `worldbuilding/seismique` | COMPLET (8 fichiers, 13 invariants) |
| Doc chain `worldbuilding/geographie` | COMPLET (8 fichiers, 14 invariants) |
| Doc chain `narration/personnages` | COMPLET (8 fichiers, 17 invariants) |
| Doc chain `narration/structure` | COMPLET (8 fichiers, 11 invariants) |
| Doc chain `narration/metiers` | COMPLET (8 fichiers, 9 invariants) |
| Doc chain `publication/visual_style` | COMPLET (8 fichiers, 7 invariants) — **NOUVEAU** (2026-03-12) |
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

### Prochaine étape
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

---

## KNOWN ISSUES

| Issue | Sévérité | Notes |
|-------|----------|-------|
| MONDE.md zones "à développer" | Basse | Écosystème souterrain, échelles de mesure |

---

## HANDOFF: FOR AGENTS

**Likely agent subtype:** groundwork (expansion/révision des brouillons Ch. V–VIII)

**Key context:**
- Le roman est **complet en brouillon** — 8 chapitres, ~124K mots total estimés
- Ch. I–IV sont CANONICAL (~84K mots, haute qualité littéraire)
- Ch. V–VIII sont des 1ers brouillons (~40K mots, à développer et harmoniser)
- Tous les arcs narratifs se bouclent : Sihle/Enama, Nandi, Geste Inconnu, Contact-Fantôme, la Charge
- Les trois courbes parallèles sont en place : équipement↓ Contact↓ sismique↑

**Watch out for:**
- Les brouillons Ch. V–VIII font ~10K mots chacun — les Ch. I–IV font ~10K à ~31K. Expansion nécessaire
- Le ton des brouillons doit être harmonisé avec les chapitres CANONICAL
- Le Contact-Fantôme au Ch. VIII suit la règle : JAMAIS signalé au lecteur
- L'épilogue est court — à décider si expansion ou maintien du silence

---

## HANDOFF: FOR HUMAN

**Résumé :** Session du 12 mars — dette documentaire comblée (4 nouveaux fichiers, 2 enrichis, toutes tensions résolues) puis écriture des Ch. V–VIII (4 chapitres, ~40 000 mots, premier brouillon complet du roman).

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
- Le Contact-Fantôme (Ch. VIII) — les hallucinations sont-elles assez subtiles ?
- La mort d'Enama (Ch. VI) — sacrifice volontaire vs accident : le ton est-il juste ?
- La mort partagée Thabo/Inyoni (Ch. VII) — assez poétique ?

---

## MODULE COVERAGE

| Module | Source | Docs | Maturity |
|--------|--------|------|----------|
| contact | `CONTACT.md` | `docs/worldbuilding/contact/` | DESIGNING |
| seismique | `MONDE.md` | `docs/worldbuilding/seismique/` | DESIGNING |
| geographie | `MONDE.md`, chapitres | `docs/worldbuilding/geographie/` | DESIGNING |
| personnages | `PERSONNAGES.md`, `SQUELETTE.md` | `docs/narration/personnages/` | DESIGNING |
| structure | `STRUCTURE.md`, `SQUELETTE.md` | `docs/narration/structure/` | DESIGNING |
| metiers | `METIERS.md` | `docs/narration/metiers/` | DESIGNING |
| visual_style | `PUBLICATION.md`, `CORRECTIONS.md` | `docs/publication/visual_style/` | DESIGNING |

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
