---
id: 2024-provincial-6
edicion: 2024-XXXIX
fase: provincial
numero: 6
titulo: Bonificaciones por doquier
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [ecuaciones, divisibilidad, patrones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0994]
estado: borrador
notas: ""
---

## Enunciado

Maya es la encargada de una tienda de moda y decide repartir 736 € de bonificaciones entre sus dependientes. El mejor empleado del mes recibe 134 € y, a partir de él, la bonificación se va reduciendo en una cantidad fija para el resto de los empleados. Si el último recibe 50 €:

a) ¿Cuántos empleados hay en la tienda?

b) ¿Cuánto recibe el segundo mejor empleado?

**Razona tus respuestas.**

## Solución

**Primera forma.** Las bonificaciones forman una progresión aritmética de $n$ términos, de 50 € a 134 €. Su suma es

$$\frac{50 + 134}{2} \cdot n = 736 \;\Rightarrow\; 92n = 736 \;\Rightarrow\; n = 8.$$

a) Hay **8 empleados**.

b) Si la diferencia entre dos empleados consecutivos es $x$, entonces $50 + 7x = 134$, de donde $x = 12$. Las bonificaciones son 50, 62, 74, 86, 98, 110, 122 y 134 €: el segundo mejor empleado recibe **122 €**.

**Segunda forma.** De $50 + (n - 1)\,x = 134$ sale $(n - 1)\,x = 84$, con $n - 1$ y $x$ enteros, así que $n - 1$ es un divisor de 84. Además, como todos reciben al menos 50 €, $50n < 736$, es decir, $n \le 14$. Probando los divisores de 84 (1, 2, 3, 4, 6, 7, 12) y sumando las bonificaciones en cada caso, solo $n - 1 = 7$, $x = 12$ da una suma de 736 €.
