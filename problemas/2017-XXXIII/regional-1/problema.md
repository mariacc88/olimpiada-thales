---
id: 2017-regional-1
edicion: 2017-XXXIII
fase: regional
numero: 1
titulo: Bolas enumeradas
bloques: [numeros]
bloques_thales: []
etiquetas: [cifras]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0876]
estado: borrador
notas: ""
---

## Enunciado

Enrique tiene 2017 bolas, numeradas del 1 al 2017, de manera que las bolas cuya suma de cifras es la misma son del mismo color. Es decir, si tenemos dos bolas y la suma de las cifras de cada una de ellas es diferente, ambas bolas son de colores distintos.

Entre las 2017 bolas, ¿cuántos colores diferentes tendremos?

**Razona tu respuesta.**

## Solución

Hay tantos colores como valores distintos puede tomar la suma de las cifras. Dividimos las bolas en cuatro grupos:

- Del 1 al 99, las sumas van de 1 a 18 (la de 99).
- Del 100 al 999, de 1 a 27 (la de 999).
- Del 1000 al 1999, de 1 a 28 (la de 1999).
- Del 2000 al 2017, de 2 a 10 (la de 2017 es 10, y la de 2009, 11; en cualquier caso, valores ya obtenidos).

Las sumas posibles son todos los números del 1 al 28, y todos aparecen. Hay **28 colores diferentes**.
