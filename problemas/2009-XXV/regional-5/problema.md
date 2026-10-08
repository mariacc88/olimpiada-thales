---
id: 2009-regional-5
edicion: 2009-XXV
fase: regional
numero: 5
titulo: 25 años
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [divisibilidad, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0755, F0756]
estado: borrador
notas: ""
---

## Enunciado

Se escriben en una pizarra los números del 1 al 25. Se eligen dos de ellos de forma arbitraria, se borran y se escribe su diferencia (habrá entonces 24 números en la pizarra). Se vuelven a coger dos números de los escritos, se borran y se escribe su diferencia. Esta operación la seguimos repitiendo mientras podamos. Al final quedará un único número**. ¿Hay alguna forma de que sea un 2? Razona la respuesta.**

## Solución

**No es posible.** La clave es la paridad de la suma de todos los números de la pizarra.

Al principio la suma es $1 + 2 + \dots + 25 = \frac{25 \cdot 26}{2} = 325$, que es impar. Si se borran $a$ y $b$ y se escribe $a - b$, la suma cambia en

$$-a - b + (a - b) = -2b,$$

que es un número par. Por tanto, la suma sigue siendo impar después de cada paso. Al final queda un único número, que es la suma: tiene que ser **impar**, así que nunca puede ser un 2. (Sí se puede conseguir, por ejemplo, un 1.)
