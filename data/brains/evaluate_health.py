"""
Brain Health Score evaluation for Contre-Terre citizens.
Uses the same algorithm as manemus/runtime/cognition/brain_health_score_periodic_calculator.py
"""
import json
import math
from pathlib import Path

BASE_DIR = Path(__file__).parent


def compute_brain_power(neurons, synapses):
    if neurons == 0:
        return 0
    base = 2.9 * math.log2(neurons + 1)
    connectivity = min(synapses / max(neurons, 1), 1.0)
    return round(base + connectivity)


def assess_health(brain_data):
    neurons = brain_data.get("neurons", 0)
    if neurons == 0:
        return "dormant"
    drives = brain_data.get("drives", {})
    if not drives:
        return "dormant"
    active_drives = [v for v in drives.values() if v > 0.15]
    drive_values = list(drives.values())
    mean_drive = sum(drive_values) / max(len(drive_values), 1)
    frustration = drives.get("frustration", 0)
    boredom = brain_data.get("emotions", {}).get("boredom", 0)
    curiosity = drives.get("curiosity", 0)
    if frustration > 0.7:
        return "stressed"
    if boredom > 0.8 and curiosity < 0.2:
        return "restless"
    if len(active_drives) >= 4 and mean_drive > 0.25 and frustration < 0.4:
        return "thriving"
    if len(active_drives) >= 2:
        return "healthy"
    return "restless"


def assess_arousal_regime(drives):
    vals = list(drives.values())
    mean = sum(vals) / max(len(vals), 1)
    frustration = drives.get("frustration", 0)
    if mean < 0.15:
        return "idle"
    if frustration > 0.8:
        return "overwhelmed"
    if frustration > 0.6:
        return "stressed"
    if mean > 0.6:
        return "focused"
    return "alert"


def load_cluster(path):
    if path.exists():
        data = json.loads(path.read_text())
        return len(data.get("nodes", [])), len(data.get("links", []))
    return 0, 0


INHERIT_MAP = {
    "metier_clusters/predicteur": "predicteur",
    "metier_clusters/explosiviste": "explosiviste",
    "metier_clusters/chef_expedition": "chef_expedition",
    "metier_clusters/cartographe": "cartographe",
    "metier_clusters/ecouteur": "ecouteur",
    "metier_clusters/meteorologue": "meteorologue",
    "metier_clusters/mineur": "mineur",
    "metier_clusters/biologiste": "biologiste",
    "metier_clusters/cuisinier": "cuisinier",
    "metier_clusters/survivaliste": "survivaliste",
    "metier_clusters/aeromaitre": "aeromaitre",
    "metier_clusters/geologue": "geologue",
    "metier_clusters/grimpeur": "grimpeur",
    "metier_clusters/specialiste_oceanique": "specialiste_oceanique",
    "metier_clusters/speleologue": "speleologue",
}


def main():
    base_n, base_l = load_cluster(BASE_DIR / "shared" / "contre_terre_base.json")
    integ_n, integ_l = load_cluster(BASE_DIR / "shared" / "integration_cluster.json")

    metier_cache = {}
    for key, fname in INHERIT_MAP.items():
        metier_cache[key] = load_cluster(BASE_DIR / "metier_clusters" / f"{fname}.json")

    print("=" * 80)
    print("CONTRE-TERRE — BRAIN HEALTH ASSESSMENT")
    print("=" * 80)
    print()

    results = []
    citizens_dir = BASE_DIR / "citizens"

    for brain_file in sorted(citizens_dir.glob("*.json")):
        data = json.loads(brain_file.read_text())
        cid = data["citizen_id"]
        age = data.get("age", "?")
        metiers = data.get("metiers", [])

        personal_nodes = len(data.get("nodes", []))
        personal_links = len(data.get("links", []))

        total_nodes = personal_nodes + base_n + integ_n
        total_links = personal_links + base_l + integ_l

        inherits = data.get("inherits", [])
        metier_parts = []
        for inh in inherits:
            if inh in metier_cache:
                mn, ml = metier_cache[inh]
                total_nodes += mn
                total_links += ml
                name = INHERIT_MAP.get(inh, inh)
                metier_parts.append(f"{name}({mn}n/{ml}l)")

        raw_drives = data.get("drives", {})
        drives = {}
        for k, v in raw_drives.items():
            if isinstance(v, dict):
                drives[k] = v.get("intensity", v.get("baseline", 0))
            else:
                drives[k] = v

        brain_power = compute_brain_power(total_nodes, total_links)
        health = assess_health({"neurons": total_nodes, "drives": drives})
        arousal = assess_arousal_regime(drives)

        sorted_drives = sorted(drives.items(), key=lambda x: -x[1])
        top_3 = [(k, v) for k, v in sorted_drives[:3]]
        mean_drive = sum(drives.values()) / max(len(drives), 1)
        active_count = len([v for v in drives.values() if v > 0.15])
        frustration = drives.get("frustration", 0)

        results.append({
            "cid": cid, "age": age, "metiers": metiers,
            "personal_nodes": personal_nodes, "personal_links": personal_links,
            "total_nodes": total_nodes, "total_links": total_links,
            "brain_power": brain_power, "health": health, "arousal": arousal,
            "drives": drives, "top_3": top_3, "mean_drive": mean_drive,
            "active_count": active_count, "metier_parts": metier_parts,
            "frustration": frustration,
        })

    for r in results:
        top3_str = ", ".join(f"{k} ({v:.2f})" for k, v in r["top_3"])
        metier_str = " + ".join(r["metier_parts"])
        print(f"--- {r['cid'].upper()} ({r['age']} ans) ---")
        print(f"  Metiers:      {', '.join(r['metiers'])}")
        print(f"  Inherited:    base({base_n}n/{base_l}l) + {metier_str} + integ({integ_n}n/{integ_l}l)")
        print(f"  Personal:     {r['personal_nodes']} nodes, {r['personal_links']} links")
        print(f"  TOTAL:        {r['total_nodes']} nodes, {r['total_links']} links")
        print(f"  Brain Power:  {r['brain_power']}")
        print()
        print(f"  HEALTH:       {r['health'].upper()}")
        print(f"  Arousal:      {r['arousal']}")
        print(f"  Drives actifs: {r['active_count']}/8  (mean: {r['mean_drive']:.2f})")
        print(f"  Frustration:  {r['frustration']:.2f}")
        print(f"  Top 3 drives: {top3_str}")
        print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    total_n = sum(r["total_nodes"] for r in results)
    total_l = sum(r["total_links"] for r in results)
    print(f"Citizens:       {len(results)}")
    print(f"Total nodes:    {total_n} (with inheritance)")
    print(f"Total links:    {total_l}")
    print()

    icons = {
        "thriving": "[+++]", "healthy": "[++ ]", "stressed": "[!! ]",
        "restless": "[~  ]", "dormant": "[   ]",
    }
    for r in results:
        icon = icons.get(r["health"], "[?  ]")
        print(f"  {icon} {r['cid']:8s}  BP={r['brain_power']:3d}  {r['health']:10s}  arousal={r['arousal']:10s}  frustration={r['frustration']:.2f}")


if __name__ == "__main__":
    main()
