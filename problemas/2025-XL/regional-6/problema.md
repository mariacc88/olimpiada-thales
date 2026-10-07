---
id: 2025-regional-6
edicion: 2025-XL
fase: regional
numero: 6
titulo: Cubo al cubo
bloques: [geometria]
bloques_thales: []
etiquetas: [pitagoras]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1008]
estado: borrador
notas: ""
---

## Enunciado

Rocío le propone a Olivia que resuelva el siguiente ejercicio geométrico de equilibrio de cubos.

Para ello, coloca un cubo pequeño, de 1 cm de lado, sobre un cubo mediano de 5 cm de lado. Finalmente, apoya el cubo grande sobre estos dos, como se muestra en la imagen, de manera que esté en equilibrio.

![Un cubo grande inclinado, apoyado en el suelo por una arista y sobre el cubo pequeño, que está encima del mediano](fig1.png)

¿Cuál es la medida del lado del cubo grande?

**Razona la respuesta.**

## Solución

Llamamos P, Q, R, S y T a los puntos de la figura:

![Vista lateral con los puntos P, Q, R, S y T](fig-solucion.png)

$QR = 5$ cm y $ST = 1$ cm; como el cubo pequeño está sobre el mediano, $RT = 5 - 1 = 4$ cm. Por Pitágoras en el triángulo rectángulo SRT:

$$RS = \sqrt{4^2 + 1^2} = \sqrt{17}\ \text{cm}.$$

Los triángulos PQR y RTS son semejantes (sus ángulos son iguales), así que

$$\frac{ST}{RQ} = \frac{RS}{PR} \;\Rightarrow\; \frac{1}{5} = \frac{\sqrt{17}}{PR} \;\Rightarrow\; PR = 5\sqrt{17}\ \text{cm}.$$

El lado del cubo grande mide

$$PS = PR + RS = 5\sqrt{17} + \sqrt{17} = 6\sqrt{17} \approx \mathbf{24{,}74\ cm}.$$
