# 05 · El combate

El combate es la parte del juego con más reglas. También es la más fácil de aprender,
porque es un procedimiento fijo: siempre se hace lo mismo, en el mismo orden.

## El procedimiento

1. **Posiciones.** El DM establece dónde está cada uno.
2. **Initiative.** Todos tiran para ver en qué orden juegan.
3. **Turnos.** Cada uno juega su turno en ese orden. Cuando todos jugaron, terminó la
   **round** y se empieza otra desde arriba. Se repite hasta que la pelea termine.

*(SRD 2024, "The Order of Combat")*

Una **round** son unos **6 segundos** en el mundo del juego. Todo lo que pasa en una
round pasa más o menos al mismo tiempo; los turnos son una convención para ordenar el
caos.

## Initiative

Al empezar el combate, todos tiran **initiative**: un **Dexterity check**, o sea `1d20 +
tu modificador de Dexterity`. El DM tira por los monstruos — un solo tiro para un grupo
de criaturas idénticas.

Se ordena de **mayor a menor** y ese orden **se mantiene igual toda la pelea**.

**Empates:** entre monstruos decide el DM, entre personajes deciden los jugadores, y si
el empate es entre un monstruo y un personaje decide el DM.

**Surprise.** Si te agarran por sorpresa, tienes **disadvantage en tu tiro de
initiative**. Eso es todo — en las reglas 2024 la sorpresa ya **no** te hace perder un
turno entero como en 2014.

## Tu turno

En tu turno tienes:

```
        Movimiento (hasta tu Speed)   +   1 action
```

Y además, si algo te lo da: **1 Bonus Action**. Y en el turno de cualquiera: **1
Reaction**.

Eliges si te mueves primero o actúas primero — y puedes **partir tu movimiento**: caminar
10 feet, atacar, y caminar los otros 20.

**Hablar es gratis.** Frases cortas y gestos no gastan nada. Un discurso completo o
convencer a alguien sí requiere una action (la action **Influence**).

**Una interacción con un objeto es gratis** por turno, durante tu movimiento o tu acción:
abrir una puerta mientras corres, sacar un arma, tomar la antorcha. La **segunda**
interacción requiere la action **Utilize**.

**Puedes no hacer nada.** Si no se te ocurre qué hacer, considera **Dodge** (defensivo) o
**Ready** (esperar un gatillo).

