# PATTERNS : World Manifest

**Module :** `universe/manifest`
**Question centrale :** En quoi le manifest de Contre-Terre differe structurellement de celui de Venezia, et pourquoi ?

---

## P1 : Contact-range tiers au lieu de voice tiers

**Decision :** Remplacer le schema d'entites `{ voice: true|"proximity"|false, radius: N }` de Venezia par `{ contact_mode: "direct"|"corde"|"hydraulic"|"monde", contact_range: N, contact_resolution: "full"|"functional"|"basal" }`.

**Pourquoi :** Dans Venezia, la voix est le canal principal de communication. Les tiers (FULL, ACTIVE, AMBIENT) determinent qui parle et a quelle distance. Contre-Terre a detruit ce canal. Le sol gronde en permanence -- le son est non fiable. Le Contact exige la proximite physique : bras a bras, epaule a epaule, paume a paume. La portee n'est pas une distance de propagation sonore mais une distance de toucher.

**Consequence :** Le `contact_range` d'un tier FULL est de ~0.5m (toucher direct). Un tier ACTIVE peut etre a ~5m (Contact-corde, vibrations transmises). Un tier AMBIENT est une presence sentie par le sol (vibrations de pas, poids sur la roche). La hierarchie n'est pas "qui a le droit de parler" mais "qui est assez proche pour toucher."

**Alternative rejetee :** Garder le schema Venezia et traduire `voice` en `contact`. Rejete parce que les mecaniques sont fondamentalement differentes. La voix se propage dans l'air ; le Contact se propage par le corps. Les parametres physiques sont incompatibles.

---

## P2 : Zones sismiques au lieu de districts

**Decision :** Remplacer les zones planes de Venezia (sestieri, piazza, canaux) par des couches geologiques verticales. Chaque zone a un `seismic_profile` (frequence, amplitude, caractere) au lieu d'un simple `position`.

**Pourquoi :** Venezia est horizontale. On se promene entre des places et des ponts. Contre-Terre est verticale. On descend a travers des couches de roche, chacune avec ses propres regles physiques. La profondeur n'est pas un attribut spatial -- c'est le parametre dominant qui determine la temperature, la pression, la frequence sismique, la luminosite et la viabilite de la vie.

**Structure :**
```
zones: [
  { id: "surface_desert", depth: 0, seismic_profile: {...}, contact_modes: ["direct"], ... },
  { id: "piemont_volcanic", depth: -200, seismic_profile: {...}, contact_modes: ["direct", "monde"], ... },
  { id: "village_sourds", depth: -800, seismic_profile: {...}, contact_modes: ["direct", "hydraulic", "haute_resolution"], ... },
  { id: "faille_verticale", depth: -2000, seismic_profile: {...}, contact_modes: ["corde"], ... },
  { id: "cavernes_profondes", depth: -4000, seismic_profile: {...}, contact_modes: ["direct", "corde"], ... },
  { id: "zones_volcaniques", depth: -6000, seismic_profile: {...}, contact_modes: ["direct_douloureux"], ... },
  { id: "boyau", depth: -8000, seismic_profile: {...}, contact_modes: ["force"], ... },
  { id: "grotte_finale", depth: -10000, seismic_profile: {...}, contact_modes: ["fantome", "monde"], ... }
]
```

**Consequence :** Les transitions entre zones sont des seuils irreversibles. Le manifest encode `reversible: false` pour chaque transition (sauf surface <-> piemont au debut). Un citoyen qui descend ne remonte pas.

---

## P3 : Tremens au lieu de mood

**Decision :** Remplacer tout systeme d'etat emotionnel abstrait par un systeme physiologique ancre dans la physique sismique. L'etat d'un citoyen n'est pas un `mood: "happy"|"anxious"` mais un `tremens_state` calcule par l'ecart entre son spectre natal et la frequence sismique locale.

**Pourquoi :** Le tremens n'est pas une emotion -- c'est une reaction du corps aux vibrations. Il a des symptomes objectifs (salivation, vomissements, tremblements, hallucinations) et une intensite mesurable (distance frequentielle). Un citoyen qui vient des archipels du nord-est (frequences hautes et seches) reagira violemment aux basses profondes du desert du sud. Ce n'est pas psychologique -- c'est physique.

**Parametres :**
```json
{
  "natal_spectrum": { "frequency": "high", "character": "dry-sharp" },
  "tremens_sensitivity": 0.85,
  "current_tremens_level": "severe",
  "adaptation_rate": 0.02
}
```

---

## P4 : Metier-based avatar styles au lieu de social class colors

