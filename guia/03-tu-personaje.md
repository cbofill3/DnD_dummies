# 03 · Tu personaje

Tu hoja de personaje se ve como un formulario del Registro Civil y asusta. En realidad
son **cinco cosas** que importan de verdad, y el resto son detalles que vas a mirar una
vez por sesión.

Para tu primera partida no necesitas crear un personaje: en
[`personajes/`](../personajes/) hay cuatro listos, con todo calculado. Este capítulo te
enseña a **leer** uno.

## Lo que de verdad tienes que saber

Si te aprendes solo esto, ya puedes jugar toda una sesión:

| Dato | Qué es | Cuándo lo usas |
|---|---|---|
| **HP** | Cuánto aguantas antes de caer | Cada vez que te pegan |
| **AC** | Qué tan difícil es pegarte | Cada vez que te atacan |
| **Modificadores de ability** | Los seis numeritos con + | Casi toda tirada |
| **Tu ataque** | El bonus para pegar y el daño que haces | Cada turno de combate |
| **Speed** | Cuánto te mueves en un turno | Cada turno de combate |

Todo lo demás lo puedes buscar cuando salga.

## Las seis abilities

Son las seis estadísticas base. Todo lo demás en la hoja se deriva de ellas.

| Ability | En criollo | Personaje típico que la tiene alta |
|---|---|---|
| **Strength** (STR) | Fuerza bruta | Fighter con armadura pesada, barbarian |
| **Dexterity** (DEX) | Agilidad, puntería, reflejos | Rogue, ranger, arquero |
| **Constitution** (CON) | Aguante, salud | Todos la quieren: da HP |
| **Intelligence** (INT) | Conocimiento, razonamiento | Wizard |
| **Wisdom** (WIS) | Percepción, sentido común, fuerza de voluntad | Cleric, druid |
| **Charisma** (CHA) | Presencia, labia, personalidad | Bard, sorcerer, warlock, paladin |

