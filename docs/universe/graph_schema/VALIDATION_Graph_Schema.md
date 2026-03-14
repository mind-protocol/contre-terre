# VALIDATION — Graph Schema

> Invariants. Ce qui doit toujours etre vrai dans le graph. Regles qui ne peuvent pas etre brisees.

---

## Invariants Structurels

### V1 : Tout citoyen est lie a exactement une zone

**Regle :** Chaque noeud Actor de type CITIZEN avec status `active` possede exactement un lien INHABITS vers un noeud Space. Pas zero (citoyen flottant). Pas deux (citoyen ubiquiste).

**Test :**
```cypher
MATCH (a:Actor {type: 'CITIZEN', status: 'active'})
OPTIONAL MATCH (a)-[l:link {type: 'INHABITS'}]->(s:Space)
WITH a, count(s) AS zone_count
WHERE zone_count != 1
RETURN a.name, zone_count
```
Resultat attendu : zero lignes.

**Exception :** Un citoyen `dead` peut avoir zero liens INHABITS (il n'habite plus nulle part). Le lien est conserve pour l'historique mais peut etre marque `status: 'historical'`.

---

### V2 : Les liens SPEAKS_TO sont bidirectionnels

**Regle :** Pour chaque lien SPEAKS_TO de A vers B, il existe un lien SPEAKS_TO de B vers A. Les poids peuvent differer (le Contact est asymetrique), mais les liens existent dans les deux directions.

**Test :**
```cypher
MATCH (a:Actor)-[l1:link {type: 'SPEAKS_TO'}]->(b:Actor)
WHERE NOT EXISTS {
    MATCH (b)-[l2:link {type: 'SPEAKS_TO'}]->(a)
}
RETURN a.name, b.name
```
Resultat attendu : zero lignes.

**Pourquoi :** Le Contact est physique. Si A touche B, B est touche par A. L'interaction est forcement bilaterale. Le poids peut differer (Sihle touche Enama avec 2 doigts froids, Enama touche Sihle avec la paume -- meme Contact, registres opposes), mais le lien existe dans les deux sens.

---

### V3 : Les Moments sismiques sont lies aux zones affectees

**Regle :** Chaque noeud Moment de subtype SEISMIC_EVENT possede au moins un lien AFFECTS vers un noeud Space. Un seisme sans zone est un seisme sans lieu -- ca n'existe pas.

**Test :**
```cypher
MATCH (m:Moment {type: 'SEISMIC_EVENT'})
WHERE NOT EXISTS {
    MATCH (m)-[l:link {type: 'AFFECTS'}]->(s:Space)
}
RETURN m.name
```
Resultat attendu : zero lignes.

---

### V4 : Pas de noeuds orphelins

**Regle :** Tout noeud dans le graph possede au moins un lien. Un noeud sans lien est un noeud inaccessible par traversal -- il n'existe pas pour le moteur.

**Test :**
```cypher
MATCH (n)
WHERE NOT EXISTS { MATCH (n)-[]-() }
RETURN labels(n), n.name, n.id
```
Resultat attendu : zero lignes.

**Pourquoi :** Le graph mind fonctionne par traversal, pas par requete directe. Un noeud orphelin ne sera jamais atteint par la physique du graph. C'est de la donnee morte.

---

### V5 : Chaque mort cree un Moment et desactive le citoyen

**Regle :** Quand un citoyen meurt, deux choses se produisent atomiquement : (1) un noeud Moment de type DEATH est cree et lie au citoyen et a la zone, (2) le status du citoyen passe a `dead`. Les deux sont indissociables.

**Test :**
```cypher
MATCH (a:Actor {type: 'CITIZEN', status: 'dead'})
WHERE NOT EXISTS {
    MATCH (m:Moment {type: 'DEATH'})-[]->(a)
}
RETURN a.name
```
Resultat attendu : zero lignes.

**Test inverse :**
```cypher
MATCH (m:Moment {type: 'DEATH'})-[]->(a:Actor {type: 'CITIZEN'})
WHERE a.status != 'dead'
RETURN a.name, m.name
```
Resultat attendu : zero lignes.

---

### V6 : Le nombre de citoyens actifs correspond a la chronologie

**Regle :** Le nombre de noeuds Actor (type: CITIZEN, status: active) est coherent avec le nombre de morts survenues. 7 au depart. 6 apres Ch. IV. 4 apres Ch. V. 3 apres Ch. VI. 1 apres Ch. VII. 0 apres Ch. VIII.

**Test :**
```cypher
MATCH (alive:Actor {type: 'CITIZEN', status: 'active'})
MATCH (dead:Actor {type: 'CITIZEN', status: 'dead'})
WITH count(alive) AS n_alive, count(dead) AS n_dead
WHERE n_alive + n_dead != 7
RETURN n_alive, n_dead
```
Resultat attendu : zero lignes.

---

## Invariants Semantiques

### V7 : Les metiers sans porteur actif sont detectables

**Regle :** Quand un metier (Narrative de type METIER) n'a plus aucun citoyen actif lie par PRACTICES, le graph doit le refleter. Ce n'est pas un invariant de prevention (ca doit arriver -- c'est l'effet cascade) mais de detection : le moteur doit pouvoir lister les metiers orphelins.

**Test :**
```cypher
MATCH (n:Narrative {type: 'METIER'})
WHERE NOT EXISTS {
    MATCH (a:Actor {type: 'CITIZEN', status: 'active'})-[l:link {type: 'PRACTICES'}]->(n)
}
RETURN n.name AS metier_perdu
```

A Ch. IV, resultat : Chef d'expedition, Cartographe.
A Ch. VIII, resultat : 13 metiers.

---

### V8 : Les predictions sont tracables

**Regle :** Chaque lien PREDICTS relie un Actor a un Moment futur. Quand le Moment se realise (status passe de `predicted` a `occurred`), le lien reste. La precision de la prediction est lisible retroactivement.

**Test :** Verifier que tout lien PREDICTS pointe vers un Moment (pas vers un autre type de noeud).

---

### V9 : La Charge est toujours portee

**Regle :** Le noeud Thing `thing:charge` a toujours au moins un lien CARRIES vers un Actor actif, tant qu'il reste au moins un citoyen vivant. La Charge ne peut pas etre abandonnee -- c'est la mission.

**Test :**
```cypher
MATCH (t:Thing {id: 'thing:charge'})
WHERE NOT EXISTS {
    MATCH (a:Actor {status: 'active'})-[l:link {type: 'CARRIES'}]->(t)
}
RETURN t.name
```
Resultat attendu : zero lignes (tant qu'il reste des survivants).

---

### V10 : Les zones forment une sequence verticale

**Regle :** Les noeuds Space de subtype GEOLOGICAL_LAYER sont ordonnes par profondeur. Les liens PRECEDES entre les Moments de type THRESHOLD tracent la descente. On ne remonte pas -- aucun citoyen ne passe d'une zone profonde a une zone moins profonde.

**Test :** Verifier que les timestamps des liens INHABITS sont monotoniquement croissants en profondeur. Un citoyen qui "remonte" viole l'invariant fondamental du recit : on ne remonte pas.

---

### V11 : Le synthesis de chaque noeud est non-vide

**Regle :** Aucun noeud ne peut avoir un `synthesis` vide ou null. Le synthesis est ce que les embeddings voient. Un noeud sans synthesis est un noeud invisible pour la recherche semantique.

**Test :**
```cypher
MATCH (n)
WHERE n.synthesis IS NULL OR n.synthesis = ''
RETURN labels(n), n.name, n.id
```
Resultat attendu : zero lignes.

---

### V12 : Les liens SPEAKS_TO des morts ne sont pas supprimes

**Regle :** Quand un citoyen meurt, ses liens SPEAKS_TO restent dans le graph. Ils sont historiques -- ils temoignent de relations qui ont existe. Les supprimer serait effacer l'histoire du Contact. Le moteur peut filtrer par `a.status = 'active'` pour ne voir que les liens vivants.

**Pourquoi :** Le graph est une memoire, pas un etat present uniquement. La traversal d'un lien SPEAKS_TO vers un mort revele l'absence -- c'est exactement ce que le roman fait quand Nandi sent le Contact-fantome.

---

## Invariants de Coherence avec le Schema Mind

### V13 : Aucun type de noeud custom

**Regle :** Seuls Actor, Space, Moment, Narrative, Thing existent comme labels. Pas de label Seisme, Contact, Metier, Zone. Toute la semantique est dans le champ `type` (string).

### V14 : Tous les liens sont de type `link`

**Regle :** Un seul type de relation dans le graph : `link`. Pas de relation TRUSTS, AT, BELIEVES comme labels Neo4j/FalkorDB. La semantique est dans `link.type` (string property).

---

*Invariants derives de : MAPPING.md, PATTERNS_Graph_Schema.md, ALGORITHM_Graph_Schema.md, VALIDATION_Contact.md*
