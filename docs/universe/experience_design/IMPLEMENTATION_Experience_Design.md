# IMPLEMENTATION — Experience Design

> Où est le code. Quels systèmes construire. Dans quel ordre.

---

## Architecture — les 4 couches

```
┌─────────────────────────────────────────────────┐
│  COUCHE 4 : EXPERIENCE                          │
│  UI/UX, Contact interface, visual feedback,     │
│  anti-nausée, HUD métier                        │
├─────────────────────────────────────────────────┤
│  COUCHE 3 : SOCIAL                              │
│  IA citoyens (Claude), Contact engine,          │
│  idiolectes, spawn dynamique, marchands         │
├─────────────────────────────────────────────────┤
│  COUCHE 2 : PHYSIQUE                            │
│  Sismique (self-calibrating), zones,            │
│  température, oxygène, géologie dynamique       │
├─────────────────────────────────────────────────┤
│  COUCHE 1 : MOTEUR                              │
│  Cities of Light engine (Three.js/WebXR),       │
│  tick system, graph (FalkorDB), embodiment      │
└─────────────────────────────────────────────────┘
```

**Couche 1** existe déjà (Venezia l'utilise). On l'étend.
**Couche 2** est le cœur de Contre-Terre — physique sismique pure.
**Couche 3** est ce qui rend le monde vivant — les citoyens IA.
**Couche 4** est ce que le joueur voit et touche.

---

## Ordre d'implémentation (Experience First)

### Phase 0 : Prototype d'expérience (PRIORITÉ IMMÉDIATE)

**But :** Tester l'expérience avant de construire l'infrastructure.

1. **2 citoyens IA + 1 joueur humain, en texte**
   - Pas de 3D. Pas de moteur. Juste des prompts.
   - Le joueur décrit ses actions. Les IA répondent.
   - Le Contact est simulé par description ("je pose ma main sur ton épaule").
   - Un séisme est annoncé par le "game master" (script simple).
   - **Question à valider :** Est-ce que ça vit ? Est-ce que l'idiolecte se forme ? Est-ce que la mort d'un IA est émotionnellement significative ?

2. **5 citoyens IA + 2 joueurs humains, en texte + images générées**
   - Le monde est décrit textuellement + illustrations statiques par zone
   - Le Contact est un menu (choix de zone du corps + intensité)
   - La physique sismique tourne (script Python, un séisme tous les X minutes)
   - **Question à valider :** Est-ce que le rythme fonctionne ? Est-ce que les joueurs ont envie de continuer ?

### Phase 1 : Monde minimal jouable

3. **Surface + 3 premières zones du volcan, en 3D basique**
   - Three.js, pas WebXR (écran d'abord)
   - 50 citoyens IA à la surface, 1 entrée de volcan
   - Contact via menu radial
   - Physique sismique self-calibrating
   - Marchands, centre d'info, spawn dynamique

### Phase 2 : Descente complète

4. **9 zones du volcan, physique complète**
   - Bioluminescence, dégradation visuelle, zones obscures
   - Contact-corde, Contact-monde, Contact-fantôme
   - 15 métiers avec perceptions sensorielles
   - Mort définitive, cascade de compétences
   - Grotte finale et activation de la Charge

### Phase 3 : Scale et polish

5. **Multiples archipels, VR, gants haptiques**
   - 7 archipels avec dialectes différents
   - WebXR pour VR
   - Interface Contact avancée
   - Économie inter-archipels

---

## Dépendances cross-univers

| Système | Partagé avec | Contre-Terre spécifique |
|---------|-------------|------------------------|
| Moteur 3D (Three.js) | Tous les univers | Zones verticales, bioluminescence |
| Tick system | Tous les univers | Tick adaptatif (plus court en profondeur) |
| Graph (FalkorDB) | Tous les univers | Contact links, tremens properties |
| Embodiment | Tous les univers | Contact gestuel (unique à CT) |
| LLM calls | Tous les univers | Prompts Contact-first (unique à CT) |
| Spawn dynamique | Potentiellement tous | Séisme-triggered (unique à CT) |
| Pathfinding | Tous les univers | 3D vertical (unique à CT) |

---

## Fichiers à créer (Phase 0)

```
scripts/
  prototype_text_adventure.py    # Prototype texte : 2 IA + 1 humain
  seismic_simple.py              # Physique sismique minimale (tension → séisme)
  contact_menu.py                # Interface Contact texte (zone + intensité)
data/
  citizens_prototype.json        # 2-5 citoyens IA avec personnalités
  zones_prototype.json           # 3 zones (surface, caverne, faille)
prompts/
  citizen_base_prompt.md         # Prompt de base citoyen Contre-Terre
  metier_perception_prompts/     # 1 prompt par métier (15 fichiers)
```

---

*Architecture dérivée de : Cities of Light engine (Venezia), conversation Nicolas 2026-03-13*
