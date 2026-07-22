# CaseKrack

CaseKrack is an elite-tier design practice application that generates highly complex, realistic design briefs for UI/UX designers, brand strategists, and product designers. It features a vault of 130 massive, real-world case studies ranging from legacy enterprise digital transformations to advanced niches like Quantum Computing and Deep Sea Tech.

## Features

- **Visible Challenge Grid**: A brutalist, edge-to-edge 30-day challenge grid displaying the core 30 briefs.
- **Endless Generator**: A "hard mode" generator at the bottom of the page that randomly accesses 100 hidden "secret" cases for unpredictable, highly complex business problems.
- **Instant PDF Export**: Beautifully formatted, multi-page PDF exports for every brief, mimicking official agency documents.
- **Deep Schema**: Every brief contains 20 rich data points including wildcards ("The Twist"), KPIs, Budget constraints, Personas, and Typography guidelines.

## Manual Update & Edit Guide

The master database of all 130 cases is stored locally in the source code as a massive JSON-like array. You do not need a database to update it!

### File Location
All case data is located in: `src/data/briefs.js`

### Editing an Existing Case
1. Open `src/data/briefs.js`.
2. Locate the case you want to edit by searching for its `id` or `title` (e.g., `"id": 1`).
3. Modify any of the 20 fields directly in the object.
4. Save the file. The changes will instantly reflect in the app.

### Adding a New Case Manually
1. Open `src/data/briefs.js`.
2. Scroll to the very bottom of the `briefs` array.
3. Add a new object at the end of the array, ensuring you follow the exact schema structure:
```javascript
{
  "id": 131,
  "title": "Your New Project Title",
  "client": "Fake Company Name, Niche",
  "theTwist": "A crazy wildcard restriction",
  "background": "Detailed company history",
  "problem": "The core issue",
  "whyNow": "Market pressure",
  "purpose": "What the design achieves",
  "kpis": "Success metrics",
  "budgetTimeline": "$XXX,XXX / X Months",
  "brandArchetype": "The Creator",
  "toneOfVoice": "Authoritative",
  "userPersona": "Detailed persona",
  "keyFeatures": "Specific UI deliverables",
  "mandatoryRestrictions": "What NOT to do",
  "palette": "Primary: #HEX, Secondary: #HEX",
  "typography": "Header: Font, Body: Font",
  "competitors": "Rival companies",
  "references": "Inspiration",
  "deliverables": "App, Brand Book, etc."
}
```
*Note: If you add more cases beyond 130, they will automatically be integrated into the Endless Generator pool! The main grid will always cap at the first 30 cases.*

## Running Locally

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```
3. Build for production:
   ```bash
   npm run build
   ```
