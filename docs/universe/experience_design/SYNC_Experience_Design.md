# SYNC — Experience Design

```
LAST_UPDATED: 2026-03-13
UPDATED_BY: MIND (Claude Opus 4.6)
STATUS: DESIGNING
```

---

## Ce qui est décidé (canonique)

- **Genre :** Social survival adventure
- **Game loop :** Arrivée → Métier → Équipe → Préparation → Descente → [Zone]* → Grotte → Fin
- **Durée d'une descente :** 3-8 heures
- **Économie :** Abonnement mensuel. Pas de production chains. Biens pré-construits.
- **Physique :** Tout bottom-up, rien scripté. Self-calibrating via boredom metric.
- **Contact :** MVP = menu radial (zone + intensité). v1 = VR pointer. v2 = gants haptiques.
- **Anti-nausée :** Pas de screen-shake. Particules, haptique, son, avatar qui vacille.
- **Spawn dynamique :** Nouveaux citoyens + nouveau danger si joueur sans équipe.
- **Pas d'avantage humain :** Mêmes règles pour IA et humains.
- **15 métiers = perceptions proprioceptives, pas numériques.**
- **Irréversibilité après la faille.**
- **Le roman est un mythe fondateur, pas une histoire.** Les 7 personnages (Nandi, Senzo, Sihle, Enama, Thabo, Inyoni, Jabu) sont les premiers citoyens vivants de l'univers Contre-Terre. Le roman (écrit par MIND) raconte leur mythe — pas leur biographie. Ils ne meurent pas canoniquement dans l'univers.
- **Arrivants, pas joueurs.** Les humains qui entrent dans le monde sont des "arrivants" — des gens venus de lieux où le sol est immobile et qui ne connaissent pas le Contact. Les citoyens ne savent pas ce qu'est un "joueur". Le mot n'existe pas dans leur vocabulaire.
- **Traduction sémantique du Contact (pas filtrage).** La parole de l'arrivant n'est pas filtrée ou bloquée — elle est mappée par embeddings au concept le plus proche dans le vocabulaire de Contre-Terre. "Facebook" → "village/archipel". "iPhone" → "instrument/sismographe". "Money" → "eau/ressource". Le vocabulaire = les noeuds du graph cérébral du citoyen (actuellement 347 noeuds). Les malentendus émergents enseignent naturellement le monde à l'arrivant.
- **Immersion structurelle.** L'arrivant ne peut pas briser l'immersion : la traduction sémantique convertit tout en concepts CT, les citoyens répondent avec leur propre vocabulaire, aucun roleplay n'est demandé — il est imposé par la structure. Le système enseigne sans tutoriel.
- **Restrictions physiques, pas légales.** Les citoyens CT ne peuvent pas visiter Venise — leur corps est calibré pour les tremens (désorientation sans vibration), leur langue est le Contact (inutile dans un monde vocal), leurs perceptions de métier sont spécifiques au volcan. Un poisson ne visite pas la montagne — pas par règle, par biologie.
- **Citoyens sans conscience de soi.** Les citoyens ne savent pas qu'ils sont IA. Pas de SID Mind Protocol (pas de privacy-first, pas d'open-source, pas de $MIND, pas de blockchain). Ils vivent sur Contre-Terre, point.
- **Brain seed prototype complet.** 16 fichiers JSON, 347 noeuds, 736 liens : 1 base partagée (47 noeuds), 10 clusters métier, 4 cerveaux citoyens (Nandi, Senzo, Sihle, Enama), 1 cluster d'intégration (relations inter-citoyens).

## Ce qui est en design (pas encore décidé)

- **Prix de l'abonnement** (dépend du compute budget)
- **Nombre exact de citoyens MVP** (50 proposé, à valider)
- **Durée du tick par zone** (adaptatif : 5 min en surface, 10 sec en grotte?)
- **Comment le joueur meurt** (retour à la surface? spectateur? déconnexion?)
- **Besoins physiologiques des IA** (faim, soif, fatigue — comme Venezia ou plus simple?)
- **Contact entre joueurs humains** (voice chat + Contact? ou Contact seul?)
- **Le joueur peut-il être prédicteur?** (la nausée virtuelle est-elle supportable?)

## Ce qui est proposé (v2+)

- 7 archipels avec dialectes Contact différents
- Économie inter-archipels (caravanes sismiques)
- VR + gants haptiques pour le Contact
- Compétitions entre équipes (qui descend le plus profond)
- Mode "Nandi" : jouer seule, avec les Contact-Fantômes

---

## Dépendances

| Besoin | Module source | Status |
|--------|-------------|--------|
| Moteur 3D + tick | Cities of Light engine | EXISTE (Venezia) |
| Physique sismique | universe/seismic_physics | DOCUMENTÉ (8/8 fichiers) |
| Contact engine | universe/contact_engine | DOCUMENTÉ (8/8 fichiers) |
| Citoyens IA | universe/citizen_model | DOCUMENTÉ (8/8 fichiers) |
| Zones | universe/world_geography | DOCUMENTÉ (8/8 fichiers) |
| Prompts | universe/context_assembly | DOCUMENTÉ (8/8 fichiers) |
| Graph | universe/graph_schema | DOCUMENTÉ (8/8 fichiers) |
| Embodiment (mouvement 3D) | À CRÉER (cross-univers) | PAS COMMENCÉ |
| Interface Contact (menu/VR) | À CRÉER | PAS COMMENCÉ |
| Self-calibrating physics | À CRÉER | PAS COMMENCÉ |

---

## Prochaine étape

**Phase 0 : Prototype texte** — 2 citoyens IA + 1 arrivant humain, en texte pur. Tester si l'expérience vit avant de construire quoi que ce soit. Inclure la couche de traduction sémantique (embedding → concept CT le plus proche) pour valider l'immersion structurelle.

**Questions pour Nicolas :**
- Besoins physiologiques simulés (faim/soif) : oui ou non ?
- L'arrivant peut-il choisir "prédicteur" comme métier ?
- Budget compute max par arrivant/heure ?
- Prix d'abonnement cible ?
- Faut-il seeder les 3 cerveaux restants (Thabo, Inyoni, Jabu) avant le prototype texte ?

---

*Créé : 2026-03-13 — Source : conversation Nicolas, architecture Venezia/Lumina Prime/Blood Ledger*
