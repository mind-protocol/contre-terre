# HEALTH — Visual Style

> Controles qualite. Comment verifier la coherence visuelle.

---

## Checks Obligatoires Avant Publication

### H1 : Test Vignette

**Quoi :** Redimensionner la couverture finale a 80x120 px.
**Pourquoi :** C'est la taille reelle sur Amazon. Si le titre est illisible, la couverture echoue.
**Comment :**
1. Ouvrir le fichier couverture
2. Exporter a 80x120 px (sans interpolation avancee)
3. Verifier : titre lisible ? Palette reconnaissable ? Distinguish de fond gris ?
**Seuil :** Le titre doit etre lisible sans effort. Au moins 2 des 3 couleurs dominantes doivent etre identifiables.

### H2 : Coherence Palette Texte-Objet

**Quoi :** Verifier que les couleurs de la couverture correspondent a des elements du roman.
**Pourquoi :** Dissonance texte/objet = perte de confiance du lecteur attentif.
**Comment :** Lister les couleurs de la couverture. Pour chacune, trouver au moins un passage du manuscrit qui la contient.

### H3 : Compteur de Survivants

**Quoi :** Verifier l'exactitude du compteur de mains/silhouettes dans tous les supports visuels.
**Pourquoi :** Une erreur de comptage est une erreur factuelle visible.
**Comment :** Croiser le compteur avec `PERSONNAGES.md` (ordre de mort) et la table V6 dans VALIDATION.

### H4 : Absence d'Elements SF Generiques

**Quoi :** Scanner la couverture et les visuels marketing pour tout element SF classique.
**Pourquoi :** Invariant V1. Contre-Terre ne vend pas de la SF visuelle.
**Comment :** Demander a 3 personnes : "C'est quoi ce livre ?" Si 2+ disent "SF/espace", c'est un echec.

### H5 : Progression Chromatique du Manuscrit

**Quoi :** Verifier que les references lumineuses du texte suivent la descente.
**Pourquoi :** Invariant V3. La lumiere meurt avec les personnages.
**Comment :**
1. Pour chaque chapitre, lister les mots-cles de lumiere/couleur
2. Tracer la courbe : la tendance doit etre monotone descendante
3. Signaler toute remontee qui n'est pas un eclat ponctuel justifie

### H6 : Dimensions KDP Conformes

**Quoi :** Verifier les dimensions des fichiers images avant upload.
**Pourquoi :** Amazon rejette les fichiers hors specs.
**Comment :**
- eBook : 1600x2560 px, RGB, JPEG ou TIFF
- Broche front : hauteur + 3.175mm bleed de chaque cote
- Broche full wrap : front + dos + spine (largeur dos = nombre pages x 0.0572mm pour creme, x 0.0529mm pour blanc)
- Resolution : 300 DPI minimum

---

## Checks de Coherence Cross-Module

### H7 : Alignement avec Contact

**Quoi :** Les visuels marketing montrent-ils des mains de maniere coherente avec le systeme du Contact ?
**Comment :** Les mains sur la couverture/infographie doivent evoquer la communication tactile, pas le combat ou la priere.

### H8 : Alignement avec Structure

**Quoi :** L'infographie et les separateurs refletent-ils la structure exacte en 8 chapitres ?
**Comment :** Croiser avec `STRUCTURE.md` et `SQUELETTE.md`.

---

*Checks traces dans : `PUBLICATION.md` (specs), `VALIDATION_Visual_Style.md` (invariants)*