Las acciones disponibles están en la tabla de
[04 · Cómo se juega](04-como-se-juega.md#las-acciones).

## Atacar

Estructura de todo ataque *(SRD 2024, "Making an Attack")*:

1. **Elige un objetivo** dentro del alcance.
2. **Determina modificadores.** El DM ve si el objetivo tiene **cover** y si tienes
   advantage o disadvantage.
3. **Resuelve.** Tira el attack roll. Si pegas, tiras el daño.

### El attack roll

```
        1d20  +  ability modifier  +  proficiency bonus   ≥   AC del objetivo
```

- **Melee con arma** → Strength. **A distancia con arma** → Dexterity.
- Armas con **Finesse** (dagger, rapier, shortsword) → eliges STR o DEX.
- **Spell attack** → la ability de tu class.
- El **proficiency bonus** se suma si sabes usar esa arma. Con spells, siempre.

**20 natural** = pegas sí o sí, y es **Critical Hit**. **1 natural** = fallas sí o sí.

### El daño

Si pegas, tiras el daño que dice el arma y le sumas **el mismo ability modifier que
usaste para el attack roll**. Una longsword empuñada por alguien con STR +3 hace
`1d8 + 3`.

Detalle de daño, tipos, resistencias y críticos en
[06 · Daño, curación y descanso](06-danio-y-descanso.md).

### Melee y reach

Un ataque melee alcanza a lo que esté dentro de tu **reach**, que normalmente es **5
feet**. Algunas criaturas grandes tienen más; lo dice su statblock.

### A distancia

Cada arma a distancia tiene dos números, por ejemplo `80/320 feet`:

- Hasta **80 feet**: tiro normal.
- Entre 80 y **320 feet**: tiras con **disadvantage**.
- Más allá de 320: no puedes.

## Moverse

Tu **Speed** es cuánto puedes recorrer en tu turno. En un mapa cuadriculado, **1 cuadro =
5 feet**.

**Difficult terrain** (escombros, nieve, maleza, escaleras empinadas): cada pie de
movimiento cuesta **1 pie extra**. En la práctica, avanzas la mitad. No se acumula: dos
cosas difíciles en el mismo espacio siguen costando el doble, no el cuádruple.

**Tirarte al suelo** (darte la condition Prone) es gratis, no gasta acción ni movimiento.
**Pararte de nuevo** cuesta **la mitad de tu Speed**.

**Pasar por el lado de otros.** Puedes atravesar el espacio de un aliado, de una criatura
Incapacitated, de una criatura Tiny, o de una que sea dos tamaños más grande o más chica
que tú. El espacio de otra criatura es difficult terrain para ti, salvo que sea aliada o
Tiny. **No puedes terminar tu movimiento en el espacio de otro.**

### Opportunity attacks

La Reaction más común del juego:

> Puedes hacer una **Opportunity Attack** cuando una criatura **que puedes ver** sale de
> tu **reach** usando su acción, su Bonus Action, su Reaction o su movimiento. Gastas tu
> **Reaction** para hacer **un** ataque melee con arma o Unarmed Strike contra ella. El
> ataque ocurre justo **antes** de que salga de tu alcance.
>
> *(PHB 2024, glosario)*

Cómo **no** provocarla:

- Tomar la action **Disengage**.
- Teleportarte.
- Ser movido sin usar tu movimiento, acción, Bonus Action o Reaction — si una explosión
  te lanza por los aires, o si te caes pasando al lado del enemigo, no provocas nada.

Y ojo: **acercarte no provoca nada**. Solo alejarte. Moverte *alrededor* de un enemigo
sin salir de sus 5 feet tampoco provoca.

## Cover

Paredes, árboles, otras criaturas: todo eso puede tapar al objetivo.

**Cover** *(SRD 2024)*

| Grado | Beneficio para el objetivo | Lo da… |
|---|---|---|
| **Half** | +2 a la AC y a los Dexterity saving throws | Otra criatura, o un objeto que cubra al menos la mitad |
| **Three-Quarters** | +5 a la AC y a los Dexterity saving throws | Un objeto que cubra al menos tres cuartos |
| **Total** | No puede ser objetivo directo | Un objeto que lo cubra entero |

Solo aplica **el grado más protector**, no se suman. Y solo cuenta si el ataque viene del
lado opuesto de la cobertura.

## Atacar sin ver

- Si atacas a algo que **no puedes ver**: **disadvantage**. Y si no está donde apuntaste,
  fallas automáticamente.
- Si una criatura **no puede verte a ti**: tienes **advantage** contra ella.
- Si estabas escondido y atacas, **delatas tu posición** — pegues o falles.

## Cómo termina el combate

Cuando un lado es derrotado: muerto, noqueado, rendido o arrancado. O cuando ambos lados
acuerdan parar.

**Rendirse, negociar y arrancar son jugadas válidas.** Los monstruos también las usan.

## Un turno completo, de principio a fin

> **DM:** Turno de Brenna. Hay dos goblins: uno a 15 feet frente a ti, otro arriba de la
> viga con un shortbow.
>
> **Jugadora:** Corro hacia el del suelo y lo ataco con la longsword.
>
> **DM:** 15 feet, te queda movimiento de sobra. Tira el ataque.
>
> **Jugadora:** *(1d20)* 16... más 5. **Veintiuno**.
>
> **DM:** La AC del goblin es 15. Le pegaste. Tira el daño.
>
> **Jugadora:** *(1d8)* 6... más 3. **Nueve de slashing.**
>
> **DM:** Nueve. El goblin tenía 10 HP, o sea que queda vivo por un pelo y muy asustado.
> Te quedan 15 feet de movimiento y ya usaste tu action. ¿Algo más?
>
> **Jugadora:** Me quedo ahí. Fin de turno.
>
> **DM:** El goblin herido usa **Nimble Escape** para Disengage y arranca hacia la
> escalera. Como hizo Disengage, **no** provocas Opportunity Attack.

---

**Anterior:** [04 · Cómo se juega](04-como-se-juega.md) · **Siguiente:** [06 · Daño, curación y descanso](06-danio-y-descanso.md)
