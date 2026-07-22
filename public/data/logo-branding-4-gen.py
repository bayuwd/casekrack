import json
import random

def generate_case_studies():
    case_studies = []
    
    twists = [
        "The brand must never use the color blue, despite being in the water tech industry.",
        "The logo cannot contain any straight lines whatsoever.",
        "The typography must exclusively use monospaced fonts to reflect their engineering roots.",
        "The brand identity must incorporate a generative element that changes based on live weather data.",
        "The primary brand mark must be recognizable when scaled down to exactly 16x16 pixels.",
        "The brand is legally prohibited from using any word starting with the letter 'E'.",
        "The logo must be purely typographical, with absolutely no symbols, icons, or marks.",
        "The identity must work perfectly in both high-tech AR environments and low-fi thermal printed receipts.",
        "The brand colors are strictly limited to two distinct neon shades and pure black.",
        "The logo must integrate an optical illusion that reveals a secondary meaning when viewed from a distance.",
        "The visual identity must subtly incorporate elements of 19th-century botanical illustrations.",
        "The brand name and tagline must always be presented as an integrated, inseparable lockup.",
        "The identity system must rely entirely on negative space to define its core visual elements.",
        "The brand must launch without a permanent logo, instead using a system of 5 rotating marks.",
        "The typography must be custom-developed and legible to both humans and legacy OCR scanners.",
        "The color palette must be derived entirely from the spectral emissions of rare earth elements.",
        "The brand must communicate luxury without using traditional signifiers like gold, silver, or serifs.",
        "The logo must act as a functional QR code while retaining aesthetic elegance.",
        "The entire identity must be modular, allowing users to assemble their own version of the logo.",
        "The brand must utilize a stark brutalist aesthetic, avoiding all gradients and soft shadows."
    ]

    for i in range(20):
        case_studies.append({
            "id": 61 + i,
            "title": f"Project Alpha {i}",
            "client": f"ClientCorp {i}, Technology",
            "brandName": f"Brand {i}",
            "tagline": f"We do things better {i}.",
            "category": "Logo and Branding Design",
            "categorySlug": "logo-branding",
            "theTwist": twists[i],
            "background": f"Detailed company history for Brand {i}. Founded in 2010, they have been a staple in the tech space but recently lost their edge due to increased competition and a stagnant visual identity.",
            "problem": f"The core issue they are facing is a disjointed brand image that no longer resonates with their evolving, younger target audience.",
            "whyNow": f"Market pressure from new, agile startups threatens to erode their market share by Q4 if a rebrand isn't successfully launched.",
            "purpose": f"To modernize the brand, establish trust with Gen Z, and differentiate themselves from corporate legacy competitors.",
            "kpis": f"25% increase in brand recall, 15% bump in social engagement, positive sentiment in focus groups.",
            "budgetTimeline": f"$150,000 / 12 weeks",
            "brandArchetype": f"The Magician / The Creator",
            "toneOfVoice": f"Visionary, concise, slightly irreverent.",
            "userPersona": f"Alex, 24, software engineer. Values authenticity and technical excellence, highly skeptical of traditional corporate marketing.",
            "keyFeatures": f"Dynamic logo system, custom iconography, comprehensive brand guidelines.",
            "mandatoryRestrictions": f"Do not use stock photography. Do not use generic tech tropes like circuits or clouds.",
            "palette": f"Deep Space Black, Cyber Neon Green, Ghost White.",
            "typography": f"Primary: Roobert. Secondary: JetBrains Mono.",
            "competitors": f"MegaTech, Innovate Corp, FutureSystems.",
            "references": f"Stripe, Vercel, Linear.",
            "deliverables": "Brand Strategy, Logo Design, Visual Identity System, Brand Guidelines, Social Media Templates"
        })
    
    with open('/Users/macbook/INI FOLDER/Coding/CaseKrack/public/data/logo-branding-4.json', 'w') as f:
        json.dump(case_studies, f, indent=2)

if __name__ == '__main__':
    generate_case_studies()
