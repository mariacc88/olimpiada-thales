---
id: 2016-regional-5
edicion: 2016-XXXII
fase: regional
numero: 5
titulo: Números
bloques: [numeros]
bloques_thales: []
etiquetas: [patrones]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0862]
estado: borrador
notas: ""
---

## Enunciado

A Isa y Pepe les siguen gustando los números y se proponen uno al otro los siguientes cálculos:

![Fotografía: un profesor con un papel en la mano](ilustracion.png)

**Isa:** «¿Cuál es el resultado de $\left(2^{2016} - 2^{2015} + 2^{2014} - 2^{2013} + 2^{2012} - 2^{2011} + 2^{2010} - 2^{2009}\right) : 2^{2008}$?»

**Pepe:** «Como sabes que la suma de los 59 primeros números naturales es 1770, ¿cuál será el resultado de $1^2 - 2^2 + 3^2 - 4^2 + 5^2 - 6^2 + 7^2 - \dots - 58^2 + 59^2$?»

Estamos convencidos de que vosotros tardáis menos tiempo en resolverlos. ¡Ánimo, y da de forma razonada las respuestas correctas!

## Solución

**a)** Escribimos cada potencia como $2^{2008}$ por otra potencia de 2 ($2^a = 2^{a-b} \cdot 2^b$) y sacamos factor común:

$$2^{2008}\left(2^8 - 2^7 + 2^6 - 2^5 + 2^4 - 2^3 + 2^2 - 2\right) = 2^{2008}\,(256 - 128 + 64 - 32 + 16 - 8 + 4 - 2) = 2^{2008} \cdot 170.$$

Por tanto, $\left(2^{2008} \cdot 170\right) : 2^{2008} = \mathbf{170}$.

**b)** Usamos que $a^2 - b^2 = (a + b)(a - b)$ y agrupamos los términos de dos en dos, empezando por el segundo:

$$-2^2 + 3^2 = (3 + 2)(3 - 2) = 2 + 3, \quad -4^2 + 5^2 = 4 + 5, \quad \dots, \quad -58^2 + 59^2 = 58 + 59.$$

Entonces

$$1^2 - 2^2 + 3^2 - \dots - 58^2 + 59^2 = 1 + (2 + 3) + (4 + 5) + \dots + (58 + 59) = 1 + 2 + 3 + \dots + 59 = \mathbf{1770}.$$
