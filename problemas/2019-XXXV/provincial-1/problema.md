---
id: 2019-provincial-1
edicion: 2019-XXXV
fase: provincial
numero: 1
titulo: La contraseña
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [cifras, divisibilidad, deduccion]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0914]
estado: borrador
notas: ""
---

## Enunciado

A Miguel le regalaron una tableta por su cumpleaños y, para evitar que nadie pueda usarla, se inventó una contraseña de cinco cifras. Por si acaso se olvidaba de ella, escribió las siguientes pistas en un WhatsApp que le envió a Sagrario, su amiga de confianza:

![Ilustración: una tableta](ilustracion.png)

- Todas sus cifras son números impares.
- La suma de sus cifras es 25.
- La primera cifra es la diferencia entre el doble de la quinta cifra y la cuarta cifra.
- La cuarta cifra es un múltiplo de tres.
- El mínimo común múltiplo de la segunda y la quinta cifra es 15.
- La contraseña es el menor número que cumple las condiciones anteriores.

Lo peor ha ocurrido: se olvidó de la contraseña. Ayuda a Miguel recuperando su contraseña.

**Razona tu respuesta.**

## Solución

Llamamos $a, b, c, d, e$ a las cifras. Las pistas dicen:

- Las cifras son 1, 3, 5, 7 o 9.
- $a + b + c + d + e = 25$.
- $a = 2e - d$.
- $d$ es múltiplo de 3 e impar: $d = 3$ o $d = 9$.
- $\text{m.c.m.}(b, e) = 15$ con cifras impares: $b = 3$ y $e = 5$, o $b = 5$ y $e = 3$.

Estudiamos los cuatro casos:

- $b = 3$, $e = 5$, $d = 3$: $a = 10 - 3 = 7$ y $c = 25 - 7 - 3 - 3 - 5 = 7$. Contraseña 73735.
- $b = 3$, $e = 5$, $d = 9$: $a = 10 - 9 = 1$ y $c = 25 - 1 - 3 - 9 - 5 = 7$. Contraseña 13795.
- $b = 5$, $e = 3$, $d = 3$: $a = 6 - 3 = 3$ y $c = 25 - 3 - 5 - 3 - 3 = 11$, que no es una cifra.
- $b = 5$, $e = 3$, $d = 9$: $a = 6 - 9 = -3$, imposible.

Hay dos números que cumplen las cinco primeras pistas, 73735 y 13795. Como la contraseña es el menor, la contraseña de Miguel es **13795**.
