---
id: 2025-provincial-5
edicion: 2025-XL
fase: provincial
numero: 5
titulo: Los dados
bloques: [estadistica]
bloques_thales: []
etiquetas: [combinatoria, probabilidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F1014]
estado: borrador
notas: "ENUNCIADO PERDIDO: el PDF publicado solo contiene la solución. El enunciado de aquí es una reconstrucción a partir de ella (es el clásico problema de Galileo); hay que sustituirlo por el original si aparece."
---

## Enunciado

*Enunciado reconstruido; el original no se ha publicado.*

Lanzamos tres dados y sumamos sus puntuaciones. ¿Es más fácil obtener una suma de 9 o una suma de 10? ¿De cuántas formas se puede obtener cada una?

**Razona tu respuesta.**

## Solución

Escribimos las puntuaciones ordenadas de menor a mayor y contamos, para cada combinación, de cuántas formas puede salir teniendo en cuenta el orden de los dados (6 si los tres números son distintos, 3 si hay dos iguales y 1 si son los tres iguales).

| Suma 9 | Formas | | Suma 10 | Formas |
|---|---|---|---|---|
| (1, 2, 6) | 6 | | (1, 3, 6) | 6 |
| (1, 3, 5) | 6 | | (1, 4, 5) | 6 |
| (1, 4, 4) | 3 | | (2, 2, 6) | 3 |
| (2, 2, 5) | 3 | | (2, 3, 5) | 6 |
| (2, 3, 4) | 6 | | (2, 4, 4) | 3 |
| (3, 3, 3) | 1 | | (3, 3, 4) | 3 |
| **Total** | **25** | | **Total** | **27** |

Las dos sumas se pueden escribir de seis maneras, pero teniendo en cuenta el orden hay **25 formas de sumar 9 y 27 de sumar 10**, así que es algo más probable sacar 10 ($\frac{27}{216}$ frente a $\frac{25}{216}$).
