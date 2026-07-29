# 06 · Daño, curación y descanso

## Cómo funcionan los HP

Cada vez que recibes daño, se lo restas a tus **HP** actuales.

**Perder HP no te debilita.** Con 30 HP o con 3 HP peleas exactamente igual, tiras
exactamente igual. El único umbral que importa es **0**.

Los HP no son "heridas" literales. Son aguante, suerte, voluntad y capacidad de convertir
un tajo mortal en un rasguño. Por eso una noche de sueño los devuelve todos.

> Si tienes **la mitad o menos** de tus HP, estás **Bloodied**. Por sí solo no hace nada;
> algunas habilidades de monstruos lo usan como gatillo.

## Tirar el daño

Cada arma, spell y habilidad dice qué daño hace.

- **Con arma:** tiras los dados del arma y sumas **el mismo ability modifier que usaste
  para el attack roll**. `1d8 + 3`.
- **Con spell:** el spell dice qué dados tirar y si se suma algo. Muchos **no** suman tu
  modificador.
- Si el daño es un **número fijo** sin dados, **no** le sumas tu modificador.
- El daño nunca puede ser negativo. Puede ser 0, no menos.

### Critical Hits

Cuando sacas un **20 natural** en un attack roll:

> Tiras **los dados de daño dos veces**, los sumas, y después sumas los modificadores
> **una sola vez**.

Con una dagger `1d4 + 3`, un crit es `2d4 + 3`. **No** `2d4 + 6`, y **no** el doble del
total.

Si el ataque incluye otros dados de daño (el Sneak Attack de un rogue, por ejemplo), esos
también se tiran dos veces.

### Daño por saving throw

Muchos efectos de área hacen daño a varios a la vez y les piden un save.

- **Se tira el daño una sola vez** para todos los objetivos. Un fireball no se tira por
  cada víctima.
- El que **pasa** el save típicamente recibe **la mitad** (redondeando hacia abajo). El
  que falla recibe todo. Lo dice el efecto.

## Tipos de daño

Cada instancia de daño tiene un tipo. Por sí mismos no hacen nada — importan porque otras
reglas (resistances, immunities) los usan.

| Físicos | Elementales | Mágicos / exóticos |
|---|---|---|
| Bludgeoning (contundente) | Fire | Force |
| Piercing (perforante) | Cold | Necrotic |
| Slashing (cortante) | Lightning | Radiant |
| | Thunder | Psychic |
| | Acid | |
| | Poison | |

*(PHB 2024, glosario)*

### Resistance, vulnerability, immunity

| Tienes… | Efecto |
|---|---|
| **Resistance** a un tipo | Recibes **la mitad** del daño de ese tipo (redondeando abajo) |
| **Vulnerability** a un tipo | Recibes **el doble** |
| **Immunity** a un tipo | Recibes **cero** |

**No se acumulan:** tener Resistance a Necrotic *y* Resistance a todo daño sigue siendo
una sola reducción a la mitad.

**Orden de aplicación:** primero bonos, penalizadores y multiplicadores; después
Resistance; al final Vulnerability.

*(SRD 2024, "Resistance and Vulnerability")*

También existe **Immunity a conditions** — un elemental no puede quedar Poisoned.

## Temporary Hit Points

Algunos spells te dan **Temporary HP**: un colchón encima de tus HP reales.

- **Se pierden primero.** Con 5 temp HP, si recibes 7 de daño pierdes los 5 y después 2
  HP reales.
- **No se suman a tus HP** ni cuentan como curación, y la curación no los restaura.
- **No se acumulan.** Si te dan 12 cuando ya tienes 10, eliges quedarte con 12 **o** con
  10. No 22.
- **Duran** hasta que se gastan o hasta que terminas un long rest.
- Con **0 HP**, recibir temp HP **no** te despierta. Solo la curación real.

## Llegar a 0 HP

Aquí es donde el juego se pone tenso. Léelo antes de tu primera pelea.

### Los monstruos mueren; tú no (todavía)

Un monstruo **muere al instante** al llegar a 0 HP. Un personaje jugador, no: cae
**Unconscious** y empieza a jugarse la vida.

### Death Saving Throws

Cada vez que **empiezas tu turno con 0 HP**, tiras un **Death Saving Throw**. No usa
ninguna ability — es un `1d20` pelado:

