---
id: 2009-provincial-5
edicion: 2009-XXV
fase: provincial
numero: 5
titulo: Especulación inmobiliaria
bloques: [logica]
bloques_thales: [logica]
etiquetas: [deduccion, juegos]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0730, F0734]
estado: borrador
notas: ""
---

## Enunciado

Supón que hay cinco edificios contiguos entre sí de tres, cuatro, dos, cinco y un pisos de altura, respectivamente. Si miramos los edificios desde la izquierda solamente podremos ver tres de ellos: el de tres pisos, el de cuatro y el de cinco, ya que los edificios de dos pisos y de uno están tapados por el de cuatro y el de cinco respectivamente. Vistos desde la derecha podremos ver solamente el edificio de un piso y el de cinco, ya que los demás quedarán tapados por el de cinco pisos.

En la siguiente cuadrícula te damos al inicio y al final de cada fila y columna el número de edificios que se ven desde ese lado.

| | | | | | |
|---|---|---|---|---|---|
| | 2 | 1 | 2 | 3 | |
| **2** | | | | | **2** |
| **3** | | | | | **2** |
| **3** | | | | | **1** |
| **1** | | | | | **4** |
| | 1 | 2 | 3 | 2 | |

**Coloca en cada fila y en cada columna un edificio de un piso, otro de dos pisos, otro de tres y otro de cuatro.**

## Solución

- Desde la derecha de la última fila se ven 4 edificios: tienen que estar en orden decreciente, 4, 3, 2, 1.
- Desde donde solo se ve 1 edificio, el primero es el de 4 pisos (si no, se vería también el de 4).
- En la última columna se ven 3 desde abajo: como el 4 ya está, el 2 y el 3 van en orden creciente.
- En la primera fila se ven 2 desde la derecha: entre el 4 y el 2 queda el 1, tapado por el 2, y el 3 ocupa la casilla que falta.
- En la segunda fila se ven 3 desde la izquierda: el 1, el 2 y el 4 en ese orden, con el 3 tapado detrás del 4.
- El resto se completa sabiendo que en cada fila y columna hay un edificio de cada altura.

| | | | | | |
|---|---|---|---|---|---|
| | 2 | 1 | 2 | 3 | |
| **2** | 3 | 4 | 1 | 2 | **2** |
| **3** | 1 | 2 | 4 | 3 | **2** |
| **3** | 2 | 1 | 3 | 4 | **1** |
| **1** | 4 | 3 | 2 | 1 | **4** |
| | 1 | 2 | 3 | 2 | |
