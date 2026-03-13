# HEALTH : Verification de la Qualite du Systeme des Metiers

## Signaux de sante et verifications

---

## Checks actifs

### H1 : Couverture des demonstrations

**Question :** Chaque metier est-il montre en action au moins une fois avant la mort de son porteur ?

**Methode :** Pour chaque metier, lister la premiere scene de demonstration. Si aucune scene n'existe et que le porteur doit mourir dans un chapitre encore non ecrit, le marquer comme REQUIS.

**Etat actuel :**

| Metier | Montre | Score |
|--------|--------|-------|
| Chef d'expedition (#12) | Multiples scenes (Ch. I-IV) | SAIN |
| Cartographe (#7) | Ch. II, IV | SAIN |
| Seismo-auditeur (#8) | Ch. I, II, IV | SAIN |
| Meteorologue (#1) | Non montre | REQUIS avant Ch. V |
| Mineur (#4) | Partiel (Ch. I, caissons) | A RENFORCER |
| Ocean (#2) | Ch. III (gourdes) | SAIN |
| Speleologue (#14) | Partiel (Ch. II, baton chimique) | A RENFORCER |
| Biologiste (#3) | Ch. II | SAIN |
| Cuisiniere (#13) | Ch. I | SAIN |
| Survivaliste (#10) | Non montre | REQUIS avant Ch. VI |
| Aeromaitre (#15) | Ch. I, II, III, IV | SAIN |
| Geologue (#6) | Non montre | REQUIS avant Ch. VII |
| Grimpeuse (#11) | Ch. I, II, IV | SAIN |
| Explosiviste (#5) | Non montre | REQUIS avant Ch. VII |
| Predictrice (#9) | Ch. I, II, III, IV | SAIN |
| Explosiviste backup (#5b) | Non montre | REQUIS avant Ch. VIII |

**Score global :** 9/16 sains, 2 partiels, 5 requis.
**Verdict :** ACCEPTABLE pour 4 chapitres ecrits sur 8. Les 5 manquants correspondent aux chapitres non encore ecrits.

---

### H2 : Coherence des assignations

**Question :** Les trois sources (METIERS.md, SQUELETTE.md, chapitres) sont-elles alignees ?

**Methode :** Croiser les assignations des trois sources.

**Etat actuel :**

| Issue | Severite | Detail |
|-------|----------|--------|
| METIERS.md assigne "Speleologue (?)" a Thabo | HAUTE | SQUELETTE.md dit Geologue. Thabo n'est pas speleologue. |
| METIERS.md a des "?" sur la plupart des personnages | MOYENNE | Les assignations sont vagues ou absentes dans METIERS.md |
| METIERS.md pas a jour par rapport a SQUELETTE.md | MOYENNE | SQUELETTE.md est plus complet et plus recent |

**Verdict :** METIERS.md devrait etre mis a jour pour s'aligner sur SQUELETTE.md. C'est une dette documentaire, pas une erreur narrative (les chapitres suivent SQUELETTE.md).

---

### H3 : Cascade operationnelle

**Question :** La degradation des competences suit-elle la progression prevue ?

**Methode :** A chaque mort, verifier que les competences perdues et les competences restantes correspondent a ALGORITHM_Metiers.md.

**Etat actuel :** Seul Ch. IV est verificable (une mort ecrite).
- Senzo mort : le groupe perd chef + cartographe → VERIFIE dans le texte (scene 6 : "Sans carte. Sans chef. Sans Senzo.")

**Verdict :** SAIN pour les chapitres ecrits. A verifier chapitre par chapitre a l'ecriture.

---

### H4 : Ironie geologique

**Question :** Chaque mort est-elle liee a l'expertise du personnage ?

**Methode :** Pour chaque mort ecrite, verifier que l'element de mort correspond au domaine d'expertise.

**Etat actuel :**
- Senzo (chef/cartographe) → meurt en choisissant une route et en protegeant l'equipe (glissement de terrain). Ironie : la route l'a tue. VERIFIE.

**Verdict :** SAIN. A verifier pour chaque mort ecrite.

---

### H5 : Scenes de perte ressentie

**Question :** Apres chaque mort, le groupe est-il confronte a l'absence du metier ?

**Methode :** Identifier la scene de manque apres chaque mort.

**Etat actuel :**
- Apres Senzo (Ch. IV) : "Qui choisirait maintenant ?" + "Sans carte. Sans chef." + pas de nouveau signal de route → VERIFIE.

**Verdict :** SAIN. La scene 6 du Ch. IV est exemplaire pour ce pattern.

---

## Signaux de degradation

Le systeme se degrade si :

1. **Un metier devient invisible.** Si un metier assigne a un personnage n'est jamais montre dans le texte avant sa mort, la perte sera abstraite. Le lecteur ne ressentira pas la cascade.

2. **Les assignations divergent entre les sources.** Si METIERS.md, SQUELETTE.md et les chapitres se contredisent, les futures sessions d'ecriture risquent d'introduire des incoherences.

3. **La cascade perd sa gradation.** Si un chapitre ne montre pas la consequence de la perte precedente (le groupe n'est jamais montre en difficulte a cause d'un metier perdu), l'effet cascade est rompu.

4. **Les metiers sont nommes au lieu d'etre montres.** Si un personnage dit "je suis meteorologue" ou si le narrateur liste les competences, le pattern d'immersion est casse.

5. **Un personnage exerce un metier apres la mort de son porteur.** Erreur de continuite qui brise l'invariant V1.

---

## Recovery

Si une degradation est detectee :

1. **Metier invisible :** Ajouter une scene de demonstration dans le chapitre en cours ou le precedent. Pas d'exposition — un geste, un reflexe, une action.

2. **Assignations divergentes :** Mettre a jour METIERS.md en s'alignant sur SQUELETTE.md. Ne jamais modifier SQUELETTE.md pour s'aligner sur METIERS.md (SQUELETTE.md fait autorite).

3. **Cascade rompue :** Ajouter une scene de manque — le groupe face a un probleme que le mort aurait su resoudre.

4. **Metier nomme :** Supprimer la nomination. La remplacer par une action. "Thabo, l'Aeromaitre, testa l'air" → "Thabo sortit son tissu."

5. **Metier exerce post-mortem :** Supprimer ou transformer en hallucination (Contact-fantome, Ch. VIII uniquement).
