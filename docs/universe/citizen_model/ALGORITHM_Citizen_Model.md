# ALGORITHM — Citizen Model

> Structure de donnees. Comment un citoyen est encode.

---

## Structure du Citoyen

```
citizen {
    // Identite
    id: string                          // Identifiant unique
    name: string                        // Nom zulu (convention du roman)
    archipel_origin: string             // Archipel de naissance (1 des 7 majeurs)

    // Corps
    tremens_sensitivity: float [0.0-1.0]  // 0 = insensible, 1 = predicteur pur
    physical_state: {
        feet: enum [intact, worn, damaged, destroyed]
        hands: enum [intact, calloused, cut, burned, destroyed]
        skin: enum [intact, abraded, burned, scarred]
        inner_ear: enum [intact, strained, damaged, deaf]
        general: enum [healthy, fatigued, exhausted, critical]
    }

    // Metiers (organes de perception)
    metiers: [{                         // 1 a 3 metiers parmi les 15
        id: int [1-15]
        name: string
        perception_channel: string      // Ce que ce metier permet de percevoir
        active: bool                    // False si le corps ne le permet plus
    }]

    // Contact (langue)
    contact_vocabulary: {
        base_gestures: [string]         // Gestes universels (epaule-urgence, bras-info, etc.)
        personal_idiolect: [{           // Gestes propres a ce citoyen
            gesture: string             // Description du geste
            meaning: string             // Ce qu'il signifie
            body_zone: string           // Zone du corps (epaule, nuque, bras, main, etc.)
        }]
        learned_variants: [string]      // Variantes apprises (Contact-corde, Contact-haute-resolution, etc.)
    }

    // Idiolectes de paire (vocabulaires relationnels)
    pair_idiolects: [{
        partner_id: string              // ID de l'autre citoyen
        gestures: [{
            gesture: string             // Description du geste
            meaning: string             // Signification
            origin_chapter: int         // Quand ce geste a ete invente (optionnel)
        }]
        status: enum [active, orphaned, dead]
        // active = les deux vivants
        // orphaned = un des deux est mort, l'autre porte l'idiolecte comme manque
        // dead = les deux sont morts
    }]

    // Localisation
    zone: {
        current_archipel: string        // Archipel actuel (ou "profondeur" pendant la descente)
        depth_level: int [0-8]          // 0 = surface, 8 = grotte finale
        sub_zone: string                // Zone specifique (desert, faille, caverne, boyau, etc.)
    }

    // Relations (historique Contact)
    relationships: [{
        citizen_id: string              // ID de l'autre citoyen
        contact_history: [{
            chapter: int                // Chapitre de l'interaction
            type: string                // Type de Contact (standard, intime, conflit, urgence, deuil)
            body_zone: string           // Zone du corps impliquee
            significance: string        // Ce que cette interaction a change
        }]
        bond_nature: string             // Nature du lien (intime, collegue, conflit, minimal, absent)
    }]

    // Etat narratif
    alive: bool
    death: {                            // null si vivant
        chapter: int
        cause: string                   // Cause de mort (geologique)
        element: string                 // Element associe (glissement, chute, noyade, lave, eboulement, explosion)
        metiers_lost: [string]          // Metiers perdus pour le groupe
        idiolects_killed: [string]      // Idiolectes de paire tues par cette mort
        vocabulary_lost: [string]       // Gestes propres qui disparaissent
    }
}
```

---

## Mecaniques Cles

### A1 : Tremens et Prediction

La sensibilite tremens d'un citoyen determine sa relation a la terre :

```
tremens_sensitivity >= 0.8  → predicteur : sent les seismes futurs, nausee, vomissements
tremens_sensitivity 0.5-0.8 → ecouteur : percoit les seismes presents avant les instruments
tremens_sensitivity 0.2-0.5 → sensible : conscience du tremens comme bruit de fond
tremens_sensitivity < 0.2   → insensible : vit avec le tremblement sans le lire
```

La prediction n'est pas un calcul — c'est une souffrance. Plus la sensibilite est haute, plus le corps reagit violemment aux changements de frequence sismique. Nandi (`tremens_sensitivity: 0.95`) vomit quand la magnitude change. C'est le prix de la prescience.

### A2 : Degradation Physique et Perte de Capacite

La degradation du corps affecte les capacites en cascade :

```
feet: damaged → metier "predicteur" perd en acuite (le sol ment a travers la douleur)
feet: destroyed → metier "predicteur" desactive (plus de lecture du sol)

hands: cut → Contact fin impossible (idiolectes de paire complexes desactives)
hands: burned → Contact douloureux (chaque geste coute)
hands: destroyed → Contact mort (le citoyen ne peut plus parler)

inner_ear: damaged → metier "ecouteur" perd en acuite
inner_ear: deaf → Contact-corde illisible (ne sent plus les vibrations)

skin: burned → tout Contact = douleur (la communication devient sacrifice)
```

### A3 : Effet Cascade des Morts

Quand un citoyen meurt, l'algorithme est :

