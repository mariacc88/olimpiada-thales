---
id: 2012-regional-4
edicion: 2012-XXVIII
fase: regional
numero: 4
titulo: Adornando fachadas
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [patrones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1051]
estado: borrador
notas: ""
---

## Enunciado

En Todolandia existe una gran competencia entre todos los vecinos y vecinas de todos los barrios en el adorno de todas las fachadas, para ver quién gana el concurso convocado por el Ayuntamiento.

Las fachadas de sus casas están adornadas con macetas, pero la cantidad de estas depende de la numeración del portal de cada casa.

En el lujoso barrio Decoralotodo, el portal n.º 1 tiene 2 macetas en su fachada, en el portal n.º 2 tiene 6 macetas, en el portal n.º 3 la cantidad de macetas es 12 y en el portal n.º 4 hay 20 macetas.

En el majestuoso barrio vecino de Embellecelotodo, en la fachada del portal n.º 1 solo hay una maceta, en el portal n.º 2 tiene 6 macetas, en el portal n.º 3 la cantidad de macetas es de 13 y en el portal n.º 4 hay 22 macetas.

Averigua cuántas macetas hay en los portales números 5 y 10 de cada barrio. Y busca una forma de cómo podemos calcular la cantidad de macetas que habría en cualquier portal de estos prestigiosos barrios todolandeses. **Razona las respuestas.**

## Solución

**Decoralotodo.** $2 = 1 \cdot 2$, $6 = 2 \cdot 3$, $12 = 3 \cdot 4$, $20 = 4 \cdot 5$: el portal $n$ tiene $n(n + 1) = n^2 + n$ macetas. El portal 5 tiene $5 \cdot 6 = 30$ y el 10, $10 \cdot 11 = 110$.

**Embellecelotodo.** Las diferencias entre portales consecutivos son 5, 7, 9, … (aumentan de 2 en 2), y los números son $1 = 2^2 - 3$, $6 = 3^2 - 3$, $13 = 4^2 - 3$, $22 = 5^2 - 3$: el portal $n$ tiene $(n + 1)^2 - 3 = n^2 + 2n - 2$ macetas. El portal 5 tiene $6^2 - 3 = 33$ y el 10, $11^2 - 3 = 118$.

| Portal | 1 | 2 | 3 | 4 | 5 | 10 | $n$ |
|---|---|---|---|---|---|---|---|
| Decoralotodo | 2 | 6 | 12 | 20 | 30 | 110 | $n(n+1)$ |
| Embellecelotodo | 1 | 6 | 13 | 22 | 33 | 118 | $(n+1)^2 - 3$ |
