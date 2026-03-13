# Contre-Terre — Mapping vers le Schema Mind

Comment le vocabulaire de Contre-Terre se traduit en schema mind universel.

Le schema mind est fixe : 5 `node_types` (actor, moment, narrative, space, thing), 1 `link` type.
Tout le contenu va dans `content` (prose) et `synthesis` (résumé embeddable).

---

## NODE TYPE MAPPING

### actor → Personnages

Les 7 membres de l'expédition et les personnages secondaires (villageois, vieille femme, vieux).

| Entité projet | node_type | type (subtype) | Notes |
|---------------|-----------|-----------------|-------|
| Senzo | actor | personnage | Chef, Cartographe. Mort Ch. IV |
| Nandi | actor | personnage | Prédictrice, Explosiviste backup. Dernière survivante |
| Sihle | actor | personnage | Séismo-auditeur, Météo, Mineur. Mort Ch. V |
| Enama | actor | personnage | Biologiste, Cuisinière, Survie. Mort Ch. VI |
| Thabo | actor | personnage | Aéromaître, Géologue. Mort Ch. VII |
| Inyoni | actor | personnage | Grimpeuse, Explosiviste. Mort Ch. VII |
| Jabu | actor | personnage | Océanologue, Spéléologue. Mort Ch. V |
| Vieille femme | actor | personnage_secondaire | Village des sourds. Transmet le geste inconnu |
| Vieux (avertissement) | actor | personnage_secondaire | Village des sourds. Compte les échos |

### space → Lieux géographiques

Les couches géologiques traversées.

| Entité projet | node_type | type (subtype) | Notes |
|---------------|-----------|-----------------|-------|
| Désert de surface | space | couche_geologique | Ch. I — magnitude 4, sable, soleil |
| Piémont volcanique | space | couche_geologique | Ch. II — gravier, fréquences en hausse |
| Cavernes bioluminescentes | space | couche_geologique | Ch. II — filaments bleus, première descente |
| Village des sourds | space | lieu_habite | Ch. III — Contact haute définition, amortissement 40% |
| Faille verticale | space | couche_geologique | Ch. IV — escalade, Contact-corde |
| Cavernes profondes | space | couche_geologique | Ch. V — air rare, passages noyés |
| Zones volcaniques | space | couche_geologique | Ch. VI — chaleur extrême, fumerolles |
| Intérieur du volcan | space | couche_geologique | Ch. VII — boyau, magma |
| Grotte finale | space | couche_geologique | Ch. VIII — chambre de détonation |

### space → Modules documentaires

| Entité projet | node_type | type (subtype) | Notes |
|---------------|-----------|-----------------|-------|
| Module contact | space | module | `docs/worldbuilding/contact/` |
| Module seismique | space | module | `docs/worldbuilding/seismique/` |
| Module geographie | space | module | `docs/worldbuilding/geographie/` |
| Module personnages | space | module | `docs/narration/personnages/` |
| Module structure | space | module | `docs/narration/structure/` |
| Module metiers | space | module | `docs/narration/metiers/` |

### moment → Événements narratifs

Les moments-clés du récit.

| Entité projet | node_type | type (subtype) | Notes |
|---------------|-----------|-----------------|-------|
| Mort de Senzo | moment | mort | Ch. IV — glissement, corde arrachée |
| Mort de Sihle | moment | mort | Ch. V — chute, main d'Enama trop tard |
| Mort de Jabu | moment | mort | Ch. V — noyade, séparation |
| Mort d'Enama | moment | mort | Ch. VI — lave, sacrifice |
| Mort de Thabo & Inyoni | moment | mort | Ch. VII — ensevelissement partagé |
| Détonation de Nandi | moment | mort | Ch. VIII — magnitude 11 |
| Magnitude 7 (premier gros séisme) | moment | seisme | Ch. II — Contact d'urgence |
| Entrée dans les cavernes | moment | seuil | Ch. II — bioluminescence, premier Contact-monde |
| Arrivée au village des sourds | moment | seuil | Ch. III — Contact 3 doigts |
| Geste inconnu transmis | moment | revelation | Ch. III → Ch. VIII |
| Embranchement (gauche vs droite) | moment | decision | Ch. II — Sihle vs Enama, Senzo choisit |
| Naissance du Contact-corde | moment | invention | Ch. IV — dans la faille |
| Premier deuil (cercle de Contact) | moment | rituel | Ch. IV — 6 épaules, 6 mains |

### narrative → Systèmes conceptuels

Les concepts et systèmes du worldbuilding.

| Entité projet | node_type | type (subtype) | Notes |
|---------------|-----------|-----------------|-------|
| Le Contact | narrative | systeme | Langage tactile complet |
| Le tremens | narrative | systeme | Système immunitaire physiologique |
| L'Échelle de Capitulation | narrative | systeme | Hiérarchie perception sismique |
| L'effet cascade | narrative | mecanique | 15 métiers / 7 personnes |
| Le Contact-corde | narrative | variante_contact | Né dans la faille (Ch. IV) |
| Le Contact-forcé | narrative | variante_contact | Boyau (Ch. VII) |
| Le Contact-fantôme | narrative | variante_contact | Hallucinations (Ch. VIII) |
| Le Contact-monde | narrative | variante_contact | Toucher la terre (Ch. II, VIII) |
| Le geste inconnu | narrative | mystere | Tremblement volontaire (Ch. III → VIII) |
| Arc Sihle/Enama | narrative | arc | Raison vs intuition |
| Arc de Nandi | narrative | arc | Fragile → détonatrice |
| Arc du Contact (dégradation) | narrative | arc | Langue pleine → langue morte |

### thing → Objets significatifs

| Entité projet | node_type | type (subtype) | Notes |
|---------------|-----------|-----------------|-------|
| Sismographe de Sihle | thing | instrument | Rouleau de papier, aiguille, courbes |
| Tissu de Thabo | thing | outil | Fibres noircies, teste l'air |
| Corde d'encordement | thing | outil | 50m fibre tressée, médium du Contact-corde |
| Détonateur | thing | dispositif | Objectif final de la mission |
| Carte de Senzo | thing | document | Rouleau de tissu, lignes de descente. Obsolète après le village |
| Bâtons chimiques | thing | outil | Lumière verdâtre, résine sur cuivre |
| Caissons amortisseurs | thing | equipement | Triple suspension, absorbent jusqu'à magnitude 8 |

---

## LINK PATTERNS

| Relation projet | link type | Propriétés | Exemple |
|-----------------|-----------|------------|---------|
| Personnage meurt à lieu | link | type: "meurt_a" | Senzo → Faille verticale |
| Personnage possède métier | link | type: "exerce" | Thabo → Aéromaître |
| Chapitre se déroule dans couche | link | type: "se_deroule" | Ch. IV → Faille verticale |
| Mort supprime idiolecte | link | type: "supprime" | Mort de Senzo → Idiolecte Senzo |
| Concept appartient à module | link | type: "contains" | Module contact → Le Contact |
| Événement précède événement | link | type: "precedes" | Mort Senzo → Mort Sihle |

---

## CONVENTIONS

- **IDs** suivent le pattern : `{node_type}_{SUBTYPE}_{instance}`
  - Exemples : `actor_PERSONNAGE_senzo`, `space_COUCHE_faille-verticale`, `moment_MORT_senzo`
- **content** : prose complète (description, contexte, citations)
- **synthesis** : résumé embeddable en 1-2 phrases pour la recherche sémantique
- **weight** : 0.8 pour les docs, 0.9 pour les personnages, 1.0 pour les chapitres

---

*Créé : 2026-03-11*
