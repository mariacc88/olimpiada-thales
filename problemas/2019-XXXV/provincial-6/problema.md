---
id: 2019-provincial-6
edicion: 2019-XXXV
fase: provincial
numero: 6
titulo: Las baldosas trampa
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion, juegos]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0919]
estado: borrador
notas: "El tablero de la imagen original se transcribe como tabla."
---

## Enunciado

En la Casa de los Misterios, que es una novedosa atracción de feria que llegará a Córdoba este próximo mes de mayo, hay una pequeña habitación con 25 baldosas y las inscripciones que aparecen en la imagen. Las inscripciones constan de un número del 1 al 4 y una letra N, S, E y O, que indican las direcciones norte, sur, este y oeste.

|    |    |    |    |    |
|----|----|----|----|----|
| 1E | 2S | 4S | 1O | 2S |
| 4E | 3S | 1E | 2S | 3S |
| 1N | 1O | 1S | 2S | 2O |
| 3E | 2N | 1O | 1E | 3N |
| 4N | **última baldosa** | 3N | 4N | 1O |

La atracción consiste en pisar las baldosas en un orden adecuado; para ello es fundamental la inscripción de cada una de ellas. Por ejemplo, la baldosa 2S de la esquina superior derecha nos dice que la próxima baldosa que debe pisarse está dos baldosas en dirección sur, la que tiene escrito 2O.

Si se quiere salir triunfante de la atracción, se deben pisar **el máximo número de baldosas** siguiendo la secuencia correcta. Hay dos dificultades: una es que no sabemos cuál es la primera baldosa que hay que pisar, solo la última, y otra, que hay dos baldosas trampa que harán que caigas en un túnel sin salida.

Debes encontrar **de forma razonada** la primera baldosa que debes pisar para poder así iniciar el recorrido y señalar aquellas baldosas trampa que te harán perder automáticamente el juego.

## Solución

Conviene empezar por el final, buscando desde qué baldosas se puede llegar a cada una. A la última baldosa solo se llega desde el 3S de la segunda fila; a esta, desde el 2N de la cuarta fila; a esta, desde el 1O de su derecha, y así sucesivamente. Cuando una baldosa tiene dos posibles orígenes, uno de ellos resulta ser una baldosa a la que no se puede llegar desde ninguna otra:

- Al 1E de la cuarta fila se llega desde el 3E (cuarta fila, primera columna) o desde el 2S de la segunda fila. Al 3E no se llega desde ninguna baldosa, así que es una **baldosa trampa**.
- Al 4N de la última fila se llega desde el 2S (tercera fila, cuarta columna) o desde el 1O de su derecha. Al 2S tampoco se llega desde ninguna baldosa: es la otra **baldosa trampa**.

Deshaciendo todo el camino, la **primera baldosa es el 4N de la esquina inferior izquierda** y el recorrido pisa las otras 23 baldosas (fila, columna):

4N (5,1) → 1E (1,1) → 2S (1,2) → 1O (3,2) → 1N (3,1) → 4E (2,1) → 3S (2,5) → 1O (5,5) → 4N (5,4) → 1O (1,4) → 4S (1,3) → 3N (5,3) → 1E (2,3) → 2S (2,4) → 1E (4,4) → 3N (4,5) → 2S (1,5) → 2O (3,5) → 1S (3,3) → 1O (4,3) → 2N (4,2) → 3S (2,2) → última baldosa (5,2).

Las baldosas trampa son el **3E** de la cuarta fila y primera columna y el **2S** de la tercera fila y cuarta columna.
