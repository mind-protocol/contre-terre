# HEALTH -- World Geography

**Module :** `universe/world_geography`
**Univers :** Cities of Light -- 3e univers (Contre-Terre)

---

## Ce qu'on verifie -- signaux de sante du systeme geographique

Ce document definit les verifications concretes qui permettent de savoir si le systeme de zones fonctionne correctement. Pas les invariants abstraits (VALIDATION), mais les tests qu'on execute, les signaux qu'on surveille, les degradations qu'on detecte.

---

## H1 : Toutes les zones sont accessibles depuis la surface

**Verification :** A partir de n'importe quelle zone de surface (depth 0), un parcours en profondeur du graphe de connexions atteint chaque zone definie dans le systeme.

**Methode :** Parcours BFS depuis `surface_desert_sud`. Chaque zone du systeme doit apparaitre dans les noeuds visites. Si une zone n'est pas atteinte, il manque une connexion ou une zone intermediaire est isolee.

**Frequence :** A chaque modification du graphe de connexions (ajout/suppression de zone, modification de connexion, evenement sismique).

**Signal de degradation :** Une zone existe dans les definitions mais n'est accessible par aucun chemin depuis la surface. L'equipe ne pourrait jamais y arriver -- la zone est morte.

---

## H2 : Le graphe de connexions est coherent

**Verification :** Chaque connexion reference des `zone_id` qui existent dans le systeme. Aucune connexion ne pointe vers une zone inexistante. Aucune zone n'a de connexion vers elle-meme.

**Methode :** Pour chaque connexion, verifier que `target_zone_id` est un id valide. Verifier que source != target. Verifier qu'il n'existe pas de doublons (deux connexions identiques entre les memes zones).

**Signal de degradation :** Connexion orpheline (pointe vers une zone supprimee ou renommee). Boucle sur soi-meme. Connexion en double.

---

## H3 : Le gradient de profondeur est monotone

**Verification :** Les parametres physiques suivent leur direction attendue avec la profondeur :
- `temperature_range.min` : croissant avec depth (exception surface/piemont)
- `base_magnitude` : croissant avec depth (exception village amortissement)
- `habitability_score` : decroissant avec depth
- `air_quality` : decroissant avec depth (exception village ventilation)

**Methode :** Trier les zones par depth. Verifier que chaque parametre suit sa direction. Lister les exceptions documentees. Tout ecart non documente est une erreur.

**Signal de degradation :** Un parametre s'inverse sans raison documentee. Une zone profonde est plus habitable qu'une zone de surface. La temperature baisse en descendant.

---

## H4 : Le Contact evolue a chaque transition

**Verification :** Pour chaque paire de zones adjacentes (connectees), le `contact_dialect_modifier` est distinct. Au moins un des champs (amplitude, speed, resolution, pain_threshold, available_modes) differe.

**Methode :** Comparer les modifiers de chaque paire adjacente. Si tous les champs sont identiques, la transition est invisible -- le citoyen ne sent pas qu'il a change de zone.

**Signal de degradation :** Deux zones adjacentes avec le meme Contact. L'experience de la traversee perd sa texture.

---

## H5 : Les Archipels sont diversifies

**Verification :** Les zones de surface (Archipels) ont des spectres sismiques distincts -- les `contact_dialect_modifier` different suffisamment pour justifier des dialectes regionaux du Contact.

**Methode :** Comparer les modifiers des zones de depth 0. La distance entre les vecteurs (amplitude, speed, resolution) doit etre significative. Si deux Archipels sont quasi-identiques, la diversite horizontale du monde s'effondre.

**Signal de degradation :** Deux Archipels avec les memes parametres sismiques. Les personnages issus de ces Archipels n'auraient pas de difference de Contact -- le tremens de Nandi n'aurait aucune raison d'etre violent.

---

## H6 : Les connexions irreversibles sont coherentes

**Verification :** Toute connexion marquee `reversible: false` va de source.depth <= target.depth. Aucune connexion irreversible ne remonte. Les connexions irreversibles ont un mecanisme de fermeture documente (eboulement, chaleur, verticalite).

**Methode :** Filtrer les connexions irreversibles. Verifier la direction. Verifier qu'un mecanisme de seuil est documente pour chacune.

**Signal de degradation :** Connexion irreversible qui remonte (piegeage vers la surface). Connexion irreversible sans mecanisme -- le lecteur ne comprend pas pourquoi l'equipe ne peut pas revenir.

---

## H7 : La bioluminescence respecte ses limites

**Verification :** Les `fauna` contenant des filaments bioluminescents n'existent que dans les zones de depth 1-2. Aucune bioluminescence en surface (pas de cavernes) ni en profondeur (trop chaud).

**Methode :** Scanner les listes `fauna` de chaque zone. Verifier que les termes contenant "bioluminesc" n'apparaissent que pour depth 1 et depth 2.

**Signal de degradation :** Bioluminescence en surface ou en zone volcanique. Le systeme de navigation du monde souterrain deborde de ses limites.

---

## H8 : Coherence avec les chapitres

**Verification :** Les zones traversees dans le roman correspondent aux zones definies dans le systeme. Chaque chapitre a lieu dans une zone identifiable. Les parametres decrits dans la prose (temperature, lumiere, Contact, air) sont coherents avec les valeurs du systeme.

**Methode :** Pour chaque chapitre (I-VIII), identifier la zone principale. Cross-referencer les descriptions sensorielles du texte avec les parametres de la zone. Marquer les incoherences.

**Signal de degradation :** Le chapitre III decrit une temperature de 60C alors que le village est defini a 35-40C. Le chapitre VI decrit de la bioluminescence en zone volcanique. La prose et le systeme divergent.

---

## Matrice de sante

| Check | Automatisable | Critique | Frequence |
|-------|--------------|----------|-----------|
| H1 Accessibilite | Oui | Critique | A chaque modification |
| H2 Coherence graphe | Oui | Critique | A chaque modification |
| H3 Gradient monotone | Oui | Haute | A chaque ajout de zone |
| H4 Contact evolue | Oui | Haute | A chaque ajout de zone |
| H5 Diversite Archipels | Semi-auto | Moyenne | A chaque ajout d'Archipel |
| H6 Irreversibilite | Oui | Haute | A chaque modification de connexion |
| H7 Bioluminescence | Oui | Moyenne | A chaque modification de fauna |
| H8 Coherence chapitres | Manuel | Haute | A chaque revision de chapitre |

---

*Checks derives de : VALIDATION_World_Geography.md (12 invariants), ALGORITHM_World_Geography.md (structure de donnees), chapitres I-VIII*
