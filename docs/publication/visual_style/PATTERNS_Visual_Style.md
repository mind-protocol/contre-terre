# PATTERNS — Visual Style

> Decisions de design. Pourquoi cette forme visuelle. Pourquoi ces choix.

---

## P1 : Deux Palettes — Textuelle et Editoriale

**Decision :** La palette visuelle du roman (ce que le lecteur imagine en lisant) et la palette editoriale (couverture, marketing) sont distinctes mais liees.

**Palette textuelle (dans le roman) :**

| Chapitre | Lumiere dominante | Source | Sensation |
|----------|------------------|--------|-----------|
| I — Surface du Desert | Blanc / soleil ecrasant | Soleil de surface | Exposition, chaleur seche |
| II — Zones Intermediaires | Vert chimique + bleu organique | Batons chimiques + bioluminescence | Decouverte, etrangete |
| III — Le Dernier Village | Bleu domestique | Bioluminescence canalisee | Refuge, intimite, sacre |
| IV — La Faille | Vert malade + noir | Batons chimiques en declin + profondeur | Perte, verticale, premier deuil |
| V — Cavernes Profondes | Orange naissant + bleu mourant | Filaments qui virent | Transition, chaleur montante |
| VI — Zones Volcaniques | Orange dominant + gouttes de lave | Lave proche, filaments orange | Danger imminent, douleur |
| VII — Interieur du Volcan | Rouge sombre + noir | Filaments mourants, lave | Etouffement, fin imminente |
| VIII — Grotte Finale | Noir total | Plus de lumiere | Aveuglement, dissolution |

**Palette editoriale (hors du roman) :**
- Couverture : noir + orange/rouge (accent)
- Typographie : blanc ou gris clair sur fond sombre
- Marketing : gradients noir→orange, texture de roche
- Infographie : progression verticale des couleurs

**Pourquoi deux palettes :** Le roman a 8 ambiances lumineuses. La couverture ne peut en capturer qu'une. On choisit le climax visuel (noir + lave) parce qu'il est le plus distinctif et le plus fidele au ton.

---

## P2 : Mains, Pas Visages

**Decision :** Le motif visuel central est la main humaine — scarifiee, brulante, posee sur la roche, tendue vers une autre main.

**Pourquoi :** Contre-Terre est un roman ou le langage est le toucher. Les mains sont les organes de la parole. Montrer un visage, c'est promettre un personnage. Montrer des mains, c'est promettre un langage.

**Applications :**
- **Couverture** : mains sur roche incandescente (direction NotebookLM)
- **Infographie** : icones de mains par chapitre (silhouettes a 7, 6, 5... 1)
- **Separateurs de chapitres** : geste Contact stylise
- **Reseaux sociaux** : gros plans mains, jamais de visages

**Alternative rejetee :** Silhouettes de personnages devant paysage volcanique. Trop classique. Trop SF standard. Ne communique pas le Contact.

---

## P3 : Verticale Descendante

**Decision :** Toute composition visuelle est orientee vers le bas. Le regard descend.

**Pourquoi :** Le roman descend. Litteralement — les personnages descendent dans un volcan. La descente est la metaphore structurante du recit. Tout element visuel qui monte ou qui s'etale horizontalement contredit le mouvement du livre.

**Applications :**
- **Couverture** : composition haute, regard vers le fond
- **Infographie** : flux vertical (deja fait — voir `data/infography1.png`)
- **Titre** : positionne en haut, le vide en dessous
- **Dos du broche** : texte serre en haut, noir croissant vers le bas

---

## P4 : Typographie Dense, Pas Decorative

**Decision :** Typographie serree, sans serif ou serif austere. Pas de police fantaisie.

**References :**
- **La Volte** (editeur de Damasio) : Police serree, espacement minimal
- **Gallimard Folio SF** : Sobre, titre domine, fond evocateur
- **Actes Sud** : Espace blanc, texte comme evenement

**Pourquoi :** Contre-Terre est litteraire avant d'etre SF. La typo ne doit pas crier "science-fiction" — elle doit crier "roman dense". Le lecteur de Damasio reconnait cette sobriete. Le lecteur de thrillers la respecte.

**Police envisagee :** Condensed sans-serif pour le titre (genre Bebas Neue, Oswald), serif sobre pour le corps (Garamond, Adobe Caslon). A tester sur vignette 80px.

---

## P5 : Couleur Comme Arc Narratif

**Decision :** La progression chromatique du roman est elle-meme un arc narratif. La lumiere meurt en meme temps que le Contact.

**Schema :**
```
Ch. I    ████████████████  blanc/lumiere naturelle    (7 vivants, Contact plein)
Ch. II   ████████████      vert + bleu                (7 vivants, Contact-monde)
Ch. III  ██████████        bleu profond                (7 vivants, Contact haute-res)
Ch. IV   ████████          vert/bleu terne             (6 vivants, Contact-corde)
Ch. V    ██████            orange naissant              (4 vivants, Contact pauvre)
Ch. VI   ████              orange vif                   (3 vivants, Contact brulant)
Ch. VII  ██                rouge sombre                 (1 vivante, Contact mort)
Ch. VIII █                 noir total                   (1 vivante, Contact-fantome)
```

**Pourquoi :** Cette courbe visuelle est parallele a la courbe linguistique (Contact qui se degrade) et a la courbe biologique (survivants qui diminuent). Les trois courbes convergent vers le meme point : le noir, le silence, la solitude.

---

## P6 : Deux Directions de Couverture — Intime vs Geologique

**Decision ouverte.** Deux directions coexistent, en attente de validation.

**Direction A — Geologique** (brief actuel, `PUBLICATION.md`) :
- Vue plongeante dans un gouffre volcanique
- Texture de roche, fissures, lueur orange en profondeur
- Silhouettes minuscules (ou absentes)
- Sensation : la terre est le personnage

**Direction B — Intime** (proposition NotebookLM) :
- Gros plan sur des mains scarifiees posees sur de la roche incandescente
- Pas de profondeur, pas de paysage
- Peau, roche, chaleur. C'est tout.
- Sensation : le Contact est le sujet

**Les deux directions ne sont pas incompatibles.** Possibilite d'un hybride : mains au premier plan, gouffre en arriere-plan. Ou : une main qui s'enfonce dans la roche — l'activation de la Charge.

---

*Decisions tracables dans : `PUBLICATION.md`, `CORRECTIONS.md` (K2), `data/infography1.png`*
