---
id: 1988-provincial-3
edicion: 1988-IV
fase: provincial
numero: 3
titulo: ¡Qué rollo!
bloques: [numeros]
bloques_thales: []
etiquetas: [ecuaciones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0076, F0078]
estado: borrador
notas: "Publicado como applet de GeoGebra; enunciado y solución extraídos de los textos del fichero 43p.ggb."
---

## Enunciado

En un congreso de matemáticos y matemáticas, mientras se celebraba una aburrida conferencia, uno de los asistentes se dio cuenta de que todos los allí reunidos pertenecían a cuatro países diferentes: España, Portugal, Francia e Italia. No teniendo nada mejor que hacer, establece las ecuaciones siguientes y se las pasa a su vecino para ver si este es capaz de descubrir cuántas son las personas de cada país. ¿Podrías ayudarle?

$$\begin{aligned} E + P + F &= 56 \ I + F + P &= 84 \ F + I + E &= 88 \ I + E + P &= 96 \end{aligned}$$

## Solución

Restando ecuaciones dos a dos ponemos todas las incógnitas en función de $E$:

$$\begin{aligned} (1.^{\text{a}}) - (2.^{\text{a}}):&\quad E - I = -28 \;\Rightarrow\; I = E + 28 \ (2.^{\text{a}}) - (3.^{\text{a}}):&\quad P - E = -4 \;\Rightarrow\; P = E - 4 \ (2.^{\text{a}}) - (4.^{\text{a}}):&\quad F - E = -12 \;\Rightarrow\; F = E - 12 \end{aligned}$$

Sustituyendo en la primera ecuación: $E + (E - 4) + (E - 12) = 56 \Rightarrow 3E = 72 \Rightarrow E = 24$. Por tanto, $I = 52$, $P = 20$ y $F = 12$.

En el congreso hay **24 españoles, 20 portugueses, 12 franceses y 52 italianos**.

La construcción de GeoGebra original propone además una resolución gráfica: con un deslizador para $P$, las dos últimas ecuaciones se representan como rectas en función de $E = x$, y se mueve el deslizador hasta que las dos rectas corten al eje $OX$ en el mismo punto.
