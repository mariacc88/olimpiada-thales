---
id: 2006-provincial-4
edicion: 2006-XXII
fase: provincial
numero: 4
titulo: Fórmula matemática
bloques: [numeros, funciones]
bloques_thales: []
etiquetas: [divisibilidad, movimiento]
dificultad: dificil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0548, F0550]
estado: borrador
notas: ""
---

## Enunciado

Estamos en la carrera de Fórmula Matemática con la participación de los pilotos Fernando Alfa y Kimi Random. Los ingenieros de Fernando han calculado que Kimi es un segundo más lento que Fernando en cada vuelta del circuito, pero mientras que Fernando necesita repostar cada 7 vueltas tardando 20 segundos, Kimi reposta cada 10 vueltas tardando 21 segundos. La carrera dura 58 vueltas.

**¿Cuántas veces adelanta Kimi a Fernando durante la carrera? ¿Quién gana y cuánto tiempo le saca de ventaja?**

## Solución

Como Fernando es más rápido, Kimi solo puede adelantarle cuando Fernando reposta, en las vueltas 7, 14, 21, 28, 35, 42, 49 y 56. Comparamos el tiempo que ha perdido cada uno respecto de un piloto que fuera a la velocidad de Fernando sin parar:

- Fernando pierde 20 s en cada repostaje: al final de la vuelta $n$ lleva perdidos $20 \cdot \lfloor n/7 \rfloor$ segundos.
- Kimi pierde 1 s por vuelta y 21 s en cada repostaje: $n + 21 \cdot \lfloor n/10 \rfloor$ segundos.

| Vuelta | 7 | 14 | 21 | 28 | 35 | 42 | 49 | 56 |
|---|---|---|---|---|---|---|---|---|
| Fernando | 20 | 40 | 60 | 80 | 100 | 120 | 140 | 160 |
| Kimi | 7 | 35 | 63 | 70 | 98 | 126 | 133 | 161 |

Kimi va por delante (ha perdido menos tiempo) tras los repostajes de las vueltas 7, 14, 28, 35 y 49, y en la vuelta anterior a cada una iba por detrás (por ejemplo, en la vuelta 13 Fernando llevaba 20 s perdidos y Kimi 34), así que son adelantamientos de verdad. Fernando lo recupera después en cada caso (vueltas 10, 19, 30, 37 y 50). **Kimi adelanta a Fernando 5 veces.**

Al terminar la vuelta 58, Fernando ha perdido 160 s y Kimi $58 + 5 \cdot 21 = 163$ s: **gana Fernando**, por 3 segundos.
