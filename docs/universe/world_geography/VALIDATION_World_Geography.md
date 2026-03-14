# VALIDATION -- World Geography

**Module :** `universe/world_geography`
**Univers :** Cities of Light -- 3e univers (Contre-Terre)

---

## Invariants geographiques -- Regles qui ne doivent jamais etre violees

Ces invariants sont les lois du monde de Contre-Terre telles qu'elles s'appliquent au systeme de zones. Les violer detruirait la coherence interne de l'univers. Chaque zone, chaque connexion, chaque modification doit passer ces tests.

---

## Invariants absolus (violation = erreur structurelle)

### V1 : Les zones profondes sont toujours plus chaudes

**Regle :** Pour toute paire de zones (A, B), si `A.depth < B.depth`, alors `A.temperature_range.max <= B.temperature_range.min` (avec une tolerance de 5C pour les zones de meme profondeur).

**Justification :** La chaleur est le marqueur physique irreductible de la profondeur. La geothermie augmente en se rapprochant du coeur volcanique. Une zone profonde froide briserait l'ancrage sensoriel qui fait sentir la descente.

**Exception documentee :** Le village des sourds a une temperature organique (35-40C) qui est proche des cavernes d'entree (33-40C) malgre une position comparable. L'amortissement sismique du village affecte la perception thermique mais pas la temperature reelle.

---

### V2 : La magnitude de base augmente avec la profondeur

**Regle :** Pour toute paire de zones (A, B), si `A.depth < B.depth`, alors `A.base_magnitude <= B.base_magnitude`.

**Justification :** La proximite du coeur volcanique augmente l'intensite sismique. Le gradient de magnitude est la force motrice du tremens -- sans lui, la descente n'aurait pas de cout physiologique.

**Exception documentee :** Le village des sourds a une magnitude amortie (3.0 effective pour 5.0 ambiante). L'amortissement est un artefact de l'ingenierie du village (tranchees, materiaux absorbants), pas une violation du gradient naturel. La magnitude ambiante de la zone est toujours 5.0+.

---

### V3 : Toutes les zones restent connectees

**Regle :** Le graphe des connexions est toujours connexe. Il n'existe jamais de zone completement isolee (aucune connexion entrante ET sortante).

**Justification :** L'isolement total briserait la traversabilite du monde. Meme les zones les plus profondes doivent rester accessibles -- meme si le chemin est dangereux.

**Mecanisme de protection :** Quand un seisme ferme une connexion, l'algorithme verifie que la zone source et la zone cible restent accessibles par au moins un autre chemin. Si la fermeture isolerait une zone, elle ne se produit pas (le passage est endommage mais pas completement bouche).

---

### V4 : Les zones de surface sont toujours habitables

**Regle :** Toute zone de depth 0 a un `habitability_score >= 0.7`. Les Archipels sont des communautes stables. Ils peuvent subir des seismes violents, des tempetes, des crues -- mais ils restent habitables.

**Justification :** La vie de surface est la baseline du monde. Si les Archipels deviennent inhabitables, le monde n'a plus de civilisation de reference. Le contraste entre la vie possible en surface et l'impossibilite en profondeur est la tension fondamentale.

---

### V5 : L'habitabilite decroit strictement avec la profondeur

**Regle :** Pour toute paire de zones (A, B), si `A.depth < B.depth`, alors `A.habitability_score >= B.habitability_score`.

**Justification :** La profondeur est synonyme de danger. Le gradient de difficulte croissant est le contrat du monde : descendre = s'approcher de la mort.

**Nuance :** Le village des sourds (depth 2, score 0.65) est plus habitable que les cavernes d'entree generiques (depth 2, score 0.5). Les zones de meme profondeur peuvent varier, mais une zone plus profonde ne peut jamais etre plus habitable qu'une zone moins profonde.

---

## Invariants structurels (violation = incoherence)

### V6 : Chaque zone a une signature sensorielle unique

**Regle :** On doit pouvoir identifier une zone a partir de sa description sensorielle seule -- sans connaitre son nom ni sa profondeur.

