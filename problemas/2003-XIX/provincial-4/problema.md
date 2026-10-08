---
id: 2003-provincial-4
edicion: 2003-XIX
fase: provincial
numero: 4
titulo: Los hermanos golosos
bloques: [geometria, numeros]
bloques_thales: [numeros]
etiquetas: [cuerpos, divisibilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0403, F0406]
estado: borrador
notas: "La solución original da el reparto 25, 10, 20, 5 y 15 (caja de 5 × 5 × 3) y descarta otro en el que la cara superior no sería cuadrada. Hay además otra caja válida, de 3 × 3 × 7, con el reparto 9, 18, 6, 15 y 15, que la solución original no considera."
---

## Enunciado

![Ilustración: el abuelo Pinto](ilustracion.png)

El abuelo Pinto le ha regalado a sus nietos una estupenda caja de bombones con forma de prisma de base cuadrada y los chicos se han repartido el preciado contenido de una curiosa manera en función de su edad: Abrieron la caja por la parte superior, que era la cuadrada y por un lateral. A Fermín, que es el mayor, le correspondieron los bombones de la capa superior. A continuación se sirvió Piluca, llevándose los bombones que había en el costado abierto. Después fue el turno de Lola, que se sirvió llevándose los de la capa superior. Ahora le tocó a Pepito, el más pequeño, que tomó los que se encontró por la parte lateral, y la última en servirse fue Maruja, quien se llevó los quince bombones que quedaban en la última capa de la caja.

¿Cuántos bombones correspondieron a cada hermano?

## Solución

Conviene empezar por el final. Si la caja tiene base cuadrada de $n \times n$ bombones y $h$ capas, cada vez que alguien se sirve la caja pierde una «rebanada»:

| Quién | Se lleva | Queda una caja de |
|---|---|---|
| Fermín (capa superior) | $n \cdot n$ | $n \times n \times (h-1)$ |
| Piluca (lateral) | $n \cdot (h-1)$ | $n \times (n-1) \times (h-1)$ |
| Lola (capa superior) | $n \cdot (n-1)$ | $n \times (n-1) \times (h-2)$ |
| Pepito (lateral) | $n \cdot (h-2)$ | $n \times (n-2) \times (h-2)$ |

Lo que queda para Maruja es una sola capa de 15 bombones: $n \cdot (n-2) \cdot (h-2) = 15$. Si los 15 forman una fila de $5 \times 3$ con $n = 5$, entonces $n - 2 = 3$ y $h - 2 = 1$, es decir, la caja era de $5 \times 5 \times 3 = 75$ bombones y el reparto fue:

- Fermín: $5 \cdot 5 = 25$ bombones.
- Piluca: $5 \cdot 2 = 10$.
- Lola: $5 \cdot 4 = 20$.
- Pepito: $5 \cdot 1 = 5$.
- Maruja: 15.

Si colocamos los 15 últimos bombones de la otra forma posible (el lado de 5 hacia arriba), la caja reconstruida no tendría la cara superior cuadrada, así que no es válida.
