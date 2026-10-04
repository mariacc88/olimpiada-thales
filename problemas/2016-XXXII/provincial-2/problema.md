---
id: 2016-provincial-2
edicion: 2016-XXXII
fase: provincial
numero: 2
titulo: Guardando monedas
bloques: [numeros]
bloques_thales: []
etiquetas: [fracciones, patrones]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0853]
estado: borrador
notas: ""
---

## Enunciado

D.ª Elvira Guardalotodo decide conservar toda su fortuna repartiéndola en los siete cofres que posee.

![Ilustración: un cofre lleno de monedas](ilustracion.png)

En el primer cofre guarda los $\frac{2}{3}$ del total de sus monedas; en el segundo cofre mete los $\frac{2}{3}$ del resto, y así sucesivamente hasta el séptimo cofre. Cuando hubo terminado, le quedaba a D.ª Elvira en las manos una única moneda, que guardó en su monedero.

¿Cuál es el total de monedas que compone la fortuna de D.ª Elvira Guardalotodo? ¿Cuántas monedas ha guardado en cada cofre?

Razona tus respuestas.

## Solución

Resolvemos el problema de atrás hacia delante. En cada cofre se guardan los $\frac{2}{3}$ de lo que se tiene, así que lo que queda después es $\frac{1}{3}$ de lo que había antes.

- La moneda final es $\frac{1}{3}$ de lo que tenía antes del 7.º cofre: tenía 3 y guardó 2.
- Esas 3 monedas son $\frac{1}{3}$ de lo que tenía antes del 6.º cofre: tenía 9 y guardó 6.
- Antes del 5.º cofre tenía 27 y guardó 18.
- Siguiendo igual: en el 4.º cofre guardó 54, en el 3.º 162, en el 2.º 486 y en el 1.º 1458.

El total se puede calcular de dos formas:

a) Sumando la moneda sobrante y las de los cofres: $1 + 2 + 6 + 18 + 54 + 162 + 486 + 1458 = 2187$ monedas.

b) Como 1458 monedas son los $\frac{2}{3}$ del total, este es $1458 \cdot 3 : 2 = 2187$ monedas.

La fortuna es de **2187 monedas** ($= 3^7$): 1458, 486, 162, 54, 18, 6 y 2 en los cofres 1.º a 7.º, y 1 en el monedero.
