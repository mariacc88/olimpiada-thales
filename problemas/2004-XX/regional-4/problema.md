---
id: 2004-regional-4
edicion: 2004-XX
fase: regional
numero: 4
titulo: Invertinumeritis aguda
bloques: [numeros]
bloques_thales: [numeros]
etiquetas: [cifras, ecuaciones]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0466, F0469]
estado: borrador
notas: ""
---

## Enunciado

Pepito Despistes está desesperado con su calculadora. Con esto de las nuevas tecnologías ha pillado un virus informático: «El Invertinumeritis». Con este virus cada vez que introduce un número de dos cifras, la maquinita lo entiende al revés. Así por ejemplo, cuando multiplica 23 x 53, le sale 1120.

Ayer metió la pata cuando su profesor le pidió que hiciera una multiplicación con la calculadora, pero hoy ha tenido mucha suerte porque debía hallar 46 x 96

Busca tú otros dos números naturales menores que 100, formados con 4 dígitos distintos, para que al multiplicarlos con su calculadora Pepito acierte el resultado otra vez.

![Ilustración](ilustracion.png)

## Solución

Si los números son $\overline{ab} = 10a + b$ y $\overline{cd} = 10c + d$, la calculadora multiplica $\overline{ba} \cdot \overline{dc}$. Queremos que

$$(10a + b)(10c + d) = (10b + a)(10d + c).$$

Desarrollando, $100ac + 10ad + 10bc + bd = 100bd + 10bc + 10ad + ac$, es decir, $99ac = 99bd$:

$$a \cdot c = b \cdot d.$$

Basta, por tanto, buscar cuatro cifras distintas tales que el producto de las cifras de las decenas sea igual al de las unidades. Por ejemplo, $2 \cdot 4 = 1 \cdot 8$ da $21 \cdot 48 = 1008 = 12 \cdot 84$. Todas las soluciones (sin contar el orden de los factores) son:

| | | |
|---|---|---|
| $21 \cdot 36 = 12 \cdot 63$ | $21 \cdot 48 = 12 \cdot 84$ | $26 \cdot 31 = 62 \cdot 13$ |
| $28 \cdot 41 = 82 \cdot 14$ | $32 \cdot 46 = 23 \cdot 64$ | $36 \cdot 42 = 63 \cdot 24$ |
| $32 \cdot 69 = 23 \cdot 96$ | $39 \cdot 62 = 93 \cdot 26$ | $48 \cdot 63 = 84 \cdot 36$ |
| $43 \cdot 68 = 34 \cdot 86$ | | |

(El 46 · 96 del enunciado no tiene las cuatro cifras distintas.)
