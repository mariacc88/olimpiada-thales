---
id: 2023-regional-3
edicion: 2023-XXXVIII
fase: regional
numero: 3
titulo: La contraseña
bloques: [estadistica]
bloques_thales: []
etiquetas: [combinatoria, probabilidad]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0978]
estado: borrador
notas: ""
---

## Enunciado

La contraseña para poder entrar en la página de la OLIMPIADA MATEMÁTICA THALES debe estar formada por 4 caracteres de la siguiente manera:

- El primero debe ser una vocal en mayúscula.
- El último, un símbolo entre +, −, \*, /.
- Los dos centrales deben ser consonantes en minúscula de las que aparecen en la palabra OLIMPIADA (pueden ser iguales o distintas).

**Contesta razonadamente a las siguientes preguntas:**

1. ¿Cuántas contraseñas distintas pueden formarse que empiecen por A y acaben por +?
2. ¿Cuántas contraseñas distintas pueden formarse que tengan dd en sus dos sitios centrales? ¿Y que tengan dm?
3. ¿Cuántas contraseñas distintas pueden formarse que empiecen por B?
4. ¿Cuántas contraseñas distintas se pueden formar en total?
5. ¿Qué es más probable: que una contraseña empiece por E o que acabe por \*?

## Solución

Las vocales posibles son 5 (A, E, I, O, U), los símbolos 4 (+, −, \*, /) y las consonantes de OLIMPIADA 4 (l, m, p, d).

1. Con la forma A \_ \_ +, en el segundo lugar puede ir l, m, p o d, y para cada una de ellas hay otras 4 posibilidades en el tercero: $4 \cdot 4 = \mathbf{16}$ contraseñas.
2. Con dd en el centro, quedan 5 vocales para el primer lugar y 4 símbolos para el último: $5 \cdot 4 = \mathbf{20}$ contraseñas. Lo mismo con dm: **20**.
3. **Ninguna**: la contraseña tiene que empezar por vocal mayúscula. (La pregunta comprueba que se ha leído con atención el enunciado.)
4. En total: $5 \cdot 4 \cdot 4 \cdot 4 = \mathbf{320}$ contraseñas.
5. Empiezan por E: $4 \cdot 4 \cdot 4 = 64$ contraseñas. Acaban en \*: $5 \cdot 4 \cdot 4 = 80$ contraseñas. Es **más probable que acabe en \***.
