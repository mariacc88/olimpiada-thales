---
id: 2014-regional-4
edicion: 2014-XXX
fase: regional
numero: 4
titulo: ¿De dónde sacará tanto recipiente?
bloques: [numeros]
bloques_thales: []
etiquetas: [divisibilidad, proporcionalidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0842]
estado: borrador
notas: ""
---

## Enunciado

D.ª Felisa Guardalotodo es muy precavida y por ello tiene almacenado en su alacena, por si surge algún imprevisto, agua, aceite y vino.

Para ello posee 9 recipientes cuyas capacidades son 3, 6, 10, 11, 15, 17, 23, 25 y 30 litros, respectivamente. Todos sus recipientes están completamente llenos salvo uno, que está vacío.

Nos ha facilitado la siguiente información: «la cantidad de aceite que guarda en estos recipientes es el doble que la de vino, y la de agua es el triple que la de aceite».

Averigua qué recipientes ha utilizado la Sra. Guardalotodo para cada producto.

**Razona la respuesta.**

## Solución

Si hay $V$ litros de vino, hay $2V$ de aceite y $3 \cdot 2V = 6V$ de agua. En total, $V + 2V + 6V = 9V$ litros: **la cantidad almacenada es múltiplo de 9**.

Todos los recipientes suman $3 + 6 + 10 + 11 + 15 + 17 + 23 + 25 + 30 = 140$ litros. Restando la capacidad de cada uno (el que estaría vacío), solo $140 - 23 = 117$ es múltiplo de 9 (las demás diferencias son 137, 134, 130, 129, 125, 123, 115 y 110). Por tanto:

- El recipiente vacío es el de **23 litros**.
- Hay $117 : 9 = 13$ litros de vino, $26$ de aceite y $78$ de agua.

El reparto es único: el único modo de sumar 13 con los recipientes es $3 + 10$; con los que quedan, 26 solo se obtiene con $11 + 15$, y el resto suma 78:

- Vino: $3 + 10 = 13$ litros.
- Aceite: $11 + 15 = 26$ litros.
- Agua: $6 + 17 + 25 + 30 = 78$ litros.
