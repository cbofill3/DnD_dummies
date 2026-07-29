#!/usr/bin/env python3
"""Search the extracted D&D book text and report PDF page numbers.

The books live outside the repo (copyrighted); only this locator is versioned.

Usage:
    python .claude/tools/booksearch.py "spirit guardians"          # phb + dmg + mm
    python .claude/tools/booksearch.py -b mm "goblin boss"         # one book
    python .claude/tools/booksearch.py -b dmg -C 8 "chase"         # more context
    python .claude/tools/booksearch.py --loose "LEVEL 6"           # tolerate OCR spacing
    python .claude/tools/booksearch.py --page mm 147               # dump a page
    python .claude/tools/booksearch.py --toc dmg                   # chapter map

Every hit is reported as `BOOK pdf-page N`. That N is the page index in the PDF
file: pass it straight to the Read tool's `pages` argument to render the real
page as an image when the OCR text is untrustworthy.
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Resolved relative to this file: <repo>/.claude/tools/booksearch.py -> <repo> -> its
# parent. The books live in a directory sitting alongside the repo, not inside it (they
# are copyrighted and must never be committed). Cloning this repo onto another machine
# therefore means reproducing that layout:
#
#     Desktop/
#       DnD_dummies/  <- this repo
#       Dnd Books/    <- the PDFs and _text/
#
# Override with the DND_BOOKS env var if the books live somewhere else.
REPO_ROOT = Path(__file__).resolve().parents[2]
BOOKS_DIR = Path(os.environ.get("DND_BOOKS") or REPO_ROOT.parent / "Dnd Books")
TEXT_DIR = BOOKS_DIR / "_text"

BOOKS = {
    "phb":    ("phb-en-2024.txt", "PHB_2024.pdf", "PHB 2024 (English, OCR — check numbers)"),
    "phb-es": ("phb-2024.txt", "Manual del Jugador 2024.pdf", "PHB 2024 (Spanish, OCR — for Spanish phrasing)"),
    "dmg":    ("dmg-2024.txt", "Guia del Dungeon Mater (Ingles-DnDBeyond).pdf", "DMG 2024 (English, clean text)"),
    "mm":     ("mm-2024.txt",  "Manual de Monstruos - Ingles.pdf", "MM 2024 (English, OCR — numbers unreliable)"),
}

# Searched by default. phb-es is opt-in via -b: it duplicates phb in English-term
# searches and only earns its keep when you specifically want Spanish wording.
DEFAULT_BOOKS = ["phb", "dmg", "mm"]


def load(book):
    path = TEXT_DIR / BOOKS[book][0]
    if not path.exists():
        sys.exit(f"Missing {path}. Re-extract with:\n"
                 f'  pdftotext -layout -enc UTF-8 "{BOOKS_DIR / BOOKS[book][1]}" "{path}"')
    return path.read_text(encoding="utf-8", errors="replace").split("\f")


def search(book, pattern, context, max_hits):
    pages = load(book)
    rx = re.compile(pattern, re.IGNORECASE)
    hits = 0
    for i, page in enumerate(pages, start=1):
        lines = page.split("\n")
        for j, line in enumerate(lines):
            if rx.search(line):
                lo, hi = max(0, j - context), min(len(lines), j + context + 1)
                print(f"\n=== {book.upper()} pdf-page {i} ===")
                print("\n".join(lines[lo:hi]).rstrip())
                hits += 1
                break  # one excerpt per page keeps output readable
        if hits >= max_hits:
            print(f"\n[stopped at {max_hits} pages; narrow the pattern or raise --max]")
            return hits
    return hits


def show_page(book, n):
    pages = load(book)
    if not 1 <= n <= len(pages):
        sys.exit(f"{book.upper()} has {len(pages)} pages; {n} is out of range.")
    print(f"=== {book.upper()} pdf-page {n} / {len(pages)} ===")
    print(pages[n - 1].rstrip())


def show_toc(book):
    """Heuristic chapter map: lines that look like chapter/part headings."""
    pages = load(book)
    rx = re.compile(r"^\s*(CAP[IÍ]TULO|CHAPTER|PART[E]?|AP[EÉ]NDICE|APPENDIX)\b.{0,60}$",
                    re.IGNORECASE)
    print(f"=== {BOOKS[book][2]} — {len(pages)} pdf pages ===")
    seen = set()
    for i, page in enumerate(pages, start=1):
        for line in page.split("\n")[:25]:
            s = " ".join(line.split())
            if rx.match(s) and s.lower() not in seen:
                seen.add(s.lower())
                print(f"  pdf-page {i:>4}  {s}")
                break


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", help="regex to search for")
    ap.add_argument("-b", "--book", choices=list(BOOKS), action="append",
                    help="limit to a book (repeatable); default all")
    ap.add_argument("-C", "--context", type=int, default=4, help="context lines (default 4)")
    ap.add_argument("--max", type=int, default=12, help="max pages per book (default 12)")
    ap.add_argument("--page", nargs=2, metavar=("BOOK", "N"), help="dump one page")
    ap.add_argument("--toc", choices=list(BOOKS), help="print chapter map")
    ap.add_argument("--loose", action="store_true",
                    help="tolerate OCR spaces inside words (LEVEL -> L E V E L)")
    args = ap.parse_args()

    if args.loose and args.query:
        # OCR sprays spaces through words: "LE VE L b: ROVI NG", "Po uch".
        # Allow optional whitespace between every literal character.
        args.query = r"\s*".join(re.escape(c) for c in args.query if not c.isspace())

    if args.toc:
        return show_toc(args.toc)
    if args.page:
        book, n = args.page
        if book not in BOOKS:
            sys.exit(f"Unknown book {book!r}; choose from {', '.join(BOOKS)}")
        return show_page(book, int(n))
    if not args.query:
        ap.error("give a query, --page, or --toc")

    total = 0
    for book in (args.book or DEFAULT_BOOKS):
        total += search(book, args.query, args.context, args.max)
    if not total:
        print(f"No hits for {args.query!r}.\n"
              f"Three books are OCR'd. Try, in order:\n"
              f"  --loose        tolerates spaces inside words (LE VE L b: ROVI NG)\n"
              f"  a shorter fragment, e.g. the one rarest word\n"
              f"  allow for digit/letter swaps: l/1, O/0, a/4, b/6, rn/m")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
