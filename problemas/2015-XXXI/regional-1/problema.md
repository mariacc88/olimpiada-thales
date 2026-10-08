---
id: 2015-regional-1
edicion: 2015-XXXI
fase: regional
numero: 1
titulo: Números buenos y malos
bloques: [numeros]
bloques_thales: []
etiquetas: [fracciones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0849]
estado: borrador
notas: "La solución original comprueba una por una todas las descomposiciones de los números del 2 al 8."
---

## Enunciado

Don Odón Betanzos ha encargado a sus paisanas Isa y Rocío, entusiastas en el estudio de los números, que investiguen sobre los números buenos y malos.

Rocío, después de leer un famoso libro de matemáticas, le dice a Isa: «¿Sabes que los números buenos son números enteros mayores o iguales que 2 que pueden escribirse como la suma de números naturales no nulos, distintos o no, de modo que la suma de sus inversos es igual a 1, y los números malos son aquellos que no son buenos, es decir, que no cumplen la propiedad anterior?».

Por ejemplo, 18 es un número bueno, porque $18 = 3 + 3 + 6 + 6$ y $\frac{1}{3} + \frac{1}{3} + \frac{1}{6} + \frac{1}{6} = 1$.

Ya que Rocío ha explicado cuándo un número es bueno o malo, ayuda a Isa en su labor de investigación contestando **de forma razonada** a las siguientes cuestiones:

a) ¿Cuáles son los números buenos que se encuentran del 2 al 10, ambos inclusive?

b) Una vez que has calculado cuáles son los buenos, ¿puedes afirmar que sus cuadrados también lo son?

c) Si un número natural cualquiera $n$ es bueno, ¿se puede afirmar que su cuadrado también lo es?

## Solución

a) Si en la descomposición aparece un 1, la suma de inversos ya es al menos 1 y, con más sumandos, mayor que 1; así que solo sirven sumandos mayores o iguales que 2. Probando las descomposiciones de cada número:

- 2, 3: solo 1 + 1, 1 + 1 + 1, 1 + 2, que contienen un 1. Malos.
- 4 = 2 + 2 y $\frac{1}{2} + \frac{1}{2} = 1$. **Bueno**.
- 5 = 2 + 3: $\frac{5}{6} \ne 1$. Malo.
- 6 = 2 + 4, 3 + 3, 2 + 2 + 2: $\frac{3}{4}$, $\frac{2}{3}$, $\frac{3}{2}$. Malo.
- 7 = 2 + 5, 3 + 4, 2 + 2 + 3: $\frac{7}{10}$, $\frac{7}{12}$, $\frac{4}{3}$. Malo.
- 8 = 2 + 6, 3 + 5, 4 + 4, 2 + 2 + 4, 2 + 3 + 3, 2 + 2 + 2 + 2: $\frac{2}{3}$, $\frac{8}{15}$, $\frac{1}{2}$, $\frac{5}{4}$, $\frac{7}{6}$, $2$. Malo.
- 9 = 3 + 3 + 3 y $\frac{1}{3} + \frac{1}{3} + \frac{1}{3} = 1$. **Bueno**.
- 10 = 2 + 4 + 4 y $\frac{1}{2} + \frac{1}{4} + \frac{1}{4} = 1$. **Bueno**.

Los números buenos del 2 al 10 son **4, 9 y 10**.

b) Sí: $16 = 4 + 4 + 4 + 4$ con $4 \cdot \frac{1}{4} = 1$; $81$ es la suma de nueve nueves, con $9 \cdot \frac{1}{9} = 1$, y $100$ es la suma de diez dieces, con $10 \cdot \frac{1}{10} = 1$.

c) Sí, y de hecho el cuadrado de **cualquier** número $n \ge 2$ es bueno, sea $n$ bueno o no: $n^2$ es la suma de $n$ sumandos iguales a $n$, y la suma de sus inversos es $n \cdot \frac{1}{n} = 1$.
