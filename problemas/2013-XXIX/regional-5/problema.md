---
id: 2013-regional-5
edicion: 2013-XXIX
fase: regional
numero: 5
titulo: Un extraño algoritmo
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [cifras, patrones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1068]
estado: borrador
notas: "Problema CASIO (se permite la calculadora)."
---

## Enunciado

Ángel es un alumno muy brillante y le gustan los números. Cansado de que su profesor de Matemáticas, don Manuel Castro, siempre propone problemas, inventa un algoritmo y se atreve a presentárselo:

A partir de un número dado se construye una sucesión de números de la manera siguiente:

- Cada número es la suma de los cuadrados de las cifras del número precedente.
- Si el primer número es el 2332011, el segundo es

$$2^2 + 3^2 + 3^2 + 2^2 + 0^2 + 1^2 + 1^2 = 28.$$

a) ¿Cuál es el tercero? ¿Y el que ocupa el lugar 2013?

b) ¿Cuál es el número que ocupa el lugar 2013 partiendo del número 1248?

El profesor felicitó a Ángel por la iniciativa, animándole a que siguiera trabajando con los números.

Contesta de **forma razonada** a las cuestiones propuestas por Ángel.

## Solución

a) La sucesión es

2332011, 28, $2^2 + 8^2 = 68$, $6^2 + 8^2 = 100$, $1^2 + 0^2 + 0^2 = 1$, 1, 1, …

El tercero es **68**, y desde el quinto lugar todos los términos valen 1: el que ocupa el lugar 2013 es **1**.

b) Partiendo de 1248:

| Lugar | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Número | 1248 | 85 | 89 | 145 | 42 | 20 | 4 | 16 | 37 | 58 | 89 |

En el lugar 11 vuelve a salir 89, así que desde el tercer lugar los términos se repiten cada 8: el 89 aparece en los lugares 3, 11, 19, 27, … Como $2013 - 2 = 2011 = 8 \cdot 251 + 3$, el término 2013 es el mismo que el que ocupa el lugar $2 + 3 = 5$: **42**.
