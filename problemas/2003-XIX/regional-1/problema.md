---
id: 2003-regional-1
edicion: 2003-XIX
fase: regional
numero: 1
titulo: Apaga y vámonos
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion, juegos]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0413, F0415]
estado: borrador
notas: ""
---

## Enunciado

A la fiesta de fin de curso del «insti» vendrá nada más y nada menos que la popular Pimpolina Rubio. A Pepito le han encomendado la iluminación del escenario y hay una avería que hace que cuando se toca uno de los seis focos, éste se queda como estaba y todos los demás cambian (es decir, el foco que estuviera encendido se apaga y el que estuviera apagado se enciende).

A) Si durante la actuación están los seis focos encendidos, ¿podrías indicarle a Pepito cómo debe apagarlos?

B) Si en lugar de seis focos hubiera sólo tres, ¿podría apagarlos Pepito?

(En uno y otro caso sólo se puede proceder tocando un foco cada vez)

## Solución

**A)** Basta con tocar **cada uno de los seis focos una vez** (en cualquier orden). Cada foco se queda igual cuando se le toca a él y cambia cuando se toca cualquiera de los otros cinco, así que al final ha cambiado 5 veces: un número impar de veces. Como estaban todos encendidos, todos acaban apagados.

| Foco tocado | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Ninguno | ● | ● | ● | ● | ● | ● |
| 1 | ● | ○ | ○ | ○ | ○ | ○ |
| 2 | ○ | ○ | ● | ● | ● | ● |
| 3 | ● | ● | ● | ○ | ○ | ○ |
| 4 | ○ | ○ | ○ | ○ | ● | ● |
| 5 | ● | ● | ● | ● | ● | ○ |
| 6 | ○ | ○ | ○ | ○ | ○ | ○ |

(● encendido, ○ apagado.)

**B)** Con tres focos **no es posible**. Cada vez que se toca un foco cambian los otros dos, así que el número de focos encendidos varía en 0 o en 2 (por ejemplo, de 3 a 1 o de 1 a 3): siempre sigue siendo impar. Empezando con 3 encendidos, nunca se puede llegar a 0.
