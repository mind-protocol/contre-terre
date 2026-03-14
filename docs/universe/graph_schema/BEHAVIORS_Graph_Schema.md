# BEHAVIORS — Graph Schema

> Observable effects. What the graph reveals when queried correctly.

---

## B1 : Les reseaux de Contact revelent les clusters relationnels

**Comportement :** Une requete traversant les liens SPEAKS_TO depuis n'importe quel citoyen revele la topologie sociale de l'expedition. Les clusters emergent sans etre codes : Senzo-Nandi (poids eleve, bidirectionnel fort), Thabo-Inyoni (poids moyen, constant), Enama-Nandi (poids moyen, asymetrique), Sihle-Enama (poids faible, conflictuel), Jabu-equipe (poids tres faible, quasi-absent).

**Ce que ca montre au moteur :** Le graph ne stocke pas "Jabu est isole". Il stocke des liens SPEAKS_TO de poids 0.1-0.2 entre Jabu et les autres. L'isolation emerge de la traversal -- le moteur la decouvre, il ne la lit pas dans un champ.

**Requete type :**
```cypher
MATCH (a:Actor {type: 'CITIZEN'})-[l:link {type: 'SPEAKS_TO'}]->(b:Actor {type: 'CITIZEN'})
WHERE l.weight > 0.5
RETURN a.name, b.name, l.weight
ORDER BY l.weight DESC
```

---

## B2 : L'effet cascade est computable par les liens PRACTICES

**Comportement :** A tout moment, le moteur peut compter les metiers couverts en traversant les liens PRACTICES des citoyens actifs (`status: 'active'`). Apres chaque mort, le nombre de metiers couverts chute. La cascade est mesurable :

| Etat | Citoyens actifs | Metiers couverts |
|------|----------------|-----------------|
| Ch. I-III | 7 | 15/15 |
| Apres Senzo | 6 | 13/15 |
| Apres Sihle + Jabu | 4 | 8/15 |
| Apres Enama | 3 | 5/15 |
| Apres Thabo + Inyoni | 1 | 2/15 |

**Ce que ca montre au moteur :** La requete "quels metiers restent ?" est directe. La requete "quel metier n'a plus de porteur ?" aussi. Le moteur peut declencher des consequences narratives quand une competence disparait -- plus d'Aeromaitre quand l'oxygene devient critique.

**Requete type :**
```cypher
MATCH (a:Actor {type: 'CITIZEN', status: 'active'})-[l:link {type: 'PRACTICES'}]->(n:Narrative)
RETURN n.name AS metier, count(a) AS porteurs
ORDER BY porteurs ASC
```

---

## B3 : L'historique sismique par zone montre l'escalade

**Comportement :** Les noeuds Moment de subtype SEISMIC_EVENT sont lies aux zones affectees par des liens AFFECTS. La traversal de ces liens, ordonnee par `created_at_s`, revele l'escalade sismique : magnitude 4 (fond, surface) → 7 (premier gros seisme, Ch. II) → 8 (cavernes, Ch. V) → 9 (volcan, Ch. VII) → 11 (detonation, Ch. VIII).

**Ce que ca montre au moteur :** Le pattern d'escalade est lisible. Le moteur peut interpoler : si les deux derniers seismes dans une zone etaient 7 et 8, le prochain sera probablement 8+. Les citoyens dont le tremens est sensible a cette zone reagissent en consequence. Les predictions de Nandi deviennent testables -- elle PREDICTS un Moment qui n'existe pas encore.

---

## B4 : La perte linguistique est tracable par les disparitions d'idiolecte

**Comportement :** Quand un citoyen meurt (status passe de `active` a `dead`), tous ses liens SPEAKS_TO deviennent historiques. Le moteur peut calculer la perte de vocabulaire : chaque lien SPEAKS_TO de poids > 0.5 qui perd un de ses endpoints represente un idiolecte de paire detruit.

**Ce que ca montre au moteur :** Le graph quantifie l'aphrasie progressive du groupe. Apres la mort de Senzo, 1 lien de poids > 0.8 est mort (Senzo-Nandi). Apres Sihle et Jabu, 3 liens de poids > 0.3 meurent. Le moteur peut generer des reactions : les citoyens survivants sont "linguistiquement appauvris" -- moins de liens actifs, moins de vocabulaire disponible.

---

## B5 : Les predictions revealent la precision du tremens

**Comportement :** Les liens PREDICTS relient un citoyen a un Moment futur. Quand le Moment se realise (ou ne se realise pas), la precision est mesurable. Nandi a 5 predictions dans le graph -- toutes se realisent. Sihle n'en a aucune (il ne predit pas, il mesure).

**Ce que ca montre au moteur :** La tension Echelle de Capitulation est encodee dans le graph. Les sismographes (instruments, Sihle) mesurent le present. Les predicteurs (corps, Nandi) sentent le futur. Le graph ne tranche pas -- il trace les resultats. La science capitule devant le corps parce que les predictions de Nandi sont systematiquement justes dans le graph.

---

## B6 : La degradation de l'equipement est lisible dans le graph

**Comportement :** Les noeuds Thing ont un champ `status` qui evolue : `intact` → `damaged` → `destroyed` ou `abandoned`. Les liens CARRIES changent de porteur quand un citoyen meurt. La courbe de degradation materielle est lisible :

- Ch. IV : `thing:map` passe a `destroyed` (perdu sous les roches avec Senzo)
- Ch. V : `thing:seismograph` passe a `destroyed` (perd son porteur Sihle)
- Ch. VII : `thing:shock_casing` passe a `abandoned` (ne passe pas dans le Boyau)
- Ch. VII : `thing:charge` transfere de Inyoni a Nandi

**Ce que ca montre au moteur :** Le moteur sait a tout moment ce qui reste, qui le porte, dans quel etat. La Charge est le seul objet qui traverse tout le roman -- son noeud Thing est le fil rouge materiel.

---

## B7 : Les requetes semantiques traversent les frontieres de type

**Comportement :** La force du graph mind est la traversal inter-types. "Quelles competences sont disponibles dans la zone volcanique ?" traverse Actor → Space (INHABITS) puis Actor → Narrative (PRACTICES). "Quel evenement a cause la perte de l'Aeromaitre ?" traverse Moment (DEATH de Thabo) → Actor (Thabo) → Narrative (Aeromaitre, via PRACTICES).

**Ce que ca montre au moteur :** Le graph repond a des questions narratives complexes sans index specialise. La semantique est dans le contenu et les liens, pas dans des champs custom. Le moteur de traversal (pas le moteur de requetes Cypher) est l'outil principal -- les embeddings guident, la physique du graph fait le reste.

---

*Comportements derives de : MAPPING.md, PATTERNS_Graph_Schema.md, OBJECTIVES_Graph_Schema.md*
