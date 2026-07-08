# BLDGTYP Homepage — Copy Redline (v1)

> **STATUS 2026-07-02: IMPLEMENTED in the working tree** (`site/index.html`), uncommitted, awaiting
> Ed's review. The no-data edits (hero, who, services, process, assessment, knowledge, CTA, nav) are
> live in the file; the data-gated sections (Proof §8, Cost §10, Stats §12) are staged with
> `[bracketed]` placeholders pending [decision D4](./positioning-decisions.md).

*Section-by-section rewrite of `site/index.html`, in document order. Voiced for the B2B / architect-first audience per [positioning D1](./positioning-decisions.md). Rules cited as `[slug]` → see [`marketing-rules.md`](./marketing-rules.md).*

**Legend:** `KEEP` no change · `EDIT` revise copy · `ADD` new section · `UPGRADE` expand existing · `REMOVE` cut
**Placeholders** in `[BRACKETS]` need real data from you (gated on [decision D4 — publishable proof](./positioning-decisions.md)).

**Voice guardrails for every line below:**
- Speak peer-to-peer to a design professional. We're the *performance team that de-risks their project and makes them look good to their client* [mark-attard-point-6][elrond-burrell-via-architecture].
- Keep "Passive House" as the category/method (SEO + credibility); don't let it carry the *emotional* load — lead a benefit with the felt outcome, name PH a beat later [lloyd-alter-carbon-upfront].
- Felt benefits (comfort/health/quiet/resilient/durable) describe *what the building delivers*, kept secondary to professional competence — not a consumer headline.
- Honesty over hype — "tell the bad stuff too," never overpromise "no premium" [beth-campbell-passive-house-massachusetts][adam-white-intelligent-membranes].

---

## 1. `<title>` / meta — KEEP
`BLDGTYP · Passive House Consulting · New York · Massachusetts` — fine for SEO. No change.

---

