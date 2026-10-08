---
id: 2012-provincial-5
edicion: 2012-XXVIII
fase: provincial
numero: 5
titulo: El ramo de flores
bloques: [numeros]
bloques_thales: []
etiquetas: [divisibilidad, ecuaciones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1041]
estado: borrador
notas: ""
---

## Enunciado

El día 14 del mes pasado fue el día de los enamorados y por dicho motivo encargué un magnífico ramo de flores para mi novia Eulerina. El ramo me costó 68 € y estaba formado por petunias y orquídeas.

Recuerdo que el precio de cada petunia era de 0,5 € y en el ramo había 16; pero no llego a recordar cuál era el precio de una orquídea, aunque sé que este no tenía céntimos y no era múltiplo de 5.

![Ilustración: los novios con el ramo](ilustracion.png)

Ayuda a este joven enamorado calculando cuál era el precio de cada orquídea y cuántas había en el ramo, si sabemos que al sumar ambas cantidades se obtiene un número que tiene una cantidad impar de divisores.

**Razona las respuestas.**

## Solución

Las petunias costaron $16 \cdot 0{,}5 = 8$ €, así que las orquídeas costaron $68 - 8 = 60$ €. Si había $n$ orquídeas de $x$ euros, $n \cdot x = 60$, con $x$ entero y no múltiplo de 5.

Un número tiene una cantidad impar de divisores solo si es un cuadrado perfecto, así que $x + n$ debe ser un cuadrado. Probando los divisores de 60 que no son múltiplos de 5:

| $x$ | 1 | 2 | 3 | 4 | 6 | 12 |
|---|---|---|---|---|---|---|
| $n$ | 60 | 30 | 20 | 15 | 10 | 5 |
| $x + n$ | 61 | 32 | 23 | 19 | 16 | 17 |

Solo $16 = 4^2$ es un cuadrado: cada orquídea costó **6 €** y había **10 orquídeas**.
