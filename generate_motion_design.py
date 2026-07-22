import json
import os

titles = [
    "Abstract Data Visualization Reel", "Cybernetic UI Motion System", "Atmospheric Broadcast Package",
    "Micro-interaction Suite for FinTech", "Holographic Interface Walkthrough", "Fluid Dynamics Logo Reveal",
    "E-commerce 3D Product Showcase", "Immersive VR Onboarding Sequence", "Hyper-kinetic Sports Promo",
    "Kinetic Typography Manifesto", "Architectural Flythrough System", "Medical Device Operation Explainer",
    "Automotive Cluster Dashboard Motion", "Streaming Platform Ident Collection", "Web3 Protocol Launch Trailer",
    "AI Assistant Persona Animations", "Esports Tournament Graphics Package", "Museum Interactive Exhibit Loops",
    "Luxury Fashion Campaign Video", "Smart Home App State Transitions"
]

clients = [
    "Axiom Data (Analytics)", "Nexus Cyber (Security)", "Orbit Media (Broadcasting)",
    "VaultFi (Finance)", "HoloTech (AR/VR)", "AquaCore (Sustainability)",
    "LuxeCart (E-commerce)", "VirtuLearn (Education)", "Apex Athletics (Sports)",
    "TypeForge (Foundry)", "BuildVision (Architecture)", "MedicaNova (Healthcare)",
    "Velocity Motors (Automotive)", "StreamLine (Entertainment)", "ChainSync (Blockchain)",
    "CogniCore (AI)", "FragFest (Esports)", "Chrono Museum (Culture)",
    "Maison Silk (Fashion)", "Habitat Smart (IoT)"
]

brands = [
    "Axiom", "Nexus", "Orbit", "VaultFi", "HoloTech", "AquaCore", "LuxeCart",
    "VirtuLearn", "Apex", "TypeForge", "BuildVision", "MedicaNova", "Velocity",
    "StreamLine", "ChainSync", "CogniCore", "FragFest", "Chrono", "Maison Silk", "Habitat"
]

taglines = [
    "Seeing the unseen.", "Secure the future.", "Broadcasting brilliance.",
    "Finance in motion.", "Step into tomorrow.", "Flow with nature.",
    "Shop the extraordinary.", "Learn without limits.", "Push the boundaries.",
    "Words that move.", "Design the skyline.", "Healing through innovation.",
    "Drive the future.", "Entertainment reimagined.", "Decentralized dynamics.",
    "Intelligence animated.", "Game on.", "History in motion.",
    "Elegance in every frame.", "Living spaces, animated."
]

twists = [
    "Cannot use any easing curves, only linear motion.",
    "Entire sequence must be exactly 15 seconds, loopable perfectly.",
    "No use of the color red, despite it being a sports brand.",
    "Motion must be driven entirely by real-time data inputs.",
    "Must look like it was rendered on a CRT monitor.",
    "No 3D elements allowed, only 2D shapes imitating 3D.",
    "Must incorporate a glitch effect every 3 seconds.",
    "All motion must originate from a single central point.",
    "Must use only 3 distinct colors.",
    "No text allowed, convey the message purely through abstract shapes.",
    "Must run at exactly 12 frames per second to mimic stop motion.",
    "Must incorporate classical painting elements in motion.",
    "Audio must drive the animation parameters exclusively.",
    "Cannot use any scale properties, only position and rotation.",
    "Must feel like it's taking place underwater.",
    "Must be designed entirely in grayscale.",
    "Must use exclusively isometric perspective.",
    "Motion must represent the stages of grief.",
    "Must simulate physical materials like felt and clay.",
    "Cannot use any cuts, must be one continuous camera move."
]

backgrounds = [
    "A legacy company trying to modernize their image after 50 years.",
    "A disruptive startup aiming to challenge industry giants.",
    "A government agency seeking to appear more approachable.",
    "A non-profit organization raising awareness for a critical cause.",
    "A tech conglomerate launching a highly anticipated new product.",
    "A boutique agency showcasing their unique creative process.",
    "A struggling retail brand pivoting to a digital-first strategy.",
    "An educational institution promoting their new online curriculum.",
    "A sports team rebranding after a change in ownership.",
    "A fashion label debuting their sustainable clothing line.",
    "An architectural firm presenting their vision for a smart city.",
    "A medical startup explaining a complex new surgical procedure.",
    "An automotive manufacturer teasing their first electric vehicle.",
    "A streaming service announcing a major platform update.",
    "A blockchain company simplifying their complex protocol for users.",
    "An AI research lab demonstrating their new conversational model.",
    "An esports organization launching a global tournament series.",
    "A museum introducing a new interactive digital exhibit.",
    "A luxury brand creating a digital twin of their flagship store.",
    "A smart home company visualizing their interconnected ecosystem."
]

