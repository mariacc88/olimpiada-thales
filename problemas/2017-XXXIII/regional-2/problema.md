---
id: 2017-regional-2
edicion: 2017-XXXIII
fase: regional
numero: 2
titulo: Trabajando con polígonos
bloques: [geometria, numeros]
bloques_thales: []
etiquetas: [angulos, divisibilidad, ecuaciones]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0877]
estado: borrador
notas: ""
---

## Enunciado

Paco Investigalotodo siempre anda presumiendo ante sus hermanos y amigos de que es el que más sabe de todos los tipos de polígonos en Todolandia. Por eso, entre todos le han preparado esta serie de cuestiones para ver si es cierto:

a) ¿Cuál es el polígono que tiene igual número de lados que de diagonales?

b) ¿Cuál es el polígono que tiene el triple de diagonales que de lados?

c) ¿Cuáles son los polígonos regulares en los que cada uno de sus ángulos centrales (medido en grados) es un cuadrado perfecto?

d) ¿Cuál es el menor número de lados que debe tener un polígono para que la suma de todos sus ángulos interiores (en grados) sea un cuadrado perfecto?

Demuestra que conoces los polígonos mejor que Paco dando las respuestas acertadas a todas las preguntas.

**Razona las respuestas.**

## Solución

De cada vértice de un polígono de $x$ lados salen $x - 3$ diagonales (a todos los vértices salvo él mismo y los dos contiguos), y cada diagonal une dos vértices, así que el polígono tiene $\dfrac{x\,(x - 3)}{2}$ diagonales.

a) $\dfrac{x\,(x - 3)}{2} = x \Rightarrow x - 3 = 2 \Rightarrow x = 5$: el **pentágono**.

b) $\dfrac{x\,(x - 3)}{2} = 3x \Rightarrow x - 3 = 6 \Rightarrow x = 9$: el **eneágono**.

c) Cada ángulo central mide $\dfrac{360°}{x}$, y $360 = 2^3 \cdot 3^2 \cdot 5$. Para que el cociente sea un cuadrado perfecto hay que dividir al menos entre 5 y entre un 2, o entre los tres 2; y se puede dividir además entre $3^2$:

- $x = 10$: ángulo de $36° = 6^2$;
- $x = 40$: ángulo de $9° = 3^2$;
- $x = 90$: ángulo de $4° = 2^2$;
- $x = 360$: ángulo de $1° = 1^2$.

Son los polígonos regulares de **10, 40, 90 y 360 lados**.

d) Los ángulos interiores suman $180°\,(x - 2)$, y $180 = 2^2 \cdot 3^2 \cdot 5$. Para que sea un cuadrado perfecto, $x - 2$ debe ser como mínimo 5: $x = 7$, el **heptágono**, cuyos ángulos suman $900° = 30^2$.
