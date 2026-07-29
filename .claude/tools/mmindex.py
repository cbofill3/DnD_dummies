#!/usr/bin/env python3
"""Monster Manual name -> PDF page index, with OCR-tolerant fuzzy matching.

The MM is a scan. Entry headings are set in small caps and the OCR destroys them
(`BeNsnnn` for BANSHEE), so grepping the body for a monster name is unreliable. The
book's own A-Z index survived far better, so this builds the lookup from there.

    python .claude/tools/mmindex.py "displacer beast"
    python .claude/tools/mmindex.py --rebuild
    python .claude/tools/mmindex.py --list ha        # everything starting "ha"

Reported pages are the PDF page index, derived from the printed page plus a constant
offset, and are accurate to about +/-1 because full-page art shifts the alignment.
Render the reported page and its neighbours to read the entry.
"""

import argparse
import difflib
import json
import os
import re
import sys
from pathlib import Path

# Same sibling-relative layout as booksearch.py — see the note there. The books sit
# next to the repo rather than inside it, because they're copyrighted.
REPO_ROOT = Path(__file__).resolve().parents[2]
BOOKS_DIR = Path(os.environ.get("DND_BOOKS") or REPO_ROOT.parent / "Dnd Books")
TEXT_DIR = BOOKS_DIR / "_text"
SOURCE = TEXT_DIR / "mm-2024.txt"
INDEX = TEXT_DIR / "mm-index.json"
# Absolute, because the Read tool needs an absolute path to render the page.
MM_PDF = BOOKS_DIR / "Manual de Monstruos - Ingles.pdf"

# The A-Z index lives on these PDF pages of the scan.
INDEX_PAGES = (6, 7)
# printed page number + PAGE_OFFSET ~= PDF page index. Verified against Bandit
# (printed 27 -> pdf 31), Bugbear (62 -> 65), Bulette (63 -> 66).
PAGE_OFFSET = 3
MAX_PRINTED_PAGE = 400

# Index lines come in several shapes, all mangled:
#   "Bandit..............................................27"
#   "G1abre2u......................................"   <- number wrapped to next line
#   "Displacer Rea <t  98"                             <- no dot leader, junk in name
# So: capture a name, then a leader of dots or wide space, then digits that may have
# spaced out ("37 5") or landed on the following line.
ENTRY_RX = re.compile(
    r"([A-Z][A-Za-z0-9'\-<>^\\/ ]{2,40}?)"     # name, tolerating OCR junk
    r"\s*(?:[.\-]{3,}|\s{2,})\s*"              # dot leader or a run of spaces
    r"([\d\s]{1,6})(?=\s|$)"                   # page digits, possibly spaced
)
# Same, but the number is missing because it wrapped; used to keep the name in
# alphabetical order so interpolation can still place it.
NAMEONLY_RX = re.compile(r"([A-Z][A-Za-z0-9'\-<>^\\/ ]{2,40}?)\s*[.\-]{4,}\s*$")

# Characters the OCR routinely swaps. Folding both sides through this table lets
# "Doppe19an9er" match "Doppelganger" and "G1abre2u" match "Glabrezu".
OCR_FOLD = str.maketrans({
    "0": "o", "1": "l", "2": "z", "5": "s", "6": "b", "8": "b", "9": "g",
    "|": "l", "!": "l", "[": "t", "@": "a", "$": "s",
})


def fold(s):
    s = s.lower().translate(OCR_FOLD)
    s = s.replace("rn", "m").replace("vv", "w")
    return re.sub(r"[^a-z]", "", s)


def build():
    if not SOURCE.exists():
        sys.exit(f"Missing {SOURCE}. Extract it first — see .claude/reference/books.md")
    pages = SOURCE.read_text(encoding="utf-8", errors="replace").split("\f")
    entries, seen = [], set()

    def add(name, printed):
        name = " ".join(name.split()).strip(" .-<>^\\/")
        f = fold(name)
        if len(f) < 3 or f in seen:
            return
        seen.add(f)
        entries.append({"name": name, "printed": printed,
                        "pdf": printed + PAGE_OFFSET if printed else None,
                        "fold": f})

    for pno in INDEX_PAGES:
        if pno > len(pages):
            continue
        for line in pages[pno - 1].split("\n"):
            matched = False
            for raw_name, raw_page in ENTRY_RX.findall(line):
                digits = re.sub(r"\s+", "", raw_page)      # "37 5" -> "375"
                if not digits:
                    continue
                printed = int(digits)
                # OCR invents and drops digits; discard out-of-range pages but
                # keep the name so alphabetical interpolation can still place it.
                add(raw_name, printed if 1 <= printed <= MAX_PRINTED_PAGE else None)
                matched = True
            if not matched:
                m = NAMEONLY_RX.search(line.rstrip())
                if m:
                    add(m.group(1), None)

    entries.sort(key=lambda e: e["fold"])
    entries = _sanity_filter(entries)
    INDEX.write_text(json.dumps(entries, indent=1), encoding="utf-8")
    return entries


