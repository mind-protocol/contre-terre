# IMPLEMENTATION -- Context Assembly

> Architecture du code. Ou les donnees vivent, comment elles circulent, ou le pipeline se branche.

---

## Pipeline : Vue Module

```
citizen_model ─────────┐
                       │
contact_engine ────────┤
                       │
seismic_physics ───────┼───→ context_assembly ───→ prompt (system + context block)
                       │
world_geography ───────┤
                       │
narrative_engine ──────┘
```

Le pipeline `context_assembly` est un assembleur -- il ne possede pas de donnees. Il les tire des 5 modules source, les transforme en blocs de texte, et produit un prompt pret pour le LLM. C'est un pipeline de lecture, pas un pipeline de stockage.

---

## Modules Source

### citizen_model

**Fournit :** `tremens_sensitivity` (Hz, constante natale), `metiers` (liste de metiers), `idiolect` (gestes propres), `pair_idiolects` (idiolectes de paire, cle = partenaire), `extremity_state` (pieds, mains, peau).

**Format :** Objet `Citizen` avec champs structures. Les idiolectes de paire sont indexes par partenaire et portent un flag `is_alive`.

**Point d'attention :** Les partenaires morts restent dans le modele mais sont marques. Le pipeline doit filtrer les vivants pour `active_idiolects` et utiliser le passe pour les morts.

### contact_engine

**Fournit :** `recent_interactions` (liste des Contacts des dernieres N heures). Chaque interaction : `{partner, gestures[], registers_reached[], timestamp}`.

**Format :** Liste chronologique. Le pipeline calcule la saturation (nombre de partenaires x diversite de registres) et les partenaires recents.

**Point d'attention :** Les registres sont des zones du corps (epaule, bras, main, nuque), pas des labels emotionnels. Le trust derive de la profondeur des registres atteints, pas d'un score.

### seismic_physics

**Fournit :** `current_magnitude`, `recent_events` (liste de seismes recents), `trend` (montante / descendante / stable), `background_frequency` (Hz).

**Format :** Sortie de `query_seismic_situation(zone_id)`. Les evenements recents sont filtres sur 1 heure.

**Point d'attention :** Ce module n'a pas d'equivalent dans Venezia. Il est specifique a Contre-Terre et alimente le bloc `[LE SOL]` qui est un invariant non-coupable (VALIDATION V2).

### world_geography

**Fournit :** `temperature` (celsius), `air_quality` (% O2), `seismic_frequency` (Hz de la zone).

**Format :** Proprietes de la zone courante du citoyen. La frequence sismique locale est comparee a la calibration natale pour calculer le tremens.

### narrative_engine

**Fournit :** `personal_beliefs` (croyances du citoyen dans le graph), `zone_narratives` (rumeurs de la zone, croyances des autres citoyens a proximite).

**Format :** Requetes FalkorDB sur le graph. Les croyances sont sismiques et relationnelles, pas economiques (VALIDATION V1).

---

## Structure du Prompt

Le pipeline produit deux blocs :

### System Prompt (~250-350 tokens)

```
[QUI TU ES]     -- nom, metiers comme filtres sensoriels
[TON CORPS]     -- tremens natal, etat des extremites
[TA LANGUE]     -- Contact : gestes universels + idiolecte
[TON MONDE]     -- substrat sismique, Contact comme langue
[REGLES]        -- spatial audio, pas d'assistant, pas de markdown
```

Le system prompt est stable entre les interactions -- il change rarement (seulement quand un partenaire meurt ou qu'une extremite se degrade). Il definit l'identite permanente du citoyen.

### Context Block (~340-570 tokens)

```
[TON ETAT PHYSIQUE]   -- tremens + pieds + mains + temperature + air + filtre metier
[TON CONTACT RECENT]  -- saturation, partenaires, registres, idiolectes vivants
[TON ETAT]            -- mood emerge (descripteurs corporels, intensite)
[LE SOL]              -- magnitude, tendance, frequence de fond, seismes recents
[CE QUE TU CROIS]     -- croyances personnelles + rumeurs de zone
[COMMENT REPONDRE]    -- contraintes Contact + registre du metier
[CE QU'ILS T'ONT DIT] -- parole du visiteur
```

Le context block change a chaque interaction. C'est l'etat ephemere -- ce que le citoyen sent maintenant.

---

## Token Budget

Cible totale : < 1500 tokens (system + context). Marge confortable a 590-920 tokens estimes.

**Priorite de coupe (si depassement) :**
1. `[CE QUE TU CROIS]` -- les croyances enrichissent mais ne fondent pas l'identite
2. `[COMMENT REPONDRE]` -- reduction des exemples, pas des contraintes
3. Jamais : `[LE SOL]` (VALIDATION V2), `[TON ETAT PHYSIQUE]`, `[TON CONTACT RECENT]`

---

## Adaptation depuis Venezia

Le pipeline s'adapte depuis `poc_mind_context_assembly.py` (Venezia) avec les substitutions suivantes :

| Venezia | Contre-Terre | Nature du changement |
|---------|-------------|---------------------|
| `compute_financial_state()` | `compute_physical_state()` | Remplacement complet -- corps au lieu d'economie |
| `SocialClass` → registre vocale | `metiers` → filtre sensoriel | La perception remplace le statut |
| `TrustScore` (0-100) | Historique Contact (registres atteints) | Qualitatif au lieu de numerique |
| `Ekman mood scores` | `MOOD_MATRIX` triaxial | Mood corporel, pas psychologique |
| `recent_interactions` (social) | `recent_interactions` (Contact) | Le toucher remplace la conversation |
| Pas d'equivalent | `query_seismic_situation()` | Module entierement nouveau |

La structure globale (system prompt + context block + LLM call) reste identique. Ce qui change est le contenu des blocs et la source des donnees.

---

*Sources : `poc_mind_context_assembly.py` (Venezia), `ALGORITHM_Context_Assembly.md`, `OBJECTIVES_Context_Assembly.md`*
