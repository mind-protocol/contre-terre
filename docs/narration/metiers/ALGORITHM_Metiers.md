# ALGORITHM : Mecanique du Systeme des Metiers

## Matrice d'assignation, progression de la cascade, ruptures par chapitre

---

## Matrice d'assignation

```
                #1   #2   #3   #4   #5   #6   #7   #8   #9   #10  #11  #12  #13  #14  #15
               Met  Oce  Bio  Min  Exp  Geo  Car  Eco  Pre  Sur  Gri  Lea  Cui  Spe  Aer
Senzo           .    .    .    .    .    .    X    .    .    .    .    X    .    .    .
Sihle           X    .    .    X    .    .    .    X    .    .    .    .    .    .    .
Jabu            .    X    .    .    .    .    .    .    .    .    .    .    .    X    .
Enama           .    .    X    .    .    .    .    .    .    X    .    .    X    .    .
Thabo           .    .    .    .    .    X    .    .    .    .    .    .    .    .    X
Inyoni          .    .    .    .    X    .    .    .    .    .    X    .    .    .    .
Nandi           .    .    .    .   (B)   .    .    .    X    .    .    .    .    .    .
```

Legende : X = competence principale, (B) = backup, . = non assigne

Total : 15 metiers assignes (14 principaux + 1 backup) sur 7 personnages.
Repartition : 2 metiers x 5 personnages + 3 metiers x 2 personnages (Sihle, Enama).

---

## Hierarchie sismique : les trois etages

La perception sismique est structuree en trois niveaux, du plus institutionnel au plus corporel :

```
L3 : PREDICTION (Nandi, #9)
     Corps predit le futur via le tremens.
     Rejetee par la science. Pas d'instrument.
     Precision : seismes + direction + magnitude approximative
     |
L2 : ECOUTE (Sihle, #8)
     Corps entraine a percevoir le present.
     Validation par instruments.
     Precision : seismes en temps reel, avant les instruments
     |
L1 : INSTRUMENTS (Sihle, sismographe)
     Mesure mecanique du present.
     Precision : magnitudes, frequences, courbes
     Limite : ne mesure que ce qui est deja arrive
```

**Tension narrative :** L1 et L2 sont portes par la meme personne (Sihle). Quand Sihle meurt, les deux premiers niveaux disparaissent simultanement. Il ne reste que L3 (Nandi) — le niveau le plus puissant mais le moins legitime.

Cette structure est un miroir du conflit raison/intuition. Sihle represente les deux etages valides de la connaissance : l'instrument et le sens entraine. Nandi represente l'etage que la connaissance refuse : le corps qui sait avant de comprendre.

---

## Progression de la cascade

### Etat initial (Ch. I-III) : 15/15 competences

Equipe complete. Tous les metiers sont actifs. Le groupe fonctionne comme un organisme :

```
Navigation :   Cartographe (Senzo) + Speleologue (Jabu) = 2/2
Perception :   Seismo-auditeur (Sihle) + Predictrice (Nandi) + Aeromaitre (Thabo) = 3/3
Science :      Meteorologue (Sihle) + Geologue (Thabo) + Biologiste (Enama) = 3/3
Survie :       Survivaliste (Enama) + Cuisiniere (Enama) + Specialiste ocean (Jabu) = 3/3
Operation :    Mineur (Sihle) + Grimpeuse (Inyoni) + Explosiviste (Inyoni) = 3/3
Commandement : Leader (Senzo) = 1/1
```

### Mort de Senzo (Ch. IV) : 13/15 competences

