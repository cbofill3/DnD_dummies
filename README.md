# D&D para novatos

Una guía para aprender a jugar **Dungeons & Dragons** desde cero, en castellano, con una
aventura corta lista para jugar y cuatro personajes ya armados.

**No necesitas los libros. No necesitas saber nada.** Con dados y un par de amigos te
sobra — y si te falta cualquiera de las dos cosas,
[Claude te dirige la partida](#jugar-con-claude).

Usa el **ruleset 2024** (el que también llaman 5.5e).

---

## Jugar con Claude

Si tienes [Claude Code](https://claude.com/claude-code) instalado, no necesitas leer nada
ni buscar con quién jugar. Abre este repo y escribe:

```
/play
```

Claude te pregunta qué necesitas y toma el camino que corresponda:

| Comando | Qué hace |
|---|---|
| `/play` | La puerta de entrada. Si no sabes por dónde empezar, parte acá |
| `/learn` | Te enseña las reglas de a una, con tiradas de práctica |
| `/dm` | **Claude dirige *La Rueda Rota* para ti.** Puedes jugar solo |

Funciona con dados de verdad o sin ninguno — si no tienes, Claude tira por ti y te dice
qué salió. Y si prefieres jugar con amigos y que dirija una persona, el repo está escrito
para eso desde el principio: anda a [Cómo dirigir esto](one-shot/README.md).

---

## Por dónde parto

| Si eres… | Anda a |
|---|---|
| **Jugador, nunca has jugado** | [00 · Qué es D&D](guia/00-que-es-dnd.md), y sigue en orden |
| **Jugador, con la partida el viernes** | [10 · Chuleta](guia/10-chuleta.md) y tu [personaje](personajes/README.md) |
| **El que va a dirigir** | [Cómo dirigir esto](one-shot/README.md) |
| **Alguien buscando una regla puntual** | [09 · Glosario](guia/09-glosario.md) o la [chuleta](guia/10-chuleta.md) |
| **Solo, sin grupo y sin dados** | [Jugar con Claude](#jugar-con-claude) — escribe `/play` |

---

## La guía

Once capítulos, en orden de lectura. Cada uno agrega una sola idea nueva. Los tres últimos
(08, 09 y 10) son de consulta: no se leen de corrido, se tienen abiertos en la mesa.

| # | Capítulo | De qué se trata |
|---|---|---|
| 00 | [Qué es D&D](guia/00-que-es-dnd.md) | Quién es quién, el bucle del juego, qué se necesita |
| 01 | [Los dados](guia/01-los-dados.md) | Los siete dados y cómo se lee `2d6 + 3` |
| 02 | [La prueba de d20](guia/02-la-prueba-d20.md) | **El motor del juego.** Checks, saves, ataques, DC, advantage |
| 03 | [Tu personaje](guia/03-tu-personaje.md) | Cómo leer la hoja: abilities, HP, AC, proficiency |
| 04 | [Cómo se juega](guia/04-como-se-juega.md) | Las acciones, hablar con NPCs, explorar |
| 05 | [El combate](guia/05-el-combate.md) | Initiative, turnos, atacar, moverse, cover |
| 06 | [Daño, curación y descanso](guia/06-danio-y-descanso.md) | Daño, críticos, llegar a 0 HP, curarse, descansos |
| 07 | [La magia](guia/07-la-magia.md) | Cantrips, spell slots, concentration |
| 08 | [Las conditions](guia/08-conditions.md) | Las 15 conditions, para tener abierta en la mesa |
| 09 | [Glosario](guia/09-glosario.md) | Inglés ↔ castellano de todos los términos |
| 10 | [Chuleta](guia/10-chuleta.md) | **Una página, para imprimir** |

Si solo vas a leer un capítulo antes de tu primera partida, que sea el
**[02](guia/02-la-prueba-d20.md)**. Todo lo demás son detalles de ese.

---

## La aventura

**[La Rueda Rota](one-shot/aventura.md)** — unas 3 horas, para 1–6 personajes de nivel 1
(escrita para 4, y se ajusta).

El molino del pueblo dejó de girar y el molinero no volvió. Hay goblins adentro, pero no
vinieron a saquear: su madriguera se inundó.

| | |
|---|---|
| [**Cómo dirigir esto**](one-shot/README.md) | Curso rápido para quien nunca ha sido DM. Quince minutos |
| [**La aventura**](one-shot/aventura.md) | Cuatro escenas, ordenadas para enseñar una regla cada una |
| [**Statblocks**](one-shot/statblocks.md) | Los monstruos y la matemática honesta del encuentro |

Se puede terminar **sin pelear**. Los goblins negocian si alguien lo intenta.

---

## Los personajes

Cuatro hojas de **nivel 1** listas para imprimir, con todo calculado. Elige una y juega.

Si van a jugar **una o dos personas**, lleven **dos personajes cada uno** — y que uno sea
Vera. El [por qué está acá](one-shot/statblocks.md#con-uno-o-dos-jugadores).

| Personaje | Class | HP | AC | Qué hace |
|---|---|---|---|---|
| [Borin Pedernal](personajes/borin-fighter.md) | Fighter (Dwarf) | 13 | 17 | Aguanta y pega fuerte |
| [Pip Rastrojo](personajes/pip-rogue.md) | Rogue (Halfling) | 10 | 14 | Daño, sigilo, cerraduras |
| [Vera Ceniza](personajes/vera-cleric.md) | Cleric (Human) | 10 | 16 | Cura, apoya, habla |
| [Ilweth Rama-de-Plata](personajes/ilweth-wizard.md) | Wizard (Elf) | 8 | 12 | Magia, saber, resolver |

**Si nunca has jugado, toma a Borin.** Detalle en [personajes/](personajes/README.md).

---

## Dos cosas antes de empezar

**Los términos mecánicos están en inglés a propósito** — *saving throw*, *DC*, *AC*, *HP*,
*spell*, los nombres de las classes y de las conditions. Es porque los libros, las apps y
todo lo que vas a encontrar buscando están en inglés, y aprender el término local te deja
sin poder buscar nada. El [glosario](guia/09-glosario.md) traduce todo.

**Esto enseña las reglas 2024.** Si buscas cosas en internet te vas a topar con material
de 2014, que se parece pero no es igual — cambiaron las conditions, los backgrounds y
varias acciones. Cuando algo cambió, acá te enseñamos solo la versión nueva.

---

## Licencia y contribuciones

Esto es [CC BY-NC-SA 4.0](LICENSE): puedes compartirlo y adaptarlo sin fines
comerciales, dando crédito y manteniendo la misma licencia. Úsalo en tu mesa, imprímelo,
forkéalo y cámbialo.

Las reglas, statblocks y spells provienen del **System Reference Document 5.2** de
Wizards of the Coast — el SRD de las reglas 2024, que en la guía citamos como
*"SRD 2024"* —, disponible bajo licencia
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Este repo no está afiliado a
Wizards of the Coast ni cuenta con su respaldo.

**El repo no acepta contribuciones externas** — es material de enseñanza de un solo
autor y los pull requests se cierran solos. Si encontraste un error, arréglalo en tu
fork. Detalle en [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Para quien mantenga este repo

Las convenciones (qué se cita, qué idioma va dónde, cómo se verifica un número antes de
escribirlo) están en [`CLAUDE.md`](CLAUDE.md).

Los comandos `/play`, `/learn` y `/dm` son skills en `.claude/skills/`, y viajan con el
repo: quien lo clone los tiene sin instalar nada. Están escritas en inglés a propósito
—son instrucciones, no material de mesa— pero le hablan al jugador en castellano. La
matemática de encuentros no está duplicada en ellas: la leen de
[`one-shot/statblocks.md`](one-shot/statblocks.md), que es la única fuente.

Las reglas se verifican contra los libros con `.claude/tools/booksearch.py`,
renderizando la página real cuando el número importa. Los libros viven
**afuera** del repo, en un directorio `Dnd Books/` al lado, porque tienen copyright y
esto es un repo público. Cuánto se puede confiar en cada fuente está en
[`.claude/reference/books.md`](.claude/reference/books.md) — **lectura obligatoria antes
de citar un libro**, porque tres de los cuatro están OCR'd y sus números vienen corruptos
de formas documentadas.
