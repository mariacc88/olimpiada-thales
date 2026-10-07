---
id: 2022-provincial-1
edicion: 2022-XXXVII
fase: provincial
numero: 1
titulo: Laberinto en el aulario de Ángel
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion, juegos]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0957]
estado: borrador
notas: "Tomado del PDF de soluciones de la fase provincial (páginas 1-4). La solución original introduce los puentes de Königsberg; en el PDF la figura de la solución del aula 5 está cortada, por eso no se incluye."
---

## Enunciado

Cinco aulas del IES de Ángel están divididas en compartimentos como se muestra en las figuras adjuntas. Ángel le propone a su hermano Jaime un reto: debe pasar por todos los compartimentos del aula en una sola visita, sin volver a cruzar por los que ya ha pasado, empezando por la flecha de entrada y terminando en la flecha de salida.

![Cinco aulas: tres de 3 × 3 compartimentos y dos de 4 × 4, cada una con una flecha de entrada y otra de salida](fig1.png)

Dibuja aquellas opciones donde sea posible recorrerlos con las condiciones anteriores.

## Solución

La situación se puede modelizar con la teoría de grafos, como el célebre problema de los siete puentes de Königsberg, que Euler resolvió en 1736 dando origen a esa teoría: los compartimentos son los vértices y las puertas entre ellos, las aristas.

**Aula 1.** Es posible, y de varias formas; por ejemplo:

![Dos recorridos posibles del aula 1](fig-solucion1.png)

**Aula 2.** Es **imposible**: cualquier intento, o bien deja un compartimento sin visitar, o bien pasa dos veces por el mismo.

**Aula 3.** Es posible, también de varias formas:

![Dos recorridos posibles del aula 3](fig-solucion2.png)

**Aula 4.** Es **imposible**, por el mismo motivo que el aula 2.

**Aula 5.** Sí es posible: se entra por la fila de abajo, se recorre de izquierda a derecha y se va subiendo en zigzag por las filas hasta llegar a la salida.

¿Hay alguna otra posibilidad en las aulas 1, 3 y 5?
