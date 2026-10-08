---
id: 2010-provincial-6
edicion: 2010-XXVI
fase: provincial
numero: 6
titulo: Deliciosos caramelos
bloques: [numeros, estadistica]
bloques_thales: []
etiquetas: [ecuaciones, combinatoria]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0784, F0774, F1082]
estado: borrador
notas: "El nodo de la web solo contenía un applet de GeoGebra; el enunciado se ha tomado de las hojas individuales de la prueba y la solución, de los textos del fichero 266p.ggb."
---

## Enunciado

![Ilustración: Pepito con un caramelo](ilustracion.png)

Pepito Tragalotodo posee una bolsa con 71 deliciosos caramelos de los siguientes sabores: limón, naranja, fresa y menta. Hay el doble número de caramelos de limón que de fresa; los caramelos de naranja son uno menos que los de fresa y los de menta son seis caramelos menos que los de limón.

Pepito quiere comerse dos caramelos del mismo sabor. **¿Cuál es el mínimo número de caramelos que tiene que sacar para estar seguro de tener por lo menos dos caramelos del mismo sabor?**

**¿Y cuántos de estos deliciosos caramelos tendría que sacar como mínimo para estar seguro de poder comerse por lo menos dos sabores?**

**Razona las respuestas.**

## Solución

Si hay $F$ caramelos de fresa, hay $2F$ de limón, $F - 1$ de naranja y $2F - 6$ de menta. En total, $6F - 7 = 71$, así que $F = 13$: hay **26 de limón, 12 de naranja, 13 de fresa y 20 de menta**.

- **Dos del mismo sabor.** En el peor de los casos, los cuatro primeros son de sabores distintos; el quinto repite sabor seguro. Hay que sacar **5 caramelos**.
- **Dos sabores distintos.** En el peor de los casos salen seguidos todos los del sabor más abundante, los 26 de limón; el siguiente es de otro sabor. Hay que sacar **27 caramelos**.
