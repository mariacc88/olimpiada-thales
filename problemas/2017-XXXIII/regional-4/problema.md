---
id: 2017-regional-4
edicion: 2017-XXXIII
fase: regional
numero: 4
titulo: Jugando con dados
bloques: [estadistica]
bloques_thales: []
etiquetas: [probabilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0879]
estado: borrador
notas: "La solución original resuelve el problema con una tabla de casos; aquí se añaden las probabilidades."
---

## Enunciado

Juan y Andrés han ideado un juego con un dado cúbico de 6 caras equilibradas y las siguientes normas:

- A Juan se le asignan los números 1 y 2, y a Andrés los números 3, 4, 5 y 6.
- Si en la primera tirada sale el 1, Juan gana el juego y ya no se tira más.
- Si no sale el 1 en la primera tirada, se apunta un punto quien tenga asignado el número que salga.
- A continuación se realiza una segunda tirada y se apunta 1 punto a quien le corresponda el número que haya salido.
- Gana el juego quien tenga más puntos; si están empatados a puntos, nadie gana.

¿Cuál de los dos amigos tiene más posibilidades de ganar el juego?

**Razona tu respuesta.**

## Solución

Estudiamos los casos según las dos tiradas:

| 1.ª tirada | 2.ª tirada | Resultado | Probabilidad |
|---|---|---|---|
| 1 | — | gana Juan | $\frac{1}{6} = \frac{6}{36}$ |
| 2 | 1 o 2 | gana Juan (2–0) | $\frac{1}{6} \cdot \frac{2}{6} = \frac{2}{36}$ |
| 2 | 3, 4, 5 o 6 | empate (1–1) | $\frac{1}{6} \cdot \frac{4}{6} = \frac{4}{36}$ |
| 3, 4, 5 o 6 | 1 o 2 | empate (1–1) | $\frac{4}{6} \cdot \frac{2}{6} = \frac{8}{36}$ |
| 3, 4, 5 o 6 | 3, 4, 5 o 6 | gana Andrés (0–2) | $\frac{4}{6} \cdot \frac{4}{6} = \frac{16}{36}$ |

Juan gana con probabilidad $\frac{8}{36} = \frac{2}{9}$, Andrés con $\frac{16}{36} = \frac{4}{9}$, y empatan con $\frac{12}{36} = \frac{1}{3}$. **Andrés** tiene más posibilidades de ganar.