## 2. Nav (line 919) — EDIT (minor)
Add two anchors for the new sections so they're reachable: **Work** (proof) and **Resources** (knowledge). Proposed link set:
`Services · Process · Work · Massachusetts · Resources · Contact`
*(If that's too many for the bar, drop "Process".)*

---

## 3. Hero (lines 949–960) — EDIT  ★P0

**Before:**
> Your Passive House questions. *Answered.*
> // Passive House design and consulting for architects, developers, and builders.
> // We find the answers so you can build with confidence.
> [Reach out today: info@buildingtype.com]

**After — recommended (A):**
> # The performance team behind high-performance buildings.
> // Passive House energy consulting for architects, developers, and builders across New York & Massachusetts. We model it, prove it, and carry the certification — so your project hits its targets and your client gets a building that's comfortable, quiet, and resilient for decades.
> [Send us your drawings →]   ·   info@buildingtype.com

**Alternate (B) — keeps your current "answers" equity:**
> # Your Passive House questions. *Answered.*
> // The energy-modeling and certification team architects and developers call when performance has to be right the first time. We de-risk the building science so you can design and build with confidence.
> [Send us your drawings →]   ·   info@buildingtype.com

**Why:** Leads with professional competence + de-risk, not the PH *name* as the value; states audience explicitly; the felt outcome ("comfortable, quiet, resilient") rides along as *what the building delivers* [kristof-irwin-positive-energy][lloyd-alter-carbon-upfront]; CTA upgraded from a raw mailto to the corpus's classic low-friction lead magnet "send us your drawings" [aaron-waldt-475-high-performance-building-supply]. *Decision embedded: A demotes the name harder; B is the lower-risk evolution. My pick: A.*

> **Implementation note:** "Send us your drawings →" can keep the `mailto:` for v1 (prefilled subject) — no backend needed.

---

## 4. "Who do we work with?" (lines 962–1002) — EDIT  ★P0

Keep the 3-column structure (it's the best part of the page) but re-voice each to *de-risk + make-you-look-good + speak their value system* [mariana-pickering-b-public-prefab].

**Architects** — *before:* "You care about craft, comfort, and precision. We bring the energy science to match your design ambition — without compromising your architecture."
*after:*
> **You own the design. We own the performance.** We're the outside pair of eyes that runs the energy model, resolves the thermal bridges, and keeps the certification on track — so you keep design control and hand your client a building that performs exactly as promised.
> `Single-family · Townhouse · Brownstone renovation`

**Developers** — *before:* "You need certification, incentives, and energy performance that pencils out. We model efficiently and deliver documentation your review team will accept."
*after:*
> **Performance is a risk to manage — so we manage it.** We model efficiently, right-size the mechanicals, capture the incentives (Mass Save, stretch-code, LIHTC points), and deliver documentation your certifier and review team will accept the first time. Fewer surprises, fewer change orders.
> `Affordable housing · Mixed-use · Multifamily`

*Why:* developers hear "cost, red tape, delays" when they hear "performance" — reframe everything as risk management [michael-quast-passive-house-canada]; name the incentives [alexander-gard-murray-passive-house-massachusetts].

**Builders** — *before:* "You're building it — and you need to know the assemblies will perform. Our standard assessment gives you clear, actionable guidance on envelope details, airtightness, and mechanical sizing."
*after:*
> **Your name is on it.** We give you blower-door-ready details and right-sized mechanicals you can actually install — so you get fewer callbacks, no no-heat emergencies, and measured proof your crew's work is the best on the block.
> `Single-family · Custom builds · Renovations`

*Why:* builders/trades are the most underserved conversion target; sell craft-pride + fewer callbacks, not energy [brian-pearson-studio-pear][valentine-gomez-gomex-engineering].

**ADD — reassurance microcopy (the "ride-along owner," thin layer per D1).** One small line under the grid, muted styling:
> *// Were you sent here by your architect or builder? In plain terms: we're the specialists your team brings in to make sure your home is healthy, comfortable, quiet, and built to last — and to prove it with numbers before anyone breaks ground.* [graham-irwin-essential-habitat-architecture]

---

## 5. Services (lines 1004–1041) — EDIT

Lead each card with the *outcome*, keep the searchable technical title.

**Energy Modeling** — subtitle `Design with real numbers`
> We model the whole building — envelope to mechanicals — so design decisions rest on real data, not assumptions. The payoff: right-sized, lower-cost HVAC and a clear path to your performance target before construction locks in. [lindsey-love-regenerative-building-solutions]

**Thermal Bridges** — `Find the hidden losses` *(KEEP — strong differentiator; light edit)*
> 2D and 3D finite-element modeling finds where the envelope bleeds heat — and where condensation and mold risk hide — before it's built. Every junction verified, every detail buildable. *(adds the durability angle, not just energy)*

**Certification** — subtitle `De-risk the whole build` *(was "Cross the finish line")*
> Phius and PHI certification is durability insurance — it catches the costly envelope defects a code inspector never will. We run the modeling, documentation, and review so you don't carry the risk. **Want the performance without the plaque?** We'll hit the targets either way. [josh-salinger-birdsmouth-design-build]

*Why the last line:* a large share of clients abandon certification as too costly — offer "targets vs. plaque" up front so you keep them instead of losing them mid-stream [jeremy-clarke-simple-life-homes][tessa-bradley-artisans-group].

---

## 6. Process (lines 1043–1080) — EDIT (light)

Steps 1–5 are solid (they sell the "easy button" / de-risk path [hans-breaux-project-co-op]). Two tweaks:
- **Step 3 "Review together"** — add the money line: *"…the most cost-effective upgrades, and where we can shrink the mechanical system to save you money. Real numbers, real options."*
- **Step 5 "Build with confidence"** — fine; optionally tie to proof: *"…and we can verify the finished building performs as modeled."* (sets up the new Proof section + M&V offering).

---

## 7. Design-Phase Assessment (lines 1082–1142) — EDIT

Keep the report mockup and the great closing line. Two adds:
- **ADD a felt-outcome caption** under the metric mockup (muted):
  > *What these numbers mean in the building: even temperatures room-to-room, fresh filtered air, and a home that holds ~70°F for days without power.* [enrico-bonilauri-emu-passive][kristof-irwin-positive-energy]
- **EDIT the intro** from "Every project receives a detailed design-phase report covering:" →
  > **One deliverable that de-risks the whole project.** Bring us in at concept and you get a design-phase report that turns open questions into a documented performance target — covering: *(keep the bullet list)*

*Why:* translate metrics into felt outcomes [enrico-bonilauri-emu-passive]; "get us to the table at the beginning" [mark-attard-point-6].

---

## 8. ADD — "Proof / Selected Work" section  ★P0  (NEW, place after Design-Phase Assessment)

The single most important addition. The corpus ranks **measured-vs-modeled performance as the #1 proof**, ahead of certification logos [hans-breaux-project-co-op][bronwyn-barry-passive-house-bb]. Proposed block:

> `section-label:` **DOES IT ACTUALLY WORK?**
> ## We don't model performance and hope. We measure it.
>
> **Three project cards** (`[fill from real projects]`):
> - **[PROJECT NAME]** — [Brooklyn townhouse EnerPHit]. Modeled heating demand **[X]**, measured **[Y]** — within **[±Z%]**. *"[short visceral client line — e.g. "I don't wear a sweater in my own house anymore."]"* [tessa-bradley-artisans-group]
> - **[PROJECT NAME]** — [MA affordable multifamily, NN units]. Certified Phius; **[2–3%]** premium, projected operating cost **[~40%]** of code-built. [alexander-gard-murray-passive-house-massachusetts]
> - **[PROJECT NAME]** — [thermal-bridge / retrofit]. [one-line result].

*If we can publish only one measured-vs-modeled chart, that alone is worth more than the whole stats bar.* Gated on [D4]. If no client names are clearance-ready yet, run anonymized ("a 12-unit Passaic affordable project").

---

## 9. UPGRADE — Open-Source strip → "Knowledge Resource" section (lines 1144–1151)

Today this differentiator is one grey line. Expand into a real section — it's the proof we're *a knowledge company that consults*, not a vendor [aaron-waldt-475-high-performance-building-supply].

> `section-label:` **WE BUILD THE TOOLS, TOO**
> ## The same rigor we put into every building goes into our tools. 
> **BLDGTYP** builds and maintains [Passive House Tools](https://www.passivehousetools.com/) — the open-source toolkit used by Passive House practitioners worldwide — and Ed publishes modeling walkthroughs on [YouTube]. When your project needs an answer the textbook doesn't have, we're the team that wrote the tool.
> [Explore the open-source tools →] [Watch on YouTube →]

*Why:* "give value first / jab-jab-right-hook" — public expertise is top-of-funnel trust [elrond-burrell-via-architecture]. Pulls Ed's YouTube up from a nav icon into a credibility asset.

---

## 10. ADD — honest cost answer  ★P0 (NEW; small block, place before or after Stats)

Cost is THE universal objection; the page is silent on it. A short, honest block:

> `section-label:` **WHAT ABOUT COST?**
> ## The premium is smaller — and shorter — than you think.
> On multifamily, a well-run Passive House project typically runs a **[~2–3%]** premium that's recovered in operating savings; on custom residential, much of the "premium" is really a one-time learning curve, not a permanent cost [beth-eckenrode-auros-group]. We won't pretend it's always free — it depends on the team — but we *will* show you the numbers for your project before you commit. [beth-campbell-passive-house-massachusetts]

*Why honesty:* refusing to overpromise "no premium" is itself a credibility move [beth-campbell][adam-white]. Confirm the figure in [D4].

---

## 11. Massachusetts (lines 1153–1207) — KEEP
Best section on the site — specific, localized, cited, honest disclaimer. Model the rest on it. No change.

---

## 12. Stats (lines 1209–1236) — EDIT

`section-label:` "WHY PASSIVE HOUSE?" → **"WHY IT'S WORTH IT"**. Swap generic movement stats for proof-of-outcome (keep one or two movement numbers for context):

| Keep / Replace | Number | Label |
|---|---|---|
| REPLACE | **[±X%]** | Modeled vs. measured energy on our certified projects `[D4]` |
| REPLACE | **2–3%** | Typical multifamily cost premium — recovered in operating savings |
| KEEP (reframe) | **~70°F** | Held for days with no power *(resilience, not "90% energy reduction")* |
| KEEP | **#1** | Fastest-growing high-performance standard in the US |

*Why:* lead with *our* proof and felt/risk outcomes, not abstract energy reductions [hans-breaux][kristof-irwin].

---

## 13. Final CTA (lines 1238–1245) — EDIT

**Before:** "Ready to get started? We work with architects, developers, and builders constructing to the highest standard…"
**After:**
> ## Bring us in early. It's the cheapest time to get performance right.
> The earlier we're at the table, the more we can de-risk — and the more your design budget buys. Send us your drawings at any stage and we'll tell you where your project stands.
> [Send us your drawings → info@buildingtype.com]

*Why:* "get us to the table at the beginning" + "cheapest time to make a building work well is at the start" [mark-attard-point-6][alexander-gard-murray-passive-house-massachusetts]; low-friction CTA.

---

## 14. Footer (lines 1248–1259) — KEEP
PHI/Phius seals are good trust signals [aaron-waldt-475-high-performance-building-supply]. No change.

---

## Summary of changes

| # | Section | Action | Priority | Needs data? |
|---|---|---|---|---|
| 3 | Hero | EDIT (benefit-led, better CTA) | P0 | — |
| 4 | Who we work with | EDIT + reassurance line | P0 | — |
| 8 | Proof / Selected Work | **ADD** | P0 | ✅ D4 |
| 10 | Cost answer | **ADD** | P0 | ✅ D4 (figure) |
| 5 | Services | EDIT (outcome-first) | P1 | — |
| 7 | Design-Phase Assessment | EDIT (felt caption) | P1 | — |
| 9 | Knowledge Resource | UPGRADE | P1 | — |
| 12 | Stats | EDIT (proof) | P1 | ✅ D4 |
| 13 | Final CTA | EDIT | P1 | — |
| 2 | Nav | EDIT | P2 | — |
| 6 | Process | EDIT (light) | P2 | — |
| 1,11,14 | Title / MA / Footer | KEEP | — | — |

**No-data-needed changes (3,4,5,6,7,9,13, nav)** can ship immediately. **Proof/cost/stats (8,10,12)** need real numbers from you — until then I can stage them with clearly-marked placeholders or anonymized examples.

---

## How I'd implement (on your go)
1. Land all **no-data** edits first (hero, who, services, process, assessment, knowledge, CTA, nav) — pure copy/markup in `index.html`, fully reversible.
2. Stage **Proof + Cost + Stats** with placeholders + `<!-- TODO: real data, see D4 -->` so the structure is in place and you just drop numbers in.
3. Keep everything on the bt-branding tokens; no new dependencies.
