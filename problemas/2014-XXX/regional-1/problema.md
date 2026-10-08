---
id: 2014-regional-1
edicion: 2014-XXX
fase: regional
numero: 1
titulo: Familias de primos
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [numeros-primos, divisibilidad, cifras, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0842]
estado: borrador
notas: "Las familias se transcriben como tablas. La solución original es interactiva (se elige la respuesta con el ratón)."
---

## Enunciado

En Matelandia nos encontramos familias de números formadas por tres números primos de tres dígitos cada uno, y en cada una de ellas se utilizan todos los dígitos del 1 al 9 una sola vez. Observa tres de estas familias:

| | | |
|---|---|---|
| 127 | 463 | 859 |
| 149 | 563 | 827 |
| 239 | 461 | 587 |

El Sr. Miletos está intentando reunificar a otras dos familias de números primos que se encuentran dispersas por Matelandia. Ayúdale averiguando los números que le faltan a cada una de estas familias:

| | | |
|---|---|---|
| ☐☐☐ | ☐☐☐ | 461 |
| 659 | ☐☐☐ | ☐☐☐ |

Sabiendo que en la primera de las familias el número primo mayor es el 461, y en la segunda de las familias el número primo menor es el 659.

**Razona las respuestas.**

## Solución

**Primera familia.** Faltan las cifras 2, 3, 5, 7, 8 y 9. Como 461 es el mayor, las centenas de los otros dos números son menores que 4: son el **2** y el **3**. Las unidades de un primo de tres cifras no pueden ser pares ni 5, así que, de las cifras 5, 7, 8, 9, las unidades son 7 y 9 y las decenas, 5 y 8. Quedan cuatro posibilidades: 257 y 389, 259 y 387, 287 y 359, 289 y 357. Pero $259 = 7 \cdot 37$, $387 = 3 \cdot 129$, $287 = 7 \cdot 41$, $289 = 17^2$ y $357 = 3 \cdot 119$. La única familia de primos es

**257, 389 y 461.**

**Segunda familia.** Faltan las cifras 1, 2, 3, 4, 7 y 8. Como 659 es el menor, las centenas de los otros dos son mayores que 6: el **7** y el **8**. Las unidades, impares y distintas de 5, son 1 y 3, y las decenas, 2 y 4. De las posibilidades 721 y 843, 723 y 841, 741 y 823, 743 y 821, solo la última está formada por primos ($721 = 7 \cdot 103$, $843 = 3 \cdot 281$, $723 = 3 \cdot 241$, $841 = 29^2$, $741 = 3 \cdot 247$). La familia es

**659, 743 y 821.**
