# Repo Conventions

This is a **teaching repo**: a "how to play D&D" guide for people who have never
played, plus a starter one-shot to learn on. It is not a campaign. Nothing here is
canon for any table — it's the on-ramp.

Ruleset: **2024 (5.5e)**. No house rules. If a house rule would be needed, that's a
sign the guide is explaining too much.

## Layout

| Path | Holds |
|---|---|
| `guia/` | The learn-to-play chapters, numbered in reading order |
| `one-shot/` | *La Rueda Rota* — a ~3 hour adventure for level 1 |
| `personajes/` | Pregenerated level-1 characters, ready to print and play |
| `.claude/skills/` | `/play`, `/learn`, `/dm` — how Claude runs the repo for a reader |
| `.claude/reference/` | How much to trust each rulebook — read before quoting one |
| `.claude/tools/` | Book search and Monster Manual page lookup |

The skills are **reader-facing at runtime but maintainer-facing as files**: written in
English like everything else under `.claude/`, but they speak Chilean Spanish to the
player. They must not restate rules or encounter math that already live in `guia/` or
`one-shot/` — they read those files instead, so there is one source and it's the one a
human can read.

## Rules handling

- **2024 SRD is the default** for every stat, spell, monster, and subsystem.
- When a rule changed between 2014 and 2024, this repo teaches **2024 only**. Don't
  mention the 2014 version unless a reader would otherwise be confused by an older
  video or book they've found — and label it **[2014]** when you do.
- Never invent a rule and present it as official. A simplification made for teaching
  is fine, but say so in the text ("acá lo simplificamos; la regla completa está en…").
- **Look rules up, don't recall them.** Model recall mixes 2014 and 2024 rules. Verify
  any spell, statblock, condition, or magic item against the books (below) before
  writing it down; during play, the repo's own verified files are the source.
- **The full books cover what the SRD doesn't.** The PHB, DMG and MM live in a
  `Dnd Books/` directory sitting **alongside** this repo — never inside it, because
  they're copyrighted. Search them with `python .claude/tools/booksearch.py`, which
  reports PDF page numbers, and find monsters with `python .claude/tools/mmindex.py`.
  To check a number against the real page, rasterise it with `pdftoppm` and read the
  PNG — the Read tool can't open these PDFs directly. Both tools print the command.
  **`.claude/reference/books.md` is required reading before quoting any book** — three
  of the four are OCR'd and their numbers are corrupted in specific, documented ways.
  Book text never gets committed to this repo; it's copyrighted.

## Content rules

- **Reader-facing content is written in Chilean Spanish.** Everything in `guia/`,
  `one-shot/` and `personajes/` is Spanish. **D&D mechanical terms stay in English** —
  spell, cantrip, saving throw, DC, AC, HP, CR, XP, class names, condition names,
  statblock terms — because the table plays with English books, and everything a reader
  finds searching (apps, videos, the books themselves) is in English.
- The first time a mechanical term appears in a chapter, gloss it once in Spanish and
  then use the English term from there on. `guia/09-glosario.md` is the full
  English↔Spanish list; link to it rather than re-glossing everywhere.
- This file and everything under `.claude/` stay in English. They're instructions, not
  table material. `README.md` is Spanish — it's the reader's front door.
- Everything is Markdown. Directory and file names stay English-ish `kebab-case`;
  they're identifiers.
- Cross-reference with relative links (`[el combate](05-el-combate.md)`) so a reader
  who lands mid-guide can find their way.

## Writing style

The audience has **never played**. That is the whole design constraint.

- **One new idea at a time**, and always the concrete before the abstract: show the
  roll, then name it.
- **No jargon before it's defined.** If a chapter needs a term from a later chapter,
  either move the term earlier or explain it inline.
- **Assume no books.** A reader with this repo, dice, and a friend should be able to
  play. Anything that requires the PHB is a bug in the guide, not a prerequisite.
- Cite where the full rule lives (`PHB 2024, cap. 1`) so a curious reader can go
  deeper — but never make them.
- Keep the numbers right. A beginner can't tell a typo from a rule, so a wrong DC or
  damage die does more damage here than in a campaign file. Verify before writing.
- Tables and short paragraphs beat prose. This gets read at a table with dice in hand.

## Scope

Player-side only, plus the minimum a first-time DM needs to run the included one-shot.
Deep DM craft, campaign building, homebrew and levels beyond 1 are **out of scope** —
if a section is drifting there, cut it and point at the DMG instead.
