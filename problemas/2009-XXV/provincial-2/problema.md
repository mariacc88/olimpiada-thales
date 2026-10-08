---
id: 2009-provincial-2
edicion: 2009-XXV
fase: provincial
numero: 2
titulo: La gala benéfica
bloques: [estadistica]
bloques_thales: [estadistica]
etiquetas: [combinatoria, probabilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0717, F0720]
estado: borrador
notas: ""
---

## Enunciado

El señor Frac-thales aprovecha cualquier oportunidad para vestirse de gala. En esta ocasión, ha acudido a una gala benéfica en favor de los niños que no saben matemáticas, en la que tiene la oportunidad de jugar en una tómbola. Después de entregar un donativo, le ponen por delante tres tarjetas:

Tarjeta 1: Dos premios.

Tarjeta 2: 1 premio.

Tarjeta 3: Inténtalo de nuevo.

Frac-thales decide jugar tres veces antes de ir a recoger sus premios (caso de que le toquen). A su lado está Eulerín, que le pregunta qué tal le ha ido, a lo que Frac-thales responde:

- «En mi segundo intento he sacado peor tarjeta que en el primero».

¿Cuántas posibilidades existen de que la tercera tarjeta también sea peor que la primera? Justifica la respuesta.

## Solución

Damos a cada tarjeta un valor: «inténtalo de nuevo» = 1, «un premio» = 2 y «dos premios» = 3. Hay $3 \cdot 3 \cdot 3 = 27$ resultados posibles de las tres jugadas.

Como la segunda tarjeta fue peor que la primera, la pareja (primera, segunda) es (2, 1), (3, 1) o (3, 2); con cualquiera de los 3 valores de la tercera, quedan $3 \cdot 3 = 9$ posibilidades. La tercera es peor que la primera en:

- (2, 1, 1);
- (3, 1, 1), (3, 1, 2);
- (3, 2, 1), (3, 2, 2).

Hay **5 posibilidades de 9**.
