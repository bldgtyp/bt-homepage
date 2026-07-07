# BLDGTYP Homepage — Alignment Audit & Business-Model Critique

*Compares the current `site/index.html` against the field rules in [`marketing-rules.md`](./marketing-rules.md), distilled from 38 "Marketing Passivhaus" episodes. Two lenses: (A) marketing/messaging alignment, (B) business-model / product-and-service strategy. Citations point to the rule's source guest + slug so every recommendation traces back to a practitioner.*

---

## How to read this

- **Part 1 — Executive summary**: the five things that matter most.
- **Part 2 — The core strategic tension** (the "Passive House" name) and how to resolve it for *our* situation.
- **Part 3 — Section-by-section scorecard** of the live page.
- **Part 4 — Prioritized action list** (DEVELOP / EDIT / REMOVE / ADD / UPDATE / UPGRADE), tagged P0–P2.
- **Part 5 — Concrete copy rewrites** (before → after).
- **Part 6 — Business-model & offerings critique** — where the *product*, not just the words, should change.
- **Part 7 — Open decisions for Ed.**

A blunt one-line verdict up front: **the site is professional, fast, and well-segmented, but it sells like an engineer talking to engineers — energy-first, metric-heavy, name-first — which is exactly the anti-pattern the corpus warns against most loudly.**

---

## Part 1 — Executive summary

1. **We lead with energy and jargon; the field says lead with the felt human benefits.** Comfort, health, quiet, resilience, durability, safety appear essentially *nowhere* on the page. This is the #1, highest-consensus rule (~30+ guests) and our biggest single gap. Energy is supposed to be the *proof*, not the *pitch* — "you get this happy little accident, which is energy efficiency" [josh-salinger-birdsmouth-design-build].

2. **There is no homeowner on this website.** Hero, "who we work with," and both CTAs address only architects/developers/builders. Yet single-family EnerPHit retrofits & second homes are a core BLDGTYP line, the website is "the dominant inbound channel for residential PH leads" [tessa-bradley-artisans-group], and the corpus repeatedly says to market to the *experience-driven decision-maker / "other spouse"* [graham-irwin-essential-habitat-architecture]. Either we deliberately don't want owner leads (a legitimate B2B-only stance — see Part 7) or this is a large hole.

