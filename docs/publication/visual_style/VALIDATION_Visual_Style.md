# VALIDATION — Visual Style

> Invariants. Ce qui doit toujours etre vrai. Regles visuelles inviolables.

---

## Invariants Absolus

### V1 : Aucun Element SF Generique

**Regle :** Aucun support visuel (couverture, infographie, marketing) ne contient de vaisseau spatial, de planete vue de l'espace, de laser, de casque, de combinaison spatiale, ni de creature alien.

**Test :** Montrer l'image a quelqu'un qui ne connait pas le livre. S'il dit "c'est de la SF", c'est un echec. S'il dit "c'est un roman sur la terre" ou "c'est un roman de survie", c'est une reussite.

**Pourquoi :** Contre-Terre est de la SF par le concept, pas par l'imagerie. Le positionnement visuel est geologique/charnel, pas spatial/technologique.

---

### V2 : Lisibilite en Vignette 80x120 px

**Regle :** La couverture doit etre lisible a 80x120 pixels. Le titre doit etre identifiable. La palette dominante doit etre reconnaissable.

**Test :** Redimensionner la couverture a 80x120 px. Si le titre est illisible ou si la palette se confond avec un aplat gris uniforme, la couverture est invalide.

**Pourquoi :** 90% des acheteurs KDP voient d'abord une vignette. La couverture est jugee en 2 secondes a cette taille.

---

### V3 : La Palette Textuelle Suit la Descente

**Regle :** Dans le manuscrit, les references visuelles (lumiere, couleur, obscurite) suivent une progression monotone descendante. Ch. VIII n'est jamais plus lumineux que Ch. I. Aucun chapitre n'est plus lumineux que le precedent (sauf eclats ponctuels : detonation de lave, eclair de baton chimique).

**Test :** Lister les references lumineuses de chaque chapitre. Verifier que la tendance generale est a l'assombrissement. Un baton chimique allume au Ch. V est acceptable. Un retour a la lumiere naturelle est une violation.

---

### V4 : Pas de Visage en Couverture

**Regle :** Aucun visage humain reconnaissable sur la couverture, les infographies, ou les visuels marketing principaux.

**Test :** Si un oeil, un nez, ou une bouche sont identifiables a 200%, c'est une violation.

**Pourquoi :** Montrer un visage impose une identite au personnage. Contre-Terre est un roman de mains, pas de visages. Le lecteur doit projeter, pas identifier.

**Exception :** Silhouettes lointaines (comme dans l'infographie) sont tolerees — elles montrent le nombre, pas l'identite.

---

### V5 : Coherence Texte-Couverture

**Regle :** Les elements visuels de la couverture doivent exister dans le roman. Pas de roche bleue si la roche n'est jamais bleue dans le texte. Pas de lave en surface si la lave n'apparait qu'en profondeur.

**Test :** Chaque element visuel de la couverture peut etre trace vers une scene ou un passage du manuscrit.

---

### V6 : Le Compteur de Mains est Exact

**Regle :** Dans les infographies et separateurs, le nombre de silhouettes/mains correspond exactement au nombre de survivants au debut du chapitre concerne.

| Chapitre | Survivants | Verification |
|----------|-----------|--------------|
| I | 7 | Depart complet |
| II | 7 | Pas de mort |
| III | 7 | Pas de mort |
| IV | 7 → 6 | Senzo meurt |
| V | 6 → 4 | Jabu + Sihle meurent |
| VI | 4 → 3 | Enama meurt |
| VII | 3 → 1 | Thabo + Inyoni meurent |
| VIII | 1 → 0 | Nandi meurt |

**Test :** Croiser avec `PERSONNAGES.md` et `SYNC_Project_State.md`.

---

### V7 : Le Sous-Titre ou Slogan Est Present

**Regle :** La couverture (ou le bandeau) porte soit le sous-titre ("Sept corps. Un langage du toucher. Plus personne ne remonte.") soit le slogan ("Chaque mort ampute un mot."). Jamais les deux. Jamais ni l'un ni l'autre.

**Test :** Verifier la presence sur le fichier couverture final.

---

*Invariants tracables dans : `PUBLICATION.md`, `CORRECTIONS.md` (K1, K2)*
