# Book sources and how much to trust them

Read this before quoting anything from the books. Three of the four are OCR'd, and this
repo is read by beginners who cannot tell a typo from a rule — a wrong number here is
worse than no number.

## The sources, in order of authority

**1. `dnd-rules` MCP server (Open5e, 2024 SRD).** The only source whose *numbers* are
machine-exact. Use it first for any statblock, spell, condition, magic item, or class
feature that exists in the SRD. Tools: `dnd_get_spell`, `dnd_get_creature`,
`dnd_search_creatures`, `dnd_get_magic_item`, `dnd_get_condition`, `dnd_get_rule`, etc.

### Reading MCP responses correctly

The MCP returns **several editions in one payload**, and its top-level labels lie. A
`dnd_get_condition("Frightened")` response carries a `descriptions` array with three
entries, while the top-level `gamesystem` reads `5th Edition 2014`:

| `document` / `gamesystem` | What it actually is | Use it? |
|---|---|---|
| `srd-2024` / `5e-2024` | 2024 SRD — this repo's default | **Yes** |
| `srd-2014` / `5e-2014` | 2014 SRD | Only as labelled **[2014]** fallback |
| `a5e-ag` / `a5e` | *Level Up: Advanced 5e* — a **different game** | **Never** |

So:

- **Pick the `srd-2024` entry out of `descriptions[]`.** Don't take the first one, and
  don't read the top-level `gamesystem` as the answer's edition — it frequently says 2014
  even when a 2024 description is present.
- **`a5e` is not D&D.** It's a separate publisher's system, and teaching its rules to a
  beginner would leave them unable to play at a real table.
- If only `srd-2014` exists, that's a genuine 2014 fallback: use it and label it
  **[2014]**, per `CLAUDE.md`.

**2. The DMG text.** Clean, native, English. Trustworthy for both prose and numbers.
This is the one book you can quote tables from directly — the XP budget table in
`one-shot/` came from here.

**3. The PHB text.** English, OCR'd. Prose is good; numbers are not guaranteed — the OCR
sprays spaces through words and swaps digits (`LE VE L b: ROVI NG` is `LEVEL 6: ROVING`).
Good for rules *descriptions* — the 2024 Actions table and the Short/Long Rest glossary
entries both came from here — but cross-check every value against the MCP or the
rendered page.

**4. The MM text.** OCR'd from a scan, and **the numbers are corrupted**. Use it for
lore, habitat, behaviour and flavour — never for mechanics.

**5. The PDF page, rendered as an image.** The fallback when a number matters, the SRD
doesn't have it, and the OCR is garbage. See "Reading a page for real" below.

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

`booksearch.py` finds *where* something is. When you need to read it accurately, pass that
page to the Read tool and it renders the actual page as an image:

```
Read(file_path="<books dir>/Manual de Monstruos - Ingles.pdf", pages="147")
```

The Read tool needs an **absolute** path, and the books directory differs per machine — so
don't hand-write it. `mmindex.py` prints a ready-to-paste `Read(...)` call with the correct
absolute path already filled in; use that. For the other books, resolve `<books dir>` the
same way the tools do: the `DND_BOOKS` environment variable if set, otherwise `Dnd Books/`
alongside the repo.

This is the escape hatch for the Monster Manual. Locate the entry, then render the page to
read its statblock correctly. Max 20 pages per request.

## Finding a monster by name

**Do not grep the MM for a monster's name.** Entry headings are small caps and the OCR
destroys them — `BeNsnnn` is BANSHEE, `BucsnARS` is BUGBEARS, `BenrcuRA` is BARLGURA. Use
the index instead:

```bash
python .claude/tools/mmindex.py "displacer beast"   # -> pdf p.101
python .claude/tools/mmindex.py --list gl           # browse a prefix
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

**So: never state a number that came only from OCR'd text.** Confirm it via the MCP or by
rendering the page. If you genuinely can't confirm it, leave it out — a beginner will
copy whatever you write straight onto their character sheet.

## Language

Per `CLAUDE.md`: reader-facing content is Chilean Spanish, but **D&D mechanical terms stay
in English** — spell, saving throw, DC, AC, HP, CR, condition and class names.

All four books answer English search terms, so this is mostly friction-free. The one
trap: if you deliberately consult `phb-es` for Spanish phrasing, translate the mechanical
terms back to English before writing them into `guia/` (`dote` → feat, `tirada de
salvación` → saving throw, `estado` → condition, `conjuro` → spell). Prose around the
mechanics stays Spanish; the mechanical nouns do not.
