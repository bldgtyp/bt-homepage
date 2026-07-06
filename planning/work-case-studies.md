# Work / Case Studies Section

## Status

Hidden from the public homepage until cleared case-study content is ready.

## Current Site State

- `site/index.html` still contains the `#work` section markup, but the section is hidden with the `hidden` attribute.
- The homepage nav no longer links to `#work`.
- The Hugo shared nav no longer links to `/#work`.
- The About page "THE WORK" card now says `case studies forthcoming` instead of linking to the hidden section.

## Why It Is Hidden

The current section still uses bracketed placeholders for project names, modeled-vs-measured results, cost premium, and client quote text. Publishing those placeholders weakens the site and implies proof we have not yet cleared for public use.

## References

- Homepage section: `site/index.html`, `section.proof#work`
- Hugo nav source: `hugo/layouts/partials/nav.html`
- About page source: `hugo/layouts/_default/about.html`
- Generated About page: `site/about/index.html`
- Research blocker: `research/synthesis/positioning-decisions.md`, D4 "Publishable proof"
- Original copy plan: `research/synthesis/homepage-copy-redline.md`, section 8 "Proof / Selected Work"

## Turn Back On When

- Project names or anonymized descriptions are approved.
- Modeled-vs-measured figures are available and checked.
- Any cost-premium claim is sourced or removed.
- Client quote text is approved, or the quote slot is removed.
- The homepage nav and About-page link can point to the section without sending visitors to placeholder content.
