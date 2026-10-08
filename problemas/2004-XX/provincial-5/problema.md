---
id: 2004-provincial-5
edicion: 2004-XX
fase: provincial
numero: 5
titulo: Rima rimando
bloques: [estadistica]
bloques_thales: [estadistica]
etiquetas: [combinatoria, probabilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0450, F0452]
estado: borrador
notas: ""
---

## Enunciado

Entre las provincias de Andalucía

parece que no hay rima consonante

(como la tiene poetisa con abscisa);

mas sí la hay, entre algunas, asonante.

Que concuerden sólo las vocales

es lo que esto significa...

Esta misma estrofa, en este instante,

a modo de ejemplo serviría.

Si se eligen tres de las provincias al azar

(ya que mérito no tendría: ninguna se repite),

¿habría alguna posibilidad

de que dos de ellas rimen

para así un terceto formar

en cuyos nombres sus versos terminen?

Razona si tiene más o menos posibilidades

lo que el intento de soneto sugería

o que tengan el mismo número de vocales

las tres provincias elegidas.

## Solución

Las ocho provincias son Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga y Sevilla. Se pueden elegir tres de ellas de $\frac{8 \cdot 7 \cdot 6}{6} = 56$ formas.

**Rima asonante.** Solo riman Málaga con Granada (a-a) y Almería con Sevilla (í-a); no hay tres provincias que rimen entre sí. Cada pareja que rima puede completarse con cualquiera de las otras 6 provincias, así que hay $6 + 6 = 12$ elecciones en las que dos provincias riman.

**Mismo número de vocales.** Agrupamos las provincias por su número de vocales:

- 2 vocales: Cádiz, Jaén.
- 3 vocales: Córdoba, Granada, Huelva, Málaga, Sevilla.
- 4 vocales: Almería.

Solo se pueden elegir tres con el mismo número de vocales entre las cinco de tres vocales: $\frac{5 \cdot 4 \cdot 3}{6} = 10$ formas.

Como $12 > 10$, **es más probable poder formar el terceto** (con probabilidad $\frac{12}{56}$) que elegir tres provincias con el mismo número de vocales ($\frac{10}{56}$).
