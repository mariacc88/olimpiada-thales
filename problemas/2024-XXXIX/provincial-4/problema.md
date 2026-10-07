---
id: 2024-provincial-4
edicion: 2024-XXXIX
fase: provincial
numero: 4
titulo: Situación de aprendizaje
bloques: [logica, estadistica, numeros]
bloques_thales: []
etiquetas: [deduccion, estadistica-descriptiva, fracciones]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0992]
estado: borrador
notas: ""
---

## Enunciado

Con la nueva ley de educación, los alumnos deben acostumbrarse a las nuevas calificaciones basadas en situaciones de aprendizaje (SdA), que van asociadas a ciertos criterios de evaluación. Por eso, el profesor de Matemáticas de 2.º de ESO ha evaluado en el primer trimestre seis de esos criterios. Tres alumnos escogidos al azar, Ana, Berto y Carla (a partir de ahora, A, B y C), han sido evaluados.

Partiendo de las siguientes premisas, debes averiguar razonadamente qué nota ha obtenido cada alumno en cada uno de los 6 criterios, y sus notas medias:

- Las notas de los criterios van del 0 al 10, y ningún alumno repitió nota en dos criterios. Entre los tres alumnos aparecen todas las notas del 0 al 10.
- La nota media de A ha sido 6; la de B, un número natural, y la de C, un número racional no entero.
- Los tres tuvieron en los criterios 4 y 5 la misma nota. La media de esos dos criterios es 6, que coincide con la nota que compartieron A y C en el criterio 6, cuya media es un 5.
- A y B compartieron en el criterio 3 la misma nota, que fue la máxima. En cambio, B y C compartieron en el criterio 1 la peor de las notas posibles.
- La media del criterio 2 es un 7.

¿Podrías decir también qué tipo de número racional ha obtenido Carla en su media?

## Solución

- **Criterios 4, 5 y 6.** En el criterio 6, A y C tienen un 6 y la media es 5, así que B tiene un 3. Los tres tienen la misma nota en el criterio 4 y en el 5, y su media es 6; como nadie repite nota, ninguna puede ser 6. La solución es un 4 en el criterio 4 y un 8 en el 5.
- **Criterios 3 y 1.** A y B tienen un 10 en el criterio 3; B y C tienen un 0 en el criterio 1.
- **Criterio 2 y media de B.** B tiene ya $0 + 10 + 4 + 8 + 3 = 25$ puntos; para que $\frac{25 + x}{6}$ sea natural, $x = 5$, y su media es 5.
- **A y C en el criterio 2.** La media es 7, así que A y C suman 16 en ese criterio. Para que la media de A sea 6, A tiene un 7 en el criterio 2 y un 1 en el criterio 1, y C un 9.
- **Criterio 3 de C.** Falta la nota 2, que es la de C.

| | C1 | C2 | C3 | C4 | C5 | C6 | Media |
|---|---|---|---|---|---|---|---|
| A | 1 | 7 | 10 | 4 | 8 | 6 | 6 |
| B | 0 | 5 | 10 | 4 | 8 | 3 | 5 |
| C | 0 | 9 | 2 | 4 | 8 | 6 | 4,8333… |
| Media | 0,33… | 7 | 7,33… | 4 | 8 | 5 | |

La media de Carla es $\frac{29}{6} = 4{,}8\overline{3}$, un **decimal periódico mixto**.