problems = [
    "Users find the current interface confusing and static.",
    "The brand feels outdated compared to newer competitors.",
    "Complex data is currently presented in boring, static charts.",
    "The onboarding process has a high drop-off rate.",
    "The product features are hard to understand without seeing them in action.",
    "The brand lacks a distinct visual identity in motion.",
    "The current marketing materials are not engaging enough on social media.",
    "The educational content is dry and fails to retain attention.",
    "The sports broadcasts lack dynamic and exciting graphics.",
    "The typography feels rigid and lacks personality.",
    "The architectural presentations fail to convey the scale and atmosphere.",
    "The medical procedures are too graphic to show with real footage.",
    "The automotive dashboard is distracting and overwhelming.",
    "The streaming platform lacks a cohesive and memorable intro sequence.",
    "The blockchain protocol is too abstract for the average user to grasp.",
    "The AI assistant feels robotic and lacks human-like nuances.",
    "The esports graphics are cluttered and hard to read during fast gameplay.",
    "The museum exhibits are passive and do not encourage interaction.",
    "The fashion campaign lacks a narrative thread.",
    "The smart home app state transitions are jarring and confusing."
]

why_nows = [
    "Competitors have just launched highly polished updates.",
    "A major industry event is happening next month.",
    "User engagement metrics have hit an all-time low.",
    "A massive marketing campaign is about to launch.",
    "The company just secured a new round of funding.",
    "A new CEO wants to make a strong first impression.",
    "The target demographic has shifted towards younger users.",
    "A new product line is heavily reliant on this digital experience.",
    "The current platform is being sunset in three months.",
    "There's a sudden surge in market demand for this specific service."
]

purposes = [
    "To clarify complex information through intuitive motion.",
    "To establish a modern, dynamic brand presence.",
    "To guide users seamlessly through a digital experience.",
    "To evoke a specific emotional response from the audience.",
    "To showcase the product's features in an engaging way.",
    "To create a memorable and shareable visual moment.",
    "To improve user retention and task completion rates.",
    "To educate the audience on a difficult topic.",
    "To build anticipation and excitement for a launch.",
    "To create a cohesive visual language across all platforms."
]

kpis = [
    "Increase user engagement by 25%.",
    "Reduce bounce rate on the landing page by 15%.",
    "Achieve 1 million views on the launch video within 24 hours.",
    "Increase brand recall in surveys by 30%.",
    "Decrease support tickets related to onboarding by 20%.",
    "Achieve a 50% increase in social media shares.",
    "Improve user satisfaction scores by 1.5 points.",
    "Increase time spent on the app by 10%.",
    "Achieve a 40% click-through rate on the promo.",
    "Reduce task completion time by 5 seconds."
]

budget_timelines = [
    "$50k, 4 weeks",
    "$120k, 8 weeks",
    "$30k, 3 weeks",
    "$250k, 12 weeks",
    "$80k, 6 weeks",
    "$150k, 10 weeks",
    "$45k, 5 weeks",
    "$200k, 14 weeks",
    "$75k, 7 weeks",
    "$100k, 9 weeks"
]

archetypes = [
    "The Creator", "The Magician", "The Sage", "The Explorer",
    "The Hero", "The Rebel", "The Lover", "The Jester",
    "The Caregiver", "The Ruler"
]

tones = [
    "Innovative and visionary.",
    "Mysterious and powerful.",
    "Wise and informative.",
    "Adventurous and bold.",
    "Courageous and determined.",
    "Disruptive and edgy.",
    "Passionate and elegant.",
    "Playful and energetic.",
    "Nurturing and supportive.",
    "Authoritative and commanding."
]

personas = [
    "Tech-savvy millennials looking for seamless digital experiences.",
    "C-suite executives needing quick, clear data insights.",
    "Creative professionals seeking inspiration and cutting-edge tools.",
    "Students needing engaging and accessible learning materials.",
    "Gamers who demand high-energy, visually stimulating content.",
    "Eco-conscious consumers looking for sustainable brands.",
    "Fitness enthusiasts wanting motivation and dynamic tracking.",
    "Healthcare professionals needing precise and clear information.",
    "Car enthusiasts looking for futuristic and intuitive interfaces.",
    "Crypto investors needing complex protocols simplified."
]

