---
id: 2010-regional-6
edicion: 2010-XXVI
fase: regional
numero: 6
titulo: Las hermanas Pascalinas
bloques: [numeros]
bloques_thales: []
etiquetas: [ecuaciones, divisibilidad]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0796, F0790, F1089, F1090]
estado: borrador
notas: "El nodo de la web solo contenía un applet de GeoGebra; el enunciado se ha tomado de las hojas individuales de la prueba. La solución no es la original (los ficheros 266r.ggb no contienen texto)."
---

## Enunciado

En la fiesta de Faylimn, Gelsey, la menor de las tres hermanas Pascalinas, pidió su mayor deseo a la Gran Reina de las Hadas:

*«No quiero alcanzar nunca la edad de Eolande, la mayor de mis hermanas, que es cinco años mayor que yo».*

![Ilustración: un hada](ilustracion.png)

La Gran Reina le concedió su deseo y, a partir de ese momento, Gelsey no cumpliría más años. Cuando sus hermanas se enteraron, se enojaron muchísimo. Eolande se le acercó y le dijo recriminándole:

*«¿Es que no piensas? ¿No te has dado cuenta de que, con tu deseo, el próximo año perderemos 504 onzas de oro? ¿Has olvidado que nuestro padre nos tiene prometido que cada año nos entregará una cantidad de onzas de oro igual al producto de nuestras edades?»*

**¿Cuáles son las edades de las hermanas Pascalinas? Razona la respuesta.**

## Solución

Sea $g$ la edad de Gelsey; Eolande tiene $g + 5$ y la mediana, $m$, está entre las dos: $g < m < g + 5$. El año próximo, sin el deseo, recibirían $(g + 1)(m + 1)(g + 6)$ onzas; con el deseo, Gelsey sigue teniendo $g$ años y reciben $g(m + 1)(g + 6)$. La diferencia es

$$(m + 1)(g + 6) = 504.$$

Como $g + 2 \le m + 1 \le g + 5$, los dos factores son casi iguales: $m + 1$ está entre $(g + 6) - 4$ y $(g + 6) - 1$. Entre las formas de escribir $504 = 2^3 \cdot 3^2 \cdot 7$ como producto de dos factores, la única que cumple esto es $504 = 21 \cdot 24$, con $g + 6 = 24$ y $m + 1 = 21$.

Gelsey tiene **18 años**, la hermana mediana **20** y Eolande **23**.
