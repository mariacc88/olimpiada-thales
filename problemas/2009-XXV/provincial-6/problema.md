---
id: 2009-provincial-6
edicion: 2009-XXV
fase: provincial
numero: 6
titulo: Curiosa forma de preguntar
bloques: [numeros, estadistica]
bloques_thales: [estadistica]
etiquetas: [divisibilidad, probabilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0735, F0738]
estado: borrador
notas: ""
---

## Enunciado

D. Anacleto Enseñalotodo, profesor de la escuela de Todolandia, tiene una curiosa forma de elegir a cuáles de sus 25 alumnos les va a preguntar. Cuando llega por la mañana lanza dos dados y suma las puntuaciones conseguidas en cada uno de ellos. Del resultado de esta suma calcula los divisores y los múltiplos menores o iguales que 25 y aquellos alumnos que su número de clase coincida con algunos de los números que ha obtenido son a los que les pregunta las lecciones y actividades del día. Todos sus alumnos están muy preocupados porque no saben cuáles son sus posibilidades de ser ellos los preguntados. Ayuda a estos intranquilos alumnos informándoles de:

a) ¿Cuál o cuáles son los que tienen posibilidades de que les pregunten todos los días?

b) ¿Existe algún alumno al que no preguntaría nunca? ¿Cuál o cuáles serían?

c) ¿Quién tendría menos posibilidades que le preguntase, el alumno número 4, el número 10 ó el número 20?

Razona todas las respuestas.

## Solución

La suma de los dos dados puede ser 2, 3, …, 12, y de las 36 tiradas posibles, cada suma sale de 1, 2, 3, 4, 5, 6, 5, 4, 3, 2 y 1 formas, respectivamente.

- **El alumno n.º 1** es divisor de cualquier suma: **le pregunta todos los días**.
- **Nunca pregunta** a los alumnos 13, 17, 19 y 23: son primos mayores que 12, así que no son divisores ni múltiplos de ninguna suma posible. (Todos los demás números hasta 25 son divisor o múltiplo de alguna suma.)
- Contamos las tiradas favorables de cada alumno:
  - **N.º 4**: sumas 2 y 4 (4 es múltiplo) y 8 y 12 (4 es divisor): $1 + 3 + 5 + 1 = 10$ de 36.
  - **N.º 10**: sumas 2, 5 y 10: $1 + 4 + 3 = 8$ de 36.
  - **N.º 20**: sumas 2, 4, 5 y 10: $1 + 3 + 4 + 3 = 11$ de 36.

El que tiene menos posibilidades es el **n.º 10**.
