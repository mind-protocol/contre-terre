# SYNC — Visual Style

> Etat actuel du module. Ce qui existe, ce qui reste a faire.

```
LAST_UPDATED: 2026-03-12
UPDATED_BY: Claude (agent, voice)
STATUS: DESIGNING
```

---

## Etat General

L'identite visuelle de Contre-Terre est definie conceptuellement mais pas encore realisee. Les decisions de design sont documentees (palette textuelle tracee sur 8 chapitres, deux directions de couverture proposees, infographie de reference existante). La production des assets visuels attend la finalisation du manuscrit et la validation de la direction de couverture.

---

## Ce Qui Existe

| Element | Statut | Fichier |
|---------|--------|---------|
| Infographie 8 chapitres | FAIT | `data/infography1.png` |
| Brief couverture (direction A) | ECRIT | `PUBLICATION.md` |
| Proposition couverture (direction B) | ECRIT | `CORRECTIONS.md` (K2) |
| Palette textuelle (8 chapitres) | TRACEE | PATTERNS (P1, P5), IMPLEMENTATION |
| Codes couleur hex | DEFINIS | ALGORITHM (Procedure 4) |
| Sous-titre | ECRIT | `PUBLICATION.md` |
| Slogan alternatif | PROPOSE | `CORRECTIONS.md` (K1) |
| Doc chain visual style | COMPLET | ce repertoire (8 fichiers) |

## Ce Qui Reste a Faire

| Tache | Priorite | Dependance | Bloqueur |
|-------|----------|------------|----------|
| Valider direction couverture A vs B | HAUTE | Decision Nicolas | @mind:escalation |
| Valider slogan vs sous-titre | HAUTE | Decision Nicolas | @mind:escalation |
| Generer couverture eBook | HAUTE | Direction validee | Modele generatif |
| Tester couverture en vignette 80px | HAUTE | Couverture generee | — |
| Creer separateurs de chapitres | MOYENNE | Decision compteur vs barre | — |
| Generer visuels reseaux sociaux | BASSE | Couverture finalisee | — |
| Calculer couverture broche (dos) | BASSE | Mise en page finale | Nombre de pages definitif |

---

## Decisions en Attente (@mind:escalation)

### Direction couverture : A (geologique) ou B (intime) ?

**A** = vue plongeante, gouffre volcanique, silhouettes minuscules
**B** = gros plan mains scarifiees sur roche incandescente
**Hybride possible** = mains au premier plan, gouffre en arriere-plan

→ Nicolas doit valider avant generation.

### Slogan ou sous-titre ?

**Sous-titre actuel** = "Sept corps. Un langage du toucher. Plus personne ne remonte."
**Slogan NotebookLM** = "Chaque mort ampute un mot."

→ Les deux sont forts. Le slogan est plus percutant, le sous-titre est plus informatif. Possibilite d'utiliser le slogan en bandeau et le sous-titre en quatrieme.

---

## Handoff

**Pour l'agent groundwork (generation d'assets) :**
- Lire ALGORITHM pour les procedures de generation
- Respecter VALIDATION (V1-V7) — pas de SF visuelle, pas de visage, vignette lisible
- Tester chaque asset avec HEALTH (H1-H8)
- La palette de reference est dans ALGORITHM (Procedure 4)

**Pour Nicolas :**
- Deux decisions bloquantes : direction couverture et slogan
- L'infographie existante est bonne mais devra etre mise a jour si le contenu des chapitres change
- La palette textuelle est tracee — les corrections P1-P2 ne devraient pas la briser

---

*Derniere mise a jour : 2026-03-12*
