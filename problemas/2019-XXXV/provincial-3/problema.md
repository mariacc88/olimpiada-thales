---
id: 2019-provincial-3
edicion: 2019-XXXV
fase: provincial
numero: 3
titulo: El planeta cercano
bloques: [numeros]
bloques_thales: []
etiquetas: [proporcionalidad]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0916]
estado: borrador
notas: "Problema CASIO (se permite la calculadora). La solución original añade la variante con el año sidéreo de 365 días, 6 h, 9 min y 10 s, que da 1 mes, 34 días, 43 h, 29 min y 36 s."
---

## Enunciado

Acaba de aterrizar en la Tierra un alumno de intercambio del planeta cercano Próxima C5. Este planeta tarda en girar alrededor de su estrella, Próxima Centauri, el mismo tiempo que la Tierra en girar alrededor del Sol, pero cada año consta de 500 días, cada mes de 50 días, cada día de 50 horas, cada hora de 50 minutos y cada minuto de 50 segundos.

![Ilustración: un planeta](ilustracion.png)

Marta, para integrar al nuevo chico, le pregunta: «¿Dónde duran más los segundos, en tu planeta o en el mío? Y si me voy a tu planeta los meses de julio y agosto, ¿cuánto tiempo estoy (contando los días, las horas, los minutos y los segundos) realmente en el tuyo?».

Ayuda al sorprendido visitante dando las respuestas **de forma razonada**.

## Solución

Un año terrestre tiene $365 \cdot 24 \cdot 60 \cdot 60 = 31\,536\,000$ segundos, y un año de Próxima C5 tiene $500 \cdot 50 \cdot 50 \cdot 50 = 62\,500\,000$ segundos. Como los dos años duran lo mismo y en Próxima C5 caben casi el doble de segundos, **los segundos duran más en la Tierra** (casi el doble).

Julio y agosto tienen $62$ días, es decir, $62 \cdot 24 \cdot 60 \cdot 60 = 5\,356\,800$ segundos terrestres. En segundos de Próxima C5 son

$$5\,356\,800 \cdot \frac{62\,500\,000}{31\,536\,000} \approx 10\,616\,438 \text{ segundos}.$$

Pasamos a las unidades del planeta dividiendo sucesivamente entre 50:

- $10\,616\,438 = 212\,328 \cdot 50 + 38$: 212 328 minutos y 38 segundos.
- $212\,328 = 4246 \cdot 50 + 28$: 4246 horas y 28 minutos.
- $4246 = 84 \cdot 50 + 46$: 84 días y 46 horas.
- $84 = 1 \cdot 50 + 34$: 1 mes y 34 días.

Marta estará en Próxima C5 **1 mes, 34 días, 46 horas, 28 minutos y 38 segundos**.
