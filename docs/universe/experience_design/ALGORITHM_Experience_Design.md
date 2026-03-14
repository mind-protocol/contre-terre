# ALGORITHM — Experience Design

> Comment ça marche. Les mécanismes concrets.

---

## A1 : Game Loop — la boucle centrale

```
ARRIVE → CHOISIR_METIER → FORMER_EQUIPE → PREPARER → DESCENDRE → [ZONE_N → ZONE_N+1]* → GROTTE_FINALE → FIN
                                                                      ↓ (mort)
                                                                  SPECTATEUR → SURFACE → RECOMMENCER
```

**Durée totale d'une descente :** 3-8 heures (selon la profondeur atteinte et le rythme de l'équipe).

**Conditions de fin :**
- **Victoire :** Quelqu'un active la Charge dans la grotte finale → séisme magnitude 11 contrôlé → le monde est sauvé
- **Défaite :** Toute l'équipe meurt avant d'atteindre la grotte → la mission échoue → une autre équipe devra essayer
- **Abandon :** L'équipe décide de remonter (possible uniquement avant la faille — après, irréversible)

---

## A2 : Self-Calibrating Seismic — la physique qui s'auto-régule

Le cœur du système. La physique sismique suit une courbe de pacing narratif, mais les événements individuels sont physiques (pas scriptés).

**Input :** Score de boredom/engagement des citoyens IA (extractible en temps réel).

```
engagement_score = moyenne(
    interaction_frequency,      // combien de Contact par tick
    vocabulary_growth,          // est-ce que l'idiolecte s'enrichit
    movement_diversity,         // est-ce qu'ils explorent ou stagnent
    emotional_intensity         // stress, excitation, peur
)
```

**Courbe cible :** Montée progressive avec des pics et des plateaux.

```
target_tension(t) = baseline + amplitude * sin(frequency * t) * (t / total_duration)^exponent
```

- `baseline` = tension de fond (magnitude 4-5, toujours présente)
- `amplitude` = force des oscillations (augmente avec la profondeur)
- `frequency` = fréquence des cycles tension/relâchement (augmente avec la profondeur)
- `exponent` = accélération vers le climax (> 1.0 → exponentielle)

**Calibration :** Si `engagement_score` < seuil → la physique accélère la montée de tension. Si `engagement_score` > seuil → la physique maintient le plateau actuel. Le système ne fabrique pas d'événements — il ajuste la vitesse à laquelle la tension s'accumule, et la physique fait le reste.

---

## A3 : Spawn Dynamique — le monde qui peuple à la demande

```
SI joueur_sans_equipe ET temps_attente > 2min:
    1. Instancier 4-6 citoyens IA (métiers complémentaires, personnalités variées)
    2. Augmenter tension_sismique dans une zone du volcan
    3. Les citoyens commencent à discuter entre eux de la menace
    4. Un citoyen approche le joueur : proposition d'équipe
    5. Si le joueur accepte → formation d'équipe → préparation → descente
```

**Règles de spawn :**
- Les métiers couvrent les essentiels (prédicteur, écouteur, géologue minimum)
- Les personnalités sont tirées d'un pool de templates (courageux, prudent, scientifique, mystique, pragmatique)
- Les relations entre les nouveaux citoyens sont initialisées (certains se connaissent, d'autres non)
- Le danger sismique est réel (pas simulé pour l'occasion — la physique génère une vraie montée de tension)

---

## A4 : Économie de surface — marchands et équipement

**Structure :**
- 3-5 marchands IA à la surface (permanents, personnalités distinctes)
- Inventaire de base : cordes, bâtons chimiques, eau, nourriture, vêtements résistants
- Inventaire rare : la Charge (résonateur sismique — 1 par équipe), sismographe, matériel de grimpe
- Prix en monnaie locale (tokens d'aventure, gagnés par abonnement)

**Pas de production chain :** Les biens arrivent "par bateau" (importés). Le joueur ne voit pas la chaîne de production. Il voit un marchand avec un étal.

---

## A5 : Compute Budget — ce qui coûte quoi

**Par citoyen IA actif :**
- 1 appel LLM par interaction significative (Contact, décision, conversation)
- Autopilot pour les déplacements routiniers (pathfinding simple, pas de LLM)
- Perception sensorielle = query sur l'état du monde (pas de LLM, juste des données)
- Réaction aux séismes = règles physiques (pas de LLM)

**Estimation par équipe de 6-8 (1-2 humains + 4-6 IA) :**
- En préparation (surface) : ~10 appels LLM/minute (conversations, négociations)
- En descente (calme) : ~3 appels LLM/minute (Contact, observations)
- En crise (séisme) : ~1 appel LLM/minute (réactions physiques, pas de conversation)
- Pic : ~15 appels LLM/minute (mort d'un coéquipier, décisions critiques)

**Optimisations :**
- Autopilot pour 90% du mouvement (pas de LLM pour marcher)
- Réactions physiques pré-calculées (tremens, nausée, Contact dégradé → pas de LLM)
- LLM uniquement pour les décisions sociales, les conversations, le Contact significatif
- Cache de personnalité : le prompt du citoyen est pré-assemblé, pas recalculé à chaque appel

**Population idle (surface, pas en mission) :** ~1 appel LLM/5 minutes (vie quotidienne, interactions entre eux)

---

## A6 : Scale — combien de quoi

**MVP (v0) :**
- 1 archipel de surface (50 citoyens IA)
- 5 marchands
- 1 centre d'info (maire)
- 1 entrée de volcan → 9 zones
- Max 3 équipes simultanées dans le volcan
- Max 10 joueurs humains connectés simultanément

**v1 :**
- 3 archipels de surface (150 citoyens IA)
- Dialectes Contact différents par archipel
- Max 10 équipes simultanées
- Max 50 joueurs humains

**v2 :**
- 7 archipels (toute la surface)
- 500+ citoyens IA
- Économie inter-archipels (caravanes)
- Max 100 joueurs humains

---

## A7 : Contact humain — interface sans gants VR

**MVP (écran + clavier/manette) :**
- Menu radial contextuel : {épaule, bras, main, nuque, front, sol}
- Le joueur sélectionne la zone → l'avatar fait le geste
- L'intensité est déduite du contexte (urgence = fort, conversation = doux)
- Le feedback est visuel (animation) + haptique (vibration manette) + sonore

**v1 (VR sans gants) :**
- Le joueur pointe la zone du corps de l'autre avatar avec le contrôleur VR
- La durée du toucher est le temps de maintien du trigger
- L'intensité est la force du press

**v2 (VR avec gants haptiques) :**
- Contact direct. Le joueur sent la pression, la chaleur, le rythme.
- L'idiolecte se forme naturellement par la répétition des gestes.

---

*Algorithmes dérivés de : conversation Nicolas 2026-03-13, architecture Venezia (tick, spawn, marchands), physique self-calibrating*
