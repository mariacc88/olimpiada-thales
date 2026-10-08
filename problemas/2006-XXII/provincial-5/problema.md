---
id: 2006-provincial-5
edicion: 2006-XXII
fase: provincial
numero: 5
titulo: La suerte está en los números
bloques: [numeros, estadistica]
bloques_thales: []
etiquetas: [divisibilidad, probabilidad]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0553, F0555]
estado: borrador
notas: ""
---

## Enunciado

En una Olimpiada se ha numerado a los participantes del 1 al 500. De entre ellos, se va a seleccionar un grupo para hacer una encuesta. El participante número 462 quisiera ser seleccionado porque sabe que sortearán un regalo entre los encuestados.

Las formas que se están estudiando para realizar la selección son:

a) Elegir a todos los participantes con número par.

b) Elegir a todos los participantes con número múltiplo de 11.

c) Elegir a todos los participantes con número par y múltiplo de 11.

d) Elegir a todos los participantes con número múltiplo de 3 y de 7.

**¿Con cuál de los cuatro criterios tiene más posibilidades de conseguir el regalo el olímpico 462? **

## Solución

Como $462 = 2 \cdot 3 \cdot 7 \cdot 11$, el número 462 cumple los cuatro criterios. Tendrá más posibilidades con el criterio que seleccione a menos participantes. Entre 1 y 500 hay:

a) 250 números pares.

b) 45 múltiplos de 11 ($500 = 11 \cdot 45 + 5$).

c) 22 números pares y múltiplos de 11, es decir, múltiplos de 22 ($500 = 22 \cdot 22 + 16$).

d) 23 múltiplos de 3 y de 7, es decir, múltiplos de 21 ($500 = 21 \cdot 23 + 17$).

Le conviene el **criterio c**, con el que solo hay 22 seleccionados.
