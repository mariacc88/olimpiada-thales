---
id: 2022-regional-3
edicion: 2022-XXXVII
fase: regional
numero: 3
titulo: Los dados de Julia y Andrés
bloques: [numeros, logica, geometria]
bloques_thales: []
etiquetas: [numeros-primos, deduccion, pitagoras]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0958]
estado: borrador
notas: "Tomado del PDF de soluciones de la fase regional (páginas 5-7). Los desarrollos de los dados de la solución original se describen como parejas de caras opuestas."
---

## Enunciado

Los dados «estándar» (de parchís) tienen forma de cubo, la suma de cada dos caras opuestas es siempre la misma y están compuestos por los números 1, 2, 3, 4, 5 y 6.

Andrés y Julia quieren construir dados «surrealistas» que cumplan las siguientes condiciones: que tengan forma de cubo, que las sumas de cada dos caras opuestas sean siempre la misma y que estén formados por seis números naturales distintos, siendo siempre el menor 3 y el mayor 13. Siguiendo estas instrucciones, cada uno construye un dado diferente.

Cuando Andrés empieza a jugar con el dado construido por él, comenta que lo ha lanzado tres veces y le han salido tres números con los que puede formar un triángulo rectángulo.

Julia lo intenta también con el suyo y no lo consigue, pero observa que, de los números elegidos por ella para sus caras, solo hay uno que no es primo.

Construye de forma razonada los dados de Julia y Andrés.

## Solución

El 3 tiene que estar enfrente del 13: si el 3 estuviera enfrente de otro número $n < 13$, la suma sería menor que 16 y el 13 no tendría pareja. Así que las caras opuestas suman 16, y las parejas posibles son

$$3 + 13 = 4 + 12 = 5 + 11 = 6 + 10 = 7 + 9 = 16$$

(8 + 8 no vale, porque los números no se pueden repetir). Cada dado tiene la pareja 3–13 y otras dos de estas.

**Dado de Andrés.** Con tres de sus números se puede formar un triángulo rectángulo, es decir, una terna pitagórica. Probando con los números posibles, las únicas ternas son $3^2 + 4^2 = 5^2$ y $5^2 + 12^2 = 13^2$, y las dos obligan a usar las parejas 4–12 y 5–11. El dado de Andrés tiene las caras opuestas **3–13, 4–12 y 5–11**.

**Dado de Julia.** Entre los números posibles, los primos son 3, 5, 7, 11 y 13. Como solo una de sus caras no es prima, sus parejas son 3–13, 5–11 y 7–9 (el 9 es el único no primo). El dado de Julia tiene las caras opuestas **3–13, 5–11 y 7–9**, y efectivamente con sus números no se forma ninguna terna pitagórica.
