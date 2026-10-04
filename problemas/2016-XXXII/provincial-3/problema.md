---
id: 2016-provincial-3
edicion: 2016-XXXII
fase: provincial
numero: 3
titulo: Concurso de ingenio
bloques: [funciones]
bloques_thales: []
etiquetas: [ecuaciones]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0854]
estado: borrador
notas: ""
---

## Enunciado

A un concurso de ingenio se presentan cuatro amigos y deben resolver cuatro retos cada uno de ellos. Una vez terminadas las cuatro pruebas, para conocer la clasificación, debes calcular la puntuación obtenida por cada uno de ellos, que depende del tiempo que han empleado. El tiempo óptimo para cada prueba es de dos minutos para el jeroglífico y el sudoku, y de un minuto y medio para las otras dos pruebas.

Todos parten de 100 puntos; por cada segundo de más sobre este tiempo se penaliza con 2 puntos y por cada segundo de menos se recompensa con 2 puntos.

Si los tiempos son los de la tabla, ¿cómo quedaría la clasificación?

| | Puzle | Jeroglífico | Sudoku | Tangram |
|---|---|---|---|---|
| Isaac | 1 min 50 s | 2,5 min | 2 min 5 s | 1 min 15 s |
| María | 1 min 45 s | 2 min 12 s | 1 min 54 s | 1 min 5 s |
| Elena | 1 min 5 s | 2 min 10 s | 2 min 27 s | 1 min 48 s |
| Pedro | 2 min 5 s | 1 min 38 s | 1 min 55 s | 1 min 23 s |

Busca una fórmula para calcular las puntuaciones.

Razona las respuestas.

## Solución

Como se ganan o se pierden 2 puntos por cada segundo, sea cual sea la prueba, lo que importa es el tiempo total empleado en las cuatro pruebas. Pasamos los tiempos a segundos y sumamos:

| | Puzle | Jeroglífico | Sudoku | Tangram | Total |
|---|---|---|---|---|---|
| Isaac | 110 | 150 | 125 | 75 | 460 s |
| María | 105 | 132 | 114 | 65 | 416 s |
| Elena | 65 | 130 | 147 | 108 | 450 s |
| Pedro | 125 | 98 | 115 | 83 | 421 s |

A menor tiempo, mejor puesto: **1.º María, 2.º Pedro, 3.º Elena y 4.º Isaac.**

El tiempo óptimo total es $90 + 120 + 120 + 90 = 420$ s. La puntuación se obtiene sumando a 100 el doble de la diferencia entre el tiempo óptimo y el empleado:

- Isaac: $100 + 2\,(420 - 460) = 20$ puntos.
- María: $100 + 2\,(420 - 416) = 108$ puntos.
- Elena: $100 + 2\,(420 - 450) = 40$ puntos.
- Pedro: $100 + 2\,(420 - 421) = 98$ puntos.

Llamando $t$ al tiempo total en segundos, la fórmula es

$$P = 100 + 2\,(420 - t) = 940 - 2t.$$
