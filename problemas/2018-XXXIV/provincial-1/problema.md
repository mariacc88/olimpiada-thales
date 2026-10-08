---
id: 2018-provincial-1
edicion: 2018-XXXIV
fase: provincial
numero: 1
titulo: Parcelas inundadas
bloques: [geometria, logica]
bloques_thales: []
etiquetas: [areas, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0894]
estado: borrador
notas: "La solución original coloca las parcelas una a una en varias diapositivas; aquí se resume."
---

## Enunciado

El huerto urbano de Matelandia, que es un cuadrado de 70 × 70 m, se ha inundado y hay que volver a señalar los límites de las parcelas que lo forman.

Sabemos cuántos metros cuadrados medía cada una, y que las parcelas son rectangulares o cuadradas.

Usa la siguiente cuadrícula para dibujar, **de forma razonada**, las quince parcelas. Cada parcela incluirá un solo número, que representará su área.

![Cuadrícula de 7 × 7 con las áreas de las quince parcelas escritas en algunas casillas](fig1.png)

## Solución

Cada casilla de la cuadrícula mide $10 \times 10 = 100\ \text{m}^2$, así que una parcela de 300 m² ocupa 3 casillas, una de 600 m², 6, etc.

Hay que empezar por las parcelas que solo se pueden colocar de una manera. Por ejemplo, la de 600 m² de la esquina inferior izquierda solo puede ser un rectángulo de 1 × 6 casillas (10 × 60 m) a lo largo del borde, y a partir de ahí se van reduciendo las posibilidades de las demás: la de 200 m² de arriba cubre el hueco que deja la anterior, la de 300 m² de arriba solo tiene una opción, después la otra de 600 m², etc.

![Las quince parcelas dibujadas](fig-solucion.png)
