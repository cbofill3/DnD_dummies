# 10 · Chuleta

Una página. Imprímela y ponla al lado de tu hoja de personaje.

---

## El motor del juego

```
        1d20  +  modificador   ≥   número objetivo   →   funciona
```

| Sabor | Cuándo | Objetivo |
|---|---|---|
| **Ability check** | Tú intentas algo | **DC** (lo pone el DM) |
| **Saving throw** | Algo te intenta a ti | **DC** (lo pone el efecto) |
| **Attack roll** | Le pegas a algo | **AC** del objetivo |

**Advantage:** dos d20, usas el **más alto**.
**Disadvantage:** dos d20, usas el **más bajo**.
Nunca se acumulan. Si tienes los dos, tiras **un solo** d20.

**Redondea siempre hacia abajo.**

**20 natural = pega sí o sí + Critical Hit. 1 natural = falla sí o sí.**
Solo en **attack rolls**. No en checks ni en saves.

---

## Tu turno en combate

```
        Movimiento (hasta tu Speed)  +  1 Action
        + 1 Bonus Action (solo si algo te la da)
        + 1 Reaction (usable en el turno de cualquiera)
```

Puedes partir el movimiento antes y después de la acción.
**1 interacción con objeto gratis** por turno; la segunda es la action **Utilize**.
Hablar poco es gratis.

### Acciones

| | |
|---|---|
| **Attack** | Atacar |
| **Dash** | Movimiento extra = tu Speed |
| **Disengage** | Tu movimiento no provoca Opportunity Attacks |
| **Dodge** | Te atacan con disadvantage; DEX saves con advantage |
| **Help** | Das advantage a un aliado, o primeros auxilios |
| **Hide** | Dexterity (Stealth) check |
| **Influence** | CHA (Deception/Intimidation/Performance/Persuasion) o WIS (Animal Handling) |
| **Magic** | Lanzar spell / usar item mágico |
| **Ready** | Preparar una acción para un gatillo |
| **Search** | WIS (Insight/Medicine/Perception/Survival) |
| **Study** | INT (Arcana/History/Investigation/Nature/Religion) |
| **Utilize** | Usar un objeto no mágico |

**Improvisar también vale.** Describe y el DM te dice qué tirar.

### Opportunity Attack

Alguien **que puedes ver sale de tu reach** → gastas tu **Reaction** para **un** ataque
melee, justo **antes** de que salga.

**No la provoca:** acercarse, moverse alrededor sin salir del reach, **Disengage**,
teleportarse, o ser movido por algo externo.

### Ataque

```
1d20 + ability mod + proficiency bonus  ≥  AC
```
Melee → STR · Ranged → DEX · Finesse → la que prefieras · Spell → la de tu class

**Daño:** dados del arma + **el mismo** ability mod.
**Crit:** dados de daño **× 2**, modificadores **× 1**.

### Cover

| | AC y DEX saves |
|---|---|
| Half | **+2** |
| Three-Quarters | **+5** |
| Total | no puede ser objetivo |

### Movimiento

1 cuadro = **5 feet** · Speed típica **30 feet** = 6 cuadros
**Difficult terrain:** cada pie cuesta el doble
**Tirarse al suelo:** gratis · **Pararse:** media Speed

---

## Cuando llegas a 0 HP

Caes **Unconscious**. Al **empezar** cada turno tiras `1d20` sin sumar nada:

| Dado | |
|---|---|
| **10+** | éxito |
| **9−** | fracaso |
| **20 nat** | ¡despiertas con **1 HP**! |
| **1 nat** | **dos** fracasos |

**3 éxitos → Stable. 3 fracasos → mueres.**
Te pegan estando en 0 → **1 fracaso** (crítico → **2**).
Cualquier curación te resetea la cuenta y te despierta.
Estabilizar a alguien: action **Help**, **DC 10 Wisdom (Medicine)**.

**Muerte instantánea:** si el daño sobrante después de llegar a 0 **iguala o supera tu HP
maximum**.

---

## Descansos

| | Dura | Te da |
|---|---|---|
| **Short Rest** | 1 hora | Gastas **Hit Point Dice**: por cada uno, `dado + CON mod` de HP |
| **Long Rest** | 8 horas | **Todos** los HP, **todos** los Hit Dice, spell slots, −1 Exhaustion |

Necesitas al menos **1 HP** para empezar cualquiera de los dos.

---

## Conditions — lo mínimo

| | |
|---|---|
| **Blinded** | Fallas checks de vista; te pegan con adv, pegas con dis |
| **Charmed** | No puedes dañar al que te encantó |
| **Deafened** | Fallas checks de oído |
| **Exhaustion** | −2 × nivel a **todo** D20 Test; −5 feet × nivel. **Nivel 6 = muerte** |
| **Frightened** | Dis en checks y ataques; no te acercas a la fuente |
| **Grappled** | Speed 0; dis atacando a otro |
| **Incapacitated** | Sin action, Bonus Action ni Reaction. Pierdes Concentration |
| **Invisible** | Te atacan con dis, atacas con adv |
| **Paralyzed** | Incapacitated, Speed 0, fallas STR/DEX saves, **crítico auto a 5 ft** |
| **Petrified** | Estatua. Resistance a todo |
| **Poisoned** | Dis en ataques y ability checks |
| **Prone** | Atacas con dis; te pegan con adv de cerca, dis de lejos |
| **Restrained** | Speed 0; te pegan con adv, pegas con dis, dis en DEX saves |
| **Stunned** | Incapacitated, fallas STR/DEX saves, te pegan con adv |
| **Unconscious** | Incapacitated + Prone, **crítico auto a 5 ft** |

Detalle completo en [08 · Las conditions](08-conditions.md).

---

## Magia

**Cantrips:** gratis, infinitos, no gastan slot.
**Spells de nivel 1+:** gastan un **spell slot**. Vuelven con **long rest**.
**Concentration:** solo **uno** a la vez. Si recibes daño → **Constitution save**,
DC **10 o la mitad del daño, el mayor**.
**Attack roll o saving throw:** lo dice el spell. Si pide save, **tú no tiras**.

---

## DCs típicos

| | DC |
|---|---|
| Very easy | 5 |
| Easy | 10 |
| Medium | **15** |
| Hard | 20 |
| Very hard | 25 |
| Nearly impossible | 30 |

---

## Cuando no sepas qué hacer

1. **Describe lo que tu personaje hace**, no la regla.
2. Si dudas en combate: **Dodge**, **Help** a un aliado, o **Attack**.
3. Si dudas fuera de combate: pregunta al DM qué ve tu personaje.
4. Si nadie sabe la regla: el DM decide algo razonable, siguen jugando, se revisa después.

---

**Anterior:** [09 · Glosario](09-glosario.md) · **Volver al** [índice](../README.md)
