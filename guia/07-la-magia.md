# 07 · La magia

Si tu personaje no lanza spells, puedes saltarte este capítulo y volver cuando te toque
un wizard. Si sí lanza, esta es la parte de la hoja que más asusta y menos complicada es.

## Qué es un spell

Un **spell** es un efecto mágico con una ficha técnica fija. Todos los spells se leen
igual:

```
FIRE BOLT                                   Evocation Cantrip
Casting Time: Action
Range: 120 feet
Components: V, S
Duration: Instantaneous

Lanzas una mota de fuego a una criatura u objeto dentro del rango.
Haces un ranged spell attack contra el objetivo. Si pegas, recibe
1d10 de Fire damage. Un objeto inflamable que no esté siendo usado
ni cargado empieza a arder.
```

*(SRD 2024, Fire Bolt.)*

| Línea | Qué te dice |
|---|---|
| **Level** | 0 (cantrip) hasta 9 |
| **School** | Evocation, Abjuration, Illusion… Es sabor; casi nunca cambia una regla |
| **Casting Time** | Normalmente una **Action**. A veces Bonus Action, Reaction, o minutos |
| **Range** | Qué tan lejos llega. `Touch` = tienes que tocarlo. `Self` = solo tú |
| **Components** | Qué necesitas para lanzarlo — abajo |
| **Duration** | `Instantaneous` (pasa y listo) o un tiempo, a veces con **Concentration** |

## Cantrips vs. spells con nivel

Esta es **la** distinción que tienes que tener clara.

**Cantrips** (level 0) — magia que sabes tan bien que no te cuesta nada.

- **No gastan spell slot.**
- Los puedes usar **infinitas veces**, toda la sesión, todos los días.
- Suben de potencia solos con tu nivel de personaje. Fire Bolt pasa de `1d10` a `2d10` en
  nivel 5, `3d10` en 11 y `4d10` en 17.

**Spells de nivel 1 y más arriba** — gastan un **spell slot**.

Regla práctica para tu primer personaje mágico: **el cantrip es tu ataque de todos los
turnos**; los spells con nivel son tus balas, y tienes poquísimas.

## Spell slots

Un **spell slot** es una carga. Lanzar un spell de nivel 1 gasta un slot de nivel 1.

En tu hoja hay casillas por nivel de slot. Las vas marcando al gastarlas.

- **Un wizard de nivel 1 tiene dos slots de nivel 1.** Dos. En todo el día.
- Se recuperan con un **long rest**.
- No importa qué spell lanzaste: el slot se gasta igual.

### Lanzar a un nivel más alto

Si gastas un slot **más grande** del que el spell necesita, muchos spells se ponen mejor.
Lo dice la línea *"Using a Higher-Level Spell Slot"* del spell.

*Cure Wounds* es de nivel 1 y cura `2d8 + tu spellcasting modifier`. Lanzado con un slot
de nivel 2 cura `4d8 + modificador`; de nivel 3, `6d8`; y así.

**Los cantrips nunca se lanzan a nivel más alto** — no gastan slot.

## Prepared spells

Tu class te dice cuántos spells puedes tener **preparados**. Los preparados son los que
puedes lanzar hoy; el resto de tu lista existe pero está guardado.

Se cambian al terminar un long rest. En 2024 varias classes preparan una vez y cambian
de a uno al subir de nivel — revisa tu class, porque cambió respecto a 2014.

Los **cantrips no se preparan**: los sabes siempre.

## Los tres números mágicos

En tu hoja aparecen tres, y salen de tu **spellcasting ability** (INT para wizard, WIS
para cleric y druid, CHA para bard, sorcerer, warlock y paladin):

| Número | Para qué |
|---|---|
| **Spellcasting modifier** | Se suma al daño/curación de los spells que lo digan |
| **Spell save DC** | El DC que los enemigos tienen que superar cuando tu spell les pide un saving throw |
| **Spell attack bonus** | Lo que sumas al d20 cuando tu spell requiere un attack roll |

### Attack roll o saving throw

Un spell que hace daño funciona de una de dos formas, y **el spell te dice cuál**:

- **"Make a ranged spell attack"** → tú tiras `1d20 + spell attack bonus` contra la AC.
  Fire Bolt es así.
- **"The target makes a Dexterity saving throw"** → **tú no tiras nada**. El objetivo
  tira contra tu **spell save DC**. Si falla, recibe todo; si pasa, típicamente la mitad.

Es el error más común de las mesas nuevas: tirar un d20 cuando el spell pide un save.

## Components

Qué necesitas para lanzarlo:

| Sigla | Significa | Implica |
|---|---|---|
| **V** | Verbal | Tienes que poder hablar |
| **S** | Somatic | Necesitas una mano libre |
| **M** | Material | Necesitas un ingrediente |

Para la **M**, un **Spellcasting Focus** (un bastón, un símbolo sagrado, un cristal)
reemplaza los materiales — **salvo** que el spell consuma el material o le ponga un
precio. Esos hay que tenerlos de verdad.

## Concentration

Algunos spells duran en el tiempo, pero solo mientras mantengas **Concentration**.

> **Solo puedes concentrarte en un spell a la vez.** En el momento en que empiezas a
> lanzar otro que requiere Concentration, el primero se cae.

Puedes soltarla cuando quieras, sin gastar nada. Y se rompe sola por:

- **Daño.** Cada vez que recibes daño tiras un **Constitution saving throw**. El DC es
  **10, o la mitad del daño recibido (redondeando abajo), el que sea mayor** — con un
  máximo de DC 30.
- **Quedar Incapacitated, o morir.**

*(PHB 2024, glosario, "Concentration")*

Ejemplo: estás concentrando y recibes 9 de daño → la mitad es 4, que es menos que 10, así
que el DC es **10**. Si recibes 26 → la mitad es 13, así que el DC es **13**.

## Rituals

Un spell con la etiqueta **Ritual** que tengas preparado se puede lanzar **como ritual**:
tarda **10 minutos más** de lo normal, pero **no gasta spell slot**. No se puede lanzar a
nivel más alto de esa forma.

Fuera de combate, con tiempo, es magia gratis. Úsala.

## Errores clásicos de principiante

**Guardar los slots para el momento perfecto** y terminar el día con todos sin gastar. Se
recuperan con un long rest; gástalos.

**Olvidar los cantrips.** No cuestan nada. Si dudas, tira un cantrip.

**Tirar el d20 cuando el spell pide un saving throw.** Lee la primera línea del efecto.

**Concentrar dos spells.** No se puede. Revisa si tu spell dice Concentration *antes* de
lanzar otro.

---

**Anterior:** [06 · Daño, curación y descanso](06-danio-y-descanso.md) · **Siguiente:** [08 · Las conditions](08-conditions.md)
