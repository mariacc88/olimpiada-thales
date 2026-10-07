---
id: 2021-regional-1
edicion: 2021-XXXVI
fase: regional
numero: 1
titulo: La barca
bloques: [logica]
bloques_thales: []
etiquetas: [juegos]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0948]
estado: borrador
notas: "Edición online por la pandemia."
---

## Enunciado

Cuatro amigos se encuentran en la orilla norte del río Guadalquivir y quieren cruzar a la orilla sur. Para ello tienen una barca en la que Andrés, que es el más rápido, tarda un minuto en cruzar; Benito lo hace en dos minutos, Carlos necesita tres minutos y Dionisio cuatro minutos.

La barca solo soporta el peso de dos personas y, cuando lleva a dos, va a la velocidad del más lento.

¿Cómo han de realizar los viajes para cruzar los cuatro en el menor tiempo posible?

Cuando iban a emprender la travesía se presentan tres amigas suyas: Elena, que tarda en cruzar con la barca cinco minutos; Flor, que emplea seis minutos, y Gema, que es la más lenta y necesita siete minutos. También desean atravesar el río para ir a la otra orilla.

¿Cómo deben organizarse ahora para cruzar los siete en la barca empleando el menor tiempo posible?

## Solución

Representamos a cada persona por su inicial.

**Los cuatro amigos.** Una forma de hacerlo en el mínimo tiempo:

| Orilla norte | Viaje | Duración | Orilla sur |
|---|---|---|---|
| C, D | A y B cruzan | 2 min | A, B |
| A, C, D | A vuelve | 1 min | B |
| A | C y D cruzan | 4 min | B, C, D |
| A, B | B vuelve | 2 min | C, D |
| — | A y B cruzan | 2 min | A, B, C, D |

En total, **11 minutos** (también se puede hacer en 11 minutos de otras formas, por ejemplo con A acompañando a cada uno y volviendo: $2 + 1 + 3 + 1 + 4$).

**Los siete amigos.** Hacen falta como mínimo **28 minutos**, por ejemplo así:

| Orilla norte | Viaje | Duración | Orilla sur |
|---|---|---|---|
| C, D, E, F, G | A y B cruzan | 2 min | A, B |
| A, C, D, E, F, G | A vuelve | 1 min | B |
| A, C, D, E | F y G cruzan | 7 min | B, F, G |
| A, B, C, D, E | B vuelve | 2 min | F, G |
| C, D, E | A y B cruzan | 2 min | A, B, F, G |
| A, C, D, E | A vuelve | 1 min | B, F, G |
| A, C | D y E cruzan | 5 min | B, D, E, F, G |
| A, B, C | B vuelve | 2 min | D, E, F, G |
| B | A y C cruzan | 3 min | A, C, D, E, F, G |
| A, B | A vuelve | 1 min | C, D, E, F, G |
| — | A y B cruzan | 2 min | todos |
