import json
import random

categories = [
    ("Logo and Branding Design", "logo-branding"),
    ("Packaging Design", "packaging-design"),
    ("UI/UX Design", "ui-ux-design"),
    ("Motion Design", "motion-design"),
    ("Clothing Design", "clothing-design"),
    ("Illustration", "illustration"),
    ("Editorial Design", "editorial-design"),
    ("Poster Design", "poster-design")
]

companies = [
    ("Aegis Dynamics", "Aerospace Defense"),
    ("Synthos", "Biotech"),
    ("Vanguard Holdings", "Investment Banking"),
    ("NeuraLink", "Neurotech"),
    ("OmniCorp", "Robotics"),
    ("Starlight Media", "Entertainment"),
    ("Aura Health", "Healthcare"),
    ("Quantum Logistics", "Supply Chain"),
    ("Apex Fitness", "Fitness"),
    ("Zenith Motors", "Automotive")
]

brandNames = [
    "AeroTech", "BioGen", "CapitalMax", "NeuroSync", "RoboWorks", "MediaStar", "HealthPlus", "LogiQ", "FitPro", "AutoZen"
]

taglines = [
    "Reaching New Heights.", "Innovating Life.", "Securing Your Future.", "Connecting Minds.", "Building Tomorrow."
]

twists = [
    "Must use only geometric shapes.", "No blue allowed.", "Must incorporate a hidden optical illusion.", "Typography must be custom built.",
    "Must work flawlessly in pure black and white."
]

backgrounds = [
    "Founded in 1995, the company has grown from a small startup to a global powerhouse.", "A recent merger has created a need for a new unified brand identity.",
    "Once a market leader, the company has lost market share to newer, more agile competitors."
]

problems = [
    "The current brand is outdated and doesn't resonate with younger demographics.", "The user interface is complex and confusing, leading to high churn rates."
]

whyNows = [
    "A major competitor has just launched a highly successful rebrand.", "The company is preparing for an IPO in the next 12 months."
]

purposes = [
    "To establish the brand as the undisputed leader in the market.", "To increase user engagement and retention by 50%."
]

kpis = [
    "20% increase in brand awareness within 6 months.", "30% reduction in bounce rate on the website."
]

budgetTimelines = [
    "$150k / 3 months", "$250k / 6 months", "$500k / 9 months", "$1M / 12 months"
]

brandArchetypes = [
    "The Creator", "The Ruler", "The Sage", "The Magician", "The Hero"
]

toneOfVoices = [
    "Authoritative and Clinical", "Playful and Irreverent", "Sophisticated and Elegant", "Bold and Daring"
]

userPersonas = [
    "Tech-savvy millennials who value convenience and speed.", "Affluent professionals looking for premium experiences."
]

keyFeaturesList = [
    "Interactive onboarding, personalized dashboard, real-time analytics.", "Custom illustrations, bespoke typography, motion graphics."
]

mandatoryRestrictionsList = [
    "No stock photography.", "No generic icons.", "No more than 3 clicks to reach any page."
]

palettes = [
    "Deep Navy, Crimson Red, Off-White", "Emerald Green, Gold, Charcoal", "Neon Pink, Cyan, Pitch Black"
]

typographies = [
    "Inter / Merriweather", "Roboto / Playfair Display", "Montserrat / Lora"
]

competitorsList = [
    "Global Dynamics, Massive Dynamic, Wayne Enterprises", "Stark Industries, Oscorp, LexCorp"
]

referencesList = [
    "Apple, Tesla, Nike", "Google, Amazon, Microsoft", "Airbnb, Uber, Spotify"
]

deliverablesList = [
    "Brand Guidelines, Logo Suite, Business Cards", "Packaging Design, 3D Mockups, Print Files",
    "UI/UX Design, Interactive Prototype, Design System", "Motion Graphics, Explainer Video, Social Media Assets",
    "Clothing Tech Packs, Fabric Sourcing, Lookbook", "Custom Illustrations, Icon Set, Spot Illustrations",
    "Magazine Layout, Typography System, Grid System", "Poster Series, OOH Advertising, Digital Banners"
]

titles = [
    "Legacy Banking UI Overhaul", "Next-Gen Fintech Branding", "Sustainable Packaging Initiative",
    "Cyberpunk Motion Graphics", "Streetwear Capsule Collection", "Editorial Redesign for Vogue",
    "Minimalist Poster Campaign", "Healthcare App UX Optimization"
]

cases = []
current_id = 131

for cat_name, cat_slug in categories:
    for _ in range(5):
        case = {
            "id": current_id,
            "title": random.choice(titles) + f" - {current_id}",
            "client": f"{random.choice(companies)[0]} ({random.choice(companies)[1]})",
            "brandName": random.choice(brandNames),
            "tagline": random.choice(taglines),
            "category": cat_name,
            "categorySlug": cat_slug,
            "theTwist": random.choice(twists),
            "background": random.choice(backgrounds),
            "problem": random.choice(problems),
            "whyNow": random.choice(whyNows),
            "purpose": random.choice(purposes),
            "kpis": random.choice(kpis),
            "budgetTimeline": random.choice(budgetTimelines),
            "brandArchetype": random.choice(brandArchetypes),
            "toneOfVoice": random.choice(toneOfVoices),
            "userPersona": random.choice(userPersonas),
            "keyFeatures": random.choice(keyFeaturesList),
            "mandatoryRestrictions": random.choice(mandatoryRestrictionsList),
            "palette": random.choice(palettes),
            "typography": random.choice(typographies),
            "competitors": random.choice(competitorsList),
            "references": random.choice(referencesList),
            "deliverables": random.choice(deliverablesList)
        }
        cases.append(case)
        current_id += 1

with open("/Users/macbook/INI FOLDER/Coding/CaseKrack/category_cases_131_170.json", "w") as f:
    json.dump(cases, f, indent=4)
