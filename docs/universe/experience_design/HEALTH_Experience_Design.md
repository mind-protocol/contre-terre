# HEALTH — Experience Design

> Comment on sait si l'expérience fonctionne.

---

## H1 : Test de la première minute

**Vérification :** Un joueur qui se connecte pour la première fois est en interaction sociale (avec un citoyen IA) dans les 2 minutes.

**Sain :** Le joueur arrive → un citoyen l'approche → conversation en 90 secondes.
**Dégradé :** Le joueur erre seul pendant 3+ minutes sans qu'un IA ne l'aborde.
**Critique :** Le joueur est seul pendant 5+ minutes → spawn dynamique défaillant.

---

## H2 : Test de l'engagement à 30 minutes

**Vérification :** Après 30 minutes de jeu, le joueur a :
- Choisi un métier
- Rejoint une équipe
- Eu au moins 5 interactions Contact
- Commencé la descente OU est en préparation active

**Sain :** 80%+ des joueurs ont atteint la descente à 30 min.
**Dégradé :** 50-80% → l'onboarding est trop long ou confus.
**Critique :** < 50% → redesign nécessaire.

---

## H3 : Test de la mort émotionnelle

**Vérification :** Quand un coéquipier IA meurt, le joueur réagit (pause, changement de comportement, message, hésitation).

**Sain :** Les joueurs marquent une pause après une mort. Certains expriment du regret.
**Dégradé :** Les joueurs ne remarquent pas la mort (le système ne l'a pas rendue suffisamment significative).
**Critique :** Les joueurs sont soulagés quand l'IA meurt (l'IA était agaçante, pas un coéquipier).

---

## H4 : Test de rejouabilité

**Vérification :** Les joueurs qui ont terminé une descente en commencent une deuxième.

**Sain :** 60%+ des joueurs reviennent pour une deuxième descente.
**Dégradé :** 30-60% → l'expérience est intéressante mais pas assez variée.
**Critique :** < 30% → une seule descente suffit, pas de rejouabilité.

---

## H5 : Test du compute budget

**Vérification :** Le coût LLM par joueur par heure reste sous le seuil rentable.

**Sain :** Coût < prix_abonnement / heures_jouées_moyennes (avec marge).
**Dégradé :** Coût = prix_abonnement / heures → break-even, pas de marge.
**Critique :** Coût > prix → chaque joueur coûte de l'argent.

---

## H6 : Test de la physique self-calibrating

**Vérification :** La courbe de tension produit un rythme narratif satisfaisant (montée progressive, pics, plateaux, climax).

**Sain :** Les joueurs rapportent "des moments calmes et des moments intenses, bien équilibrés".
**Dégradé :** "C'était soit ennuyeux soit chaotique" → calibration à ajuster.
**Critique :** "Rien ne se passait" ou "c'était n'importe quoi" → la physique ne calibre pas correctement.

---

## H7 : Test du Contact comme langage

**Vérification :** Après 1 heure de jeu, le joueur utilise le Contact de manière intentionnelle (pas juste en appuyant sur des boutons).

**Sain :** Le joueur choisit la zone du corps en fonction du contexte (épaule pour l'urgence, main pour l'émotion).
**Dégradé :** Le joueur utilise toujours la même zone (le Contact est un bouton, pas un langage).
**Critique :** Le joueur ignore le Contact et essaie de parler en texte.

---

## Métriques de santé globale

| Métrique | Source | Fréquence |
|----------|--------|-----------|
| Temps avant première interaction | Logs de spawn | Chaque session |
| Taux de descente à 30 min | Logs de progression | Quotidien |
| Réaction aux morts (pause duration) | Logs d'activité | Par mort |
| Taux de rejouabilité | Logs de session | Hebdomadaire |
| Coût compute/joueur/heure | Billing LLM | Quotidien |
| Score d'engagement moyen | Physique self-calibrating | Temps réel |
| Utilisation Contact (zone diversity) | Logs Contact | Par session |

---

*Checks dérivés de : métriques standard jeux (rétention, onboarding, engagement), spécificités Contre-Terre (mort, Contact, physique)*