features = [
    "Fluid transitions, micro-interactions, responsive animations.",
    "Data-driven motion, complex particle systems, 3D visualizations.",
    "Kinetic typography, glitch effects, bold color shifts.",
    "Soft easing, morphing shapes, continuous camera moves.",
    "Isometric animations, loopable sequences, UI walk-throughs.",
    "Character animation, storytelling sequences, expressive motion.",
    "Abstract shapes, ambient motion, audio-reactive elements.",
    "HUD elements, cybernetic interfaces, high-tech motion.",
    "Stop-motion aesthetics, textured animations, frame-by-frame.",
    "Parallax scrolling, depth effects, immersive 3D environments."
]

restrictions = [
    "Do not use traditional keyframe animation; use code-driven motion.",
    "Avoid any reference to the color blue.",
    "Do not use human figures in any of the animations.",
    "Must not exceed 60 frames per second.",
    "Avoid completely flat design; must have some sense of depth.",
    "Do not use standard ease-in/ease-out curves.",
    "Must not rely on voiceover to explain the motion.",
    "Avoid highly complex 3D models; stick to primitives.",
    "Do not use any stock footage.",
    "Must not use any text overlays."
]

palettes = [
    "Neon Pink, Cyan, Deep Black",
    "Earthy Greens, Warm Sand, Off-White",
    "Clinical White, Soft Blue, Silver",
    "Vibrant Orange, Purple, Dark Navy",
    "Monochrome Grayscale with Gold accents",
    "Pastel Pink, Mint Green, Soft Yellow",
    "Deep Crimson, Charcoal, Metallic Silver",
    "Electric Blue, Magenta, Pitch Black",
    "Mustard Yellow, Teal, Cream",
    "Forest Green, Rust Orange, Beige"
]

typographies = [
    "Inter & Roboto Mono",
    "Playfair Display & Lora",
    "Space Grotesk & Helvetica Neue",
    "Oswald & Open Sans",
    "Bebas Neue & Montserrat",
    "Merriweather & Source Sans Pro",
    "Syne & Work Sans",
    "Clash Display & Satoshi",
    "Cinzel & Raleway",
    "Monument Extended & Neue Haas Grotesk"
]

competitors = [
    "Industry Leader A, Disruptive Startup B",
    "Legacy Brand X, Niche Player Y",
    "Global Conglomerate C, Local Agency D",
    "Tech Giant Z, Innovative Studio W",
    "Direct Competitor 1, Indirect Competitor 2"
]

references = [
    "Apple product launches, Stripe website animations",
    "Buck studio reels, ManvsMachine campaigns",
    "Tendril design work, Framestore UI concepts",
    "Territory Studio interfaces, GMUNK motion design",
    "Ordinary Folk explainers, Gunner animations"
]

deliverables = [
    "Lottie animations, MP4 video, After Effects source files",
    "UI motion guidelines, CSS/JS animation code snippets",
    "Broadcast package (bumpers, lower thirds, transitions)",
    "3D animated sequence, Render passes, Compositing files",
    "Interactive WebGL experience, Motion prototypes"
]

case_studies = []
for i in range(1, 21):
    case_studies.append({
        "id": i,
        "title": titles[i-1],
        "client": clients[i-1],
        "brandName": brands[i-1],
        "tagline": taglines[i-1],
        "category": "Motion Design",
        "categorySlug": "motion-design",
        "theTwist": twists[i-1],
        "background": backgrounds[i-1],
        "problem": problems[i-1],
        "whyNow": why_nows[i%10],
        "purpose": purposes[i%10],
        "kpis": kpis[i%10],
        "budgetTimeline": budget_timelines[i%10],
        "brandArchetype": archetypes[i%10],
        "toneOfVoice": tones[i%10],
        "userPersona": personas[i%10],
        "keyFeatures": features[i%10],
        "mandatoryRestrictions": restrictions[i%10],
        "palette": palettes[i%10],
        "typography": typographies[i%10],
        "competitors": competitors[i%5],
        "references": references[i%5],
        "deliverables": deliverables[i%5]
    })

os.makedirs(os.path.dirname('/Users/macbook/INI FOLDER/Coding/CaseKrack/public/data/motion-design-1.json'), exist_ok=True)

with open('/Users/macbook/INI FOLDER/Coding/CaseKrack/public/data/motion-design-1.json', 'w') as f:
    json.dump(case_studies, f, indent=2)

print("Done")
