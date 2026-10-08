---
id: 2010-provincial-4
edicion: 2010-XXVI
fase: provincial
numero: 4
titulo: El dato desconocido
bloques: [geometria, logica]
bloques_thales: []
etiquetas: [patrones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0782, F0774, F1079]
estado: borrador
notas: "Problema abierto. El nodo de la web solo contenía un applet de GeoGebra; el enunciado se ha tomado de las hojas individuales de la prueba y la solución, de los textos del fichero 264p.ggb."
---

## Enunciado

En las excavaciones que está realizando en Matelandia la famosa arqueóloga Lara Descifralotodo, ha encontrado restos de tablillas de arcilla con datos e ilustraciones estelares.

![Las tablillas: las tres primeras figuras tienen los datos 16, 9 y 20; la cuarta está rota](fig1.png)

La última tablilla está en muy mal estado y no ha podido descifrar el dato. **¿Podrías ayudar a nuestra arqueóloga diciéndole el número que corresponde a la misma?** No olvides explicar cómo lo has averiguado, ya que Lara es una científica muy rigurosa y no se deja convencer fácilmente.

**Dibuja una figura estelar que corresponda al número 12.**

## Solución

Es un problema abierto: hay que encontrar una relación entre cada figura y su número que valga para las tres tablillas conocidas.

Una relación sencilla es contar el **número de ángulos interiores de los polígonos que forman la figura**:

- En la segunda figura hay tres triángulos: $3 \cdot 3 = 9$ ángulos.
- En la tercera, la estrella de cinco puntas, hay cinco triángulos y un pentágono: $5 \cdot 3 + 5 = 20$.
- En la primera, sumando del mismo modo los ángulos de los polígonos que la forman, salen 16.
- En la cuarta, la estrella de seis puntas, contando así todos los ángulos se obtienen **32**.

El dato de la cuarta tablilla es **32**. Otras relaciones que también funcionan (por ejemplo, el número de segmentos más el número de triángulos) llevan al mismo resultado.

Para el número 12 basta dibujar una figura formada por polígonos con 12 ángulos en total: por ejemplo, cuatro triángulos, tres cuadriláteros, un hexágono y dos triángulos, o dos hexágonos.