Cada una tiene un **score** (número de 1 a 20) y un **modificador** (el número chico con
+ o −). **El modificador es el que usas**; el score casi nunca aparece en una tirada.
La tabla de conversión está en [02 · La prueba de d20](02-la-prueba-d20.md#ability-modifier).

> **Intelligence no es Wisdom.** INT es cuánto sabes; WIS es cuánto te das cuenta. Un
> wizard con INT 18 y WIS 8 sabe todo sobre demonios y no nota que hay uno atrás.

## Proficiency bonus

Un solo número que representa entrenamiento. **A nivel 1 es +2** y sube con el nivel.

Se suma a: skills que tengas marcadas, saving throws que tu class te dé, ataques con
armas que sepas usar, y tus spells. Cuándo aplica y cuándo no está en
[02 · La prueba de d20](02-la-prueba-d20.md#proficiency-bonus).

En la hoja, las skills y los saves con proficiency vienen con el círculo o cuadrito
**relleno**. Los números que aparecen al lado ya incluyen el +2 — no lo sumes de nuevo.

## Hit Points

**HP** = *Hit Points*. Cuánto daño puedes recibir antes de caer.

- Tu **HP maximum** es tu total sano. Está impreso en la hoja.
- Tus **HP actuales** cambian todo el rato: bajan con el daño, suben curándote. Escríbelos
  con lápiz.
- A **0 HP** caes inconsciente y empiezas a jugarte la vida — ver
  [06 · Daño, curación y descanso](06-danio-y-descanso.md).

Perder HP **no te debilita**: peleas igual de bien con 3 HP que con 30. Solo importa
llegar a 0.

*(Si tienes la mitad o menos de tus HP, estás **Bloodied**. Por sí solo no hace nada;
algunas habilidades lo usan como gatillo.)*

### Hit Point Dice

Aparte de tus HP tienes **Hit Point Dice** (o **Hit Dice**), uno por nivel. Es tu
"botiquín": los gastas en un short rest para recuperar HP. El tipo de dado lo da tu
class — d6 para wizard, d10 para fighter, etc. Ver
[06 · Daño, curación y descanso](06-danio-y-descanso.md#short-rest).

## Armor Class

**AC** = *Armor Class*. Es el número que un enemigo tiene que **igualar o superar** con
su attack roll para pegarte.

Sin armadura:

```
        AC  =  10  +  tu modificador de Dexterity
```

Con armadura, la armadura reemplaza esa fórmula (una chain mail te da AC 16 fija, por
ejemplo, sin importar tu DEX). Un **shield** suma +2 encima.

*(PHB 2024, cap. 2 y cap. 6.)*

Dos cosas:

- **Solo puedes usar una fórmula base de AC.** Si una class o un spell te da otra forma
  de calcularla, eliges cuál usar, no las sumas.
- En tu hoja el número ya está calculado. Si te pones o te sacas la armadura durante la
  partida, hay que recalcularlo.

## Initiative y Speed

**Initiative** es lo que le sumas al d20 al empezar un combate, para ver el orden de los
turnos. Casi siempre es tu modificador de Dexterity, pero algunos feats lo suben — **usa
el número de Initiative de tu hoja**, que ya viene con todo sumado. Ver
[05 · El combate](05-el-combate.md).

**Speed** es cuántos pies te mueves en un turno. La mayoría de los personajes tienen
**30 feet**. Se mide en pies porque el juego es gringo; en un mapa cuadriculado, cada
cuadro son 5 feet, así que 30 feet = 6 cuadros.

## Las tres etiquetas de identidad

Arriba de la hoja hay tres palabras que definen qué es tu personaje:

**Class.** Qué *hace*. Fighter, Rogue, Cleric, Wizard, Bard… Es la etiqueta que más
afecta las reglas: da tus HP, tus proficiencies, tus features y —si corresponde— tu
magia. Tu **level** (nivel) es de tu class: empiezas en nivel 1.

**Species.** Qué *es*. Human, Elf, Dwarf, Halfling, Orc… Da rasgos chicos pero útiles:
Darkvision, resistencias, una velocidad distinta.

**Background.** De dónde *viene*. Soldier, Acolyte, Criminal, Sage… En las reglas 2024 el
background es más importante que antes: da skills, una herramienta, un idioma, equipo
inicial, y un **feat** de nivel 1.

## Equipo y ataques

La sección de ataques lista, para cada arma:

| Columna | Qué es |
|---|---|
| **Nombre** | Longsword, Shortbow, Dagger… |
| **Bonus de ataque** | Lo que sumas al d20 para pegar |
| **Daño** | Lo que tiras si pegas, ej. `1d8 + 3` |
| **Tipo** | Slashing, Piercing, Bludgeoning, Fire… |

El bonus de ataque ya viene calculado y sale de: ability modifier + proficiency bonus.
Qué ability usa cada arma:

| Ability | Tipo de ataque |
|---|---|
| Strength | Ataque melee con arma, o Unarmed Strike |
| Dexterity | Ataque a distancia con arma |
| Varía | Spell attack (lo define tu class) |

*(SRD 2024, Attack Roll Abilities.)*

**Excepción útil:** las armas con la propiedad **Finesse** (dagger, rapier, shortsword)
te dejan elegir STR **o** DEX. Un rogue con DEX alta usa DEX para pegar *y* para el daño.

## Si tu personaje tiene magia

Aparecen tres números más:

- **Spellcasting ability** — INT para wizard, WIS para cleric y druid, CHA para bard,
  sorcerer, warlock y paladin.
- **Spell save DC** — el DC que tienen que superar los enemigos cuando tu spell les pide
  un saving throw.
- **Spell attack bonus** — lo que sumas al d20 cuando tu spell requiere un attack roll.

Más los **spell slots** y la lista de spells. Todo eso en
[07 · La magia](07-la-magia.md).

## Cómo llenar tu propia hoja (después)

Para tu primera partida: usa un pregen. Cuando quieras armar el tuyo, el orden 2024 es:

1. Elegir **class**
2. Elegir **origin** (species + background)
3. Determinar **ability scores**
4. Elegir **alignment**
5. Rellenar detalles: HP, AC, initiative, equipo, nombre

*(SRD 2024, "Create Your Character"; PHB 2024, cap. 2.)*

Hazlo con alguien que ya haya jugado, o con una herramienta como D&D Beyond. Es la parte
más lenta y menos divertida de aprender, y no hay ninguna necesidad de pasarla primero.

---

**Anterior:** [02 · La prueba de d20](02-la-prueba-d20.md) · **Siguiente:** [04 · Cómo se juega](04-como-se-juega.md)
