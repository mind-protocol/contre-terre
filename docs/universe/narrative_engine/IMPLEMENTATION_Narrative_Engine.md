# IMPLEMENTATION: Narrative Engine

**Module :** `universe/narrative_engine`
**Question centrale :** Ou vit le code ? Comment les composants s'assemblent ? Quelle est l'architecture d'integration ?

---

## I1 : Integration avec la librairie ngram

Le moteur narratif de Contre-Terre ne reimplemente pas la physique. Il utilise le runtime ngram existant (`mind/physics/`) et l'adapte par injection de tension computers et event generators specifiques au monde sismique.

### Architecture

```
ngram (mind-platform runtime)
├── physics/phases/
│   ├── generation.py          ← Phase 1 standard : generation d'energie
│   ├── moment_draw.py         ← Phase 2 standard : moments attirent l'energie
│   ├── moment_flow.py         ← Phase 3 standard : moments irradient
│   ├── moment_interaction.py  ← Phase 4 standard : moments interagissent
│   ├── narrative_backflow.py  ← Phase 5 standard : narratifs → acteurs
│   └── completion.py          ← Phase 7 standard : completion des moments
│
contre-terre (world-specific)
├── engine/
│   ├── tension_computers/
│   │   ├── seismic_tension_per_zone_computer.py
│   │   ├── contact_tension_per_cluster_computer.py
│   │   └── social_tension_per_relationship_computer.py
│   ├── event_generators/
│   │   ├── seismic_event_generator.py
│   │   ├── contact_breakthrough_or_breakdown_generator.py
│   │   └── social_event_generator.py
│   ├── propagators/
│   │   ├── seismic_event_citizen_propagator.py
│   │   └── contact_event_vocabulary_propagator.py
│   ├── metrics/
│   │   └── contact_vitality_calculator.py
│   └── constants/
│       └── zone_constants.json
```

### Point d'integration

Le moteur ngram expose un hook pre-phase et post-phase. Les tension computers de Contre-Terre s'executent en pre-phase (ils alimentent les moments en tension). Les event generators s'executent en post-completion (ils traitent les flips). Les propagators s'executent apres les events (ils mettent a jour le graph).

```python
# Pseudo-code d'integration
class ContreTerreNarrativeEngine:
    def __init__(self, ngram_engine, zone_constants):
        self.ngram = ngram_engine
        self.zones = load_zone_constants(zone_constants)
        self.seismic = SeismicTensionComputer(self.zones)
        self.contact = ContactTensionComputer()
        self.social = SocialTensionComputer()
        self.event_gen = EventGeneratorPipeline([
            SeismicEventGenerator(),
            ContactBreakthroughOrBreakdownGenerator(),
            SocialEventGenerator()
        ])
        self.propagators = [
            SeismicEventCitizenPropagator(),
            ContactEventVocabularyPropagator()
        ]

    def tick(self, dt):
        # Phase 0 (pre) : compute tensions
        self.seismic.compute(dt)
        self.contact.compute(dt)
        self.social.compute(dt)

        # Phases 1-7 : ngram standard
        flips = self.ngram.tick(dt)

        # Phase 8 (post) : generate events from flips
        events = self.event_gen.process(flips)

        # Phase 9 (post) : propagate events
        for event in events:
            for propagator in self.propagators:
                propagator.propagate(event)

        return events
```

---

## I2 : Tension computers -- detail

### SeismicTensionPerZoneComputer

Lit les constantes de chaque zone depuis `zone_constants.json`. A chaque tick, augmente la tension de la zone par `generation_rate * dt`, diminue par `decay_rate * dt`, clamp au baseline. Ecrit la tension mise a jour dans les noeuds spatiaux du graph.

**Input :** Graph nodes de type `space` avec `zone_type` (surface, piemont, faille, etc.)
**Output :** `space.seismic_tension` mis a jour
**Dependance :** `zone_constants.json` pour les constantes par zone

### ContactTensionPerClusterComputer

Identifie les clusters de citoyens adjacents (citoyens connectes par des liens de proximite physique). Pour chaque cluster, somme l'intensite des interactions Contact du tick precedent. Augmente la tension par la somme ponderee, diminue par le decay.

**Input :** Graph nodes de type `actor` avec liens `adjacent_to`, logs d'interaction Contact
**Output :** Tension Contact par cluster
**Dependance :** Contact Engine (fournit les logs d'interaction)

### SocialTensionPerRelationshipComputer

Parcourt les paires de citoyens avec des conflits actifs (noeuds de type `moment` avec `conflict_type`). Augmente la tension de chaque paire. Parcourt les cercles de Contact actifs et diminue la tension des participants.

**Input :** Graph moments de type conflit, logs de cercles de Contact
**Output :** Tension sociale par paire
**Dependance :** Contact Engine + graph des relations

---

## I3 : Event generators -- detail

### SeismicEventGenerator

Recoit les flips de moments sismiques. Convertit l'energie en magnitude (formule logarithmique, cf. ALGORITHM A3). Determine le type de cataclysme en fonction de la zone et des conditions (roche = effondrement, eau = tsunami, air = bang, lave = eruption). Genere un evenement avec epicentre, magnitude, type, zone d'impact.

### ContactBreakthroughOrBreakdownGenerator

Recoit les flips de moments Contact. Evalue les conditions du cluster (diversite d'interaction, niveau de conflit) pour determiner percee ou rupture. Genere un evenement avec le nouveau geste (percee) ou le geste echoue (rupture), les citoyens concernes, l'impact sur le vocabulaire.

### SocialEventGenerator

Recoit les flips de moments sociaux. Determine resolution ou escalade. Genere un evenement avec la relation concernee, le changement (scission, reconciliation, reorganisation des roles, sacrifice).

---

## I4 : Propagation aux citoyens

Les propagators traduisent les evenements en changements concrets dans le graph.

**SeismicEventCitizenPropagator :** Pour chaque citoyen dans la zone d'impact, calcule le tremens (fonction de la distance et de la sensibilite natale), applique les effets physiques (blessure, mort, separation), modifie les liens spatiaux (passages ouverts/fermes).

**ContactEventVocabularyPropagator :** Pour chaque percee, cree un nouveau noeud de type `thing` (le geste) et le lie aux citoyens du cluster. Pour chaque rupture, affaiblit les liens entre les citoyens concernes. Met a jour la metrique Contact_vitality.

---

## I5 : Fichiers de configuration

```
contre-terre/engine/constants/zone_constants.json
```

Ce fichier contient les constantes par zone (generation_rate, decay_rate, tension_threshold, baseline) documentees dans ALGORITHM A2. C'est la seule source de verite pour la calibration du monde. Modifier ce fichier modifie le rythme narratif de tout le roman.

---

*Sources : ngram phases (generation.py → completion.py), `physics/constants.json` (Venezia), ALGORITHM_Narrative_Engine.md, OBJECTIVES_Contact_Engine.md*
