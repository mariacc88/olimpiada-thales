---
id: 2010-provincial-3
edicion: 2010-XXVI
fase: provincial
numero: 3
titulo: El número secreto
bloques: [numeros]
bloques_thales: []
etiquetas: [cifras, ecuaciones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0779, F0774, F1078]
estado: borrador
notas: "El nodo de la web solo contenía un applet de GeoGebra; el enunciado se ha tomado de las hojas individuales de la prueba y la solución, de los textos del fichero 263p.ggb."
---

## Enunciado

La caja fuerte del Banco Nacional Todolandés tiene una combinación formada por siete dígitos o cifras, que es el secreto mejor guardado de todo el país. Pero su director, el Sr. Olvidalotodo, ha sufrido uno de sus habituales lapsus mentales. Después de mucho preguntarle hemos logrado que recuerde las siguientes pistas:

- Las tres primeras cifras forman un número que es igual al producto del número formado por la 4.ª y la 5.ª cifra y el número constituido por las dos últimas cifras.
- El número de dos cifras formado por la 4.ª y la 5.ª cifra es igual al doble del número formado por las dos últimas cifras más dos.
- La suma de las dos últimas cifras es 4.

**¿Serías capaz de averiguar y decirle al Sr. Olvidalotodo cuál es el número secreto de la combinación de la caja fuerte del Banco?** Así podrá abrir sus puertas y atender a sus clientes.

**Razona la respuesta.**

## Solución

Llamamos $A$ al número de las tres primeras cifras, $B$ al de la 4.ª y 5.ª y $C$ al de las dos últimas. Las dos últimas cifras suman 4, así que $C$ es 40, 31, 22, 13 o 04. Entonces:

| $C$ | 40 | 31 | 22 | 13 | 04 |
|---|---|---|---|---|---|
| $B = 2C + 2$ | 82 | 64 | 46 | 28 | 10 |
| $A = B \cdot C$ | 3280 | 1984 | 1012 | 364 | 40 |

$A$ debe tener tres cifras y $B$ dos: solo sirve $C = 13$. El número secreto es **3642813**.
