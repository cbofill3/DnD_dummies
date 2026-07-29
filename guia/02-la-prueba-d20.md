# 02 · La prueba de d20

Todo lo incierto en D&D se resuelve igual:

```
        1d20  +  modificador   ≥   número objetivo   →   funciona
```

Las reglas 2024 le llaman a esto un **D20 Test**. Existe en **tres sabores**, y la única
diferencia real entre ellos es de dónde sale el número objetivo.

| Sabor | Cuándo | Objetivo se llama |
|---|---|---|
| **Ability check** | Intentas algo | **DC**, lo pone el DM |
| **Saving throw** | Algo te intenta a ti | **DC**, lo pone el efecto |
| **Attack roll** | Le pegas a algo | **AC** del objetivo |

Aprende esa tabla y ya entiendes el motor del juego.

## 1. Ability check — tú intentas algo

Es la tirada de "quiero hacer esto y podría salir mal": forzar una puerta trancada,
trepar un muro, recordar una leyenda, convencer al guardia.

El DM decide qué **ability** aplica y qué tan difícil es:

**Ability Check Examples** *(SRD 2024)*

| Ability | Tiras para… |
|---|---|
| Strength | Levantar, empujar, tirar o romper algo |
| Dexterity | Moverte con agilidad, rápido o en silencio |
| Constitution | Forzar tu cuerpo más allá de lo normal |
| Intelligence | Razonar o recordar |
| Wisdom | Notar cosas del entorno o en la conducta de alguien |
| Charisma | Influir, entretener o engañar |

### El DC

**DC** = *Difficulty Class*. Es el número que hay que igualar o superar. Lo pone el DM.

**Typical Difficulty Classes** *(SRD 2024)*

| Dificultad | DC |
|---|---|
| Very easy | 5 |
| Easy | 10 |
| Medium | 15 |
| Hard | 20 |
| Very hard | 25 |
| Nearly impossible | 30 |

El DM normalmente **no te dice el DC** antes de tirar. Te dice si pasó o no.

### Si no hay riesgo, no hay tirada

Esto se les olvida a las mesas nuevas y es la causa número uno de que una sesión se
arrastre. Si tu personaje quiere abrir una puerta sin llave, **la abre**. No se tira.

Se tira solo cuando el resultado es incierto **y** el fracaso lleva a algo interesante.

## 2. Saving throw — algo te intenta a ti

Un **saving throw** (o **save**) es lo mismo al revés: no eliges hacerlo, te toca. Un
dragón escupe fuego, un spell te intenta dominar, pisas una trampa de dardos envenenados.

El efecto que te ataca dice qué save es y cuál es el DC.

**Saving Throw Examples** *(SRD 2024)*

| Ability | Tiras para… |
|---|---|
| Strength | Resistir fuerza física directa |
| Dexterity | Esquivar |
| Constitution | Aguantar algo tóxico |
| Intelligence | Darte cuenta de que una ilusión es falsa |
| Wisdom | Resistir un ataque mental |
| Charisma | Afirmar tu propia identidad |

Si **no quieres** resistir el efecto (te están curando con un spell que pide save, por
ejemplo), puedes elegir fallar sin tirar.

Muchos efectos de área hacen **la mitad del daño** si pasas el save, en vez de nada. Lo
dice el efecto. La mitad se redondea hacia abajo.

## 3. Attack roll — le pegas a algo

Tiras 1d20 + modificadores contra la **AC** (*Armor Class*) del objetivo. Igual o mayor,
pegaste. Detalle completo en [05 · El combate](05-el-combate.md).

**Solo en attack rolls** pasan estas dos cosas:

- **20 natural** (el d20 muestra 20): pegas **sí o sí**, sin importar modificadores ni la
  AC. Además es un **Critical Hit**.
- **1 natural**: fallas **sí o sí**, sin importar nada.

> ⚠️ **Ojo con esto.** El 20 natural y el 1 natural automáticos son **solo para attack
> rolls**. En un ability check o en un saving throw, un 20 en el dado es simplemente 20 +
> tus modificadores; puede no alcanzar el DC. Y un 1 puede alcanzarlo si tienes buen
> bonus. Muchas mesas lo juegan mal por costumbre de 2014 o de las películas.

## El modificador: de dónde sale el número que sumas

Casi siempre son dos piezas:

```
        1d20  +  ability modifier  +  proficiency bonus (si aplica)
```

### Ability modifier

Tu personaje tiene seis **abilities** con un puntaje de 1 a 20. Ese puntaje se traduce a
un **modificador**, que es lo que realmente sumas:

| Score | Mod | Score | Mod |
|---|---|---|---|
| 1 | −5 | 16–17 | +3 |
| 2–3 | −4 | 18–19 | +4 |
| 4–5 | −3 | 20–21 | +5 |
| 6–7 | −2 | 22–23 | +6 |
| 8–9 | −1 | 24–25 | +7 |
| 10–11 | +0 | 26–27 | +8 |
| 12–13 | +1 | 28–29 | +9 |
| 14–15 | +2 | 30 | +10 |

