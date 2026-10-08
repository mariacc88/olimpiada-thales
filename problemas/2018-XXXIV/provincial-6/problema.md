---
id: 2018-provincial-6
edicion: 2018-XXXIV
fase: provincial
numero: 6
titulo: Mensajes secretos
bloques: [logica, estadistica]
bloques_thales: []
etiquetas: [deduccion, combinatoria]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0899]
estado: borrador
notas: "Las permutaciones se escriben como en el original: la fila de abajo indica a qué posición pasa la letra de cada posición."
---

## Enunciado

Alan Turing y Adi Shamir han decidido cifrar los mensajes que se envían para que sus enemigos no los entiendan. Para ello han ideado el siguiente método.

![Ilustración: un detective con una lupa](ilustracion.png)

Tomemos como ejemplo el mensaje «NOS VEMOS LUEGO».

Primero eligen una permutación, que será la clave, por ejemplo

$$\begin{pmatrix} 1 & 2 & 3 & 4 \\ 3 & 1 & 4 & 2 \end{pmatrix}$$

(significa que la letra que está en la posición 1 pasa a la 3, la que está en la 2 pasa a la 1, la 3 a la 4 y la 4 a la 2).

A continuación descomponen el mensaje en bloques de la longitud de la permutación (en este caso, bloques de 4). Los espacios se escriben como asteriscos, y también se completa con asteriscos el último bloque. Así, el mensaje NOS VEMOS LUEGO queda:

NOS\*   VEMO   S\*LU   EGO\*

Después aplican la permutación a cada bloque:

O\*NS   EOVM   \*USL   G\*EO

con lo que el mensaje cifrado queda «O\*NSEOVM\*USLG\*EO».

**Contesta de forma razonada** los siguientes apartados:

a) Alan Turing quiere mandarle a Adi Shamir el mensaje «DONDE NOS VEMOS» con la clave $\begin{pmatrix} 1 & 2 & 3 & 4 \\ 4 & 3 & 1 & 2 \end{pmatrix}$. ¿Cómo se lo enviará cifrado?

b) La respuesta de Adi Shamir la ha enviado cifrada con la clave $\begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 3 & 1 \end{pmatrix}$. Dice así: «LE\*NUAP\*AETR\*\*EDCT\*U\*AAS». Tradúcela.

c) El mensaje «LO PASAREMOS BIEN» se ha cifrado como «P\*LAOERSMAB\*OIS\*\*E\*N». Sabemos que están utilizando una clave de longitud 5. Identifica la clave que han utilizado.

## Solución

a) Bloques de 4: DOND   E\*NO   S\*VE   MOS\*. Aplicando la clave (la 1.ª letra pasa a la 4.ª posición, la 2.ª a la 3.ª, la 3.ª a la 1.ª y la 4.ª a la 2.ª):

NDOD   NO\*E   VE\*S   S\*OM

El mensaje cifrado es **«NDODNO\*EVE\*SS\*OM»**.

b) Separamos en bloques de 4 y deshacemos la permutación (la letra que está en la posición 2 vuelve a la 1, la de la 4 a la 2, la de la 3 se queda y la de la 1 vuelve a la 4):

LE\*N   UAP\*   AETR   \*\*ED   CT\*U   \*AAS

EN\*L   A\*PU   ERTA   \*DE\*   TU\*C   ASA\*

El mensaje es **«EN LA PUERTA DE TU CASA»**.

c) En bloques de 5:

LO\*PA   SAREM   OS\*BI   EN\*\*\*

P\*LAO   ERSMA   B\*OIS   \*\*E\*N

En el primer bloque, la L (posición 1) pasa a la 3, la O (2) a la 5, el \* (3) a la 2, la P (4) a la 1 y la A (5) a la 4, y lo mismo ocurre en los demás bloques. La clave es

$$\begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 2 & 1 & 4 \end{pmatrix}.$$
