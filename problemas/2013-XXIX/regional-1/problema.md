---
id: 2013-regional-1
edicion: 2013-XXIX
fase: regional
numero: 1
titulo: El cumpleaños
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [divisibilidad, numeros-primos, cifras, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1064]
estado: borrador
notas: ""
---

## Enunciado

Pitagorín se ha apostado un refresco con Pascalina. Si Pascalina adivina su fecha de cumpleaños, invita él; pero si no es capaz de hacerlo, será Pascalina quien lo invite.

Pitagorín le ha dejado una tabla que asigna a cada mes un número:

| Enero | Febrero | Marzo | Abril | Mayo | Junio | Julio | Agosto | Septiembre | Octubre | Noviembre | Diciembre |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

Y le ha dado tres pistas:

a) El número del mes de mi cumpleaños tiene una cantidad impar de divisores.

b) La suma del día y del mes de mi cumpleaños da como resultado un número primo.

c) Si multiplico el día por el mes de mi cumpleaños, obtengo un número de tres cifras en el que la suma de la primera y la última cifra es igual a la segunda cifra.

Indica razonadamente la fecha del cumpleaños de Pitagorín para ayudar a Pascalina.

## Solución

**Pista a.** Contando divisores de los números del 1 al 12, solo tienen una cantidad impar el 1 (uno), el 4 (tres: 1, 2, 4) y el 9 (tres: 1, 3, 9), que son los cuadrados perfectos. El mes es enero, abril o septiembre.

**Pista c.** En enero el producto es el propio día, que no tiene tres cifras. En abril el día debe ser al menos 25, y en septiembre, al menos 12.

**Pista b.** En abril, $4 + d$ es primo para $d = 25$ (29) y $d = 27$ (31); los productos son 100 y 108, y ninguno cumple la pista c ($1 + 0 \ne 0$, $1 + 8 \ne 0$). En septiembre, $9 + d$ es primo para $d = 14, 20, 22, 28$ (23, 29, 31, 37), con productos 126, 180, 198 y 252. Solo 198 cumple la pista c: $1 + 8 = 9$.

El cumpleaños de Pitagorín es el **22 de septiembre**.
