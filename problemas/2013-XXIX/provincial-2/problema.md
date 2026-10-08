---
id: 2013-provincial-2
edicion: 2013-XXIX
fase: provincial
numero: 2
titulo: Enredando con la fecha
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [cifras, patrones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1059]
estado: borrador
notas: ""
---

## Enunciado

Hoy es sábado 16 de marzo de 2013. En Todolandia no paraban de darle vueltas a los números que formaban la fecha de la olimpiada, 16-3-2013, y nos han propuesto lo siguiente: ¿sabrías decir cuál es la última cifra de cada una de las siguientes cantidades?

a) $2013^3 - 16^3$

b) $(2013 : 3)^{16}$

c) $16^{2013} + 3^{2013}$

**Razona las respuestas.**

## Solución

La última cifra de un producto solo depende de las últimas cifras de los factores.

a) $2013^3$ acaba como $3 \cdot 3 \cdot 3 = 27$, en 7, y $16^3$ acaba como $6 \cdot 6 \cdot 6 = 216$, en 6. Como $2013^3 > 16^3$, la diferencia acaba en $7 - 6 =$ **1**.

b) $2013 : 3 = 671$, que acaba en 1, y cualquier potencia de un número acabado en 1 acaba en 1: la respuesta es **1**.

c) Todas las potencias de 16 acaban en 6. Las potencias de 3 acaban en 3, 9, 7, 1, 3, 9, 7, 1, …: las terminaciones se repiten cada cuatro exponentes. Como $2013 = 4 \cdot 503 + 1$,

$$3^{2013} = (3^4)^{503} \cdot 3,$$

y $3^4 = 81$ acaba en 1, así que $3^{2013}$ acaba en 3. La suma acaba en $6 + 3 =$ **9**.
