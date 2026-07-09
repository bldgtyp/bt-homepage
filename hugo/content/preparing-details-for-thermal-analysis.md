---
title: "Preparing Details for Thermal Analysis"
description: "A designer's guide to preparing CAD base-files for Passive House thermal-bridge and assembly simulations: what to draw, how much, and how to format the drawings BLDGTYP needs."
url: "/preparing-details-for-thermal-analysis/"
image: "/assets/thermal-guide/hero-detail.jpg"
---

<style>
    /* Scoped layout tweaks for the thermal-analysis guide page. */
    .guide-feature { align-items: start; }
    .guide-feature--flip .case-figure { order: 2; }
    @media (max-width: 900px) {
        .guide-feature--flip .case-figure { order: 0; }
    }
    /* Full-bleed hero: faded thermal detail behind a blue accent wash, mirroring the homepage hero. */
    .guide-hero {
        position: relative;
        overflow: hidden;
        padding-top: 128px;
        padding-bottom: 104px;
    }
    .guide-hero-bg {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        min-height: 100%;
        max-width: none;
        object-fit: cover;
        object-position: center;
        pointer-events: none;
        z-index: 0;
    }
    [data-theme="light"] .guide-hero-bg { opacity: 0.18; filter: grayscale(62%); }
    [data-theme="dark"] .guide-hero-bg { opacity: 0.10; filter: contrast(200%) hue-rotate(120deg); }
    .guide-hero::after {
        content: '';
        position: absolute;
        inset: 0;
        z-index: 0;
        background: var(--accent);
        opacity: 0.25;
        pointer-events: none;
    }
    .guide-hero .page-hero-inner { position: relative; z-index: 1; }
    /* Heavier, higher-contrast intro so it holds up over the tinted background. */
    .guide-hero .page-hero-intro {
        font-weight: 500;
        color: var(--text-primary);
    }
    .guide-prose p { margin-bottom: 18px; color: var(--text-secondary); }
    .guide-prose p:last-child { margin-bottom: 0; }
    .guide-list {
        margin: 0 0 18px;
        padding-left: 1.2em;
        color: var(--text-secondary);
    }
    .guide-list li { margin-bottom: 10px; line-height: 1.6; }
    .guide-note {
        margin-top: 22px;
        padding-top: 18px;
        border-top: 1px solid var(--border-subtle);
        font-family: var(--font-mono);
        font-size: 11px;
        line-height: 1.7;
        letter-spacing: 0.02em;
        color: var(--text-muted);
    }
    .guide-junctions {
        margin: 32px 0 0;
        padding: 0;
        list-style: none;
        columns: 2;
        column-gap: 48px;
    }
    @media (max-width: 760px) { .guide-junctions { columns: 1; } }
    .guide-junctions li {
        break-inside: avoid;
        display: grid;
        grid-template-columns: 30px 1fr;
        gap: 12px;
        margin-bottom: 16px;
        line-height: 1.55;
        color: var(--text-secondary);
    }
    .guide-junctions .guide-key {
        font-family: var(--font-mono);
        font-weight: 500;
        font-size: 12px;
        color: var(--accent);
        padding-top: 2px;
    }

    /* --- Magnify affordance on each figure --- */
    .zoom-media { position: relative; display: block; line-height: 0; }
    .zoom-btn {
        position: absolute;
        top: 12px; right: 12px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px; height: 40px;
        padding: 0;
        border: 1px solid rgba(255, 255, 255, 0.22);
        border-radius: 999px;
        background: rgba(15, 18, 24, 0.55);
        -webkit-backdrop-filter: blur(7px);
        backdrop-filter: blur(7px);
        color: #fff;
        cursor: pointer;
        opacity: 0.8;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.25);
        transition:
            opacity var(--transition-base),
            background-color var(--transition-base),
            border-color var(--transition-base),
            transform var(--transition-base);
    }
    .zoom-btn svg { width: 18px; height: 18px; display: block; }
    .zoom-media:hover .zoom-btn { opacity: 1; }
    .zoom-btn:hover {
        background: var(--accent);
        border-color: var(--accent);
        opacity: 1;
        transform: translateY(-1px);
    }
    .zoom-btn:focus-visible {
        opacity: 1;
        outline: 2px solid var(--accent);
        outline-offset: 2px;
    }

    /* --- Lightbox --- */
    .tg-lightbox {
        position: fixed;
        inset: 0;
        z-index: 2000;
        display: none;
        align-items: center;
        justify-content: center;
        padding: 40px;
        background: rgba(8, 10, 14, 0.88);
        -webkit-backdrop-filter: blur(6px);
        backdrop-filter: blur(6px);
    }
    .tg-lightbox.is-open { display: flex; animation: tg-fade 180ms ease both; }
    .tg-lightbox__stage {
        max-width: 94vw;
        max-height: 86vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: auto;
        border-radius: var(--radius-sm);
        -webkit-overflow-scrolling: touch;
    }
    .tg-lightbox__img {
        display: block;
        max-width: 92vw;
        max-height: 84vh;
        width: auto;
        height: auto;
        object-fit: contain;
        background: #fff;
        border-radius: var(--radius-sm);
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.55);
        cursor: zoom-in;
        animation: tg-pop 200ms ease both;
    }
    .tg-lightbox__stage.is-zoomed {
        align-items: flex-start;
        justify-content: flex-start;
    }
    .tg-lightbox__stage.is-zoomed .tg-lightbox__img {
        max-width: none;
        max-height: none;
        cursor: zoom-out;
        animation: none;
    }
    .tg-lightbox__close {
        position: fixed;
        top: 20px; right: 24px;
        z-index: 2010;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 44px; height: 44px;
        padding: 0;
        border: 1px solid rgba(255, 255, 255, 0.24);
        border-radius: 999px;
        background: rgba(15, 18, 24, 0.6);
        -webkit-backdrop-filter: blur(7px);
        backdrop-filter: blur(7px);
        color: #fff;
        cursor: pointer;
        transition: background-color var(--transition-base), border-color var(--transition-base), transform var(--transition-base);
    }
    .tg-lightbox__close svg { width: 20px; height: 20px; display: block; }
    .tg-lightbox__close:hover { background: var(--accent); border-color: var(--accent); transform: rotate(90deg); }
    .tg-lightbox__close:focus-visible { outline: 2px solid #fff; outline-offset: 2px; }
    .tg-lightbox__cap {
        position: fixed;
        left: 0; right: 0;
        bottom: 16px;
        margin: 0 auto;
        max-width: 760px;
        padding: 0 24px;
        text-align: center;
        font-family: var(--font-mono);
        font-size: 11px;
        line-height: 1.6;
        letter-spacing: 0.03em;
        color: rgba(255, 255, 255, 0.74);
        pointer-events: none;
    }
    .tg-lightbox__hint {
        display: block;
        margin-top: 6px;
        color: rgba(255, 255, 255, 0.48);
    }
    @keyframes tg-fade { from { opacity: 0; } to { opacity: 1; } }
    @keyframes tg-pop { from { opacity: 0; transform: scale(0.975); } to { opacity: 1; transform: none; } }
    @media (prefers-reduced-motion: reduce) {
        .tg-lightbox.is-open, .tg-lightbox__img { animation: none; }
        .zoom-btn, .tg-lightbox__close { transition: none; }
        .tg-lightbox__close:hover { transform: none; }
    }
</style>

<section class="page-hero guide-hero">
    <img class="guide-hero-bg" src="/assets/thermal-guide/hero-detail.jpg" alt="" aria-hidden="true">
    <div class="page-hero-inner">
        <span class="section-label">DESIGNER'S GUIDE</span>
        <h1>Preparing details for thermal analysis.</h1>
        <p class="page-hero-intro type-body-lg">
            To verify envelope performance for Passive House certification, BLDGTYP runs a series of
            thermal simulations of a project's typical assemblies and its critical junctions. Those
            simulations only work if the design team hands off clean CAD base-files. This guide explains
            exactly what to draw, how much, and how to format the drawings so the models are accurate the
            first time.
        </p>
    </div>
</section>

<section class="page-section page-section--alt">
    <div class="page-section-inner">
        <div class="case-feature guide-feature">
            <figure class="case-figure">
                <img src="/assets/thermal-guide/process-steps.jpg" alt="Three-step thermal simulation workflow: a flat 2D CAD base-file, closed polygons with materials assigned, and the finished heat-transfer simulation">
                <figcaption>
                    1) A flat 2D CAD base-file is created for each assembly and detail, drawn full scale with
                    hatches, notes, and dimensions removed to leave clean outlines. &nbsp;2) In the simulation
                    environment, closed polygons are built for every element, materials (conductivity,
                    emissivity, etc.) are assigned, and boundary conditions applied to interior and exterior.
                    &nbsp;3) Simulations are run and the relevant values (R-values, surface temperatures) are
                    output for the whole-building model or certification.
                </figcaption>
            </figure>
            <div class="guide-prose">
                <span class="section-label">THERMAL SIMULATION</span>
                <h2 class="page-heading">Why we need base-files.</h2>
                <p>
                    To verify and demonstrate envelope performance for Passive House certification, BLDGTYP
                    executes a series of thermal simulations of: (a) all "typical" building assemblies for
                    walls, roofs, and floors; and (b) all detail thermal bridging at critical junctions between
                    two envelope elements, such as where the roof connects to the wall.
                </p>
                <p>
                    To run these simulations, the design team prepares base-files and transmits them to
                    BLDGTYP. These flat 2D CAD drawings are imported into our simulation environment, which we
                    use to evaluate:
                </p>
                <ul class="guide-list">
                    <li>R-values of all assemblies</li>
                    <li>Psi-values of all critical junctions</li>
                    <li>Critical interior surface temperatures for durability</li>
                </ul>
                <p>This guide explains how to prepare the required base-files.</p>
                <p class="guide-note">
                    // Reference documents: all thermal-bridge models follow the protocols in ISO 10211
                    ("Thermal bridges in building construction"), ISO 13788 ("Hygrothermal performance of
                    building components and building elements"), and ISO 10077-2 ("Thermal performance of
                    windows, doors and shutters"). See these references for detail on any specific requirement.
                </p>
            </div>
        </div>
    </div>
</section>

<section class="page-section">
    <div class="page-section-inner">
        <div class="case-feature guide-feature guide-feature--flip">
            <figure class="case-figure">
                <img src="/assets/thermal-guide/detail-catalog.png" alt="Pages from a project thermal-bridge catalog, collecting each envelope detail alongside its simulation results">
                <figcaption>A project detail catalog collects each key detail alongside its thermal-analysis results for the certification review.</figcaption>
            </figure>
            <div class="guide-prose">
                <span class="section-label">DETAILS · CATALOGING</span>
                <h2 class="page-heading">Every detail lands in the catalog.</h2>
                <p>
                    As part of the Passive House certification submission, BLDGTYP builds a project detail
                    "catalog" that collects and organizes all the key project details alongside their
                    thermal-analysis results. This catalog is a central piece of the certification review.
                </p>
                <p>
                    It is the design team's responsibility to provide accurate details so BLDGTYP can produce
                    the catalog and the required simulations. All detail geometry, material specifications, and
                    any special considerations should be communicated to BLDGTYP so the project details are
                    clean and consistent for the certification reviewers.
                </p>
                <p>
                    All details in the catalog must match the as-built conditions as closely as possible, and
                    are coordinated with the whole-building energy model.
                </p>
            </div>
        </div>
    </div>
</section>

<section class="page-section page-section--alt">
    <div class="page-section-inner">
        <div class="case-feature guide-feature">
            <figure class="case-figure">
                <img src="/assets/thermal-guide/drawing-set-detail.png" alt="An architectural floor-connection detail showing insulation, air barrier, vapor control, and structural bridging elements clearly labeled">
                <figcaption>A drawing-set detail should read clearly: insulation layers, structural and bridging elements, air-tightness, vapor control, and waterproofing all identified.</figcaption>
            </figure>
            <div class="guide-prose">
                <span class="section-label">DETAILS · DRAWING SET</span>
                <h2 class="page-heading">What each detail must show.</h2>
                <p>
                    Each project detail and assembly must be documented in the architectural drawing set in a
                    way that lets the detail catalog reference it &mdash; typically a separate drawing for each
                    relevant detail. To allow for Passive House certification review, every detail should
                    clearly illustrate:
                </p>
                <ol class="guide-list">
                    <li>All insulation layers and materials used as part of the envelope.</li>
                    <li>All structural and bridging elements &mdash; studs, beams, shelf angles, or anything else penetrating the insulation &mdash; with their material designations / product information.</li>
                    <li>All air-tightness layers and materials.</li>
                    <li>All moisture / vapor-control layers and materials.</li>
                    <li>All exterior waterproofing.</li>
                </ol>
            </div>
        </div>
    </div>
</section>

<section class="page-section">
    <div class="page-section-inner">
        <div class="case-feature guide-feature guide-feature--flip">
            <figure class="case-figure">
                <img src="/assets/thermal-guide/base-file-prep.jpg" alt="CAD drawing of thermal-bridge details being prepared: flat linework organized on layers, with a thumbnail index of the detail set">
                <figcaption>Base-files are delivered flat, full-scale, in DXF or DWG, with all objects drawn as closed polygons.</figcaption>
            </figure>
            <div class="guide-prose">
                <span class="section-label">BASE-FILES</span>
                <h2 class="page-heading">How to prepare the CAD.</h2>
                <p>
                    All drawings should be full scale and delivered in CAD format (DXF or DWG). Take care that
                    the drawing is flat (no 3D elements) and that all hatches, dimensions, and notes are
                    removed or placed on dedicated layers, separate from the basic geometry profiles. Groups,
                    blocks, and other dynamic objects should be un-grouped, broken into raw geometry, and
                    flattened. <strong>All objects to be simulated must be drawn as closed polygons, with every
                    vertex overlapping or touching &mdash; no gaps or breaks in the lines or objects.</strong>
                </p>
                <p>
                    Multiple details / assemblies may be supplied in a single CAD file if preferred, provided
                    the different details do not touch or overlap and it is clear how they are organized within
                    the file.
                </p>
                <p>
                    If needed, notes or other reference information may be added to the "Defpoints" layer to
                    communicate information to the thermal modeler or to name / catalog the details.
                </p>
            </div>
        </div>
    </div>
</section>

<section class="page-section page-section--alt">
    <div class="page-section-inner">
        <div class="case-feature guide-feature">
            <figure class="case-figure">
                <img src="/assets/thermal-guide/geometry-2d.png" alt="Diagram of a 2D corner junction showing minimum drawing length equal to the larger of 3x the assembly thickness or 1m, plus half a stud bay, with a right and wrong example of closed polygons">
                <figcaption>Minimum dimension (d) = larger of 3&times;b or 1m in each direction. Extend past the minimum to include half a typical stud/joist bay (L<sub>w</sub>). Right: vertices coincident with no gaps.</figcaption>
            </figure>
            <div class="guide-prose">
                <span class="section-label">2D GEOMETRIC / CONSTRUCTION BRIDGES</span>
                <h2 class="page-heading">How much to draw at a junction.</h2>
                <p>
                    Per ISO 10211, for all junctions &mdash; corners, parapets, and the like &mdash; the
                    minimum dimension (d) is 1m in both directions (x and y). In addition, length (d) should be
                    at least 3&times; the thickness (b) of the assembly. If the assembly includes repeating
                    thermal bridges (studs), extend the drawing beyond the minimum to include half the length
                    of a typical stud/joist bay (L<sub>w</sub>). Any assembly may be drawn larger than the
                    minimum if desired.
                </p>
                <p>
                    What if your wall isn't actually 1m long? Even if windows, doors, or other elements sit
                    closer than 1m to the corner, omit those elements here. Draw only the "typical" assembly
                    and the structural items (columns, beams) related to the corner or intersection under
                    investigation. Those additional disruptions (window jack studs, etc.) are calculated
                    separately and included in the energy model as their own thermal bridges.
                </p>
                <p>
                    And remember: all objects to be simulated should be drawn as closed polygons, with every
                    vertex overlapping or touching &mdash; no gaps or breaks.
                </p>
            </div>
        </div>
    </div>
</section>

<section class="page-section">
    <div class="page-section-inner">
        <div class="case-feature guide-feature guide-feature--flip">
            <figure class="case-figure">
                <img src="/assets/thermal-guide/assemblies.png" alt="Diagrams of a framed assembly with two repeating studs and an unframed assembly showing a 32-inch minimum drawing length">
                <figcaption>Framed assembly: include at least two typical framing members plus half-bays. Unframed assembly (e.g. cast-in-place slab): draw a minimum of 32&Prime; long.</figcaption>
            </figure>
            <div class="guide-prose">
                <span class="section-label">ASSEMBLIES</span>
                <h2 class="page-heading">How much to draw for R-value.</h2>
                <p>
                    To properly assess assembly R-values, we simulate the effective R-value of each assembly,
                    including all material layers, framing elements, and finish surfaces &mdash; including
                    battens and air layers.
                </p>
                <p>
                    For each "typical" assembly in the building (walls, floors, roofs), the drawing should be
                    long enough to include at least two typical framing elements (studs, joists, etc.). If no
                    repeating elements are present &mdash; as in a cast-in-place concrete slab &mdash; the
                    drawing should be a minimum of 32&Prime; long.
                </p>
            </div>
        </div>
    </div>
</section>

<section class="page-section page-section--alt">
    <div class="page-section-inner">
        <span class="section-label">WHICH DETAILS TO DRAW</span>
        <h2 class="page-heading">Where thermal bridges hide.</h2>
        <p class="page-intro type-body-lg">
            Details to be assessed for thermal bridging include, but are not always limited to, any area
            where the envelope changes direction by more than 60&deg;, any area where the thickness of the
            primary insulation layer changes, and any area where the material conductivity of the insulation
            layer shifts because of bridging elements or a change in material type. If you're unsure whether a
            detail needs to be drawn and simulated, let us know and we'll review it together.
        </p>
        <figure class="case-figure">
            <img src="/assets/thermal-guide/junction-details.png" alt="A grid of common junction thermal-bridge detail types: parapets, balconies, floor-to-wall connections, footings, roof mountings, beam bearings, penetrations, overhangs, eaves, canopies, and elevator pits">
            <figcaption>Common junction details required for thermal-bridge analysis.</figcaption>
        </figure>
        <ul class="guide-junctions">
            <li><span class="guide-key">A</span><span>All parapet details, including any mountings for railings or guardrails.</span></li>
            <li><span class="guide-key">B</span><span>All balcony details, including thermal-break products with correct dimensions / thicknesses.</span></li>
            <li><span class="guide-key">C</span><span>All floor-to-wall connections, particularly where "interior" insulation is used.</span></li>
            <li><span class="guide-key">D</span><span>All footings / walls below grade and floor-to-wall connections; indicate average grade level relative to floor.</span></li>
            <li><span class="guide-key">E</span><span>All roof mountings / footings for elements such as HVAC, solar, or other fixed objects.</span></li>
            <li><span class="guide-key">F</span><span>All details bearing on steel or concrete beams, particularly at roof decks.</span></li>
            <li><span class="guide-key">G</span><span>All penetrations through the wall or roof, including HVAC, plumbing (roof drains), and electrical.</span></li>
            <li><span class="guide-key">H</span><span>All footings or floor-to-wall connections at grade; indicate average grade level relative to floor.</span></li>
            <li><span class="guide-key">I</span><span>All roof overhangs, eaves, or cornices.</span></li>
            <li><span class="guide-key">J</span><span>All overhangs / bays that protrude from the main geometry, including all floor insulation layers.</span></li>
            <li><span class="guide-key">K</span><span>All connections for canopies, signs, awnings, fire escapes, or other exterior elements that anchor through the insulation.</span></li>
            <li><span class="guide-key">L</span><span>All elevator-pit details, including any raft-slab / footings and vertical walls up to floor level.</span></li>
        </ul>
    </div>
</section>

<section class="page-section">
    <div class="page-section-inner">
        <div class="case-feature guide-feature guide-feature--flip">
            <figure class="case-figure">
                <img src="/assets/thermal-guide/window-details.jpg" alt="Finite-element thermal simulations of a window jamb, head, and sill showing temperature gradients and surface-temperature factors through the frame and surrounding assembly">
                <figcaption>Windows need head, sill, and jamb base-files per unique type &mdash; drawn with all blocking, framing, and trim insulation, out to 1m from the frame.</figcaption>
            </figure>
            <div class="guide-prose">
                <span class="section-label">WINDOWS &amp; DOORS</span>
                <h2 class="page-heading">A special case.</h2>
                <p>
                    Windows demand even more careful attention than typical assemblies or construction
                    junctions. For each unique window type, CAD base-files are required for the head, sill, and
                    jamb details. A unit with multiple frame configurations (e.g. a simulated double-hung with
                    two different jamb configurations) may need more than one CAD detail. This includes all
                    doors &mdash; and door thresholds in particular, which are often critical for condensation
                    risk.
                </p>
                <p>
                    Even if multiple windows share an identical frame type, if they are installed differently
                    or in distinct assemblies, each should have its own base-files and detail set.
                </p>
                <p>
                    Window details should include all blocking, framing, trim insulation, and other elements
                    that support and are part of the installation. Draw the frames accurately with the correct
                    profile, and note that sills and jambs are often different from head profiles &mdash;
                    especially for doors and sliding units. Where a window or door is installed at the junction
                    of more than one assembly element (such as a roof deck), draw those elements following the
                    dimension conventions above (&gt;1m, 3&times;thickness, etc.).
                </p>
            </div>
        </div>
    </div>
</section>

<section class="page-cta">
    <div class="page-cta-inner">
        <h2>Have details that need thermal-bridge modeling?</h2>
        <p class="page-cta-subtitle">Send us your detail set and we'll identify which junctions need simulation and how to prepare the base-files. See our <a href="/thermal-bridge-modeling/" class="link" target="_blank" rel="noopener">thermal-bridge modeling</a> and <a href="/nyc-thermal-bridging/" class="link" target="_blank" rel="noopener">NYC 2025 energy-code</a> pages for more.</p>
        <a class="btn-primary" href="mailto:info@buildingtype.com">Get in touch &rarr; info@buildingtype.com</a>
    </div>
</section>

<script>
(function () {
    var ICON_ZOOM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"></circle><line x1="15.5" y1="15.5" x2="21" y2="21"></line><line x1="10.5" y1="7.5" x2="10.5" y2="13.5"></line><line x1="7.5" y1="10.5" x2="13.5" y2="10.5"></line></svg>';
    var ICON_CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="6" y1="6" x2="18" y2="18"></line><line x1="18" y1="6" x2="6" y2="18"></line></svg>';

    function fullSrc(src) { return src.replace('/thermal-guide/', '/thermal-guide/full/'); }

    var lb = document.createElement('div');
    lb.className = 'tg-lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Enlarged figure');
    lb.innerHTML =
        '<button class="tg-lightbox__close" type="button" aria-label="Close">' + ICON_CLOSE + '</button>' +
        '<div class="tg-lightbox__stage"><img class="tg-lightbox__img" alt=""></div>' +
        '<p class="tg-lightbox__cap"><span class="tg-lightbox__cap-text"></span><span class="tg-lightbox__hint">Click image to zoom &middot; Esc to close</span></p>';
    document.body.appendChild(lb);

    var stage = lb.querySelector('.tg-lightbox__stage');
    var lbImg = lb.querySelector('.tg-lightbox__img');
    var capText = lb.querySelector('.tg-lightbox__cap-text');
    var closeBtn = lb.querySelector('.tg-lightbox__close');
    var lastFocus = null;

    function open(src, caption, alt) {
        lbImg.src = fullSrc(src);
        lbImg.alt = alt || caption || '';
        capText.textContent = caption || '';
        stage.classList.remove('is-zoomed');
        stage.scrollTop = 0; stage.scrollLeft = 0;
        lb.classList.add('is-open');
        document.body.style.overflow = 'hidden';
        lastFocus = document.activeElement;
        closeBtn.focus();
    }
    function close() {
        lb.classList.remove('is-open');
        document.body.style.overflow = '';
        lbImg.removeAttribute('src');
        if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    function toggleZoom() {
        var zoomed = stage.classList.toggle('is-zoomed');
        if (!zoomed) { stage.scrollTop = 0; stage.scrollLeft = 0; }
    }

    closeBtn.addEventListener('click', close);
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    lbImg.addEventListener('click', toggleZoom);
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lb.classList.contains('is-open')) close();
    });

    var figs = document.querySelectorAll('figure.case-figure');
    Array.prototype.forEach.call(figs, function (fig) {
        var img = fig.querySelector('img');
        if (!img) return;
        var cap = fig.querySelector('figcaption');
        var media = document.createElement('div');
        media.className = 'zoom-media';
        img.parentNode.insertBefore(media, img);
        media.appendChild(img);
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'zoom-btn';
        btn.setAttribute('aria-label', 'View this figure larger');
        btn.innerHTML = ICON_ZOOM;
        media.appendChild(btn);
        var caption = cap ? cap.textContent.trim().replace(/\s+/g, ' ') : '';
        btn.addEventListener('click', function () {
            open(img.getAttribute('src'), caption, img.getAttribute('alt'));
        });
    });
})();
</script>
