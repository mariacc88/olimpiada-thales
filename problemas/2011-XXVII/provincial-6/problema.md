---
id: 2011-provincial-6
edicion: 2011-XXVII
fase: provincial
numero: 6
titulo: "¿Dónde se encuentra el 2011?"
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [patrones, divisibilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1032]
estado: borrador
notas: ""
---

## Enunciado

Thalevago ha contado a su compañera Calculina que su profesora de mates, Eulerina, ha propuesto hoy en clase la siguiente serie de números:

| A | B | C | D | E |
|---|---|---|---|---|
| | 1 | | 4 | |
| 13 | | 10 | | 7 |
| | 16 | | 19 | |
| 28 | | 25 | | 22 |
| | 31 | | … | |

Y les ha pedido que averigüen en qué columna y en qué fila aparecerá en dicha serie el número que corresponde al año actual. Para que practiquen, les ha dicho que investiguen buscando primero la posición del número 73.

Ambos se encuentran un poco despistados: ayúdales a encontrar de forma razonada las respuestas.

## Solución

Los números de la serie son 1, 4, 7, 10, 13, 16, … : el término que ocupa el lugar $n$ es $3n - 2$. Se colocan de 5 en 5 cada dos filas: el 1.º en la columna B, el 2.º en la D (fila impar), y el 3.º, 4.º y 5.º en las columnas E, C y A (fila par, de derecha a izquierda). Por tanto:

- La columna depende del resto de dividir $n$ entre 5: resto 1 → B, 2 → D, 3 → E, 4 → C, 0 → A.
- Cada grupo completo de 5 términos ocupa 2 filas.

**El 73.** $3n - 2 = 73$, $n = 25 = 5 \cdot 5$: es el último término del 5.º grupo, en la **columna A** y la **fila 10**.

**El 2011.** $3n - 2 = 2011$, $n = 671 = 5 \cdot 134 + 1$: tras 134 grupos completos (268 filas) es el primer término del siguiente, en la **columna B** y la **fila 269**.
