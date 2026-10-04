---
id: 1991-regional-8
edicion: 1991-VII
fase: regional
numero: 8
titulo: Equiáreas
bloques: [geometria]
bloques_thales: []
etiquetas: [areas]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0176, F1070]
estado: borrador
notas: "Publicado como applet de GeoGebra; enunciado y solución transcritos de las imágenes de texto del fichero 78r.ggb. El dato BC = CA se deduce de la solución original."
---

## Enunciado

Localiza el punto $P$ sobre el lado $BC$ del triángulo isósceles $ABC$ (con $BC = CA$), de tal forma que los triángulos $ABP$ y $APC$ tengan igual área.

Señala el punto $Q$ sobre el mismo lado si ahora lo que deseamos es que ambos triángulos tengan igual perímetro.

## Solución

**Punto P.** Si tomamos $BP$ y $PC$ como bases, los triángulos $ABP$ y $APC$ tienen la misma altura (la distancia de $A$ a la recta $BC$). Para que tengan igual área, sus bases tienen que ser iguales: **$P$ es el punto medio de $BC$**.

**Punto Q.** Los triángulos $ABQ$ y $AQC$ comparten el lado $AQ$, así que para que tengan el mismo perímetro debe cumplirse

$$AB + BQ = QC + CA.$$

Sustituyendo $BQ = BC - QC$ y recordando que el triángulo es isósceles ($BC = CA$):

$$AB + BC - QC = QC + BC \;\Rightarrow\; AB = 2\,QC.$$

Es decir, **$Q$ es el punto de $BC$ cuya distancia a $C$ es la mitad de $AB$**. Se puede construir trazando la circunferencia de centro $C$ y radio $AB/2$ y cortándola con el segmento $BC$.
