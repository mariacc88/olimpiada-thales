---
id: 2025-regional-1
edicion: 2025-XL
fase: regional
numero: 1
titulo: Operando con potencias
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [cifras, patrones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1003]
estado: borrador
notas: ""
---

## Enunciado

Salvador le ha propuesto a su hijo Pablo que investigue y averigüe cuál va a ser la cifra de las unidades del resultado de las siguientes operaciones:

$$\left(3^{2024} + 2^{2025}\right) \cdot 5^{40} \qquad\qquad \left(3^{2024} - 2^{2025}\right) \cdot 7^{40}$$

Ayuda a Pablo calculando de forma razonada cuál será esa cifra en cada caso.

## Solución

**Primera operación.** $3^{2024}$ es impar (las potencias de 3 terminan en 3, 9, 7 o 1) y $2^{2025}$ es par, así que su suma es impar. $5^{40}$ termina en 5, y un impar por un número terminado en 5 termina en 5. La cifra de las unidades es **5**.

**Segunda operación.** Las cifras de las unidades de las potencias se repiten cíclicamente cada cuatro exponentes:

- Potencias de 3: 3, 9, 7, 1, … Como $2024$ es múltiplo de 4, $3^{2024}$ termina en **1**.
- Potencias de 2: 2, 4, 8, 6, … Como $2025$ da resto 1 al dividir entre 4, $2^{2025}$ termina en **2**.
- Potencias de 7: 7, 9, 3, 1, … Como $40$ es múltiplo de 4, $7^{40}$ termina en **1**.

$3^{2024}$ es mayor que $2^{2025}$, así que la resta es positiva y termina en $11 - 2 = 9$. Multiplicada por un número terminado en 1, sigue terminando en 9. La cifra de las unidades es **9**.
