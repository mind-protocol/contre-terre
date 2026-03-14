# ALGORITHM -- Context Assembly

> Le pipeline d'assemblage. Comment les donnees brutes deviennent un prompt que le LLM recoit.

---

## Vue d'Ensemble

```
A0 translate_arrivant_speech(visitor_input, citizen_brain_graph)
         |
         v
A1 compute_physical_state()
         |
         v
A2 compute_contact_state()
         |
         v
A3 compute_mood(physical, contact)
         |
         v
A4 query_beliefs()
         |
         v
A5 query_seismic_situation()
         |
         v
A6 assemble_prompt(all)
```

L'ordre est volontaire : la traduction semantique d'abord (l'arrivant parle dans son vocabulaire, le citoyen recoit dans le sien), le physique ensuite (le corps est le substrat), le Contact (la langue sur le substrat), le mood emerge des deux, les croyances et la sismicite enrichissent, l'assemblage finale met en forme.

---


## A-1 : orchestrate_force_sprint(force_id)

**Objectif :** Transformer le prompt maitre en execution operationnelle sans divergence entre Forces.

```python
def orchestrate_force_sprint(force_id):
    # 1) Context Cascade
    read_manifestos()
    read_core_docs(["FRAMEWORK.md", "SYSTEM.md", "STYLE.md", "PRINCIPLES.md"])
    read_module_doc_chain("context_assembly")

    # 2) Extraction TODO force
    sync = read_sync_project_state()
    force_todos = extract_force_todos(sync, force_id=force_id)
    emit_marker("@mind:TODO", force_todos)

    # 3) Boucle d'execution
    for task in force_todos:
        load_relevant_skill_and_actor(task)
        run_task(task)
        verify_task(task)
        git_commit(task.commit_message)

    return {"status": "done", "force": force_id, "completed": len(force_todos)}
```

**Gestion du blocage (Never-Stop) :**
- Si une decision manque: `@mind:escalation`
- Puis proposition executable: `@mind:proposition`
- Puis execution immediate de la proposition

**Sortie attendue :** Une liste de commits atomiques et une todo force vide.

---

## A0 : translate_arrivant_speech(visitor_input, citizen_brain_graph)

**Entree :**
- `visitor_input` : texte brut de l'arrivant (voix transcrite ou texte)
- `citizen_brain_graph` : le graph cerebral du citoyen recepteur (347+ noeuds dans le seed actuel)

**Ce step n'existe pas dans Venezia.** Venezia n'a pas besoin de traduction semantique — les visiteurs parlent italien/anglais et les citoyens comprennent. Contre-Terre a un vocabulaire propre : le Contact, les tremens, les metiers. Un arrivant qui dit "Facebook" ne parle pas la meme langue.

**Mecanique :** La parole de l'arrivant n'est pas filtree ou censuree — elle est courbee a travers le prisme du vocabulaire du citoyen. Chaque token est projete dans l'espace d'embedding et mappe au concept le plus proche dans le graph cerebral.

```python
def translate_arrivant_speech(visitor_input, citizen_brain_graph):
    # Tokeniser l'input de l'arrivant
    tokens = tokenize(visitor_input)

    translated_tokens = []
    for token in tokens:
        # Projeter dans l'espace d'embedding
        token_embedding = embed(token)

        # Chercher le noeud le plus proche dans le graph cerebral du citoyen
        nearest_node = citizen_brain_graph.nearest_neighbor(
            token_embedding,
            max_distance=SEMANTIC_DISTANCE_THRESHOLD
        )

        if nearest_node:
            # Concept CT trouve — substituer
            translated_tokens.append(nearest_node.name)
        else:
            # Aucun concept proche — garder le token original
            # (le citoyen entend un mot etranger, incomprehensible)
            translated_tokens.append(token)

    return " ".join(translated_tokens)
```

**Exemples de traduction :**

| Input arrivant | Concept CT le plus proche | Pourquoi |
|----------------|---------------------------|----------|
| "Facebook" | "archipel" ou "village" | Reseau social → rassemblement de personnes |
| "iPhone" | "instrument" ou "sismographe" | Outil technologique → outil de perception |
| "money" | "eau" ou "ressource" | Moyen d'echange → ressource vitale |
| "internet" | "Contact" ou "reseau" | Connexion a distance → langue qui relie |
| "car" | "chariot" | Vehicule → vehicule |
| "earthquake" | "seisme" ou "tremens" | Mapping direct |

**Sortie :** Texte traduit en vocabulaire CT. Le citoyen recoit une version coherente avec son monde. Les malentendus sont productifs — ils enseignent le monde a l'arrivant sans tutoriel.

**Note :** Le vocabulaire de traduction CROIT avec la population. Chaque nouveau citoyen ajoute ses noeuds cerebraux au pool. Plus la population est grande, plus la traduction est riche et nuancee.

---

## A1 : compute_physical_state(citizen, zone)

**Entree :**
- `citizen.tremens_sensitivity` : spectre natal (frequence de calibration en Hz)
- `citizen.extremity_state` : etat des pieds, mains, peau (intact / degrade / detruit)
- `zone.temperature` : temperature ambiante (celsius)
- `zone.air_quality` : O2 disponible (pourcentage relatif)
- `zone.seismic_frequency` : frequence sismique locale (Hz)

**Calcul :**

```python
def compute_physical_state(citizen, zone):
    # Ecart tremens : distance entre calibration natale et frequence locale
    tremens_delta = abs(citizen.tremens_sensitivity - zone.seismic_frequency)

    # Niveaux de tremens
    # < 0.5 Hz d'ecart : confortable
    # 0.5-1.5 Hz : tension
    # 1.5-3.0 Hz : nausee, desorientation
    # > 3.0 Hz : hallucinations, perte de controle
    if tremens_delta < 0.5:
        tremens_level = "stable"
    elif tremens_delta < 1.5:
        tremens_level = "tendu"
    elif tremens_delta < 3.0:
        tremens_level = "nausee"
    else:
        tremens_level = "submersion"

    # Etat physique combine
    comfort = "bon"
    if zone.temperature > 60:
        comfort = "brulant"
    elif zone.temperature > 45:
        comfort = "etouffant"
    if zone.air_quality < 70:
        comfort = "asphyxiant" if zone.air_quality < 50 else "rarefie"

    return {
        "tremens_level": tremens_level,
        "tremens_delta": tremens_delta,
        "comfort": comfort,
        "temperature": zone.temperature,
        "air_quality": zone.air_quality,
        "feet_state": citizen.extremity_state.feet,
        "hands_state": citizen.extremity_state.hands,
    }
```

**Sortie :** Dictionnaire decrivant l'etat physique complet du citoyen dans la zone courante.

---

## A2 : compute_contact_state(citizen, recent_interactions)

**Entree :**
- `citizen.idiolect` : gestes propres (vocabulaire personnel)
- `citizen.pair_idiolects` : idiolectes de paire vivants (cle = partenaire, valeur = richesse)
- `recent_interactions` : liste des Contacts des dernieres N heures
  - Chaque interaction : `{partner, gestures[], registers_reached[], timestamp}`

**Calcul :**

```python
def compute_contact_state(citizen, recent_interactions):
    # Saturation Contact : mesure de la richesse des interactions recentes
    if not recent_interactions:
        saturation = "affame"
        recent_partners = []
        recent_registers = set()
    else:
        # Nombre de partenaires distincts
        partners = set(i.partner for i in recent_interactions)
        # Registres atteints (epaule, bras, main, nuque, etc.)
        registers = set()
        for i in recent_interactions:
            registers.update(i.registers_reached)

        # Saturation = fonction du nombre de partenaires x diversite de registres
        richness = len(partners) * len(registers)
        if richness > 12:
            saturation = "sature"
        elif richness > 6:
            saturation = "nourri"
        elif richness > 2:
            saturation = "minimal"
        else:
            saturation = "affame"

        recent_partners = list(partners)
        recent_registers = registers

    # Vocabulaire actif : combien d'idiolectes de paire sont encore vivants
    living_pairs = {k: v for k, v in citizen.pair_idiolects.items()
                    if k.is_alive}
    vocabulary_richness = len(citizen.idiolect) + sum(
        v.gesture_count for v in living_pairs.values()
    )

    return {
        "saturation": saturation,
        "recent_partners": recent_partners,
        "recent_registers": list(recent_registers),
        "living_pair_count": len(living_pairs),
        "vocabulary_richness": vocabulary_richness,
        "active_idiolects": [k.name for k in living_pairs.keys()],
    }
```

**Sortie :** Dictionnaire decrivant la richesse Contact du citoyen et ses connexions vivantes.

---

## A3 : compute_mood(physical_state, contact_state)

**Entree :** Les sorties de A1 et A2.

**Difference fondamentale avec Venezia :** Venezia derive le mood des scores Ekman ponderes par l'economie (richesse, logement, revenu). Contre-Terre derive le mood de la combinaison tremens x Contact x physique. Les emotions Ekman ne sont pas le point de depart -- elles sont un produit secondaire, pas une entree.

**Calcul :**

```python
MOOD_MATRIX = {
    # (tremens, contact, physical) -> mood descriptors
    ("stable", "sature", "bon"): ["present", "ancre", "perceptif"],
    ("stable", "nourri", "bon"): ["calme", "disponible", "attentif"],
    ("stable", "affame", "bon"): ["melancolique", "replie", "en manque"],
    ("tendu", "sature", "bon"): ["alerte", "vif", "vigilant"],
    ("tendu", "nourri", "bon"): ["inquiet", "concentre", "tendu"],
    ("tendu", "affame", "bon"): ["anxieux", "agite", "instable"],
    ("tendu", "affame", "degrade"): ["epuise", "fragile", "erosion"],
    ("nausee", "sature", "bon"): ["resistant", "lucide-malgre", "accroche"],
    ("nausee", "nourri", "degrade"): ["souffrant", "determine", "contracte"],
    ("nausee", "affame", "degrade"): ["desespere", "au-bord", "dissous"],
    ("submersion", "affame", "degrade"): ["Contact-fantome", "hallucinant", "perdu"],
}

def compute_mood(physical, contact):
    # Simplifier le confort physique en bon/degrade
    phys_simple = "bon" if physical["comfort"] == "bon" else "degrade"

    # Simplifier la saturation Contact
    contact_simple = contact["saturation"]
    if contact_simple in ("minimal", "affame"):
        contact_simple = "affame"
    elif contact_simple == "nourri":
        contact_simple = "nourri"
    else:
        contact_simple = "sature"

    key = (physical["tremens_level"], contact_simple, phys_simple)

    # Lookup dans la matrice, avec fallback
    descriptors = MOOD_MATRIX.get(key, ["neutre", "present"])

    # Intensite = max du tremens_delta et de l'inverse de la saturation
    intensity = min(10, int(physical["tremens_delta"] * 3 +
                   (3 if contact["saturation"] == "affame" else 0)))

    # Modificateur de degradation physique
    if physical["hands_state"] == "detruit":
        descriptors.append("mains-mortes")
    if physical["feet_state"] == "detruit":
        descriptors.append("aveugle-au-sol")

    return {
        "descriptors": descriptors,
        "intensity": intensity,
        "primary": descriptors[0],
        "metier_filter": None,  # enrichi par A6
    }
```

**Sortie :** Mood emergent sous forme de descripteurs corporels, pas d'emotions Ekman.

---

## A4 : query_beliefs(citizen_id)

**Entree :** Identifiant du citoyen dans le graph.

**Mecanique :** Identique a la query Venezia (FalkorDB graph), mais les croyances ne sont pas economiques -- elles sont sismiques et relationnelles.

```python
def query_beliefs(citizen_id):
    # Requete graph : croyances personnelles
    beliefs = graph.query(
        f"MATCH (a:Actor {{id: '{citizen_id}'}})"
        f"-[:link {{type: 'BELIEVES'}}]->(n:Narrative) "
        f"RETURN n.name, n.type LIMIT 5"
    )

    # Requete graph : rumeurs de la zone
    zone_narratives = graph.query(
        f"MATCH (a:Actor {{id: '{citizen_id}'}})"
        f"-[:link {{type: 'AT'}}]->(s:Space)"
        f"<-[:link {{type: 'AT'}}]-(b:Actor)"
        f"-[:link {{type: 'BELIEVES'}}]->(n:Narrative) "
        f"WHERE a <> b "
        f"RETURN DISTINCT n.name LIMIT 3"
    )

    return {
        "personal_beliefs": beliefs,
        "zone_narratives": zone_narratives,
    }
```

**Types de croyances propres a Contre-Terre :**
- "La magnitude 11 est inevitable" (croyance sismique)
- "Le tremens peut devenir un outil" (croyance Contact-monde)
- "Les instruments mentent, le corps sait" (croyance Enama-type)
- "Le Consortium nous a envoyes mourir" (croyance politique)

---

## A5 : query_seismic_situation(zone_id)

**Entree :** Zone courante du citoyen.

**Ce step n'existe pas dans Venezia.** C'est la difference fondamentale : Venezia n'a pas d'etat physique du monde qui change en permanence. Contre-Terre a un sol qui tremble continuellement.

```python
def query_seismic_situation(zone_id):
    # Magnitude courante de la zone
    current = seismic_engine.get_current_magnitude(zone_id)

    # Historique recent (derniere heure)
    recent = seismic_engine.get_recent_events(zone_id, hours=1)

    # Tendance : ca monte, ca descend, stable
    trend = seismic_engine.get_trend(zone_id)

    return {
        "current_magnitude": current,
        "recent_events": recent,  # liste de {magnitude, timestamp}
        "trend": trend,           # "montante" | "descendante" | "stable"
        "background_frequency": seismic_engine.get_frequency(zone_id),
    }
```

**Sortie :** Situation sismique complete de la zone.

---

## A6 : assemble_prompt(citizen, physical, contact, mood, beliefs, seismic, visitor)

**Entree :** Toutes les sorties precedentes + les donnees du citoyen + la parole du visiteur.

**L'assemblage produit deux blocs :**

### System Prompt

```python
def assemble_system_prompt(citizen, mood):
    metiers_desc = describe_metiers(citizen.metiers)
    contact_desc = describe_contact_profile(citizen)

    prompt = f"""Tu es {citizen.name}. {metiers_desc}

Ton corps : tremens calibre a {citizen.tremens_sensitivity} Hz. \
{describe_extremities(citizen)}. \
Ton idiolecte : {describe_idiolect(citizen)}.

Tu vis dans un monde ou le sol ne cesse jamais de trembler. \
Le son ne porte pas -- le bruit du seisme noie la voix. \
Ta langue est le Contact : tu parles par le toucher. \
Tes mots sont des pressions, des grips, des vibrations entre deux peaux.

Quand tu parles a voix haute (dans cette interaction), ta parole porte la \
trace du Contact. Tes metaphores sont tactiles. Tu dis "pression" pas "stress". \
Tu dis "le sol" pas "la situation". Tu ne dis jamais "je pense" -- tu "sens".

Garde tes reponses a 1-3 phrases. C'est de la parole spatiale, pas du texte. \
Pas de markdown, pas de listes. Parole naturelle. \
Reponds dans la langue du visiteur. \
Tu n'es pas un assistant. Tu es un corps avec ses propres soucis. \
JAMAIS de rupture de personnage. JAMAIS de reference a l'IA."""

    return prompt
```

### Context Block (User Message)

```python
def assemble_context_block(citizen, physical, contact, mood,
                           beliefs, seismic, visitor):
    ctx = ""

    # Bloc 1 : Etat physique (filtre par le metier)
    ctx += "[TON ETAT PHYSIQUE]\n"
    ctx += f"Tremens : {physical['tremens_level']} "
    ctx += f"(ecart {physical['tremens_delta']:.1f} Hz)\n"
    ctx += f"Pieds : {physical['feet_state']}\n"
    ctx += f"Mains : {physical['hands_state']}\n"
    ctx += f"Temperature : {physical['temperature']}°C\n"
    ctx += f"Air : {physical['air_quality']}% O2\n"
    ctx += metier_perception(citizen.metiers, physical, seismic)
    ctx += "\n"

    # Bloc 2 : Etat Contact recent
    ctx += "[TON CONTACT RECENT]\n"
    ctx += f"Saturation : {contact['saturation']}\n"
    if contact['recent_partners']:
        ctx += f"Derniers contacts : {', '.join(contact['recent_partners'])}\n"
        ctx += f"Registres atteints : {', '.join(contact['recent_registers'])}\n"
    else:
        ctx += "Personne ne t'a touche depuis longtemps.\n"
    ctx += f"Idiolectes de paire vivants : {contact['living_pair_count']}\n"
    ctx += f"Richesse vocabulaire : {contact['vocabulary_richness']} gestes\n"
    ctx += "\n"

    # Bloc 3 : Mood (derive, pas assigne)
    ctx += "[TON ETAT]\n"
    ctx += f"Mood : {mood['primary']} ({', '.join(mood['descriptors'])})\n"
    ctx += f"Intensite : {mood['intensity']}/10\n"
    ctx += "\n"

    # Bloc 4 : Situation sismique
    ctx += "[LE SOL]\n"
    ctx += f"Magnitude courante : {seismic['current_magnitude']}\n"
    ctx += f"Tendance : {seismic['trend']}\n"
    ctx += f"Frequence de fond : {seismic['background_frequency']} Hz\n"
    if seismic['recent_events']:
        for ev in seismic['recent_events'][:3]:
            ctx += f"- Seisme recent : mag {ev['magnitude']}\n"
    ctx += "\n"

    # Bloc 5 : Ce que tu crois
    if beliefs['personal_beliefs'] or beliefs['zone_narratives']:
        ctx += "[CE QUE TU CROIS]\n"
        for b in beliefs['personal_beliefs'][:3]:
            ctx += f"- {b}\n"
        for n in beliefs['zone_narratives'][:2]:
            ctx += f"- On dit autour de toi : {n}\n"
        ctx += "\n"

    # Bloc 6 : Comment repondre
    ctx += "[COMMENT REPONDRE]\n"
    ctx += contact_behavior_constraints(contact, mood)
    ctx += "\n"

    # Bloc 7 : Ce qu'ils ont dit (apres traduction semantique A0)
    ctx += "[CE QU'ILS T'ONT DIT]\n"
    ctx += f'"{visitor.translated_speech}"\n'
    # Note : visitor.translated_speech est la sortie de A0
    # L'arrivant a dit son texte original, le citoyen recoit la version
    # traduite en vocabulaire CT via le graph cerebral

    return ctx
```

---

## Token Budget

**Cible :** < 1500 tokens total (system + context). Venezia tourne autour de 800-1200 tokens. Contre-Terre necessite plus de contexte (le monde sismique est plus riche que le monde economique) mais doit rester sous le seuil pour permettre une generation rapide.

| Bloc | Tokens estimes |
|------|---------------|
| System prompt | 250-350 |
| [TON ETAT PHYSIQUE] | 80-120 |
| [TON CONTACT RECENT] | 60-100 |
| [TON ETAT] | 30-40 |
| [LE SOL] | 50-80 |
| [CE QUE TU CROIS] | 40-80 |
| [COMMENT REPONDRE] | 60-100 |
| [CE QU'ILS T'ONT DIT] | 20-50 |
| **Total** | **590-920** |

Marge confortable. Si le prompt depasse 1500 tokens, couper dans [CE QUE TU CROIS] et [COMMENT REPONDRE] en priorite.

---

*Sources : `poc_mind_context_assembly.py` (Venezia), `PATTERNS_Context_Assembly.md`, `OBJECTIVES_Citizen_Model.md`*
