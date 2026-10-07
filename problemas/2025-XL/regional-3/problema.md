---
id: 2025-regional-3
edicion: 2025-XL
fase: regional
numero: 3
titulo: Una extraña frase
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [patrones, divisibilidad, ecuaciones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1005]
estado: borrador
notas: ""
---

## Enunciado

En el lejano planeta ABC viven unos extraterrestres cuyo alfabeto está compuesto únicamente por tres letras, que son (¡oh, sorpresa!) la A, la B y la C.

Supongamos que escribimos la siguiente lista, compuesta por 150 palabras:

A   BB   CCC   AAAA   BBBBB   CCCCCC   AAAAAAA   …

**Contesta de forma razonada:**

a) ¿De qué letra está formada la última palabra?

b) ¿Cuántas letras hemos escrito en total?

c) Si uniésemos todas las palabras, ¿cuál es la letra que se encuentra justamente en medio?

## Solución

a) Las letras se repiten en el orden A, B, C, A, B, C…, así que las palabras de letras C ocupan los puestos múltiplos de 3. Como 150 es múltiplo de 3, la última palabra está formada por **C**.

b) Hay que sumar $1 + 2 + 3 + \dots + 150$. Con el truco de Gauss, sumando la lista consigo misma al revés:

$$2S = 151 + 151 + \dots + 151 = 150 \cdot 151 \;\Rightarrow\; S = \frac{150 \cdot 151}{2} = \mathbf{11\,325\ letras}.$$

c) Como hay un número impar de letras, la central ocupa la posición $\frac{11\,325 - 1}{2} + 1 = 5663$. Buscamos en qué palabra cae, con las sumas $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$:

$$\frac{105 \cdot 106}{2} = 5565 < 5663 \le 5671 = \frac{106 \cdot 107}{2}.$$

La letra central está en la palabra 106. Como $106 = 3 \cdot 35 + 1$, esa palabra está formada por letras A: la letra central es una **A**.
