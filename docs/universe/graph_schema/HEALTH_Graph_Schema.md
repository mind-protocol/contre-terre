# HEALTH — Graph Schema

> Controles qualite. Comment verifier que le graph FalkorDB de Contre-Terre est sain, coherent, et exploitable par le moteur.

---

## Checks Obligatoires Apres Chaque Modification

### H1 : Distribution des types de noeuds

**Quoi :** Verifier que les 5 types existent et que leur distribution est equilibree.

**Test :**
```cypher
MATCH (n)
RETURN labels(n)[0] AS type, count(n) AS total
ORDER BY total DESC
```

**Resultat attendu :**
- Actor : 7 principaux + 2-3 secondaires = 9-10
- Space : 9 zones
- Narrative : 15 metiers + ~12 systemes/arcs/variantes = ~27
- Thing : 7 objets
- Moment : variable (croit avec les evenements)

**Signal d'alerte :** Un type a zero noeuds. Ou Moment represente plus de 50% du graph (surcharge evenementielle).

---

### H2 : Aucun noeud orphelin

**Quoi :** Tout noeud possede au moins un lien. Un noeud sans lien est invisible a la traversal.

**Test :**
```cypher
MATCH (n)
WHERE NOT EXISTS { MATCH (n)-[]-() }
RETURN labels(n), n.name, n.id
```

**Resultat attendu :** Zero lignes.

**Frequence :** Apres chaque seeding ou mise a jour.

---

### H3 : Les poids Contact evoluent correctement

**Quoi :** Les liens SPEAKS_TO ont des poids dans [0.0, 1.0] et les poids refletent la matrice des relations de PERSONNAGES.md.

**Test :**
```cypher
MATCH (a:Actor)-[l:link {type: 'SPEAKS_TO'}]->(b:Actor)
WHERE l.weight < 0 OR l.weight > 1.0
RETURN a.name, b.name, l.weight
```

**Resultat attendu :** Zero lignes.

**Verification qualitative :** Senzo-Nandi > 0.8, Jabu-quiconque < 0.2, Sihle-Enama < 0.4. Si ces ordres sont inverses, les poids ne refletent pas le recit.

---

### H4 : La cascade de mort fonctionne

**Quoi :** Quand un citoyen meurt, l'ensemble de la procedure se deroule : Moment DEATH cree, status passe a `dead`, objets transferes, metiers orphelins detectables.

**Test :** Apres chaque `on_citizen_death` :
1. Le citoyen a `status: 'dead'`
2. Un Moment DEATH existe et est lie au citoyen et a la zone
3. Les liens CARRIES sont transferes au nouveau porteur (si applicable)
4. Les liens SPEAKS_TO du mort restent dans le graph (V12 -- pas de suppression)
5. Si le mort etait le dernier porteur d'un metier, ce metier est orphelin

**Frequence :** A chaque mort simulee.

---

### H5 : Les synthesis sont non-vides et pertinents

**Quoi :** Chaque noeud a un `synthesis` non-vide, construit selon les regles d'ALGORITHM A3.

**Test :**
```cypher
MATCH (n)
WHERE n.synthesis IS NULL OR n.synthesis = '' OR size(n.synthesis) < 20
RETURN labels(n), n.name, n.id
```

**Resultat attendu :** Zero lignes.

**Verification qualitative :** Les synthesis des Actors contiennent nom + metiers + trait tremens. Les synthesis des Spaces contiennent magnitude + conditions. Un synthesis qui dit juste "Nandi" sans metiers est trop pauvre pour les embeddings.

---

### H6 : Coherence du nombre de survivants

**Quoi :** Le nombre de citoyens actifs + morts = 7 a tout moment.

**Test :**
```cypher
MATCH (a:Actor {type: 'CITIZEN'})
WITH sum(CASE WHEN a.status = 'active' THEN 1 ELSE 0 END) AS alive,
     sum(CASE WHEN a.status = 'dead' THEN 1 ELSE 0 END) AS dead
WHERE alive + dead != 7
RETURN alive, dead
```

**Resultat attendu :** Zero lignes.

---

### H7 : La Charge est toujours portee

**Quoi :** `thing:charge` a un lien CARRIES depuis un Actor actif, tant qu'il reste des survivants.

**Test :** Invariant V9 de VALIDATION_Graph_Schema.md.

**Frequence :** Apres chaque mort (transfert de porteur).

---

## Signaux de Degradation

### Le graph copie Venezia sans adaptation

**Symptome :** Presence de liens TRUSTS/DISTRUSTS, de noeuds Actor avec `social_class`, de references a `voice`. Champs `wealth`, `guild`, `contracts`.

**Cause probable :** Script de seeding derive de `seed_venice_graph.py` sans adaptation complete.

**Recovery :** Supprimer tous les noeuds/liens specifiques a Venezia. Verifier que les seuls types de liens sont ceux documentes dans PATTERNS P7. Relire MAPPING.md pour les conventions Contre-Terre.

---

### Les Moments sismiques n'ont pas de zone

**Symptome :** Noeuds Moment de type SEISMIC_EVENT sans lien AFFECTS vers un Space.

**Cause probable :** Creation de Moment sans la deuxieme etape (liaison aux zones).

**Recovery :** Pour chaque Moment SEISMIC_EVENT orphelin, identifier la zone affectee a partir du chapitre et creer le lien AFFECTS.

---

### Les poids SPEAKS_TO stagnent

**Symptome :** Tous les liens SPEAKS_TO ont le meme poids qu'au seeding, meme apres des interactions simulees.

**Cause probable :** Le hook `on_contact` ne met pas a jour les poids, ou la formule d'increment est desactivee.

**Recovery :** Verifier que `on_contact` appelle bien la formule d'ALGORITHM A2 : `new_weight = min(1.0, old_weight + 0.05 * quality)`. Tester manuellement avec un Contact Senzo-Nandi et verifier que le poids augmente.

---

### La mort ne cascade pas

**Symptome :** Un citoyen est `dead` mais ses liens CARRIES ne sont pas transferes, ou son Moment DEATH n'existe pas.

**Cause probable :** La procedure de mort (ALGORITHM A2) n'est pas executee atomiquement.

**Recovery :** Verifier chaque etape de la procedure. Creer les noeuds/liens manquants manuellement. Le graph doit etre reparable sans re-seeding complet.

---

## Checklist Rapide

Avant chaque session de travail sur le graph :

```
[ ] 5 types de noeuds presents (H1)
[ ] Zero noeuds orphelins (H2)
[ ] Poids SPEAKS_TO dans [0, 1] (H3)
[ ] Citoyens actifs + morts = 7 (H6)
[ ] Synthesis non-vides sur tous les noeuds (H5)
[ ] La Charge a un porteur actif (H7)
[ ] Aucun champ Venezia residuel (pas de TRUSTS, voice, wealth)
```

---

*Derives de : VALIDATION_Graph_Schema.md, ALGORITHM_Graph_Schema.md, HEALTH_Manifest.md*