Pertes : Leader (#12), Cartographe (#7)

```
Navigation :   Cartographe MORT + Speleologue (Jabu) = 1/2     [DEGRADE]
Perception :   Inchange = 3/3
Science :      Inchange = 3/3
Survie :       Inchange = 3/3
Operation :    Inchange = 3/3
Commandement : Leader MORT = 0/1                                [PERDU]
```

**Impact narratif :** Le groupe perd sa capacite de decision et sa carte. A partir d'ici, les choix de route ne sont plus rationnels — ils sont des actes de survie. Le conflit Sihle/Enama s'aggrave parce que personne ne tranche.

### Mort de Sihle + Jabu (Ch. V) : 8/15 competences

Pertes : Seismo-auditeur (#8), Meteorologue (#1), Mineur (#4), Specialiste ocean (#2), Speleologue (#14)

```
Navigation :   Cartographe MORT + Speleologue MORT = 0/2       [PERDU]
Perception :   Seismo-auditeur MORT + Predictrice (Nandi) + Aeromaitre (Thabo) = 2/3
Science :      Meteorologue MORT + Geologue (Thabo) + Biologiste (Enama) = 2/3
Survie :       Survivaliste (Enama) + Cuisiniere (Enama) + Ocean MORT = 2/3
Operation :    Mineur MORT + Grimpeuse (Inyoni) + Explosiviste (Inyoni) = 2/3
Commandement : Leader MORT = 0/1                                [PERDU]
```

**Impact narratif :** La moitie des competences est perdue. La navigation est totalement detruite — ni carte, ni speleologue. Le groupe avance a l'instinct. La hierarchie sismique perd ses deux premiers niveaux (L1 et L2). Seul L3 reste — et c'est le niveau que Sihle niait.

**Point de bascule :** Enama porte desormais 3 des 8 competences restantes (biologie, cuisine, survie). Elle devient indispensable et culpabilisee simultanement — c'est elle qui a cause la mort de Sihle.

### Mort d'Enama (Ch. VI) : 5/15 competences

Pertes : Biologiste (#3), Cuisiniere (#13), Survivaliste (#10)

```
Navigation :   0/2                                              [PERDU]
Perception :   Predictrice (Nandi) + Aeromaitre (Thabo) = 2/3
Science :      Geologue (Thabo) = 1/3
Survie :       0/3                                              [PERDU]
Operation :    Grimpeuse (Inyoni) + Explosiviste (Inyoni) = 2/3
Commandement : 0/1                                              [PERDU]
```

**Impact narratif :** Trois domaines entiers sont detruits : navigation, survie, commandement. Le groupe ne se dirige plus, ne survit plus, ne decide plus. Il avance par inertie. Les seules competences restantes sont la perception, une science partielle, et les operations — le minimum pour accomplir la mission.

### Mort de Thabo + Inyoni (Ch. VII) : 1/15 competences (+ 1 backup)

Pertes : Aeromaitre (#15), Geologue (#6), Grimpeuse (#11), Explosiviste principal (#5)

```
Navigation :   0/2                                              [PERDU]
Perception :   Predictrice (Nandi) = 1/3
Science :      0/3                                              [PERDU]
Survie :       0/3                                              [PERDU]
Operation :    Explosiviste BACKUP (Nandi) = (1)/3              [CRITIQUE]
Commandement : 0/1                                              [PERDU]
```

**Impact narratif :** Il ne reste qu'une competence pleine : la prediction. Et une competence de backup : les explosifs. L'Aeromaitre meurt quand l'oxygene est critique. La grimpeuse meurt quand il faut encore se deplacer dans des passages verticaux. L'explosiviste principale meurt quand la charge doit encore etre posee.

Nandi est seule avec :
- Un corps qui predit les seismes (son metier)
- Des mains qui ont vu le detonateur (son backup)
- Aucune autre competence

### Etat final — Nandi seule (Ch. VIII) : 1/15 + backup

```
Competences actives :
  - Prediction (#9) : ACTIVE — son corps est un sismographe
  - Explosifs (#5) : BACKUP — ses mains savent le geste, pas la theorie

Competences perdues : 13 sur 15

La mission repose sur :
  1. Son corps la guide vers le point de detonation (prediction)
  2. Ses mains activent la charge (backup explosiviste)
  3. La magnitude 11 fait le reste (la terre)
```

---

## Dependencies critiques entre metiers

Certains metiers fonctionnent en binome ou en chaine. Quand l'un tombe, l'autre est diminue :

```
Cartographe (Senzo) ←→ Speleologue (Jabu)
  La carte guide le speleologue. Le speleologue corrige la carte.
  Senzo meurt Ch. IV → Jabu perd sa reference.
  Jabu meurt Ch. V → la navigation est detruite.

Seismo-auditeur (Sihle) ←→ Predictrice (Nandi)
  Sihle valide/invalide les predictions de Nandi par ses instruments.
  Nandi donne a Sihle des signaux que ses instruments ne captent pas.
  Sihle meurt Ch. V → Nandi n'a plus de validation.
  Mais aussi : Nandi n'a plus de contradicteur.

Aeromaitre (Thabo) ←→ Meteorologue (Sihle)
  Thabo lit l'air present. Sihle predit l'air futur (meteo).
  Sihle meurt Ch. V → Thabo lit le present sans prevision.
  Thabo meurt Ch. VII → l'air n'est plus lu du tout.

Explosiviste (Inyoni) ←→ Explosiviste backup (Nandi)
  Inyoni execute. Nandi observe.
  Inyoni meurt Ch. VII → Nandi doit executer.
  Ecart de competence : formation complete vs observation.

Grimpeuse (Inyoni) ←→ Speleologue (Jabu)
  La verticale et l'horizontal des profondeurs.
  Jabu meurt Ch. V → plus d'horizontal expert.
  Inyoni meurt Ch. VII → plus de vertical expert.
```

---

## Regle de la mort-ironie

Chaque mort obeit au pattern suivant :

```
Le personnage meurt PAR l'element de son expertise
  Jabu (ocean) → noye
  Sihle (ecoute/mineur) → tombe dans le vide (le silence sismique)
  Enama (biologie/survie) → lave (la terre vivante la tue)
  Thabo (air/geologie) → enseveli (la roche l'etouffe, l'air disparait)
  Inyoni (grimpe/explosifs) → ensevelie (la montagne refuse qu'elle monte)
  Nandi (prediction/explosifs) → detonation (elle DEVIENT le seisme)

Le personnage meurt PARCE QU'il s'engage dans le domaine de son expertise
  Jabu va vers l'eau parce que c'est SON domaine
  Thabo entre dans le boyau parce qu'il a verifie l'air
  Inyoni est dans le boyau parce qu'elle est devant (grimpeuse)
  Senzo est sur le bord parce qu'il tire la corde (leader)
```

L'ironie n'est pas cynique. Elle est structurelle : chaque expert s'expose au danger qu'il connait le mieux parce que c'est son role de le faire. L'expertise est un chemin vers la mort autant qu'un outil de survie.

---

## Quand montrer chaque metier (exigence narrative)

Chaque metier doit etre montre en action **au moins une fois** avant la mort de son porteur. Sinon la perte est abstraite et le lecteur ne la sent pas.

```
Senzo (meurt Ch. IV) :
  Chef → Ch. I (signaux), Ch. II (compte les corps), Ch. III (entre en premier), Ch. IV (choisit la route) ✓
  Cartographe → Ch. II (deroule la carte), Ch. IV (carte blanche) ✓

Sihle (meurt Ch. V) :
  Seismo-auditeur → Ch. I (lit les courbes), Ch. II (note 6.2), Ch. IV (pointe la droite) ✓
  Meteorologue → A MONTRER Ch. V (prevision atmospherique avant la descente)
  Mineur → Ch. I (caissons amortisseurs). A RENFORCER.

Jabu (meurt Ch. V) :
  Ocean → Ch. III (remplit les gourdes au-dela du necessaire) ✓
  Speleologue → Ch. II (allume les batons chimiques). A RENFORCER.

Enama (meurt Ch. VI) :
  Biologiste → Ch. II (filaments bioluminescents, mains sur le mur) ✓
  Cuisiniere → Ch. I (bouillie de tubercules) ✓
  Survivaliste → A MONTRER Ch. V ou VI (technique de survie en situation extreme)

Thabo (meurt Ch. VII) :
  Aeromaitre → Ch. I (tissu dans le vent), Ch. II (range le tissu lentement), Ch. III (tissu recu du village), Ch. IV (tissu dans la faille) ✓
  Geologue → A MONTRER Ch. V ou VI (evaluation d'une paroi, identification de roche)

Inyoni (meurt Ch. VII) :
  Grimpeuse → Ch. I (sangles), Ch. II (detache/repartit), Ch. IV (verticale, noeuds, pitons) ✓
  Explosiviste → A MONTRER (verification charges, manipulation detonateur) AVANT Ch. VII

Nandi (meurt Ch. VIII) :
  Predictrice → Ch. I, II, III, IV (omnipresent) ✓
  Explosiviste backup → A MONTRER (apprentissage par observation d'Inyoni) AVANT Ch. VII
```
