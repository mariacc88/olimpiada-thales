---
id: 2004-regional-1
edicion: 2004-XX
fase: regional
numero: 1
titulo: Baldomero el camionero
bloques: [geometria]
bloques_thales: []
etiquetas: [pitagoras]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0456, F0459]
estado: borrador
notas: ""
---

## Enunciado

Baldomero conduce un camión y le gusta recorrer todas las carreteras con él. Pero hoy se le plantea un problema MATEMÁTICO. Tú dirás: ¿qué tienen que ver las matemáticas con conducir un camión?. Escucha y te convencerás: La carretera por la que Baldomero circula tiene un túnel de doble sentido por el que inevitablemente debe pasar y con una altura máxima de 4 metros. El camión de Baldomero tiene 325 cm de alto y 228 cm de ancho, pero no sabe si podrá atravesar el túnel...

Seguirás pensando: ¿por qué tiene problemas si el camión es más bajo que el túnel?. Muy sencillo, porque el túnel tiene forma de semicírculo y Baldomero es muy respetuoso con las normas de circulación, por lo que circulará siempre por el carril derecho. ¿Tú qué crees? ¿Puede Baldomero estar tranquilo y atravesar el túnel?

![Ilustración: el camión](ilustracion.png)

## Solución

El túnel es un semicírculo de 4 m (400 cm) de radio, y el camión va por el carril derecho: es un rectángulo de 228 cm de ancho y 325 cm de alto apoyado en el suelo, con un lado en la línea central. Cabe si su esquina superior exterior queda dentro del semicírculo, es decir, si la distancia de esa esquina al centro de la base (la diagonal del rectángulo) es menor que el radio.

Por el teorema de Pitágoras,

$$d^2 = 228^2 + 325^2 = 51\,984 + 105\,625 = 157\,609 \;\Rightarrow\; d = 397 \text{ cm}.$$

Como $397 < 400$, **el camión puede pasar por el túnel**, aunque por muy poco (3 cm).
