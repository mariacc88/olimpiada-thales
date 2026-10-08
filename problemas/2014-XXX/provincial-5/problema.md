---
id: 2014-provincial-5
edicion: 2014-XXX
fase: provincial
numero: 5
titulo: Los billetes del bus
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [cifras, ecuaciones, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0843]
estado: borrador
notas: ""
---

## Enunciado

Raquel y su hermana Ana van todos los días a clase en el autobús de la línea 62. Raquel paga siempre los billetes. Cada billete tiene impreso un número de 5 cifras.

Una mañana observa que los números de sus billetes, el suyo y el de Ana, además de consecutivos, son tales que la suma de las diez cifras es precisamente 62. Además, observa que las cifras del menor de los números van todas ellas consecutivas.

Ana entonces le dice: «Si la suma de las cifras de uno de los billetes es 35, puedo decirte el número de cada billete».

¿Cuáles eran esos números?

**Razona la respuesta.**

## Solución

Como las cifras del billete menor son consecutivas, es de la forma $A,\ A+1,\ A+2,\ A+3,\ A+4$, y la suma de sus cifras es $5A + 10$.

- Si $A + 4 < 9$, el siguiente número solo cambia la última cifra: $A,\ A+1,\ A+2,\ A+3,\ A+5$, con suma $5A + 11$. Entre los dos sumarían $10A + 21 = 62$, que no tiene solución entera.
- Si $A + 4 = 9$, es decir, $A = 5$, el billete menor es 56789 y el siguiente es 56790. Las sumas son 35 y 27, y en total $35 + 27 = 62$.

Con la pista de Ana se llega a lo mismo: si fuera el billete mayor el que suma 35, el menor sumaría $62 - 35 = 27 = 5A + 10$, imposible; así que el menor suma $35 = 5A + 10$ y $A = 5$.

Los billetes son el **56789** y el **56790**.
