---
id: 2005-provincial-3
edicion: 2005-XXI
fase: provincial
numero: 3
titulo: ¡Qué lío de camisetas!
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0490, F0492]
estado: borrador
notas: ""
---

## Enunciado

En Matelandia, las chicas y chicos del Club de Lógicaplastante, tienen la curiosa costumbre de marcar sus camisetas con una letra y un número en la espalda. Arturo, Benito, Carmen y Diana pertenecen a dicho club. Utilizan para marcar sus camisetas los números 2, 4, 6 y 8; y las letras, A, B, C y D. Para poder pertenecer a dicho club debes averiguar qué letra y qué número lleva cada uno de ellos en su camiseta. Para conseguirlo debes atender a las siguientes pistas:

1.- El número que va con la C es dos veces el número de Carmen.

2.- La letra de Carmen aparece en su nombre.

3.- El número de Arturo es el número de Diana menos el número de Benito.

4.- El número de Arturo es dos unidades inferior al de Diana.

5.- La posición de la letra de Benito en el alfabeto (C, por ejemplo, sería 3) es mayor que el número de Benito, y éste es igual que la posición de la letra de Arturo.

¿Puedes averiguarlo y formar así parte del club?

## Solución

- Por la pista 2, la letra de Carmen es la A o la C; por la 1, el número que va con la C es el doble que el de Carmen, así que Carmen no lleva la C: Carmen lleva la **A**, y su número es 2 o 4 (su doble ha de estar entre los números).
- Por la pista 5, el número de Benito es la posición de la letra de Arturo (1, 2, 3 o 4) y debe ser par: 2 o 4. Además, la letra de Benito está en una posición mayor que su número, así que Benito tiene el 2 y una letra de posición 3 o 4 (C o D); y Arturo lleva la **B** (posición 2).
- Por la pista 3, Arturo = Diana − Benito = Diana − 2, que es la pista 4. Con Benito = 2, Arturo y Diana son 4 y 6 o 6 y 8. Carmen lleva el 2 o el 4, pero el 2 es de Benito, así que Carmen lleva el **4**; entonces Arturo **6** y Diana **8**.
- Por la pista 1, la C va con el 8, que es de Diana. Benito lleva la D.

| | Letra | Número |
|---|---|---|
| Arturo | B | 6 |
| Benito | D | 2 |
| Carmen | A | 4 |
| Diana | C | 8 |
