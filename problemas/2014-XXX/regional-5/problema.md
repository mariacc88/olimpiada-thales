---
id: 2014-regional-5
edicion: 2014-XXX
fase: regional
numero: 5
titulo: El contestador loco
bloques: [logica]
bloques_thales: []
etiquetas: [deduccion]
dificultad: medio
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0842]
estado: borrador
notas: ""
---

## Enunciado

El contestador telefónico de Pepe Pinto no funciona correctamente y graba los mensajes en desorden y superpuestos. Sabe que tiene un mensaje cada hora a partir de las 15:00, y ha conseguido descifrar algunos datos, pero le resulta un verdadero enigma lograr entenderlos. Los datos que consiguió descifrar han sido los siguientes:

- Rosana llamó antes que la persona que dejó un saludo grabado.
- Lola llamó a las 15:00, y Carmen no llamó a las 19:00.
- La hija y la prima llamaron para reclamar el pago de una deuda y para hacer una invitación, respectivamente.
- Encarna es el nombre de la esposa de Pepe Pinto y Rocío el de su suegra.
- Ni Rocío, ni Encarna, ni Lola llamaron para hacer una invitación o una pregunta.
- El mensaje de la abuela estaba después del saludo. Y la persona que contó el chiste lo hizo justamente a las 19:00.
- La hija no llamó a las 16:00. El saludo no fue dejado por la suegra.

Sabemos que eres un experto en la resolución de problemas: ayuda de forma razonada a Pepe Pinto a averiguar la hora, el parentesco y el motivo de los mensajes de cada una de las personas que le llamaron el día de ayer.

## Solución

Hay cinco llamadas (de 15:00 a 19:00), cinco parentescos (esposa, suegra, hija, prima y abuela) y cinco motivos (deuda, invitación, pregunta, saludo y chiste).

- Ni Rocío, ni Encarna, ni Lola hicieron la invitación ni la pregunta: las hicieron **Rosana y Carmen**. Como la prima hizo la invitación, la prima es una de ellas dos.
- La hija reclamó la deuda, así que no es Rosana ni Carmen; tampoco Encarna (esposa) ni Rocío (suegra): la hija es **Lola**, que llamó a las 15:00 para reclamar la deuda.
- A Encarna y Rocío les quedan el saludo y el chiste. El saludo no lo dejó la suegra: **Encarna dejó el saludo y Rocío contó el chiste, a las 19:00**.
- Rosana llamó antes del saludo y la abuela después, así que Rosana no es la abuela: **Rosana es la prima** (invitación) y **Carmen es la abuela** (pregunta).
- Quedan las 16:00, 17:00 y 18:00 para Rosana, Encarna y Carmen, en ese orden: Rosana a las 16:00, Encarna a las 17:00 y Carmen a las 18:00.

| Nombre | Hora | Parentesco | Motivo |
|---|---|---|---|
| Lola | 15:00 | Hija | Reclamar el pago de una deuda |
| Rosana | 16:00 | Prima | Hacer una invitación |
| Encarna | 17:00 | Esposa | Dejar un saludo |
| Carmen | 18:00 | Abuela | Hacer una pregunta |
| Rocío | 19:00 | Suegra | Contar un chiste |
