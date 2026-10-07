---
id: 2021-provincial-1
edicion: 2021-XXXVI
fase: provincial
numero: 1
titulo: Reparto en cajas
bloques: [numeros]
bloques_thales: []
etiquetas: [divisibilidad, ecuaciones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0943]
estado: borrador
notas: "Edición online por la pandemia."
---

## Enunciado

En un supermercado hay 360 botes de miel y 300 botes de mermelada. Se van a meter en cajas. Una vez finalizado, han salido tres cajas más de botes de miel que de mermelada, y las cajas de miel contienen un bote menos que las de mermelada.

a) ¿Cuántas cajas había de miel?

b) ¿Cuántas cajas había de mermelada?

c) ¿Cuántos botes hay en cada caja de miel?

**Explica el procedimiento que has seguido para resolver las tres cuestiones anteriores.**

## Solución

**Con divisores.** Buscamos las parejas de divisores de 360 y de 300 (número de cajas × botes por caja):

- $360$: $1 \cdot 360$, $2 \cdot 180$, $3 \cdot 120$, $4 \cdot 90$, $5 \cdot 72$, $6 \cdot 60$, $8 \cdot 45$, $9 \cdot 40$, $10 \cdot 36$, $12 \cdot 30$, $15 \cdot 24$, $18 \cdot 20$.
- $300$: $1 \cdot 300$, $2 \cdot 150$, $3 \cdot 100$, $4 \cdot 75$, $5 \cdot 60$, $6 \cdot 50$, $10 \cdot 30$, $12 \cdot 25$, $15 \cdot 20$.

Las únicas parejas con tres cajas más de miel y un bote menos por caja de miel son: **miel, 15 cajas de 24 botes**, y **mermelada, 12 cajas de 25 botes**.

**Con álgebra.** Sea $x$ el número de cajas de mermelada e $y$ el número de botes en cada una. Entonces hay $x + 3$ cajas de miel con $y - 1$ botes:

$$x\,y = 300, \qquad (x + 3)(y - 1) = 360.$$

Sustituyendo $x = \frac{300}{y}$ en la segunda ecuación y simplificando:

$$y^2 - 21y - 100 = 0 \;\Rightarrow\; y = \frac{21 \pm 29}{2} \;\Rightarrow\; y = 25 \ (\text{o } y = -4, \text{ que no vale}).$$

Por tanto $x = 12$, $x + 3 = 15$ e $y - 1 = 24$.

a) **15 cajas de miel**. b) **12 cajas de mermelada**. c) **24 botes** en cada caja de miel (y 25 en cada caja de mermelada).