**Test :** Extraire les valeurs de `temperature_range`, `base_magnitude`, `light_source`, `fauna`, `character`. La combinaison doit etre unique pour chaque zone.

---

### V7 : Le Contact change a chaque transition de zone

**Regle :** Toute paire de zones adjacentes (connectees) doit avoir des `contact_dialect_modifier` distincts. Le Contact ne reste jamais identique en changeant de zone.

**Justification :** La geographie modifie le langage. C'est le mecanisme fondamental de Contre-Terre. Si deux zones adjacentes ont le meme Contact, la transition entre elles est invisible -- et la geographie perd son role.

---

### V8 : Les connexions irreversibles vont toujours vers le bas

**Regle :** Si une connexion a `reversible: false`, alors `source.depth <= target.depth`. On ne peut jamais etre piege en remontant sans le vouloir.

**Justification :** L'irreversibilite est le mecanisme de la descente. Les seuils de non-retour vont toujours dans le sens de la profondeur -- la gravite narrative tire vers le bas.

---

### V9 : La bioluminescence n'existe qu'en zone de depth 1-2

**Regle :** Les filaments bioluminescents ne sont presents que dans les zones de depth 1 (piemont) et depth 2 (cavernes d'entree, village). Ils sont absents en surface (pas de cavernes) et en profondeur (trop chaud).

**Justification :** La bioluminescence marque la frontiere entre le monde habitable et l'inhabitable. Sa disparition en profondeur est le signal que plus rien de vivant ne subsiste. Sa presence est un systeme de navigation qui s'arrete la ou la navigation devient impossible.

---

### V10 : L'air se rarefie avec la profondeur

**Regle :** Pour toute paire de zones (A, B), si `A.depth < B.depth`, alors `A.air_quality >= B.air_quality`.

**Justification :** La rarefaction de l'air est le mecanisme d'hallucination et de delire. C'est aussi ce qui rend l'Aeromaitre indispensable et sa mort catastrophique.

**Exception documentee :** Le village des sourds beneficie d'une ventilation naturelle par les failles (air_quality 0.9 malgre depth 2). C'est une des raisons de son emplacement.

---

## Invariants inter-modules

### V11 : Coherence geographie-Contact

**Regle :** Chaque zone dont `contact_dialect_modifier.pain_threshold > 0.5` doit avoir des `available_modes` reduits par rapport aux zones precedentes.

**Justification :** Quand le Contact fait mal, les modes complexes disparaissent. On ne fait pas du Contact haute-resolution quand la peau brule.

---

### V12 : Coherence geographie-seismique

**Regle :** La `base_magnitude` de chaque zone doit etre coherente avec le modele sismique defini dans `ALGORITHM_Seismique.md`. Les cataclysmes possibles dans une zone sont determines par sa `base_magnitude` et sa `depth`.

---

## Matrice de verification rapide

| Invariant | Test | Automatisable |
|-----------|------|---------------|
| V1 Temperature croissante | Comparer temperature_range par depth | Oui |
| V2 Magnitude croissante | Comparer base_magnitude par depth | Oui |
| V3 Connexite | Algorithme de parcours du graphe | Oui |
| V4 Surface habitable | Verifier habitability_score >= 0.7 pour depth 0 | Oui |
| V5 Habitabilite decroissante | Comparer habitability_score par depth | Oui |
| V6 Signature unique | Comparer combinaisons de parametres | Semi-auto |
| V7 Contact change | Comparer dialect_modifier des zones adjacentes | Oui |
| V8 Irreversibilite vers le bas | Verifier depth source <= depth target pour reversible=false | Oui |
| V9 Bioluminescence limitee | Verifier fauna pour depth 0 et 3+ | Oui |
| V10 Air decroissant | Comparer air_quality par depth | Oui |
| V11 Contact-douleur | Verifier modes reduits quand pain > 0.5 | Oui |
| V12 Coherence sismique | Cross-reference avec ALGORITHM_Seismique | Manuel |

---

*Invariants derives de : `VALIDATION_Geographie.md` (14 invariants narratifs), `VALIDATION_Contact.md`, `VALIDATION_Seismique.md`*
