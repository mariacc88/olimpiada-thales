---
id: 2003-regional-4
edicion: 2003-XIX
fase: regional
numero: 4
titulo: Mala cabeza
bloques: [numeros]
bloques_thales: [numeros]
etiquetas: [cifras]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0423, F0425]
estado: borrador
notas: ""
---

## Enunciado

El profe de Informática tiene muy buena cabeza pero muy mala memoria. Nunca se acuerda de la contraseña para iniciar el sistema...

Como no quiere que la sepamos y es buen matemático, para que se la recordemos sólo nos ha dicho que es un número de 5 cifras que termina en 7, se pasa en cuatro unidades de un capicúa y le faltan 7 unidades para el siguiente capicúa.

Yo estoy intrigado, ¿sabrías ayudarme a averiguar la contraseña?

(Un número capicúa es aquel que se lee igual de izquierda a derecha que de derecha a izquierda, por ejemplo 23532)

## Solución

La contraseña tiene 5 cifras y termina en 7; al restarle 4 sale un capicúa y al sumarle 7 sale otro.

**Restando 4.** La contraseña es $\overline{abcd7}$ y $\overline{abcd7} - 4 = \overline{abcd3}$ es capicúa, así que $a = 3$ y $b = d$: la contraseña es $\overline{3bcb7}$.

**Sumando 7.** $\overline{3bcb7} + 7$ acaba en 4 (7 + 7 = 14, nos llevamos una). Para que sea capicúa, debe empezar también por 4, lo que obliga a que la llevada llegue hasta la primera cifra: todas las sumas intermedias deben dar 10, es decir, $b + 1 = 10$ y $c + 1 = 10$, así que $b = c = 9$.

La contraseña es **39997**: $39997 - 4 = 39993$ y $39997 + 7 = 40004$, que son capicúas.
