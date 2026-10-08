---
id: 2008-provincial-4
edicion: 2008-XXIV
fase: provincial
numero: 4
titulo: Las tres amigas
bloques: [numeros, logica]
bloques_thales: [logica]
etiquetas: [ecuaciones, proporcionalidad, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0654, F0655]
estado: borrador
notas: ""
---

## Enunciado

En Matelandia, iban paseando las amigas Algebrina, Geometrina y Aritmetina cuando se encontraron con Thalecalculín, que las saludó efusivamente.

-*Como vais juntas todo el rato y sois tan altas y tan parecidas* --dijo-, *siempre os confundo a las tres. Sé que vuestros padres se llaman Leonardo Euler, Agustín Cauchy y Carlos Gauss, pero no tengo claro cuál de estos apellidos os corresponde a cada una*.

Las chicas, divertidas al ver la cara de desconcierto de Thalecalculín, decidieron proponerle el siguiente acertijo:

- *Has de saber que en nuestras familias nos gusta coleccionar sellos -*empezó a decir Algebrina-. *Entre las tres tenemos 198 sellos,* *pero yo tengo 5 sellos más que Geometrina, y Aritmetina tiene 5 sellos más que yo*.

-*En cuanto a nuestros padres* --continuó Geometrina-, *Leonardo Euler tiene tantos sellos como su hija, Agustín Cauchy tiene el doble que su hija, Carlos Gauss tiene una vez y media el número de sellos de su hija, y entre todos los padres y todas las hijas tenemos 500 sellos*.

**-¿Podrías decirnos nuestros nombres y apellidos?** --preguntó finalmente Aritmetina con una amplia sonrisa.

## Solución

Si Geometrina tiene $x$ sellos, Algebrina tiene $x + 5$ y Aritmetina $x + 10$:

$$x + (x + 5) + (x + 10) = 198 \;\Rightarrow\; x = 61.$$

Geometrina tiene 61 sellos, Algebrina 66 y Aritmetina 71.

Carlos Gauss tiene una vez y media los sellos de su hija, que tiene que ser un número entero: $1{,}5 \cdot 61 = 91{,}5$ y $1{,}5 \cdot 71 = 106{,}5$ no lo son, así que **Algebrina es Gauss** y su padre tiene 99 sellos. Para Euler y Cauchy quedan $500 - 198 - 99 = 203$ sellos.

- Si Euler fuera el padre de Aritmetina, tendría 71 y Cauchy 132, que no es el doble de 61.
- Si Euler es el padre de Geometrina, tiene 61 y Cauchy 142, que es el doble de 71. ✓

Son **Algebrina Gauss, Geometrina Euler y Aritmetina Cauchy**.
