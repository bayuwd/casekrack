import json

with open('/Users/macbook/INI FOLDER/Coding/CaseKrack/chunk_2.json', 'r') as f:
    data = json.load(f)

additions = {
    23: {"brandName": "Olea Heritage", "tagline": "Uncompromising Greek Terroir."},
    24: {"brandName": "Forma Games", "tagline": "Strategy, Distilled."},
    25: {"brandName": "Lucid Botanics", "tagline": "The complexity of spirit, without the proof."},
    26: {"brandName": "Monolith Machining", "tagline": "Engineered for extreme precision."},
    27: {"brandName": "The Miller's Mark", "tagline": "Stone-ground heritage, baked with soul."},
    28: {"brandName": "Atelier Aether", "tagline": "Atmosphere, bottled."},
    29: {"brandName": "Velvet Reserve", "tagline": "Decadence in every drop."},
    30: {"brandName": "Concrete Syndicate", "tagline": "Built for the streets. Destroy with respect."},
    31: {"brandName": "Qubix Core", "tagline": "Visualizing the quantum realm."},
    32: {"brandName": "Subterra Command", "tagline": "Uncompromising autonomous control."},
    33: {"brandName": "GeneLink Bio", "tagline": "Connecting patients to tomorrow's cures."},
    34: {"brandName": "OmniPass", "tagline": "Your digital identity, universally accessible."},
    35: {"brandName": "OmniGlobal Nexus", "tagline": "Unifying global supply chains."},
    36: {"brandName": "AeroSpace Sentinel", "tagline": "Precision tracking for the final frontier."},
    37: {"brandName": "Apex Velocity", "tagline": "Zero latency. Absolute execution."},
    38: {"brandName": "AgriSwarm Field Ops", "tagline": "Autonomous precision for the modern farm."},
    39: {"brandName": "HealthRoute", "tagline": "Coordinating care without borders."},
    40: {"brandName": "SurgiVR", "tagline": "Rehearsing precision in spatial reality."},
    41: {"brandName": "CivicTrust", "tagline": "Securing identity anywhere, anytime."},
    42: {"brandName": "Synthetica Workbench", "tagline": "Precision engineering for the human code."},
    43: {"brandName": "SupplyPulse", "tagline": "The nervous system of global trade."},
    44: {"brandName": "AeroMerge Terminal", "tagline": "One terminal. Limitless destinations."}
}

for item in data:
    if item['id'] in additions:
        item['brandName'] = additions[item['id']]['brandName']
        item['tagline'] = additions[item['id']]['tagline']
        
        # We need to make sure we keep the properties, but let's reorder if desired, or just add them.
        # Python dicts keep insertion order. The prompt says: "Update every object in the array to include these two new properties."
        
with open('/Users/macbook/INI FOLDER/Coding/CaseKrack/chunk_2.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated chunk_2.json successfully.")
