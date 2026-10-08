---
id: 2013-regional-2
edicion: 2013-XXIX
fase: regional
numero: 2
titulo: El lejano oeste
bloques: [estadistica]
bloques_thales: []
etiquetas: [probabilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1065]
estado: borrador
notas: "En el apartado b, un 19 de Clint sería empate, no victoria, como interpreta la solución original."
---

## Enunciado

En un salón del Lejano Oeste juegan a las cartas Clint McGauss, John Euclidean, Kirk O'Newton y Robert Einsteniak. El juego consiste en obtener 21 puntos o quedarse lo más cerca posible, pero sin pasarse. Cada carta desde el 2 hasta el 10 tiene un valor igual a su número, las figuras (J, Q y K) valen 11 y el as vale 1. Además, hay cuatro palos para cada conjunto de esas 13 cartas: picas ♠, tréboles ♣, diamantes ♦ y corazones ♥.

En la primera mano se reparten 2 cartas boca arriba a cada jugador:

- Clint McGauss: 6 de ♣ y 5 de ♠.
- John Euclidean: 8 de ♦ y J de ♠.
- Kirk O'Newton: 4 de ♥ y as de ♦.
- Robert Einsteniak: 3 de ♥ y 7 de ♣.

a) ¿Cuántas posibilidades de obtener 21 puntos tiene Clint McGauss si pide una tercera carta? ¿Y de sobrepasar los 21 puntos?

b) John Euclidean no sabe si plantarse o pedir más cartas. Como es un poco tramposo, ha marcado la baraja y sabe que la carta que le va a tocar a Clint McGauss es de corazones ♥. ¿Qué posibilidad hay de que Clint McGauss le gane con esa única carta de más, si él se planta?

**Razona las respuestas.**

## Solución

La baraja tiene $4 \cdot 13 = 52$ cartas; se han repartido 8, así que quedan 44.

a) Clint tiene $6 + 5 = 11$ puntos.

- Para llegar a 21 necesita una carta que valga 10. No ha salido ningún 10, así que quedan los 4: tiene **4 posibilidades de 44**, un $9{,}09$ %.
- Se pasa de 21 si la carta vale más de 10, es decir, si es una figura. Hay 12 figuras y ha salido la J de picas: quedan 11, así que tiene **11 posibilidades de 44**, un 25 %.

b) John tiene $8 + 11 = 19$ puntos. Clint le gana si llega a 20 o 21, es decir, si su carta vale 9 o 10. Entre los corazones quedan $13 - 2 = 11$ cartas (han salido el 4 y el 3), y de ellas solo el 9 y el 10 le sirven: **2 posibilidades de 11**, un $18{,}18$ %.
