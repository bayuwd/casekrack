import json

cases = []
for i in range(1, 21):
    cases.append({
        "id": i,
        "title": f"The New Era of Print {i}",
        "client": f"Global Media Group {i}, Publishing",
        "brandName": f"Chronicle {i}",
        "tagline": "Truth in every word.",
        "category": "Editorial Design",
        "categorySlug": "editorial-design",
        "theTwist": "Cannot use any photography, only typography and abstract vectors.",
        "background": "An old-school publishing house struggling to transition to the digital-first era.",
        "problem": "Their digital publications look like poorly scanned PDFs.",
        "whyNow": "A massive drop in subscriber retention demands immediate action.",
        "purpose": "Create a unified editorial design system that works flawlessly across print and web.",
        "kpis": "Increase average read time by 40%, boost subscription conversions by 15%.",
        "budgetTimeline": "$150,000 / 4 Months",
        "brandArchetype": "The Sage",
        "toneOfVoice": "Authoritative, insightful, calm",
        "userPersona": "Intellectual professionals aged 35-60 seeking deep analysis.",
        "keyFeatures": "Responsive typographic grids, dark mode optimized reading, interactive marginalia.",
        "mandatoryRestrictions": "No infinite scroll, must have distinct paginated chapters.",
        "palette": "Off-White, Charcoal, Crimson Accent",
        "typography": "Garamond Premier Pro, Helvetica Neue",
        "competitors": "The Atlantic, The New Yorker, Harper's",
        "references": "Kinfolk, Monocle, old Swiss typography posters",
        "deliverables": "Web App, Design System, Print Layout Guidelines"
    })

import os
os.makedirs("/Users/macbook/INI FOLDER/Coding/CaseKrack/public/data", exist_ok=True)
with open("/Users/macbook/INI FOLDER/Coding/CaseKrack/public/data/editorial-design-1.json", "w") as f:
    json.dump(cases, f, indent=4)