```
1. Marquer citizen.alive = false
2. Marquer citizen.death avec cause, chapitre, element
3. Pour chaque metier du citoyen :
   - Verifier si un autre citoyen vivant possede ce metier
   - Si non → metier perdu pour le groupe (ajouter a death.metiers_lost)
4. Pour chaque pair_idiolect du citoyen :
   - Marquer le pair_idiolect comme "orphaned" chez le partenaire vivant
   - Les gestes de cet idiolecte n'existent plus que comme manque
5. Les gestes du personal_idiolect du mort → death.vocabulary_lost
6. Recalculer la couverture metier du groupe survivant
```

**Progression documentee (du roman) :**

```
Ch. IV : Senzo meurt    → 13/15 metiers couverts (perte: chef, cartographe)
Ch. V  : Sihle + Jabu   → 8/15 metiers (perte: ecouteur, meteo, mineur, ocean, speleo)
Ch. VI : Enama          → 5/15 metiers (perte: biologiste, cuisiniere, survie)
Ch. VII: Thabo + Inyoni → 2/15 metiers (perte: aeromaître, geologue, grimpeuse, explosiviste)
Ch. VIII: Nandi seule   → 2/15 metiers (predictrice + explosiviste backup)
```

### A4 : Richesse Linguistique

La richesse Contact d'un citoyen se calcule par :

```
richesse_individuelle = len(personal_idiolect) + len(learned_variants)
richesse_relationnelle = sum(len(pair.gestures) for pair in pair_idiolects if pair.status == "active")
richesse_totale = richesse_individuelle + richesse_relationnelle
```

La richesse relationnelle est toujours superieure a la richesse individuelle — le Contact vit entre les gens, pas en eux. Un citoyen seul est linguistiquement pauvre. Un citoyen avec cinq partenaires de Contact est riche.

Apres chaque mort : `richesse_relationnelle` diminue pour tous les survivants. L'arc du roman est une contraction linguistique globale.

---

## Seeding de la Population Initiale

### Parametres

- **Taille** : 50–80 citoyens (population de reference pour le monde habite)
- **Archipels** : 7 archipels majeurs (mentionnes dans `PERSONNAGES.md` — Consortium des Archipels)
- **Distribution** : 7–12 citoyens par archipel, inegale (les grands archipels ont plus de monde)

### Distribution des Metiers

Chaque archipel a une affinite geologique qui influence la distribution des metiers :

| Type d'archipel | Metiers surrepresentes | Metiers sous-representes |
|----------------|----------------------|------------------------|
| Zone de subduction | Ecouteur, Predicteur, Meteorologue | Specialiste oceanique |
| Volcanique | Aeromaître, Geologue, Mineur | Specialiste oceanique |
| Cotier | Specialiste oceanique, Speleologue | Aeromaître |
| Plateau stable | Cartographe, Chef, Cuisinier | Predicteur |

### Regles de Seeding

```
Pour chaque citoyen :
1. Assigner un archipel (proportionnel a la taille de l'archipel)
2. Assigner 1-3 metiers :
   - 1er metier : forte probabilite d'affinite avec l'archipel
   - 2e metier (70% des citoyens) : aleatoire parmi les 15
   - 3e metier (20% des citoyens) : aleatoire parmi les 15
3. Calculer tremens_sensitivity :
   - Si metier Predicteur : 0.8-1.0
   - Si metier Ecouteur : 0.5-0.8
   - Sinon : distribution normale, moyenne 0.3, ecart-type 0.15
4. Generer le contact_vocabulary :
   - base_gestures : universels (communs a tous)
   - personal_idiolect : 2-5 gestes propres (generes selon le metier)
   - learned_variants : selon l'archipel (chaque archipel a ses variantes)
5. Initialiser physical_state : tout a "intact"
6. Generer les pair_idiolects : pour chaque paire de citoyens du meme archipel,
   probabilite de 30% d'avoir un idiolecte de paire (1-3 gestes)
```

---

## Les 7 Citoyens du Roman

Les 7 personnages du roman sont des instances specifiques de ce modele :

| Citoyen | Metiers | Tremens | Idiolectes de paire |
|---------|---------|---------|---------------------|
| Senzo | Chef (#12), Cartographe (#7) | 0.35 | Senzo/Nandi (le plus riche) |
| Nandi | Predictrice (#9), Explosiviste backup (#5) | 0.95 | Senzo/Nandi, Enama/Nandi |
| Sihle | Ecouteur (#8), Meteorologue (#1), Mineur (#4) | 0.65 | Sihle/Enama (le plus pauvre) |
| Enama | Biologiste (#3), Cuisiniere (#13), Survivaliste (#10) | 0.50 | Enama/Nandi, Sihle/Enama |
| Thabo | Aeromaître (#15), Geologue (#6) | 0.30 | Thabo/Inyoni |
| Inyoni | Grimpeuse (#11), Explosiviste (#5) | 0.25 | Thabo/Inyoni |
| Jabu | Specialiste oceanique (#2), Speleologue (#14) | 0.20 | (quasi-absent — sa tragedie) |

---

*Algorithmes derives de : `METIERS.md`, `PERSONNAGES.md`, `CONTACT.md`*
