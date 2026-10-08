---
id: 2007-provincial-1
edicion: 2007-XXIII
fase: provincial
numero: 1
titulo: ¡Vaya pueblo!
bloques: [numeros, logica]
bloques_thales: [numeros]
etiquetas: [patrones]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0588, F0592]
estado: borrador
notas: ""
---

## Enunciado

![Ilustración: Pimpolina](ilustracion.png)

Los 3072 matelandeses se han vuelto cotillas. Desde que una persona conoce una noticia, no puede parar de contarla cada media hora a tres personas que la desconocen.

A las ocho de la mañana Olimpín, Triangulina y Pentagonín se han enterado de que Edur Neper viene a dar un concierto.

**¿A qué hora lo sabrá todo el pueblo? **

## Solución

Cada media hora, cada persona que conoce la noticia se la cuenta a tres nuevas, así que el número de personas que la conocen se multiplica por 4:

| Hora | 8:00 | 8:30 | 9:00 | 9:30 | 10:00 | 10:30 |
|---|---|---|---|---|---|---|
| La conocen | 3 | 12 | 48 | 192 | 768 | 3072 |

A las **10:30** lo sabe todo el pueblo.
