// Plantilla de las hojas de problemas en PDF.
// La usan scripts/hoja.py (en local) y el explorador web (en el navegador, con typst.ts).
// Cada hoja es un documento que importa estas funciones e incluye los fragmentos
// /typst/<id>-enunciado.typ y /typst/<id>-solucion.typ generados por scripts/construir.py.

#let gris = luma(110)

#let hoja(titulo: none, subtitulo: none, cuerpo) = {
  set document(title: if titulo != none { titulo } else { "Problemas de la Olimpiada Matemática Thales" })
  set page(
    paper: "a4",
    margin: (x: 2.2cm, top: 2cm, bottom: 2.2cm),
    footer: context {
      set text(8pt, fill: gris)
      [Olimpiada Matemática Thales · SAEM Thales]
      h(1fr)
      counter(page).display()
    },
  )
  set text(lang: "es", size: 11pt)
  set par(justify: true, leading: 0.62em, spacing: 0.9em)
  set list(indent: 0.8em)
  set enum(indent: 0.8em)
  // Las figuras van centradas y sin pie: el texto alternativo solo sirve para la web
  set figure(numbering: none, gap: 0.5em)
  show figure.caption: none
  show figure: set block(above: 0.9em, below: 0.9em)
  set table(stroke: 0.5pt + luma(160), inset: (x: 6pt, y: 4pt))

  if titulo != none {
    align(center, text(16pt, weight: "bold", titulo))
    if subtitulo != none { align(center, text(10pt, fill: gris, subtitulo)) }
    v(0.8em)
  }
  cuerpo
}

// Un problema: número en la hoja, título y, opcionalmente, su procedencia
#let problema(n: none, titulo: "", origen: none, cuerpo) = block(width: 100%, above: 1.6em, below: 0.6em)[
  #block(sticky: true, below: 0.7em)[
    #text(12pt, weight: "bold")[#if n != none [#n. ]#titulo]
    #if origen != none [ #h(0.4em) #text(9pt, fill: gris, origen)]
  ]
  #cuerpo
]

// Solución de un problema (tras el enunciado o en el bloque final de soluciones)
#let solucion(n: none, titulo: none, cuerpo) = block(width: 100%, above: 1.2em, below: 0.6em, inset: (left: 0.9em), stroke: (left: 1.5pt + luma(190)))[
  #text(10.5pt, weight: "bold", fill: gris)[Solución#if n != none [ #n]#if titulo != none [: #titulo]]
  #v(0.2em)
  #cuerpo
]

#let soluciones() = {
  pagebreak(weak: true)
  align(center, text(14pt, weight: "bold")[Soluciones])
  v(0.4em)
}

#let sin-solucion = text(fill: gris, style: "italic")[No se dispone de la solución oficial de este problema.]
