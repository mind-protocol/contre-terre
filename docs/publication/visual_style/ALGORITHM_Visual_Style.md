# ALGORITHM — Visual Style

> Procedures. Comment produire les elements visuels.

---

## Procedure 1 : Generation de la Couverture

### Etape 1 — Briefing du modele generatif

**Prompt structure :**
```
Sujet : mains humaines scarifiees posees sur de la roche volcanique incandescente
Cadrage : gros plan, vertical, le regard descend
Lumiere : lueur orange/rouge venant de la roche, pas de source externe
Texture : peau abimee, roche brute, fissures lumineuses
Palette : noir 70%, orange/rouge 20%, gris 10%
Exclusions : pas de visage, pas de vaisseau, pas de planete, pas de metal lisse
Mood : oppression, chaleur, intimite, fin imminente
```

**Modeles utilisables :** Gemini (via `gemini_chat` MCP tool), Ideogram, Midjourney, DALL-E

### Etape 2 — Iteration

1. Generer 4-6 variations
2. Tester chaque variation en vignette 80x120 px (redimensionner et evaluer la lisibilite)
3. Eliminer celles qui ne passent pas le test vignette
4. Superposer le titre ("CONTRE-TERRE") et le nom d'auteur
5. Evaluer : le titre est-il lisible en vignette ? La palette est-elle distinctive sur une page Amazon ?

### Etape 3 — Finalisation

- eBook : 1600x2560 px, RGB, JPEG qualite 100 ou PNG
- Broche : dimensions selon nombre de pages (calculer epaisseur du dos)
- Variantes : version avec et sans bandeau "cli-fi / hard SF"

---

## Procedure 2 : Separateurs de Chapitres

### Approche retenue : compteur de mains

```
Ch. I   : 🤚🤚🤚🤚🤚🤚🤚  (7 mains, toutes ouvertes)
Ch. II  : 🤚🤚🤚🤚🤚🤚🤚  (7 mains, une touche la roche)
Ch. III : 🤚🤚🤚🤚🤚🤚🤚  (7 mains, haute resolution)
Ch. IV  : 🤚🤚🤚🤚🤚🤚    (6 mains — Senzo mort)
Ch. V   : 🤚🤚🤚🤚          (4 mains — Jabu + Sihle morts)
Ch. VI  : 🤚🤚🤚            (3 mains — Enama morte)
Ch. VII : 🤚                  (1 main — Thabo + Inyoni morts)
Ch. VIII:                      (rien — Nandi seule, Contact mort)
```

**Realisation :** Icones vectorielles (SVG) d'une main stylisee. Meme icone repetee, mais de plus en plus degradee (fissures, brulures, disparition).

---

## Procedure 3 : Infographie Marketing

### Structure validee (`data/infography1.png`)

```
┌─────────────────────────┐
│ TITRE + SOUS-TITRE      │
├─────────────────────────┤
│ Ch. I — [descriptif]    │  fond: brun clair    survivants: 7
│ Ch. II — [descriptif]   │  fond: bleu-vert     survivants: 7
│ Ch. III — [descriptif]  │  fond: bleu profond  survivants: 7
│ Ch. IV — [descriptif]   │  fond: bleu sombre   survivants: 6
│ Ch. V — [descriptif]    │  fond: brun-orange   survivants: 4
│ Ch. VI — [descriptif]   │  fond: orange        survivants: 3
│ Ch. VII — [descriptif]  │  fond: rouge sombre  survivants: 1
│ Ch. VIII — [descriptif] │  fond: noir/rouge    survivants: 0
└─────────────────────────┘
```

**Elements par couche :**
- Colonne gauche : element-tueur (terre, eau, lave, pierre...)
- Centre : silhouettes de groupe (diminuant)
- Colonne droite : compteur survivants + etat du Contact + etat du langage

### Procedure de mise a jour

Quand le contenu d'un chapitre change (mort deplacee, scene ajoutee) :
1. Mettre a jour le descriptif dans l'infographie
2. Verifier le compteur de survivants
3. Verifier la coherence couleur/chapitre

---

## Procedure 4 : Palette de Reference

### Codes couleur

| Element | Hex | Usage |
|---------|-----|-------|
| Noir profond | `#0A0A0A` | Fond couverture, Ch. VIII |
| Gris basalte | `#3A3A3A` | Texte secondaire, roche |
| Bleu bioluminescent | `#2E6B8A` | Ch. II-III, village |
| Vert chimique | `#4A7A3D` | Batons chimiques |
| Orange lave | `#D4641A` | Ch. V-VI, accent couverture |
| Rouge magma | `#8B1A1A` | Ch. VII, lave proche |
| Blanc texte | `#E8E0D8` | Titre, texte sur fond sombre (creme chaud, pas blanc froid) |

### Utilisation

- Couverture : noir profond + orange lave + blanc texte
- Infographie : gradient vertical (brun → bleu → orange → rouge → noir)
- Reseaux sociaux : orange lave sur fond noir (contraste maximal)
- Print interieur : noir texte sur blanc papier (standard)

---

*Procedures tracables dans : `PUBLICATION.md` (brief), `data/infography1.png` (reference)*
