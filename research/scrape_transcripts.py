#!/usr/bin/env python3
"""Scrape Marketing Passivhaus episode transcripts from marketingpassivhaus.com.

Each episode has a page at /episodes/<slug>/transcript whose transcript text
lives in a single <div class="site-content-text site-episode-show-notes"> block
of <p> paragraphs with inline timestamp anchors.
"""
import html as htmllib
import re
import sys
import time
import urllib.request

BASE = "https://marketingpassivhaus.com"
OUT_DIR = "transcripts"

SLUGS = [
    "trailer",
    "aaron-waldt-475-high-performance-building-supply",
    "adam-white-intelligent-membranes",
    "alexander-gard-murray-passive-house-massachusetts",
    "alexis-jarvis-sidecar-pr",
    "beth-campbell-passive-house-massachusetts",
    "beth-eckenrode-auros-group",
    "brian-pearson-studio-pear",
    "bronwyn-barry-passive-house-bb",
    "dr-wolfgang-feist-passive-house-institute",
    "elrond-burrell-via-architecture",
    "enrico-bonilauri-emu-passive",
    "graham-irwin-essential-habitat-architecture",
    "hans-breaux-project-co-op",
    "jacob-deva-racusin-new-frameworks",
    "jeremy-clarke-simple-life-homes",
    "john-loercher-northeast-projects",
    "josh-salinger-birdsmouth-design-build",
    "katrina-belle-maine-passive-house",
    "kristof-irwin-positive-energy",
    "laurence-hamel-dorais-nzp-fenestration",
    "lindsey-love-regenerative-building-solutions",
    "lloyd-alter-carbon-upfront",
    "lorrie-rand-habit-studio",
    "mariana-pickering-b-public-prefab",
    "mark-attard-point-6",
    "martin-comas-arquitectura-regenerativa",
    "michael-quast-passive-house-canada",
    "naomi-beal-passivhausmaine",
    "rachel-rennard-mike-bratina-clay-brook-passive-house",
    "renee-relf-m-arch-cphc",
    "shefali-sanghvi-dattner-architects",
    "steve-hessler-new-energy-works",
    "tanya-savas-collective-carpentry",
    "tessa-bradley-artisans-group",
    "trey-farmer-forge-craft-architecture-design",
    "valentine-gomez-gomex-engineering",
    "zack-semke-passive-house-accelerator",
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (transcript-archiver)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def extract_title(page):
    m = re.search(r"<title>([^<]*)</title>", page)
    if not m:
        return ""
    return htmllib.unescape(m.group(1)).strip()


def extract_transcript(page):
    """Return cleaned transcript text, or None if the content block is absent/empty."""
    start = page.find('class="site-content-text site-episode-show-notes"')
    if start == -1:
        return None
    # advance to end of the opening tag
    gt = page.find(">", start)
    end = page.find("</div>", gt)
    inner = page[gt + 1:end]

    # Replace timestamp anchors with bracketed plain text: [00:00:00]
    inner = re.sub(r'<a [^>]*?>(\d{2}:\d{2}:\d{2})</a>', r'\1', inner)
    # Drop any other anchors but keep their text
    inner = re.sub(r'<a [^>]*?>(.*?)</a>', r'\1', inner, flags=re.S)
    # Paragraph + line breaks -> newlines
    inner = re.sub(r'<br\s*/?>', '\n', inner)
    inner = re.sub(r'</p>', '\n\n', inner)
    inner = re.sub(r'<p>', '', inner)
    # Strip any remaining tags
    inner = re.sub(r'<[^>]+>', '', inner)
    text = htmllib.unescape(inner)
    # Normalize whitespace
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.replace('​', '').strip()
    return text if text else None


def main():
    import os
    os.makedirs(OUT_DIR, exist_ok=True)
    results = []
    for i, slug in enumerate(SLUGS, 1):
        url = f"{BASE}/episodes/{slug}/transcript"
        try:
            page = fetch(url)
        except Exception as e:
            results.append((slug, "FETCH_ERROR", str(e)))
            print(f"[{i:02d}/{len(SLUGS)}] {slug}: FETCH ERROR {e}", file=sys.stderr)
            continue
        title = extract_title(page)
        text = extract_transcript(page)
        if not text:
            results.append((slug, "NO_TRANSCRIPT", title))
            print(f"[{i:02d}/{len(SLUGS)}] {slug}: NO TRANSCRIPT")
        else:
            header = f"# {title}\nSource: {url}\n\n"
            path = os.path.join(OUT_DIR, f"{slug}.md")
            with open(path, "w") as f:
                f.write(header + text + "\n")
            wc = len(text.split())
            results.append((slug, "OK", f"{wc} words"))
            print(f"[{i:02d}/{len(SLUGS)}] {slug}: OK ({wc} words)")
        time.sleep(0.5)

    # Summary
    ok = [r for r in results if r[1] == "OK"]
    missing = [r for r in results if r[1] != "OK"]
    print(f"\n=== {len(ok)}/{len(SLUGS)} transcripts saved ===")
    if missing:
        print("Missing / errors:")
        for slug, status, info in missing:
            print(f"  - {slug}: {status} {info}")


if __name__ == "__main__":
    main()
