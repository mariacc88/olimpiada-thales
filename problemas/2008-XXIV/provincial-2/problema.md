---
id: 2008-provincial-2
edicion: 2008-XXIV
fase: provincial
numero: 2
titulo: "¿Verdadero o falso?"
bloques: [numeros]
bloques_thales: []
etiquetas: [divisibilidad, cifras]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0648, F0649]
estado: borrador
notas: ""
---

## Enunciado

A mi profesora de mates Eulerina, ¡se le ocurre cada cosa en clase! Hoy ha dicho que encontremos el menor número de 4 cifras distintas que cumpla que:

· Es múltiplo de 6.

· Su 1ª y 3ª cifra son números consecutivos en orden creciente, así como su 2ª y 4ª cifra.

· El número formado por la 2ª y 4ª cifra es múltiplo de 3.

Yo no hago más que pensar, pero... ¡algo se me escapa que no encuentro el dichoso número!, **¿será que no existe? Razona la respuesta.**

## Solución

Llamamos $\overline{abcd}$ al número. Por la segunda condición, $c = a + 1$ y $d = b + 1$: el número es $\overline{a\,b\,(a+1)\,(b+1)}$.

- Es múltiplo de 2, así que $b + 1$ es par y $b$ impar: el número $\overline{b\,(b+1)}$ es 12, 34, 56 o 78.
- De estos, solo 12 y 78 son múltiplos de 3: $b = 1$ o $b = 7$.
- Es múltiplo de 3, así que la suma de cifras, $2a + 2b + 2$, es múltiplo de 3. Con $b = 1$ la suma es $2a + 4$, y con $b = 7$, $2a + 16$; en ambos casos $a = 1$, 4 o 7.

Los candidatos son 1122, 4152, 7182, 1728, 4758 y 7788. 1122 y 7788 repiten cifras. El menor de los demás es **1728**, así que el número existe (es verdadero): $1728 = 6 \cdot 288$.
