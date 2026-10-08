---
id: 2005-regional-5
edicion: 2005-XXI
fase: regional
numero: 5
titulo: Thal, es de Miletos
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [cifras, ecuaciones, deduccion]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0522, F0524]
estado: borrador
notas: "La solución original busca la edad probando valores en una tabla; aquí se plantea la ecuación."
---

## Enunciado

Todo el mundo en Matelandia sabe que el alcalde, Don Miletos, tiene menos de 100 años, pero nadie sabe su edad exacta. Sin embargo, Pepe Pinto cree haberla descubierto cuando sus hijos, Fermín y Piluca, hablaban con él de la fiesta de cumpleaños que celebraba esa tarde su amigo Thal:

*- Pepe: ¿Y de quién es hijo ese Thal?*

*- Piluca: Thal, es de Miletos.*

*- Pepe: ¿El hijo del alcalde? ¡Vaya! ¿Y cuántos años cumple?*

*- Fermín: No lo sé, pero parece ser que ayer Don Miletos y su hijo tenían las mismas cifras en sus edades...*

*-* *Piluca: Sí, pero hoy eso no es así. Además hoy el alcalde tiene el doble de* *años que Thal*.

Como Pepe Pinto sabe que el alcalde cumple años la semana que viene, ya sabe exactamente cuántos años cumplirá D. Miletos. ¿Puedes averiguarlo tú también?

## Solución

- Don Miletos tiene menos de 100 años, así que su edad tiene una o dos cifras.
- Ayer padre e hijo tenían las mismas cifras en sus edades; no pueden tener la misma edad, así que las dos edades tienen dos cifras, en orden inverso. Ayer Thal tenía $\overline{ab}$ años y su padre $\overline{ba}$.
- Hoy es el cumpleaños de Thal, que tiene $\overline{ab} + 1$ años. El de don Miletos es la semana que viene, así que sigue teniendo $\overline{ba}$ años. Como hoy tiene el doble que Thal:

$$10b + a = 2\,(10a + b + 1) \;\Rightarrow\; 8b = 19a + 2.$$

Con $a$ y $b$ cifras, la única solución es $a = 2$, $b = 5$. Ayer Thal tenía 25 años y su padre 52; hoy Thal cumple 26.

Don Miletos tiene **52 años**.
