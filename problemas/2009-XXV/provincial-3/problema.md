---
id: 2009-provincial-3
edicion: 2009-XXV
fase: provincial
numero: 3
titulo: Problema de idiomas
bloques: [estadistica, logica]
bloques_thales: [logica]
etiquetas: [combinatoria, deduccion]
dificultad: facil
origen_clasificacion: propuesta
tiene_solucion: true
fuentes: [F0721, F0725]
estado: borrador
notas: ""
---

## Enunciado

El profesor de Matemáticas le propuso a Arquimedín la siguiente cuestión:

"En la clase de al lado 6 estudiantes saben español, 7 inglés y 5 francés. De estos sólo uno habla los tres idiomas. De los demás, se sabe que exactamente 2 saben sólo español e inglés, exactamente 2 saben sólo inglés y francés y 1 único alumno sabe sólo español y francés.

**¿Cuántos estudiantes hay en la clase?". Arquimedín le contestó: "Profesor, estoy convencido que 12". ¿Es correcta la contestación? Razona tu respuesta.**

## Solución

Lo representamos con un diagrama de Venn de tres conjuntos: español (E), inglés (I) y francés (F). Empezamos por el centro y vamos hacia fuera:

- Los tres idiomas: 1.
- Solo español e inglés: 2; solo inglés y francés: 2; solo español y francés: 1.
- Solo español: $6 - (1 + 2 + 1) = 2$; solo inglés: $7 - (1 + 2 + 2) = 2$; solo francés: $5 - (1 + 2 + 1) = 1$.

En total hay $1 + 2 + 2 + 1 + 2 + 2 + 1 = 11$ estudiantes: **Arquimedín no tiene razón**.

(Con la fórmula de la unión de tres conjuntos: $6 + 7 + 5 - 3 - 3 - 2 + 1 = 11$, ya que hablan español e inglés $2 + 1 = 3$, inglés y francés 3, y español y francés 2.)
