---
id: 2017-provincial-3
edicion: 2017-XXXIII
fase: provincial
numero: 3
titulo: Elecciones
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [fracciones, cifras, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0872]
estado: borrador
notas: ""
---

## Enunciado

A las elecciones al parlamento se han presentado 4 partidos y, como ninguno ha obtenido mayoría absoluta, han tenido que volver a votar. A partir de los siguientes datos debes deducir **de forma razonada** cuántos representantes ha obtenido cada partido en cada una de las votaciones.

En la segunda votación:

- El partido A ha aumentado en 25 representantes, y con ello consigue el doble de los que obtuvo D.
- El partido B ha perdido un número capicúa de representantes, que se aproxima a la tercera parte de los que obtuvo al principio; con esto consigue tener los mismos representantes que D.
- El partido C ha obtenido 8 representantes más que en la primera votación.
- El partido D es el único que obtiene los mismos representantes en ambas votaciones.

Además, debes saber que:

- En total son 350 representantes.
- El partido B obtuvo el 28 % de los representantes en la primera votación.

## Solución

- **B en la primera votación:** el 28 % de 350, es decir, 98 representantes.
- **B en la segunda:** perdió un número capicúa cercano a $98 : 3 \approx 32{,}7$, es decir, 33. Le quedan $98 - 33 = 65$.
- **D:** tiene en las dos votaciones lo mismo que B en la segunda, 65.
- **A:** en la segunda votación tiene el doble que D, $2 \cdot 65 = 130$, así que en la primera tenía $130 - 25 = 105$.
- **C:** en la primera votación, $350 - (105 + 98 + 65) = 82$; en la segunda, $82 + 8 = 90$.

| Partido | 1.ª votación | 2.ª votación |
|---|---|---|
| A | 105 | 130 |
| B | 98 | 65 |
| C | 82 | 90 |
| D | 65 | 65 |
| **Total** | 350 | 350 |