| Resultado | Qué pasa |
|---|---|
| **10 o más** | Un **éxito** |
| **9 o menos** | Un **fracaso** |
| **20 natural** | Recuperas **1 HP** y te despiertas al tiro |
| **1 natural** | Cuentan **dos fracasos** |

- **3 éxitos** → quedas **Stable**.
- **3 fracasos** → **mueres**.

No tienen que ser seguidos. Llevas la cuenta de ambos hasta juntar tres de uno. La cuenta
se **resetea a cero** en cuanto recuperes cualquier HP o quedes Stable.

**Si te pegan mientras estás en 0 HP:** un fracaso automático. Si fue **Critical Hit**,
dos fracasos.

### Stable

Estar **Stable** significa: sigues en 0 HP y sigues **Unconscious**, pero ya no tiras
death saves.

- Alguien puede estabilizarte con la action **Help**: un **DC 10 Wisdom (Medicine)
  check**.
- O curarte con cualquier cosa que dé HP — eso te despierta de inmediato.
- Si no te curan, un personaje Stable **recupera 1 HP solo, después de 1d4 horas**.
- Si recibe daño, deja de estar Stable y vuelve a tirar death saves.

### Muerte instantánea

Hay una forma de morir sin pasar por los death saves: **daño masivo**.

> Si el daño te lleva a 0 HP y **sobra** daño, mueres si lo que sobró **iguala o supera
> tu HP maximum**.

Ejemplo: tienes HP maximum 12 y estás en 6 HP. Recibes 18 de daño. Bajas a 0 y sobran 12.
12 iguala tu maximum → mueres en el acto.

*(SRD 2024, "Dropping to 0 Hit Points")*

### Noquear en vez de matar

Cuando estés a punto de reducir a alguien a 0 HP **con un ataque melee**, puedes elegir
dejarlo en **1 HP y Unconscious**. Esa criatura empieza un short rest y despierta al
final; despierta antes si recupera HP o si alguien le da primeros auxilios con un **DC 10
Wisdom (Medicine) check**.

Se declara en el momento del golpe. Sirve para tomar prisioneros.

## Curación

Sumas los HP recuperados a tus HP actuales. **Nunca puedes pasar tu HP maximum**: lo que
sobre se pierde. Si tienes 14/20 y recibes 8 de curación, recuperas 6, no 8.

Fuentes: spells (*Cure Wounds*), items (*Potion of Healing*), y los descansos.

## Descansos

Hay dos, y la diferencia importa mucho para el ritmo de una sesión.

### Short Rest

> Un **Short Rest** es **1 hora** de calma en la que no haces nada más pesado que leer,
> conversar, comer o hacer guardia. Para empezarlo necesitas al menos **1 HP**.
>
> *(PHB 2024, glosario)*

**Qué te da:** puedes gastar uno o más de tus **Hit Point Dice** para recuperar HP.
Por cada dado que gastes: **tiras el dado y le sumas tu modificador de Constitution**, y
recuperas ese total (mínimo 1). Gastas los dados de a uno y puedes parar cuando quieras.

Además, varias features de class se recargan con un short rest.

### Long Rest

> Un **Long Rest** son al menos **8 horas**: duermes al menos 6 y haces como mucho 2
> horas de actividad liviana. Necesitas al menos **1 HP** para empezarlo, y después de
> terminar uno tienes que esperar **16 horas** antes de empezar otro.
>
> *(PHB 2024, glosario)*

**Qué te da:**

- **Todos tus HP** de vuelta.
- **Todos tus Hit Point Dice** gastados de vuelta.
- Tus ability scores reducidos vuelven a la normalidad.
- Tu nivel de **Exhaustion** baja en 1.
- Tus spell slots y las features que se recargan con long rest, de vuelta.

Mientras duermes tienes la condition **Unconscious**. Alguien tiene que hacer guardia.

### En criollo

**Short rest** = respiro entre peleas. Gastas de tu botiquín. Una hora.
**Long rest** = se acabó el día de aventura. Vuelves a nuevo. Una noche.

---

**Anterior:** [05 · El combate](05-el-combate.md) · **Siguiente:** [07 · La magia](07-la-magia.md)
