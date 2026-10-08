---
id: 2009-regional-1
edicion: 2009-XXV
fase: regional
numero: 1
titulo: Juguemos al waterpolo
bloques: [logica, numeros]
bloques_thales: []
etiquetas: [deduccion]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0743, F0744]
estado: borrador
notas: ""
---

## Enunciado

Los equipos femeninos de waterpolo de Rociana del Condado, Villalba del Alcor, Bollullos Par del Condado y San Juan del Puerto celebran un torneo en el que todos juegan contra todos solo una vez. Cada partido produjo el mismo número de goles, y no hubo dos partidos con el mismo resultado. De los 13 goles que marcó San Juan, 2 los hizo contra Bollullos. La siguiente tabla muestra la clasificación final:

| | Goles a favor | Goles en contra | Puntos |
|---|---|---|---|
| Rociana | 13 | 17 | 4 |
| Villalba | 17 | 13 | 3 |
| Bollullos | 17 | 13 | 3 |
| San Juan | 13 | 17 | 2 |

Si se dan 2 puntos por cada partido ganado y 1 punto por empate, ¿cuál fue el resultado entre Villalba y San Juan?

## Solución

- Se juegan 6 partidos y se marcan 60 goles: **10 goles por partido**. Como no hay dos resultados iguales, los resultados son, sin importar el orden, 10-0, 9-1, 8-2, 7-3, 6-4 y 5-5.
- San Juan marcó 2 goles a Bollullos: **Bollullos 8 - San Juan 2**.
- Villalba y Bollullos tienen un número impar de puntos, así que empataron algún partido; como solo hay un empate (5-5), **Villalba 5 - Bollullos 5**.
- Bollullos lleva $8 + 5 = 13$ goles y ha marcado 17: contra Rociana marcó 4, así que **Rociana 6 - Bollullos 4**.
- A Rociana le faltan 7 goles en dos partidos con los resultados que quedan (10-0, 9-1, 7-3): solo es posible con 0 y 7, es decir, perdió 0-10 y ganó 7-3.
- Si Villalba hubiera marcado 10 a Rociana, para llegar a 17 tendría que marcar 2 a San Juan, pero el 8-2 ya está usado. Así que **San Juan 10 - Rociana 0** y **Rociana 7 - Villalba 3**.
- Queda el 9-1 para Villalba–San Juan. San Juan tiene 2 puntos, los de su victoria ante Rociana, así que perdió.

El resultado fue **Villalba 9 - San Juan 1**.
