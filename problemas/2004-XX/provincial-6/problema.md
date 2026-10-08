---
id: 2004-provincial-6
edicion: 2004-XX
fase: provincial
numero: 6
titulo: Cumpleaño enigmático
bloques: [numeros, logica]
bloques_thales: []
etiquetas: [divisibilidad, deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0453, F0455]
estado: borrador
notas: ""
---

## Enunciado

Pepito Medi Vido invitó en sus cumpleaños a toda la clase. Les dijo a sus compis que se verían a las seis en su casa, que está en la calle Entretrés nº x, y que debían saber que:

• Si x es un múltiplo de tres está entre el 50 y el 59.

• Si x no es múltiplo de cuatro está entre el 60 y el 69.

• Si x no es un múltiplo de 6 está entre el 70 y el 79.

¿Sabrías averiguar la dirección de la casa de Pepito?

## Solución

Las tres condiciones dicen qué pasa *si* el número cumple algo:

1. Si $x$ es múltiplo de 3, está entre 50 y 59.
2. Si $x$ no es múltiplo de 4, está entre 60 y 69.
3. Si $x$ no es múltiplo de 6, está entre 70 y 79.

- **Si $x$ fuera múltiplo de 6**, también lo sería de 3 y, por 1, estaría entre 50 y 59. Además tendría que ser múltiplo de 4 (si no, por 2, estaría en los sesenta), es decir, múltiplo de 12; pero entre 50 y 59 no hay ninguno.
- Por tanto **$x$ no es múltiplo de 6** y, por 3, está entre 70 y 79. Entonces no puede estar en los cincuenta ni en los sesenta: no es múltiplo de 3 y sí es múltiplo de 4. Entre 70 y 79, los múltiplos de 4 son 72 y 76, y 72 es múltiplo de 3.

Pepito vive en la calle Entretrés, **n.º 76**.
