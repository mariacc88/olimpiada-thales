---
id: 2007-provincial-3
edicion: 2007-XXIII
fase: provincial
numero: 3
titulo: Números amigos
bloques: [numeros]
bloques_thales: [numeros]
etiquetas: [divisibilidad]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0597, F0600]
estado: borrador
notas: ""
---

## Enunciado

![Ilustración: Zipi y Zape](ilustracion.png)

El número romano Zipi = CCXX, tiene un gran amigo que, obviamente, se llama Zape. Zape es el gran amigo de Zipi porque es la suma de todos los divisores de Zipi (sin contar al propio Zipi).

**¿Podrías averiguar qué número es Zape y cómo se expresa en números romanos?**

**Comprueba también que Zipi es el gran amigo de Zape** porque es la suma de todos sus divisores (excepto Zape).

## Solución

Zipi $=$ CCXX $= 220 = 2^2 \cdot 5 \cdot 11$. Sus divisores, sin contar el propio 220, son

$$1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110,$$

que suman **Zape = 284**, que en números romanos es **CCLXXXIV**.

Comprobamos que también Zipi es el gran amigo de Zape: $284 = 2^2 \cdot 71$ y sus divisores distintos de 284 son $1, 2, 4, 71, 142$, que suman $220$. (220 y 284 son la pareja de números amigos más pequeña.)