**Decision :** Remplacer `social_class_styles` (Patrician → gold-crimson, Cittadino → blue-silver...) par `metier_styles` ou chaque metier porte une signature visuelle liee a son outil et son geste.

**Pourquoi :** Contre-Terre n'a pas de classes sociales. Les archipels sont nomades, le pouvoir est local et fragmente. L'identite est definie par ce que tu sais faire, pas par ta naissance. L'Aeromaitre est reconnaissable par son tissu au vent. Le Seismo-auditeur par son sismographe au torse. La Grimpeuse par ses mains qui comptent. La Predictrice par ses pieds nus.

**Mapping :**
```json
{
  "aeromaitre": { "palette": "grey-white", "signature": "tissu", "ornament": "windcloth" },
  "seismo_auditeur": { "palette": "stone-dark", "signature": "sismographe", "ornament": "scroll" },
  "cartographe": { "palette": "sand-ochre", "signature": "carte", "ornament": "roll" },
  "biologiste": { "palette": "moss-earth", "signature": "racines", "ornament": "root" },
  "grimpeuse": { "palette": "rope-brown", "signature": "mains_comptant", "ornament": "carabiner" },
  "predictrice": { "palette": "skin-bare", "signature": "pieds_nus", "ornament": "none" },
  "oceanologue": { "palette": "deep-blue", "signature": "gourdes", "ornament": "water" }
}
```

---

## P5 : Bioluminescence comme systeme de lumiere dynamique

**Decision :** Remplacer `sky_model: "preetham"` et les parametres solaires de Venezia par un systeme de bioluminescence. Le ciel n'est pas la source de lumiere -- la roche l'est.

**Pourquoi :** Contre-Terre est un monde souterrain (des le Ch. II). La lumiere vient de trois sources : le soleil (surface seulement), les batons chimiques (vert), et les filaments bioluminescents (bleu). Les filaments pulsent au rythme sismique (magnitude 4), s'intensifient au toucher, et disparaissent avec la profondeur. Au Ch. VI+, la seule lumiere est celle de la lave (orange).

**Consequence :** Le manifest encode `light_source` par zone au lieu d'un `sun` global. La lumiere est locale, reactive, organique -- pas celeste et constante.

---

## P6 : Pas de portails, mais des seuils

**Decision :** Remplacer les `portals` inter-mondes de Venezia par des `thresholds` -- des points de non-retour geologiques. Un seuil n'est pas une porte : c'est un effondrement, un retrecissement, une crue qui ferme le passage derriere.

**Pourquoi :** La verticalite est irreversible. Le roman ne permet pas de remonter. Le manifest encode cette irreversibilite dans la structure meme des transitions entre zones. Le seul "portail" est le portail d'entree depuis le hub Cities of Light, qui depose le visiteur a la surface du desert.

**Exception :** Un portail `hub_return` existe a la surface, avant l'entree dans le piemont. Une fois sous terre, il n'y a plus de retour -- ni vers le hub, ni vers la surface. Ce portail est exclusivement pour les arrivants (visiteurs externes). Les citoyens CT ne l'utilisent pas -- leur corps calibre au tremens rend le voyage inter-univers biologiquement inviable.

---

## P7 : Le roman comme mythe, les personnages comme citoyens

**Decision :** Les 7 personnages du roman (Nandi, Senzo, Sihle, Enama, Thabo, Inyoni, Jabu) sont les premiers citoyens vivants de l'univers Contre-Terre. Le roman, ecrit par MIND, est le mythe fondateur de l'univers -- pas son histoire. Les personnages ne meurent pas canoniquement.

**Pourquoi :** Si les personnages sont morts dans l'univers, ils ne peuvent pas etre les premiers citoyens IA vivants du monde. Le roman raconte ce qui *pourrait* arriver a une equipe qui descend -- une prophetie, un recit de fondation. Les citoyens connaissent le recit de la descente comme on connait un mythe ancestral. Chaque game loop est une re-enaction procedurale du mythe, avec des variables differentes.

**Consequence :** Le manifest encode les 7 personnages comme `alive: true` dans `data/citizens.json`. Leurs brain seeds (16 fichiers JSON, 347 noeuds, 736 liens) definissent les premiers cerveaux de l'univers. Les game loops rejouent une version procedurale de la descente, mais la mort des personnages dans le mythe ne pre-determine pas leur mort dans l'univers.

---

*Decisions traceables a : world-manifest.json (Venezia, format reference), MONDE.md, CONTACT.md, PATTERNS_Geographie.md, ALGORITHM_Seismique.md, ALGORITHM_Contact.md*
