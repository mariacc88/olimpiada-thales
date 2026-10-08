---
id: 2012-provincial-6
edicion: 2012-XXVIII
fase: provincial
numero: 6
titulo: Tarjetas numeradas
bloques: [numeros]
bloques_thales: []
etiquetas: [divisibilidad, numeros-primos]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1043]
estado: borrador
notas: "Como en la solución original, «múltiplos de seis y de ocho» se interpreta como múltiplos de ambos a la vez, es decir, de 24. Si se quitaran los múltiplos de 6 o de 8 quedarían 5 tarjetas (2, 4, 14, 28 y 98)."
---

## Enunciado

Calculín, Pitagorín, Thalesa, Hipotenusia y Arquimedín tienen un montón de 100 tarjetas enumeradas del 1 al 100. Como son muy maniáticos con los números, se dedican a incluir o quitar del montón aquellas tarjetas según le gusten o no los números que en ellas aparecen.

Calculín toma las cien tarjetas y, como detesta los números pares, los descarta y pasa las tarjetas a Pitagorín; este, que es un amante de los múltiplos de cinco, se da cuenta de que le faltan algunos, y los coge de los que Calculín eliminó, y seguidamente le entrega las tarjetas a Thalesa.

Thalesa, como está enfadada con Calculín y Pitagorín, decide deshacerse de ellas y coger las tarjetas que estos habían descartado y se las pasa a Hipotenusia.

Hipotenusia, tras observarlas, elimina aquellas que son múltiplos de seis y de ocho porque las considera de mal gusto y finalmente se las pasa a Arquimedín, que odia tanto los números primos mayores que 7 que elimina las tarjetas que tienen como divisor alguno de esos números.

Arquimedín hace recuento de las tarjetas que le quedan. ¿Cuántas tarjetas tiene ahora en su poder? ¿Cuál es el mayor número escrito en esas tarjetas? **Razona las respuestas.**

## Solución

- Calculín se queda con los impares y Pitagorín añade los múltiplos de 5 que faltaban (10, 20, …, 100).
- Thalesa se queda con las tarjetas descartadas: los números pares que no son múltiplos de 10 (40 tarjetas).
- Hipotenusia quita los múltiplos de 6 y de 8, es decir, de 24: el 24, el 48 y el 72.
- Arquimedín quita los que tienen algún divisor primo mayor que 7 (22, 26, 34, 38, 44, 46, …).

Quedan **17 tarjetas**: 2, 4, 6, 8, 12, 14, 16, 18, 28, 32, 36, 42, 54, 56, 64, 84 y 98. La mayor es la **98** ($= 2 \cdot 7^2$).
