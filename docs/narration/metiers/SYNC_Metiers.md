# SYNC : Etat Actuel du Module Metiers

```
LAST_UPDATED: 2026-03-11
UPDATED_BY: Claude (agent voice)
```

---

## Maturity

**STATUS : DESIGNING**

### Ce qui est canonique (v1) :

- La liste des 15 metiers et leurs definitions (METIERS.md)
- Les assignations completes des 7 personnages (SQUELETTE.md)
- La hierarchie sismique a trois etages (L1 instruments, L2 ecoute, L3 prediction)
- Le mecanisme de cascade (mort → perte de 2-3 competences)
- L'ordre des morts et la progression de la degradation
- Le dedoublement de l'explosiviste (Inyoni principal, Nandi backup)
- Les gestes-signatures des metiers montres dans les Ch. I-IV

### Ce qui est en cours de design :

- Les manifestations de 5 metiers pas encore montres en prose (meteorologue, survivaliste, geologue, explosiviste, explosiviste backup)
- La scene d'apprentissage de Nandi comme explosiviste backup
- Les scenes de perte ressentie pour les morts des Ch. V-VIII

### Ce qui est propose (v2) :

- Rien — le systeme est complet en design. L'execution (ecriture) est le prochain travail.

---

## Etat des sources

| Source | Statut | Issue |
|--------|--------|-------|
| METIERS.md | INCOMPLET | Assignations partielles, en retard sur SQUELETTE.md. Thabo assigne "Speleologue (?)" au lieu de "Geologue". |
| SQUELETTE.md | COMPLET | Source de verite. Assignations finalisees. |
| PERSONNAGES.md | COMPLET | Pas de contradiction. Mention des metiers mais renvoie a METIERS.md. |
| Chapitres I-IV | CANONIQUE | Metiers montres par les gestes, pas par exposition. |

---

## Issues connues

| Issue | Severite | Action |
|-------|----------|--------|
| METIERS.md desaligne avec SQUELETTE.md | MOYENNE | Mettre a jour METIERS.md : completer les assignations, corriger Thabo (Geologue, pas Speleologue) |
| 5 metiers pas encore montres en prose | BASSE | Normal — les chapitres concernes (V-VIII) ne sont pas encore ecrits |
| Meteorologue (Sihle) jamais montre | HAUTE | DOIT etre montre dans Ch. V avant la mort de Sihle |
| Explosiviste (Inyoni) jamais montree | HAUTE | DOIT etre montree manipulant les charges avant Ch. VII |
| Nandi backup explosifs non montree | HAUTE | Scene d'apprentissage requise avant Ch. VIII |

---

## Travail a faire

### Priorite 1 — A l'ecriture du Ch. V :
1. Montrer Sihle comme meteorologue (prevision atmospherique souterraine)
2. Montrer Jabu comme speleologue (navigation experte dans les cavernes)
3. Montrer Enama comme survivaliste (technique de survie)
4. Montrer les consequences de la mort de Senzo (pas de carte, pas de chef)
5. Premiere scene d'Inyoni manipulant les explosifs (verification des charges)

### Priorite 2 — A l'ecriture du Ch. VI :
1. Montrer Thabo comme geologue (evaluation de la roche)
2. L'Aeromaitre critique (detection des gaz — prevu dans SQUELETTE.md)
3. Consequences de la mort d'Enama (plus de cuisine, plus de survie)
4. Scene de Nandi observant Inyoni avec les charges (apprentissage backup)

### Priorite 3 — A l'ecriture du Ch. VII :
1. Thabo teste l'air du boyau (scene confirmee dans SQUELETTE.md)
2. Perte de l'Aeromaitre et de l'explosiviste principale
3. Nandi comprend qu'elle est seule avec les explosifs

### Priorite 4 — A l'ecriture du Ch. VIII :
1. Nandi active la charge (backup explosiviste)
2. Contact-fantome : hallucinations des metiers perdus
3. Le tremens au maximum — le corps EST le sismographe

### Priorite 5 — Documentation :
1. Mettre a jour METIERS.md pour s'aligner sur SQUELETTE.md
2. Ajouter les assignations completes
3. Corriger l'erreur Thabo (Geologue, pas Speleologue)

---

## Handoff

### Pour l'agent suivant (groundwork, ecriture) :
- Consulter ALGORITHM_Metiers.md pour la matrice de cascade avant d'ecrire chaque chapitre
- Consulter VALIDATION_Metiers.md pour les invariants a respecter
- Les metiers marques REQUIS dans HEALTH_Metiers.md DOIVENT etre montres dans le chapitre correspondant
- Ne jamais nommer un metier — le montrer par le geste (PATTERNS P4)

### Pour l'agent suivant (voice, documentation) :
- METIERS.md doit etre mis a jour (priorite 5)
- Cette doc chain est complete et n'a pas besoin de nouveaux fichiers

### Pour l'humain :
- **Decision requise :** Le mineur (Sihle, #4) est peu montre. Faut-il ajouter une scene de minage dans Ch. V, ou la mention des caissons amortisseurs (Ch. I) suffit-elle ?
- **Decision requise :** La survivaliste (Enama, #10) n'a jamais ete montree. Quelle forme prend la survie d'Enama — techniques de campement ? gestion des ressources ? medecine de fortune ?
- **Observation :** L'Aeromaitre (Thabo) est le metier le mieux incarne dans les 4 premiers chapitres. Le tissu est un objet-signature aussi puissant que le sismographe de Sihle. Les deux forment un duo sensoriel (air/terre) qui structure la perception du groupe.
