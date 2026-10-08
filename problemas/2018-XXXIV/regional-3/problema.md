---
id: 2018-regional-3
edicion: 2018-XXXIV
fase: regional
numero: 3
titulo: Fichas numéricas
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0902]
estado: borrador
notas: ""
---

## Enunciado

En el siguiente tablero hay colocadas fichas, cada una con un número natural diferente de una sola cifra (puede ser cero). En los márgenes de la tabla hay pistas con la siguiente información:

1. A la izquierda aparece el número de fichas que hay en cada fila (horizontal) y en la parte superior las que hay en cada columna (vertical).
2. A la derecha aparece el total de la suma de los números de cada fila y abajo está la suma de cada columna.

Coloca en el tablero las fichas **de forma razonada**, con el número de cada una, y completa **razonadamente** las pistas que faltan.

|            | Hay 2   | Hay 1  | Hay 4    | Hay 0    | Hay 3    |          |
|------------|---------|--------|----------|----------|----------|----------|
| **Hay 1**  |         |        |          |          |          | Suma 6   |
| **Hay 3**  |         |        |          |          |          | Suman 9  |
| **Hay 2**  |         |        |          |          |          | Suman 11 |
| **Hay 4**  |         |        |          |          |          | Suman ¿? |
| **Hay ¿?** |         |        |          |          |          | Suman ¿? |
|            | Suman 1 | Suma 5 | Suman 30 | Suman ¿? | Suman ¿? |          |

## Solución

**Pistas que faltan.** Hay en total $2 + 1 + 4 + 0 + 3 = 10$ fichas, así que están las diez cifras $0, 1, \dots, 9$, que suman 45. Las cuatro primeras filas tienen $1 + 3 + 2 + 4 = 10$ fichas, de modo que la última fila tiene **0 fichas** y suma **0**; la cuarta fila suma $45 - 6 - 9 - 11 = 19$. La cuarta columna no tiene fichas (suma **0**) y la última suma $45 - 1 - 5 - 30 = 9$.

**Posición de las fichas.** La última fila y la cuarta columna están vacías, así que en la fila «Hay 4» y en la columna «Hay 4» solo quedan 4 casillas libres: todas tienen ficha. Con eso la fila «Hay 1» ya tiene su ficha (en la columna «Hay 4») y la columna «Hay 1» también (en la fila «Hay 4»), de modo que el resto de casillas de esa fila y esa columna están vacías. Ahora la columna «Hay 3» y la fila «Hay 3» solo pueden completarse de una manera, y lo que queda se deduce igual.

**Valor de las fichas.** La ficha de la fila «Hay 1» es el **6** y la de la columna «Hay 1» es el **5**. Las dos fichas de la columna que suma 1 son el 0 y el 1; las tres de la última columna, que suman 9 sin usar el 5 ni el 6, son 2, 3 y 4; y las tres restantes de la columna que suma 30 son 7, 8 y 9. En la fila «Hay 4» las tres fichas que faltan suman $19 - 5 = 14$, lo que solo es posible con $1 + 9 + 4$; por tanto, el 0 va en la fila «Hay 3». Como esa fila suma 9, sus otras dos fichas suman 9 con una de $\{7, 8\}$ y otra de $\{2, 3\}$: son 7 y 2. En la fila «Hay 2» quedan 8 y 3, que efectivamente suman 11.

|           | Hay 2   | Hay 1  | Hay 4    | Hay 0  | Hay 3   |          |
|-----------|---------|--------|----------|--------|---------|----------|
| **Hay 1** |         |        | 6        |        |         | Suma 6   |
| **Hay 3** | 0       |        | 7        |        | 2       | Suman 9  |
| **Hay 2** |         |        | 8        |        | 3       | Suman 11 |
| **Hay 4** | 1       | 5      | 9        |        | 4       | Suman 19 |
| **Hay 0** |         |        |          |        |         | Suma 0   |
|           | Suman 1 | Suma 5 | Suman 30 | Suma 0 | Suman 9 |          |