3. **We show almost no proof.** The "stats" are generic movement statistics (9,000 units, 90% reduction, #1 fastest-growing). The corpus is emphatic that **measured-vs-modeled performance is the single most powerful proof** ("within 0.01% of the model") [hans-breaux-project-co-op][elrond-burrell-via-architecture], followed by testimonials, named projects, and warm team bios [kristof-irwin-positive-energy]. We have a portfolio and real results — none of it is on the page.

4. **We never address cost.** Cost is THE universal objection across all 38 episodes, and the winning move is to confront it with hard numbers (2–3% multifamily premium, lifetime/compounding savings, "a learning curve, not a premium") [alexander-gard-murray…][beth-eckenrode-auros-group]. The page is silent on it.

5. **Our two best authority assets are buried.** The open-source Passive House Tools and Ed's YouTube are genuine, near-unique differentiators that perfectly enable the "be a *knowledge resource*, not a vendor" positioning [aaron-waldt-475…]. Today they're a single grey strip and a nav icon. They should be load-bearing.

---

## Part 2 — The core strategic tension: should we still say "Passive House"?

The loudest rule in the corpus is "**don't lead with the name 'Passive House'** — it reads as weak/foreign, people confuse it with passive solar" [lloyd-alter-carbon-upfront][zack-semke…]. Our entire site leads with it: page title, hero headline, stats header, CTAs.

**But this rule does not apply to us the same way, and we should not go "stealth."** Here's the reasoning:

- The "never name it" advocates (Ingui, Alter, Savas) are mostly selling to **homeowners** who don't know the term. Our primary stated audience is **architects, developers, and builders** — who *search for* "Passive House consultant," already value the standard, and for whom the name is a credibility and SEO asset. Feist and Bronwyn Barry explicitly argue PH should be named as the *defined performance target* the industry otherwise lacks [dr-wolfgang-feist…][bronwyn-barry-passive-house-bb].
- We also literally *are* a Passive House certification firm. Hiding it would be incoherent.

**Recommendation — "name it, but don't let it carry the emotional load":**
- **Keep** "Passive House" in the page title, meta, MA/certification sections, and B2B copy (SEO + credibility). 
- **Stop letting it be the *hook*.** The hero and any owner-facing copy should open on the *outcome* (comfort/health/quiet/resilience/de-risked delivery) and let "Passive House" arrive as the *method* a sentence later. This is the dominant "benefits-first, soft-reveal" consensus, and it costs us nothing in SEO because the term still appears throughout.

Net: this is a **copy/sequencing** change, not a rebrand. Everywhere the page currently says "Passive House" as a *value proposition*, replace the value proposition with a felt benefit and demote "Passive House" to the *how*.

---

## Part 3 — Section-by-section scorecard

| Section | What it does now | Verdict | Primary gap vs. rules |
|---|---|---|---|
| **Title / meta** | "BLDGTYP · Passive House Consulting · NY · MA" | ✅ Keep | Fine for SEO; no change. |
| **Hero** | "Your Passive House questions. Answered." + B2B subhead + email button | ⚠️ Weak | No felt benefit; name-first; audience = B2B only; CTA is a raw mailto. [Rule 1, Lang/Framing] |
| **Who we work with** (Architects / Developers / Builders) | Segmented 3-column | ✅ Strong structure, ⚠️ thin copy | Best part of the page — segmentation is exactly right [mariana-pickering…]. But **no Homeowners column**, and builder/architect copy doesn't yet hit craft-pride / fewer-callbacks / de-risk language. |
| **Services** (Energy Modeling / Thermal Bridges / Certification) | 3 technical cards | ⚠️ Engineer-led | Framed as technical deliverables, not client outcomes. No comfort/health/risk framing. Certification sold as "cross the finish line" — but corpus says sell *de-risking/insurance*, and many clients abandon certification [josh-salinger…][jeremy-clarke…]. |
| **Process** (5 steps) | Share plans → model → review → report → build | ✅ Good | Supports the "easy button"/de-risk story [hans-breaux…]. Slightly modeling-centric; otherwise solid. |
| **Design-Phase Assessment** | Report mockup w/ kWh/m²a, W/m² + bullet list | ⚠️ Metric-dump | The mockup screams jargon (ACH/kWh) — the explicit FAIL pattern [zack-semke…]. Great tagline ("clear enough for everyone, detailed enough for an engineer") undercut by an all-numbers visual. Needs felt-outcome translation alongside the metrics. |
| **Open Source strip** | One line on PH Tools | ❌ Under-used | This is a top-3 differentiator buried in a grey bar. Should anchor "knowledge resource, not vendor." |
| **Massachusetts** | Code + incentives + our role, cited | ✅✅ Excellent | Model for the whole site: specific, localized to felt pain/incentives [bronwyn-barry…], honest disclaimer, real sources. Leave it; replicate its rigor elsewhere. |
| **Stats** ("Why Passive House?") | 9,000 / 90% / 60yrs / #1 | ⚠️ Generic & energy-led | Movement stats, not *our* proof. "90% reduction" is energy-framed. Replace/supplement with measured-vs-modeled, cost-premium-myth, and resilience numbers [hans-breaux…][alexander-gard-murray…]. |
| **Final CTA** | "Ready to get started?" B2B | ⚠️ Flat | No emotional close; B2B-only again; raw mailto. |
| **Footer** | PHI/Phius seals, contact | ✅ Keep | Good trust seals [aaron-waldt…]. |

---

## Part 4 — Prioritized action list

Tagged with the requested verbs and a priority. **P0 = do first / highest leverage.**

### P0 — Highest leverage
1. **UPDATE the hero to lead with felt benefits, soft-reveal "Passive House."** (Part 5 has copy.) Add a real benefit hook; keep a clear B2B sub-line. [Rule 1]
2. **ADD a "Why it's better to live/own/build" benefits block** — a value-stack of Comfort · Healthy air · Quiet · Resilient · Durable · Low bills (energy *last*, as the footnote). Stacking benefits so no single objection kills the sale is a high-consensus rule [brian-pearson-studio-pear][lloyd-alter…]. This is the single biggest missing section.
3. **ADD proof: measured-vs-modeled + at least 2–3 named project case snippets + client testimonial soundbites.** Even one "predicted ≈ actual" chart and one visceral quote ("I don't have to wear a beanie in my own house") would transform credibility [hans-breaux…][tessa-bradley…].
4. **ADD a cost-objection answer** somewhere (FAQ block or a stat). Use real numbers: "~2–3% premium on multifamily, gone in operating savings," "a learning curve, not a premium" [alexander-gard-murray…][beth-eckenrode…]. Be honest per Beth Campbell — "it depends on the team" — don't overpromise "no premium."

### P1 — Strong improvements
5. **~~ADD a Homeowners column~~ → RESOLVED: B2B, no consumer funnel** ([positioning D1](./positioning-decisions.md)). Instead, **UPGRADE the positioning to "architect-first / add-on team member / outside pair of eyes"** — make the architect/developer look good and de-risk *their* project [mark-attard…][elrond-burrell…]. **ADD a thin plain-language reassurance layer** (one short "what this means for your client" note) so a referred homeowner doing due diligence can confidently endorse hiring us — secondary to the professional voice [graham-irwin…].
6. **EDIT the Services cards** to lead each with the *outcome* then the *method*: e.g. Certification → "De-risk your build / durability insurance," not "cross the finish line" [josh-salinger…]. Translate the deliverable mockup's metrics into a felt line ("≈ stays 70°F for days without power").
7. **UPGRADE the Open-Source strip into a real "Knowledge Resource" section** — PH Tools + YouTube + (future) resources. Positions us as the firm that *teaches*, the "give value first / jab-jab-right-hook" engine [elrond-burrell…][aaron-waldt…].
8. **UPDATE the Stats** to mix in BLDGTYP-specific / felt-outcome proof rather than only abstract movement numbers.
9. **ADD low-friction lead magnets / CTAs beyond mailto** — "Send us your drawings for a plan review," a downloadable best-practices/detail one-pager [aaron-waldt…][beth-campbell…]. Replace raw `mailto:` buttons with a softer ask.

### P2 — Polish / longer-horizon
10. **ADD "make the invisible visible" media** — a blower-door/fog clip, an IAQ/sensor dashboard mock, a cutaway assembly animation. "You can't take a picture of good air quality" — so build the visual [alexis-jarvis…][adam-white…].
11. **ADD an experience/tour or "see one" path** (even "ask us about visiting a finished project") [wolfgang-feist…][john-loercher…].
12. **ADD a soft "near-PH / pretty-good-house welcome"** line so we don't read as gatekept/elitist and we capture clients who balk at full certification [michael-quast…][naomi-beal…].
13. **ADD warm team bios** (2-person firm is an asset, not a liability — personal connection converts) [kristof-irwin…].
14. **REMOVE / rework** the pure-energy "90% reduction" stat as the lead metric; keep it but reframe.

> Note: I'm **not** recommending removing much — the page is lean. The work is overwhelmingly *reframe + add proof + add benefits*, not delete.

---

## Part 5 — Concrete copy rewrites (before → after)

**Hero** — *before:*
> Your Passive House questions. *Answered.*
> // Passive House design and consulting for architects, developers, and builders. We find the answers so you can build with confidence.

*after (option A, benefit-first, soft-reveal):*
> **Buildings that are quiet, healthy, and comfortable — and stay that way when the power doesn't.**
> // We're the Passive House engineering team behind high-performance homes and multifamily across New York & Massachusetts. We de-risk the performance so architects, developers, and builders deliver with confidence.
> [Send us your drawings →]  ·  info@buildingtype.com

*Why:* opens on felt outcome + resilience [kristof-irwin…][lloyd-alter…], names PH as the *method*, keeps the B2B audience explicit, upgrades the CTA from raw mailto to a low-friction offer [aaron-waldt…].

**Builders column** — *add craft-pride + fewer-callbacks:*
> You're building it — and your name is on it. We give you blower-door-proven details and right-sized mechanicals, so you get fewer callbacks, fewer no-heat emergencies, and proof your craft is the best on the block. *("You can't unlearn Passive House.")* [valentine-gomez…][brian-pearson…]

**Certification card** — *before:* "Cross the finish line." *after:*
> **De-risk the whole build.** Third-party Phius/PHI certification is durability insurance — it catches the costly envelope defects a code inspector never will. We run the modeling, documentation, and review so you don't carry the risk. [josh-salinger…]

**Design-Phase Assessment** — keep the metrics, but add a felt-outcome caption under the report mockup:
> *What these numbers mean: even temperatures in every room, fresh filtered air, and a home that holds ~70°F for days with no power.* [enrico-bonilauri…][kristof-irwin…]

**Stats** — swap one or two for proof:
> **±2%** modeled vs. measured energy on our certified projects · **2–3%** typical cost premium on multifamily (recovered in operating savings) · **70°F** held for days without power. [hans-breaux…][alexander-gard-murray…]

---

## Part 6 — Business-model & offerings critique

Beyond words: the corpus surfaces several places where the *product/service shape* — not just the marketing — could change. Ranked by my estimate of leverage for a 2-person firm.

1. **Productize & elevate the front-end as the flagship — and get to the table earlier.** Our "Design-Phase Assessment" is *already* the right move (a named, productized early-design offering), but it's framed as a metrics report. The corpus says: name front-end consulting in plain language, sell it as a distinct service *before* modeling, and "get to the table at the beginning" because late involvement strips every lever [mark-attard-point-6][jeremy-clarke…][bronwyn-barry…]. **Action:** rename/position the assessment around *de-risking + right-sizing + saving money at the cheapest possible moment*, and make "bring us in at concept" an explicit pitch.

2. **ADD a measurement & verification (M&V) / monitoring tier — this is the highest-value new product.** Measured-vs-modeled is simultaneously (a) the #1 proof the website lacks, (b) a recurring-revenue line that keeps us "long term at the table," and (c) content fuel. The corpus describes a productized "minimum viable M&V" — utility meters + IAQ sensors + a dashboard for under ~$10k [beth-eckenrode-auros-group]. For us this is a near-perfect fit: it generates the proof assets *and* a new revenue stream off projects we already model. **Strong recommend.**

3. **Lean into the open-source PH Tools as the business moat — "a knowledge company that happens to consult."** Almost no competitor maintains a respected open-source toolkit. That's a durable authority asset that justifies premium fees and inbound trust [aaron-waldt…]. The "same rigor in our software as our buildings" line already on the page is gold — *expand it into a positioning pillar*, not a footnote.

4. **Build the content/education engine into a service + top-of-funnel.** Ed already has YouTube + open tools. The corpus's repeated playbook: a recurring single-topic webinar/seminar series (475's "Building Blocks," Emu's free talks), plain-English explainers, a downloadable detail handbook, a free calculator — all "give value first" jabs that drive inbound [enrico-bonilauri…][elrond-burrell…][aaron-waldt…]. This can also be a *paid* training line (utilities even reimburse training fees) [enrico-bonilauri…].

5. **A "homeowner's manual / how to operate your Passive House" deliverable** is a cheap, differentiating add-on that improves outcomes and reviews [aaron-waldt…]. Easy win.

6. **Right-sizing mechanicals as an explicit, sellable money-saving value-add.** Clients and developers respond to "our model lets you install a smaller, cheaper HVAC system." It directly answers the cost objection and is concrete [lindsey-love…][beth-eckenrode…]. Make it a named benefit, not an implicit byproduct of modeling.

7. **Trigger-event retrofit offering** (boiler failure, any major renovation → whole-building optimum-performance analysis instead of like-for-like swap) [beth-eckenrode…]. Fits our EnerPHit / second-home / Berkshires retrofit reality precisely.

8. **Decision-reduction onboarding.** Productize the client experience: "here are the 3 decisions we need from you, and your options." Reduces overwhelm and reinforces the de-risk/easy-button brand [jeremy-clarke…][valentine-gomez…].

9. **Consider the "trifecta" bundle** — PH + low-embodied-carbon + healthy/Red-List-free materials — as a differentiator for climate- and health-motivated clients/architects [valentine-gomez…]. **Caveat:** lead with health/comfort, keep carbon as the *secondary* hook — multiple guests warn that *leading* with carbon "preaches to the choir" and loses the market [steve-hessler…][jacob-deva-racusin…].

10. **Sell targets, not the plaque.** Since the certification-abandonment problem is real and widespread [jeremy-clarke…][tessa-bradley…][lorrie-rand…], offer a clear "performance-target (uncertified) vs. full-certification" choice up front. Capture the clients who want the building but not the badge — instead of losing them when they drop certification mid-stream.

---

## Part 7 — Open decisions for Ed

These change the scope of any redesign; worth deciding before we touch `index.html`:

1. **~~Do we want direct homeowner leads, or stay B2B?~~ — RESOLVED 2026-06-29 → B2B.** See [`positioning-decisions.md` D1](./positioning-decisions.md). BLDGTYP is a B2B services firm (~99% architects/developers); we do **not** market directly to homeowners. A referred homeowner is a "ride-along" reader who must be able to confidently endorse hiring us, but is not a lead-gen target. **Effect on this doc:** drop the "add a Homeowners column / consumer funnel" recommendation (P1 #5); instead center *architect-first / add-on team member / outside-pair-of-eyes / portfolio-as-proof* positioning, with only a thin plain-language reassurance layer for the sent-over owner. All other recommendations stand.

2. **How hard do we soft-pedal the "Passive House" name?** My recommendation (Part 2) is "keep for SEO/credibility, demote from the emotional hook." Confirm you're comfortable with that vs. either extreme.

3. **Appetite for the M&V / monitoring product line?** It's the highest-leverage new offering but it's a genuine new service to stand up, not just a copy change.

4. **What proof can we actually publish?** Which projects can be named, which clients will give a testimonial, do we have a clean measured-vs-modeled dataset to chart? The proof recommendations are only as good as what we're allowed to show.

5. **Scope of the next step:** do you want me to (a) draft the actual rewritten copy + new sections as a redline against `index.html`, (b) build a styled HTML version of *this* document to match the rules report, or (c) both?

---

*Sources throughout: [`marketing-rules.md`](./marketing-rules.md) and the per-episode notes in [`../episode-notes/`](../episode-notes/). Bracketed slugs map to those files.*
