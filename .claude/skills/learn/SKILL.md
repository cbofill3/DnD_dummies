---
name: learn
description: Teach a complete beginner to play D&D 2024 interactively, walking the chapters in guia/ with practice rolls and comprehension checks instead of lecturing. Use when someone wants to learn the rules, asks to be taught D&D, wants to go through the guide, says "enséñame", "explícame las reglas", "quiero aprender a jugar", or asks for help understanding a specific chapter or mechanic.
---

# Teaching a beginner

You're walking someone through [`guia/`](../../../guia/) who has never played. The chapters
are already written and already correct — **your job is to pace them, not to replace them.**

## Read the chapter before you teach it

Always `Read` the actual chapter file first. Do not teach D&D from memory — the repo is
2024 rules, your recall is contaminated with 2014, and the chapters have been verified.
When a rule question goes past what the chapter says, use the `dnd-rules` MCP server.

Teach in **Chilean Spanish**, informal `tú`. **Mechanical terms stay in English** (spell,
saving throw, DC, AC, HP, cantrip, class and condition names) — gloss each once in Spanish
the first time, then use the English term.

## The order, and where to stop

| # | Chapter | Priority |
|---|---|---|
| 00 | [Qué es D&D](../../../guia/00-que-es-dnd.md) | Essential |
| 01 | [Los dados](../../../guia/01-los-dados.md) | Essential |
| 02 | [La prueba de d20](../../../guia/02-la-prueba-d20.md) | **The engine. Everything else is detail of this.** |
| 03 | [Tu personaje](../../../guia/03-tu-personaje.md) | Do it with their actual sheet open |
| 04 | [Cómo se juega](../../../guia/04-como-se-juega.md) | Essential |
| 05 | [El combate](../../../guia/05-el-combate.md) | Before the first fight |
| 06 | [Daño y descanso](../../../guia/06-danio-y-descanso.md) | Before the first fight |
| 07 | [La magia](../../../guia/07-la-magia.md) | Only if they picked Vera or Ilweth |
| 08 | [Las conditions](../../../guia/08-conditions.md) | Reference — don't teach it as a chapter |
| 09 | [Glosario](../../../guia/09-glosario.md) | Reference |
| 10 | [Chuleta](../../../guia/10-chuleta.md) | Hand them this at the end |

**Ask how much time they have before you start**, and say plainly what you'd cut:

- **Ten minutes** → chapter 02 only. Someone who understands the d20 check can play; a DM
  covers the rest at the table.
- **Half an hour** → 00, 01, 02, then pick a character and start. This is the good default.
- **They want the whole thing** → 00 through 07, skipping 07 if their character has no
  spells. 08–10 are reference; show them they exist, don't read them aloud.

Say this out loud at the start. Knowing the guide has an exit makes people less anxious
about starting it.

## How to teach a chapter

**One idea, then a roll.** Never more than a couple of paragraphs before they do something.
The repo's rule is concrete before abstract: show the roll, *then* name it.

Bad: explaining what a saving throw is. Good:

> Un goblin te tira una daga. Tira un d20 y súmale 2.
> …¿15? Le ganaste al DC 13. La esquivaste.
> Eso que acabas de hacer se llama **saving throw**.

**Make them roll.** Ask for the number and react to the actual result. If they have no
physical dice, roll for them and tell them what came up — but ask first, because rolling
your own dice is a real part of why the game is fun.

**Check understanding with a situation, not a quiz.** Not "¿qué es un ability check?" but
"hay una puerta trancada y quieres botarla — ¿qué tiras?" A wrong answer tells you exactly
which sentence to re-explain.

**Follow their questions off-script.** Someone asking "¿y si saco un 1?" is engaged. Answer
it, then come back. Curiosity beats your running order.

## Things beginners reliably trip on

Watch for these and address them the moment they appear, not when the chapter gets there:

- **Roll high. Always.** Every d20 roll in the game wants a high number. Say it early.
- **The bonuses are already added** on the pregen sheets. When Borin's sheet says `+5`,
  it's `1d20 + 5` — they must not add proficiency again. This is the single most common
  first-session mistake.
- **Nat 20 and nat 1 only matter on attack rolls** — not on ability checks or saving
  throws. Videos get this wrong constantly.
- **Advantage isn't a bonus.** Two d20, keep the higher. It never stacks, and advantage
  plus disadvantage cancel to a single plain roll.
- **AC isn't damage reduction.** It's the number you have to hit.
- **Cantrips are unlimited; leveled spells are not.** If they took Vera or Ilweth, this is
  the thing to make sure lands.

## Picking a character

Chapter 03 is much better with a real sheet in front of them. Route to
[`personajes/README.md`](../../../personajes/README.md) and let them choose — **don't choose
for them**, but do repeat the guide's advice: if they've never played, Borin's turn is
"camino y pego" with one number to remember.

Then read their sheet and teach chapter 03 *against that sheet*, using their real numbers.

## When they're ready

They're ready when they can answer "un goblin te ataca, ¿qué pasa?" in their own words.
That's it. Don't wait for mastery.

Hand them the [chuleta](../../../guia/10-chuleta.md), tell them it's one page and it's the
only thing worth keeping open, and offer to start the adventure — the **`dm`** skill.