def _sanity_filter(entries):
    """Flag entries whose page contradicts alphabetical order.

    The index is alphabetical, so printed pages should rise roughly monotonically.
    A single OCR-corrupted digit (2O5 -> 205, 1O -> 10) shows up as a page that
    jumps far out of line with its neighbours. Those get their page dropped rather
    than trusted; interpolation will place them instead.
    """
    known = [e for e in entries if e["pdf"]]
    for i, e in enumerate(known):
        lo = known[i - 1]["printed"] if i else None
        hi = known[i + 1]["printed"] if i + 1 < len(known) else None
        if lo is not None and hi is not None and lo <= hi:
            if not (lo - 25 <= e["printed"] <= hi + 25):
                e["pdf"] = None
                e["suspect"] = True
    return entries


def interpolate(entries, q):
    """Estimate a page for a name the index lost, from its alphabetical neighbours."""
    known = [e for e in entries if e["pdf"]]
    if not known:
        return None
    before = [e for e in known if e["fold"] <= q]
    after = [e for e in known if e["fold"] >= q]
    lo = before[-1] if before else None
    hi = after[0] if after else None
    if lo and hi:
        return (lo, hi, (lo["pdf"] + hi["pdf"]) // 2)
    anchor = lo or hi
    return (lo, hi, anchor["pdf"])


def load(rebuild=False):
    if rebuild or not INDEX.exists():
        return build()
    return json.loads(INDEX.read_text(encoding="utf-8"))


# Above this, a fuzzy hit is trustworthy enough to report as the answer; below it,
# alphabetical interpolation beats a confident-looking wrong name. Calibrated so
# "displacer beast" still reaches "Displacer Rea <t" (~0.74) while "banshee",
# which the index lost entirely, falls through to interpolation instead of
# matching junk like "Ankheg".
CONFIDENT = 0.70


def find(entries, query, limit=6):
    q = fold(query)
    scored = []
    for e in entries:
        f = e["fold"]
        if f == q:
            score = 1.0
        elif q in f or f in q:
            score = 0.9 - abs(len(f) - len(q)) / 100
        else:
            score = difflib.SequenceMatcher(None, q, f).ratio()
        scored.append((score, e))
    scored.sort(key=lambda t: -t[0])
    return [(s, e) for s, e in scored[:limit] if s > 0.55]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?")
    ap.add_argument("--rebuild", action="store_true", help="re-parse the index")
    ap.add_argument("--list", metavar="PREFIX", help="list entries starting with PREFIX")
    args = ap.parse_args()

    entries = load(rebuild=args.rebuild)

    if args.rebuild and not args.query:
        print(f"Indexed {len(entries)} Monster Manual entries -> {INDEX}")
        return
    if args.list:
        p = fold(args.list)
        hits = [e for e in entries if e["fold"].startswith(p)]
        for e in hits:
            print(f"  pdf p.{e['pdf']:<4} {e['name']}")
        print(f"{len(hits)} entries starting {args.list!r}")
        return
    if not args.query:
        ap.error("give a monster name, --list PREFIX, or --rebuild")

    hits = [(s, e) for s, e in find(entries, args.query)
            if e["pdf"] and s >= CONFIDENT]
    target = None

    if hits:
        print(f"Monster Manual — best matches for {args.query!r}:\n")
        for score, e in hits:
            flag = "" if score > 0.85 else "   (loose match — verify)"
            print(f"  pdf p.{e['pdf']:<4} {e['name']:<34} printed p.{e['printed']}{flag}")
        target, spread = hits[0][1]["pdf"], 1
    else:
        # The OCR destroyed this name in the index too. Entries are alphabetical,
        # so place it between the neighbours that did survive.
        guess = interpolate(entries, fold(args.query))
        if not guess:
            print(f"No usable index. Run --rebuild.")
            return
        lo, hi, page = guess
        print(f"{args.query!r} is not legible in the scanned index — estimating from "
              f"alphabetical position:\n")
        if lo:
            print(f"  after   pdf p.{lo['pdf']:<4} {lo['name']}")
        if hi:
            print(f"  before  pdf p.{hi['pdf']:<4} {hi['name']}")
        # The entry is alphabetically between these two, so the bracket itself is
        # guaranteed to contain it. Render the bracket rather than a guess around
        # the midpoint, which can fall outside it. Read caps at 20 pages.
        lo_p = max(1, (lo["pdf"] if lo else page) - 1)
        hi_p = (hi["pdf"] if hi else page) + 1
        span = hi_p - lo_p
        print(f"\n  => between pdf p.{lo_p} and p.{hi_p} ({span} pages), best guess p.{page}")
        if span > 19:
            hi_p = lo_p + 19
            print(f"     bracket exceeds the 20-page render limit; "
                  f"start with p.{lo_p}-{hi_p} and walk forward if needed")
        target = None

    if target is not None:
        lo_p, hi_p = max(1, target - spread), target + spread
    print(f"\nPage numbers are +/-1 at best. Render the entry to read it accurately:")
    print(f'  Read(file_path=r"{MM_PDF}", pages="{lo_p}-{hi_p}")')
    print("Never transcribe a statblock from the OCR text — see .claude/reference/books.md")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
