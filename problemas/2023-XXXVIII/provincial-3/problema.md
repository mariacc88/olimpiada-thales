---
id: 2023-provincial-3
edicion: 2023-XXXVIII
fase: provincial
numero: 3
titulo: Cuadrante binario
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0972]
estado: borrador
notas: "La solución original muestra tres pasadas intermedias con colores; aquí se resume el método y se da el cuadrante final."
---

## Enunciado

El mayor especialista en el sistema binario de Todolandia, D. Luis Sabelotodo, ha creado un cuadrante binario para un nuevo dispositivo electrónico que ha diseñado, pero en uno de sus frecuentes despistes se le ha borrado parte del mismo.

Ayuda al Sr. Sabelotodo a completar totalmente su cuadrante sabiendo que debe cumplir las siguientes normas:

- No puede haber más de dos 0 ni más de dos 1 consecutivos en cada una de las filas y columnas del cuadrante.
- Cada fila y cada columna contiene la misma cantidad de 0 y de 1.
- No hay dos columnas iguales, y tampoco hay dos filas iguales.

**Explica cómo lo has realizado.**

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   | 0 |   |   | 1 |   |   |   |
| 0 |   |   |   | 1 |   |   |   | 0 |   |
| 0 |   |   |   | 1 |   | 0 |   | 1 | 1 |
|   |   | 1 |   |   |   |   |   |   |   |
|   |   | 1 |   |   |   |   |   | 1 |   |
|   | 0 |   |   |   |   | 1 |   |   |   |
| 1 |   |   |   |   | 0 | 0 |   | 0 |   |
|   |   | 0 |   |   |   |   | 1 |   | 1 |
|   |   | 0 | 1 |   | 1 |   |   |   |   |
| 0 |   |   | 1 |   |   | 0 | 1 |   | 1 |

## Solución

Empezamos rellenando, en filas y columnas, las casillas anteriores y posteriores a dos dígitos iguales seguidos, y las casillas que están entre dos dígitos iguales (primera norma). Repetimos esta pasada sobre todo el cuadrante varias veces, porque cada casilla nueva permite deducir otras.

Para completar las filas y columnas que quedan usamos la segunda norma (cinco 0 y cinco 1 en cada fila y columna) y volvemos a rellenar casillas para que se siga cumpliendo la primera. Al terminar comprobamos que se cumple la tercera norma: no hay filas ni columnas repetidas.

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
