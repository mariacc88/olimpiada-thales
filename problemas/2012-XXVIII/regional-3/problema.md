---
id: 2012-regional-3
edicion: 2012-XXVIII
fase: regional
numero: 3
titulo: "Llámame al..."
bloques: [numeros]
bloques_thales: []
etiquetas: [cifras]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1049]
estado: borrador
notas: ""
---

## Enunciado

A pesar de que llevo llamando a mi amigo Patricio más de un año, nunca me acuerdo ni del número de su móvil ni el de su teléfono fijo. Debe ser porque ambos tienen todas las cifras del 1 al 9. Él siempre me dice que son muy fáciles, porque recordando las tres últimas cifras sería suficiente, ya que las tres centrales son el doble de estas y las tres primeras son el triple, además de saber que un número de móvil empieza por 6 y el de un fijo por 9.

Ayúdame a recordar los números y **explícame razonadamente** cómo los has encontrado para que no me vuelva a ocurrir.

## Solución

Si las tres últimas cifras forman el número $c$, el teléfono es $\overline{3c\;2c\;c}$, y las nueve cifras son distintas y del 1 al 9.

**Fijo.** Empieza por 9, así que $3c$ empieza por 9: $c$ está entre 300 y 333. Además, $c$ no puede tener ceros ni cifras repetidas, ni acabar en 5 (el triple y el doble acabarían en 5 o 0). Probando los candidatos (312, 314, 315, 316, …) solo $c = 327$ da nueve cifras distintas: $3 \cdot 327 = 981$, $2 \cdot 327 = 654$. El fijo es **981 654 327**.

**Móvil.** Empieza por 6, así que $c$ está entre 200 y 233. Probando de la misma manera, solo sirve $c = 219$: $3 \cdot 219 = 657$, $2 \cdot 219 = 438$. El móvil es **657 438 219**.