*(SRD 2024, Ability Modifiers)*

10–11 es "persona normal", +0. Un 8 no te hace inútil, te hace un poco malo. En tu hoja
de personaje el modificador ya está calculado — es el número grande.

**Fórmula, si la quieres:** `(score − 10) ÷ 2`, redondeando hacia abajo.

### Proficiency bonus

Es un solo número que sube con tu nivel, y representa "en esto estoy entrenado". **A
nivel 1 es +2.**

Se suma **solo cuando aplica**:

- En un **ability check**, si tienes proficiency en la **skill** o la herramienta que el
  DM considera relevante.
- En un **saving throw**, si tu class te da proficiency en ese save. Cada class da al
  menos dos.
- En un **attack roll**, si tienes proficiency con esa arma, o si es un spell attack.

Y **nunca se suma dos veces** a la misma tirada, aunque haya dos razones para sumarlo.

## Skills

Una **skill** es una especialidad dentro de una ability. No cambia qué ability tiras —
cambia si sumas tu proficiency bonus.

Cuando el DM dice *"tira un **Dexterity (Stealth) check**"*, quiere decir: tira d20, suma
tu modificador de Dexterity, y suma tu proficiency bonus **si** tienes Stealth marcada en
la hoja.

**Skills** *(SRD 2024)*

| Skill | Ability | Ejemplo de uso |
|---|---|---|
| Acrobatics | Dexterity | Mantener el equilibrio, hacer una pirueta |
| Animal Handling | Wisdom | Calmar o entrenar un animal |
| Arcana | Intelligence | Recordar cosas de magia, items mágicos, los planos |
| Athletics | Strength | Saltar más lejos, nadar contra corriente, romper algo |
| Deception | Charisma | Mentir de forma convincente, disfrazarse |
| History | Intelligence | Recordar hechos históricos, pueblos, culturas |
| Insight | Wisdom | Leer el ánimo y las intenciones de alguien |
| Intimidation | Charisma | Amenazar o impresionar para conseguir algo |
| Investigation | Intelligence | Buscar datos en libros, deducir cómo funciona algo |
| Medicine | Wisdom | Diagnosticar una enfermedad, saber de qué murió alguien |
| Nature | Intelligence | Recordar cosas de terreno, plantas, animales, clima |
| Perception | Wisdom | Notar algo fácil de pasar por alto, con cualquier sentido |
| Performance | Charisma | Actuar, contar, tocar, bailar |
| Persuasion | Charisma | Convencer a alguien honestamente y con gracia |
| Religion | Intelligence | Recordar cosas de dioses, ritos, símbolos sagrados |
| Sleight of Hand | Dexterity | Robar un bolsillo, esconder un objeto, hacer trucos |
| Stealth | Dexterity | Pasar desapercibido moviéndote en silencio y escondido |
| Survival | Wisdom | Rastrear, forrajear, encontrar un camino, evitar peligros naturales |

**Insight vs. Investigation vs. Perception** es la confusión clásica:
*Perception* es **notar** (hay algo raro en esa pared). *Investigation* es **deducir**
(la pared se abre empujando el candelabro). *Insight* es **leer gente** (el alcalde te
está mintiendo).

## Advantage y disadvantage

El mejor invento de este sistema, y es simplísimo:

> **Advantage:** tira **dos** d20 y usa el **más alto**.
> **Disadvantage:** tira **dos** d20 y usa el **más bajo**.

Sirve para cualquier D20 Test — checks, saves y attacks. Sale de spells, de features de
class, de conditions, o simplemente de que el DM decide que las circunstancias ayudan
(estás atacando a un tipo dormido) o estorban (estás trepando bajo la lluvia).

Tres reglas de arriba:

1. **No se acumulan.** Tres razones para tener advantage siguen siendo dos d20, no tres.
2. **Se cancelan.** Si tienes advantage y disadvantage al mismo tiempo, **no tienes
   ninguno** y tiras un solo d20. Da igual si eran tres fuentes de disadvantage contra
   una de advantage: se cancelan y listo.
3. Si algo te deja **repetir** el dado, repites **uno** de los dos, el que tú elijas.

## Ejemplo completo

> **DM:** La reja está oxidada y cerrada con candado. ¿Qué hacen?
>
> **Jugadora:** Mi rogue intenta abrir el candado con las ganzúas.
>
> **DM:** Dale. Es un candado viejo y barato — **Dexterity check** con proficiency de
> Thieves' Tools, DC 12.
>
> *(La rogue tiene Dexterity 16 → +3, y proficiency +2 con las herramientas.)*
>
> **Jugadora:** Saqué un 8... más 3, más 2. **Trece**.
>
> **DM:** Trece pasa. El candado cede con un chasquido más fuerte de lo que te gustaría.
> Adentro, algo dejó de moverse.

---

**Anterior:** [01 · Los dados](01-los-dados.md) · **Siguiente:** [03 · Tu personaje](03-tu-personaje.md)
