# Book sources and how much to trust them

Read this before quoting anything from the books. Three of the four are OCR'd, and this
repo is read by beginners who cannot tell a typo from a rule — a wrong number here is
worse than no number.

## The sources, in order of authority

**1. The DMG text.** Clean, native, English. Trustworthy for both prose and numbers.
This is the one book you can quote tables from directly — the XP budget table in
`one-shot/` came from here.

**2. The PHB text.** English, OCR'd. Prose is good; numbers are not guaranteed — the OCR
sprays spaces through words and swaps digits (`LE VE L b: ROVI NG` is `LEVEL 6: ROVING`).
Good for rules *descriptions* — the 2024 Actions table and the Short/Long Rest glossary
entries both came from here — but cross-check every value against the rendered page.

**3. The MM text.** OCR'd from a scan, and **the numbers are corrupted**. Use it for
lore, habitat, behaviour and flavour — never for mechanics.

**4. The PDF page, rendered as an image.** The definitive check whenever a number
matters and the source is OCR'd — but it needs poppler installed, and it goes through a
PNG rather than the Read tool. See "Reading a page for real" below before relying on it.

## The books

| Key | File | Quality |
|---|---|---|
| `phb` | `PHB_2024.pdf` — 387 pages | English, OCR, good prose / soft numbers |
| `dmg` | `Guia del Dungeon Mater (Ingles-DnDBeyond).pdf` — 470 pages | English, clean native text |
| `mm`  | `Manual de Monstruos - Ingles.pdf` — 391 pages | English, OCR, poor |
| `phb-es` | `Manual del Jugador 2024.pdf` — 389 pages | Spanish, OCR — opt-in only |

`phb-es` is the Spanish PHB. It is **not** searched by default, because it duplicates `phb`
for English queries. Reach for it with `-b phb-es` for one thing only: when you want the
official Spanish wording of a term for reader-facing text. It does not answer English
search terms — its class names are `Bárbaro`, `Explorador` (Ranger), `Pícaro`, `Brujo`,
and so on.

The books live in a directory **alongside** the repo, not inside it — they're copyrighted
and must never be committed:

```
Desktop/
  DnD_dummies/  <- this repo
  Dnd Books/    <- the PDFs, plus extracted text in _text/
```

Both tools resolve that location relative to their own file, so they work from any working
directory and on any machine that reproduces the layout. Set the `DND_BOOKS` environment
variable to point somewhere else.

Never copy book text into the repo. Cite it, don't reproduce it wholesale. This matters
more here than in a private campaign repo: `DnD_dummies` is a public GitHub repo.

## Searching

```bash
python .claude/tools/booksearch.py "spirit guardians"        # phb + dmg + mm
python .claude/tools/booksearch.py -b dmg -C 8 "chase"       # one book, more context
python .claude/tools/booksearch.py --loose "LEVEL 6"         # tolerate OCR spacing
python .claude/tools/booksearch.py --page mm 147             # dump one page
python .claude/tools/booksearch.py --toc dmg                 # chapter map
```

The query is a regex. When a search comes back empty in an OCR'd book, it is usually the
OCR's fault and not yours — reach for `--loose`, which allows optional whitespace between
every character and recovers things like `Rov ing` and `ROVI NG`. Failing that, search the
single rarest word rather than a phrase.

Hits are reported as `BOOK pdf-page N`. That N is the index of the page **within the PDF
file**, not the printed page number in the page corner — the two differ, and the printed
numbers don't extract reliably. Always cite the PDF page, and say so: "MM, PDF p.147".

**Reader-facing citations are different.** A beginner holding a paper PHB can't use a PDF
page index. In `guia/` and `one-shot/`, cite the chapter — "PHB 2024, cap. 1" — not the PDF
page. Keep PDF pages for your own verification and for notes to the repo's maintainer.

## Reading a page for real

`booksearch.py` finds *where* something is. When you need to read it **accurately**,
rasterise that page to a PNG and read the image:

```bash
mkdir -p /tmp/dnd-pages
pdftoppm -f 147 -l 147 -r 150 -png "<books dir>/Manual de Monstruos - Ingles.pdf" /tmp/dnd-pages/mm
# then Read the mm-*.png it wrote
```

