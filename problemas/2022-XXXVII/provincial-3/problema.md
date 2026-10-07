---
id: 2022-provincial-3
edicion: 2022-XXXVII
fase: provincial
numero: 3
titulo: Alfabeto secreto
bloques: [numeros, estadistica]
bloques_thales: []
etiquetas: [numeros-primos, combinatoria]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0957]
estado: borrador
notas: "Tomado del PDF de soluciones de la fase provincial (páginas 7-9). La solución original solo examina los casos en que alguna letra de OMTH toma el valor 1 o 39; se ha comprobado con las 27 asignaciones posibles que el máximo y el mínimo son los indicados. Corregida una errata: 1 · 36 · 10 · 30 = 10 800 (el original dice 324 000)."
---

## Enunciado

La agencia de detectives T.H.A.L.E.S. está buscando una forma de mandar mensajes cifrados, y para ello asigna un número, en orden, a cada letra del alfabeto (de 27 letras, con la Ñ): se empieza por el 1 y no se usan los números primos, y el número 1 se puede asignar a cualquier letra.

Por ejemplo: D = 1, E = 4, F = 6, G = 8, …

a) ¿Cuál sería el último número que se asigna en el código?

b) Si se cifra el mensaje OMTH y multiplicamos sus valores, ¿cuál es el valor máximo y el mínimo que podemos obtener?

**Debes razonar todas tus respuestas.**

## Solución

a) Los números que se usan son el 1 y los compuestos: 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39. Son 27, uno por letra, así que el último número asignado es el **39**.

Por ejemplo, empezando por A = 1:

| A | B | C | D | E | F | G | H | I | J | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 6 | 8 | 9 | 10 | 12 | 14 | 15 | 16 | 18 | 20 | 21 | 22 |

| Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 24 | 25 | 26 | 27 | 28 | 30 | 32 | 33 | 34 | 35 | 36 | 38 | 39 |

b) Al cambiar la letra a la que se asigna el 1, la lista se desplaza circularmente, pero las distancias entre las letras se mantienen. Probando las asignaciones en que alguna de las letras O, M, T, H toma el valor máximo (39) o el mínimo (1) se obtienen estos productos:

| O | M | T | H | O·M·T·H |
|---|---|---|---|---|
| 39 | 35 | 9 | 28 | 343 980 |
| 6 | 39 | 14 | 33 | 108 108 |
| 33 | 28 | 39 | 22 | **792 792** |
| 14 | 9 | 21 | 39 | 103 194 |
| 1 | 36 | 10 | 30 | 10 800 |
| 25 | 1 | 15 | 34 | 12 750 |
| 34 | 24 | 1 | 15 | 12 240 |
| 15 | 10 | 22 | 1 | **3300** |

El valor máximo es **792 792** y el mínimo, **3300**.
