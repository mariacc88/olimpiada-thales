---
id: 2018-provincial-2
edicion: 2018-XXXIV
fase: provincial
numero: 2
titulo: En la curiosa frutería
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [ecuaciones, divisibilidad, deduccion]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0895]
estado: borrador
notas: ""
---

## Enunciado

En la frutería del barrio de las Matemáticas nunca te dicen lo que cuesta una pieza de fruta, pero si les dices el dinero que llevas y lo que quieres, te dicen si puedes llevarte lo que deseas.

María se quiere llevar una manzana, un plátano y una naranja, y ha ido con dos euros a la frutería.

El frutero le dice: *«Tienes bastante para las tres piezas e incluso tendrías justo para un plátano más»*.

Pero ella quiere saber el precio exacto y entonces le dice el frutero: *«Si decides llevarte solo un tipo de fruta, no puedes llegar a comprar cuatro plátanos, pero sí un máximo de cuatro manzanas. Además, si compras cinco naranjas ya no puedes comprar ninguna más»*.

María hace sus cuentas y ve que hay varias posibilidades, así que vuelve a preguntar al frutero, y este le dice: *«Siete naranjas cuestan lo mismo que cinco manzanas»*.

**Encuentra razonadamente** el precio máximo y mínimo de cada una de las piezas de fruta que ha pedido María y averigua así el precio de cada una de ellas.

## Solución

Llamamos $m$, $p$ y $n$ a los precios, en céntimos, de una manzana, un plátano y una naranja.

- Con el dinero justo para las tres piezas y un plátano más: $m + 2p + n = 200$.
- No llega para cuatro plátanos: $4p > 200$, así que $p \ge 51$.
- Llega para cuatro manzanas pero no para cinco: $4m \le 200 < 5m$, así que $41 \le m \le 50$.
- Llega para cinco naranjas pero no para seis: $5n \le 200 < 6n$, así que $34 \le n \le 40$.

Con $2p = 200 - m - n$, el plátano cuesta entre $\frac{200 - 50 - 40}{2} = 55$ y $\frac{200 - 41 - 34}{2} = 62{,}5$ céntimos (el original da el intervalo más amplio de 51 a 66 céntimos).

Por último, $7n = 5m$, así que $n$ es múltiplo de 5: $n = 35$ o $n = 40$. Si $n = 40$, $m = 56$, que es demasiado. Por tanto, $n = 35$, $m = 49$ y $2p = 200 - 49 - 35 = 116$.

La **naranja** cuesta **35 céntimos**, la **manzana** **49 céntimos** y el **plátano** **58 céntimos**.