`mmindex.py` prints this command ready to paste, with the absolute paths already filled
in — use that rather than hand-writing them. For the other books, resolve `<books dir>`
the way the tools do: `DND_BOOKS` if set, otherwise `Dnd Books/` alongside the repo. Set
`DND_RENDER_DIR` to put the PNGs in your session scratchpad instead of the temp dir.

**Don't pass the PDFs to the Read tool directly.** Two things break it, and the second one
is permanent:

- Rendering needs **poppler** (`pdftoppm`) on PATH. `pdftotext` — which is what produced
  `_text/` — often ships without it, so check with `command -v pdftoppm` before trusting
  this path. On Windows, Git Bash's `/mingw64/bin` typically has `pdftotext` but **not**
  `pdftoppm`; install poppler (`scoop install poppler`, `choco install poppler`) to get it.
- The Monster Manual scan is **~315 MB**, over the Read tool's 100 MB ceiling. Read refuses
  it outright no matter what else is installed. `pdftoppm` has no such limit, which is why
  the recipe above goes through a PNG.

This is the escape hatch for the Monster Manual: locate the entry, render the page, read
the statblock off the image. Render a small range — a couple of pages, not twenty.

**If poppler isn't installed and you can't install it, you cannot verify an MM number.**
Say so and leave the number out rather than transcribing it from the OCR text.

## Finding a monster by name

**Do not grep the MM for a monster's name.** Entry headings are small caps and the OCR
destroys them — `BeNsnnn` is BANSHEE, `BucsnARS` is BUGBEARS, `BenrcuRA` is BARLGURA. Use
the index instead:

```bash
python .claude/tools/mmindex.py "displacer beast"   # -> pdf p.101
python .claude/tools/mmindex.py --list go           # browse a prefix
python .claude/tools/mmindex.py --rebuild           # after re-extracting the MM
```

It is built from the book's own A–Z listing (412 entries) and matches through OCR damage,
so `Doppe19an9er`, `Mind F1ayer` and `Displacer Rea <t` all resolve from clean queries.
When a name is mangled past recognition even there, it interpolates from alphabetical
position and reports a page bracket guaranteed to contain the entry.

Pages are accurate to about ±1, because full-page art shifts the alignment between printed
and PDF numbering. Render a small range, not a single page.

## What OCR does to numbers

Real examples pulled from the extracted Monster Manual:

| Printed | OCR produced |
|---|---|
| `XP 10` | `XP l0` |
| `HP 323 (34d8 + 170)` | `HP 323 (3ad8 + 170)` |
| `Truesight 120 ft.` | `Truesight .l20 ft.` |
| `Athletics +13` | `Athletics +1 3` |
| `2/Day Each` | `2lDay Each` |
| `range 20/60 ft.` | `range 20160 ft.` |
| `7 (3d4)` | `7 (3da)` |
| `LEVEL 6: ROVING` (PHB) | `LE VE L b: ROVI NG` |
| `Level 1 Spell` (PHB) | `Level 1Spell` |

`l`↔`1`, `O`↔`0`, `a`↔`4`, `b`↔`6`, `/`↔`1`, `rn`↔`m`, plus stray spaces inside and
missing spaces between words. The DMG's XP budget table extracts with its three columns
interleaved out of order — realign it against a row you can sanity-check before using it.

**So: never state a number that came only from OCR'd text.** Confirm it by rendering the
page. If you genuinely can't confirm it, leave it out — a beginner will copy whatever you
write straight onto their character sheet.

## Language

Per `CLAUDE.md`: reader-facing content is Chilean Spanish, but **D&D mechanical terms stay
in English** — spell, saving throw, DC, AC, HP, CR, condition and class names.

All four books answer English search terms, so this is mostly friction-free. The one
trap: if you deliberately consult `phb-es` for Spanish phrasing, translate the mechanical
terms back to English before writing them into `guia/` (`dote` → feat, `tirada de
salvación` → saving throw, `estado` → condition, `conjuro` → spell). Prose around the
mechanics stays Spanish; the mechanical nouns do not.
