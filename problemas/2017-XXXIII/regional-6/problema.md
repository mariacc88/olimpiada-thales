---
id: 2017-regional-6
edicion: 2017-XXXIII
fase: regional
numero: 6
titulo: La tabla mágica
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [ecuaciones, patrones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0881]
estado: borrador
notas: "La tabla del enunciado era una imagen; se ha transcrito."
---

## Enunciado

Se disponen unos números en la siguiente tabla:

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 |
| 3 | **5** | **7** | 9 | 11 | 13 | 15 | 17 |
| 6 | **8** | **10** | 12 | 14 | 16 | 18 | 20 |
| 9 | 11 | 13 | 15 | 17 | 19 | 21 | 23 |

Nos fijamos en el cuadrado señalado en la tabla (en negrita), formado por dos filas y dos columnas consecutivas. Si multiplicamos en cruz los números que lo forman y al mayor de los dos valores le restamos el menor, se obtiene 6:

$$8 \cdot 7 - 5 \cdot 10 = 56 - 50 = 6.$$

a) ¿Ocurrirá lo mismo con cualquier cuadrado de la tabla formado por dos filas y dos columnas consecutivas? **Razona tu respuesta.**

b) Si nos fijamos ahora en cualquier cuadrado formado por tres filas y tres columnas consecutivas, multiplicamos en cruz los números de las esquinas y al mayor resultado le restamos el menor, ¿se obtendrá siempre el mismo resultado? ¿Cuál será? **Razona tus respuestas.**

## Solución

En la tabla, los números aumentan de 2 en 2 hacia la derecha y de 3 en 3 hacia abajo.

a) Por ejemplo, con el cuadrado 12, 14 / 15, 17: $15 \cdot 14 - 12 \cdot 17 = 210 - 204 = 6$. En general, un cuadrado de 2 × 2 tiene la forma

| | |
|---|---|
| $x$ | $x + 2$ |
| $x + 3$ | $x + 5$ |

y $(x + 3)(x + 2) - x\,(x + 5) = x^2 + 5x + 6 - x^2 - 5x = 6$. **Siempre se obtiene 6.**

b) Por ejemplo, con 9, 13 / 15, 19 (esquinas de un cuadrado de 3 × 3): $15 \cdot 13 - 9 \cdot 19 = 195 - 171 = 24$. En general, las esquinas son $x$, $x + 4$, $x + 6$ y $x + 10$:

$$(x + 6)(x + 4) - x\,(x + 10) = x^2 + 10x + 24 - x^2 - 10x = 24.$$

**Siempre se obtiene 24.**
