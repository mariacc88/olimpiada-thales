---
id: 2016-provincial-1
edicion: 2016-XXXII
fase: provincial
numero: 1
titulo: El robot
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0852]
estado: borrador
notas: "El plano de la figura original es una cuadrícula de 3 × 3 habitaciones vacía."
---

## Enunciado

En la empresa del profesor Thayton se fabrican 3 clases de robots, los alfa (α), los beta (β) y los gamma (γ), y de cada uno de ellos existen tres modelos, el 1, el 2 y el 3. En la empresa los tienen almacenados, sin mezclar, en nueve habitaciones, como las que se muestran en el plano de la figura (una cuadrícula de 3 × 3).

![Ilustración: un robot](ilustracion.png)

El profesor Thayton tiene escrito en su cuaderno de anotaciones los siguientes datos:

1. En cada fila y en cada columna hay un modelo 1, 2 y 3.
2. Todos los modelos 2 están en una diagonal del plano.
3. Todas las habitaciones donde están los robots de la clase alfa tienen al menos en común un punto de contacto.
4. Las habitaciones de los robots de la clase gamma no están en contacto unas con otras.
5. La clase beta tiene dos modelos de robots en dos habitaciones que están en contacto y el otro está en una habitación que no tiene nada en común con las otras.
6. A la derecha de la habitación del modelo 2 de la clase gamma se encuentra la habitación del modelo 1 de la clase beta.

Coloca **de forma razonada** cada modelo de robot en su habitación correspondiente.

## Solución

Por (2), los modelos 2 ocupan una de las dos diagonales. Por (6), γ2 tiene que tener una habitación a su derecha, así que no puede estar en la columna de la derecha. Por (4), γ2 tampoco puede estar en la casilla central, que toca a todas las demás. Quedan dos posiciones para γ2: las dos esquinas de la columna izquierda.

Si γ2 está arriba a la izquierda, β1 va a su derecha y la diagonal de los modelos 2 es la que baja de izquierda a derecha. Completando los números con (1) y separando los gamma con (4), los gamma quedan en las posiciones γ2, γ3 (arriba a la derecha) y γ1 (abajo a la izquierda).

Por (5), la casilla central no puede ser β2 (tocaría a todas), luego es α2 y β2 está en la esquina inferior derecha. Por (3), los tres alfa deben tocarse, lo que fija α1 y α3, y β3 ocupa la casilla restante:

| | | |
|---|---|---|
| γ2 | β1 | γ3 |
| β3 | α2 | α1 |
| γ1 | α3 | β2 |

Si γ2 está abajo a la izquierda, el razonamiento es el mismo y se obtiene la solución simétrica respecto de la fila central («espejo, espejito…»):

| | | |
|---|---|---|
| γ1 | α3 | β2 |
| β3 | α2 | α1 |
| γ2 | β1 | γ3 |
