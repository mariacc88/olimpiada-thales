---
id: 2006-provincial-6
edicion: 2006-XXII
fase: provincial
numero: 6
titulo: "Ten amigos 'pa' esto"
bloques: [numeros, geometria]
bloques_thales: []
etiquetas: [divisibilidad, cuerpos]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0556, F0558]
estado: borrador
notas: ""
---

## Enunciado

Me ha llegado un aviso de correos para recoger un paquete. Aprovechando que mi amiga Carlota trabaja allí, la llamo para preguntarle las dimensiones y así saber si puedo ir en bici a recogerlo. En seguida me arrepentí, porque Carlota, que es una «pirada» de las Matemáticas, me dio la siguiente respuesta: Sólo te diré que tiene la misma forma que una caja de zapatos y que la superficie de sus caras es 120 c$m^{2}$, 80 c$m^{2}$ y 96 c$m^{2}$ respectivamente. **¿Cuáles son las dimensiones del paquete?**

## Solución

Si las aristas de la caja miden $a$, $b$ y $c$, las caras miden $a \cdot b = 120$, $b \cdot c = 96$ y $a \cdot c = 80$ cm².

Descomponemos: $120 = 2^3 \cdot 3 \cdot 5$, $96 = 2^5 \cdot 3$ y $80 = 2^4 \cdot 5$.

- El 5 está en 120 y en 80, pero no en 96: es un factor de $a$ (y no de $b$ ni de $c$).
- El 3 está en 120 y en 96, pero no en 80: es un factor de $b$.
- Multiplicando las tres igualdades, $(abc)^2 = 120 \cdot 96 \cdot 80 = 921\,600$, así que $abc = 960$. Entonces $c = 960 : 120 = 8$, $a = 960 : 96 = 10$ y $b = 960 : 80 = 12$.

El paquete mide **10 cm × 12 cm × 8 cm**. (Comprobación: $10 \cdot 12 = 120$, $12 \cdot 8 = 96$, $10 \cdot 8 = 80$.)
