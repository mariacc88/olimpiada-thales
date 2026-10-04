"""Fase 1: prepara el material de trabajo de cada problema de una o varias ediciones.

Para cada problema (fase + número) del inventario reúne en trabajo/<edicion>/<fase>-<n>/:

  borrador.md      metadatos propuestos + texto extraído de todas sus fuentes
  paginas/         páginas renderizadas (PDF, presentaciones convertidas, diapositivas)
  imagenes/        imágenes incrustadas en las fuentes y figuras de la web antigua

Los materiales que cubren una fase entera (una presentación o un PDF con todos los
problemas) van a trabajo/<edicion>/_<fase>-completa/.

A partir de ahí se redacta a mano problemas/<edicion>/<fase>-<n>/problema.md
(las figuras se recortan con scripts/extraer/recortar.py).

Uso:  python scripts/extraer/preparar.py 1985-I 2016-XXXII ...
"""

import csv
import hashlib
import html
import re
import shutil
import subprocess
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

import pymupdf

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
from descargar import decodificar, segmento_antigua  # noqa: E402

TRABAJO = RAIZ / "trabajo"
CONVERTIDOS = TRABAJO / "_convertidos"
SOFFICE = shutil.which("soffice") or r"C:\Program Files\LibreOffice\program\soffice.exe"

CONVERTIBLES = {"pps", "ppsx", "ppt", "pptx", "doc", "docx", "odt", "odp"}
DPI_LECTURA = 110      # páginas para leer; las figuras se recortan aparte a más resolución
MIN_IMAGEN = 60        # lado mínimo (px) de una imagen incrustada para guardarla


def leer_inventario():
    with open(RAIZ / "fuentes" / "inventario.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def leer_ediciones():
    with open(RAIZ / "fuentes" / "ediciones.csv", encoding="utf-8", newline="") as f:
        return {e["id"]: e for e in csv.DictReader(f)}


# --- Conversión y extracción --------------------------------------------------

def a_pdf(ruta):
    """Convierte presentaciones y documentos a PDF con LibreOffice (con caché)."""
    CONVERTIDOS.mkdir(parents=True, exist_ok=True)
    clave = hashlib.md5(str(ruta).encode()).hexdigest()[:8]
    destino = CONVERTIDOS / f"{ruta.stem}-{clave}.pdf"
    if destino.exists():
        return destino
    tmp = CONVERTIDOS / f"tmp-{clave}"
    tmp.mkdir(exist_ok=True)
    origen = tmp / f"{ruta.stem}{ruta.suffix}"
    shutil.copy(ruta, origen)  # copia con nombre sencillo: soffice se lleva mal con algunos nombres
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(origen)],
                   capture_output=True, timeout=300)
    generado = tmp / f"{ruta.stem}.pdf"
    if generado.exists():
        generado.replace(destino)
    shutil.rmtree(tmp, ignore_errors=True)
    return destino if destino.exists() else None


def lineas(texto):
    return [l.strip() for l in texto.splitlines() if l.strip()]


def extraer_pdf(pdf, carpeta, prefijo):
    """Texto por página, páginas renderizadas e imágenes incrustadas.

    Las presentaciones con animaciones generan diapositivas que solo añaden elementos a la
    anterior: se omite una página si todas sus líneas aparecen en la siguiente."""
    doc = pymupdf.open(pdf)
    textos = [p.get_text("text") for p in doc]
    salida = []
    vistas = set()
    for i, pagina in enumerate(doc):
        actuales = set(lineas(textos[i]))
        if i + 1 < len(doc) and actuales and actuales <= set(lineas(textos[i + 1])):
            salida.append(f"<!-- página {i + 1}: omitida (contenida en la siguiente) -->")
            continue
        nombre = f"{prefijo}-p{i + 1:02d}.png"
        pagina.get_pixmap(dpi=DPI_LECTURA).save(carpeta / "paginas" / nombre)
        salida.append(f"### Página {i + 1} (`paginas/{nombre}`)\n\n```text\n{textos[i].strip()}\n```")
        for img in pagina.get_images(full=True):
            xref = img[0]
            if xref in vistas:
                continue
            vistas.add(xref)
            try:
                info = doc.extract_image(xref)
            except Exception:
                continue
            if min(info["width"], info["height"]) < MIN_IMAGEN:
                continue
            datos = info["image"]
            h = hashlib.md5(datos).hexdigest()[:6]
            (carpeta / "imagenes" / f"{prefijo}-p{i + 1:02d}-{h}.{info['ext']}").write_bytes(datos)
    return "\n\n".join(salida)


def html_a_markdown(fragmento):
    r = subprocess.run(["pandoc", "-f", "html", "-t", "markdown-raw_html-native_divs-native_spans-header_attributes",
                        "--wrap=none"], input=fragmento.encode("utf-8"), capture_output=True)
    return r.stdout.decode("utf-8").strip()


def extraer_nodo(ruta_html):
    s = decodificar(ruta_html.read_bytes())
    seg = segmento_antigua(s)
    m = re.search(r'field-name-body.*?<div class="field-item[^"]*">(.*?)</div></div></div>', seg, re.S)
    cuerpo = m.group(1) if m else seg
    cuerpo = re.sub(r"</?font[^>]*>", "", cuerpo)
    return html_a_markdown(cuerpo)


def extraer_ggb(ruta, carpeta, prefijo):
    """Un .ggb es un zip: se guarda su miniatura y se listan los textos de la construcción."""
    try:
        with zipfile.ZipFile(ruta) as z:
            if "geogebra_thumbnail.png" in z.namelist():
                (carpeta / "imagenes" / f"{prefijo}-miniatura.png").write_bytes(z.read("geogebra_thumbnail.png"))
            xml = z.read("geogebra.xml").decode("utf-8", "replace") if "geogebra.xml" in z.namelist() else ""
    except zipfile.BadZipFile:
        return "(fichero GeoGebra no válido)"
    # Los textos de la construcción (enunciado, pasos de la solución…) son expresiones entre comillas
    textos = []
    for etiqueta, exp in re.findall(r'<expression label="([^"]+)" exp="([^"]*)"', xml):
        exp = html.unescape(exp)
        if exp.startswith('"') and len(exp) > 15:
            textos.append(f"**{etiqueta}:** {exp.strip(chr(34))}")
    return "Construcción de GeoGebra. Textos que contiene:\n\n" + "\n\n".join(textos[:60])


# --- Preparación de cada problema ---------------------------------------------

TIPOS_FUENTE = {"nodo-problema", "pdf", "pps", "ppsx", "ppt", "pptx", "doc", "docx", "odt", "odp",
                "ggb", "htm", "html", "slideshare"}


def preparar_problema(clave, filas, ed, figuras_de, carpeta):
    if carpeta.exists():
        shutil.rmtree(carpeta)
    (carpeta / "paginas").mkdir(parents=True)
    (carpeta / "imagenes").mkdir()
    partes = []
    bloques, dificultad = set(), set()
    titulo = ""
    for f in filas:
        prefijo = f["id"]
        ruta = RAIZ / f["ruta_local"] if f["ruta_local"] else None
        cab = f"## Fuente {f['id']} · {f['tipo']} · contenido: {f['contenido']}\n\n{f['url']}\n"
        if f["tipo"] == "nodo-problema":
            titulo = titulo or f["titulo"]
            bloques.update(f["bloques_thales"].split())
            dificultad.update(f["dificultad_thales"].split())
            cuerpo = extraer_nodo(ruta)
            for fig in figuras_de.get(f["id"], []):
                if fig["estado"] == "descargado":
                    destino = carpeta / "imagenes" / f"{fig['id']}-{Path(fig['ruta_local']).name}"
                    shutil.copy(RAIZ / fig["ruta_local"], destino)
                    cuerpo += f"\n\n<!-- figura de la web: imagenes/{destino.name} ({fig['url']}) -->"
                else:
                    cuerpo += f"\n\n<!-- FIGURA PERDIDA (404): {fig['url']} -->"
        elif f["tipo"] == "slideshare":
            jpgs = sorted(ruta.glob("*.jpg"))
            for j in jpgs:
                shutil.copy(j, carpeta / "paginas" / f"{prefijo}-{j.name}")
            cuerpo = f"Presentación sin texto extraíble: {len(jpgs)} diapositivas en `paginas/{prefijo}-*.jpg`."
        elif f["tipo"] == "ggb":
            cuerpo = extraer_ggb(ruta, carpeta, prefijo)
        elif f["tipo"] in ("htm", "html"):
            cuerpo = html_a_markdown(decodificar(ruta.read_bytes()))
        else:
            pdf = ruta if f["tipo"] == "pdf" else a_pdf(ruta)
            cuerpo = extraer_pdf(pdf, carpeta, prefijo) if pdf else "(no se pudo convertir a PDF)"
        titulo = titulo or f["titulo"]
        partes.append(cab + "\n" + cuerpo)

    fase, numero = clave
    meta = [
        "---",
        f"id: {ed['año']}-{fase}-{numero}" if numero else f"id: {ed['año']}-{fase}-completa",
        f"edicion: {ed['id']}",
        f"fase: {fase}",
        f"numero: {numero}",
        f"titulo: {titulo.strip().rstrip('.')}",
        f"bloques: [{', '.join(sorted(bloques))}]",
        "etiquetas: []",
        f"dificultad: {next(iter(dificultad), '')}",
        f"origen_clasificacion: {'thales' if bloques or dificultad else 'propuesta'}",
        "tiene_solucion: ",
        f"fuentes: [{', '.join(f['id'] for f in filas)}]",
        "estado: borrador",
        "---",
    ]
    (carpeta / "borrador.md").write_text("\n".join(meta) + "\n\n" + "\n\n---\n\n".join(partes) + "\n", encoding="utf-8")


def preparar_edicion(id_ed, inventario, ediciones):
    ed = ediciones[id_ed]
    filas = [f for f in inventario if f["edicion"] == id_ed]
    figuras_de = defaultdict(list)
    for f in filas:
        if f["tipo"] == "imagen" and f["contenido"] == "figura":
            figuras_de[f["origen"]].append(f)

    grupos = defaultdict(list)
    vistos = set()
    for f in filas:
        if f["tipo"] not in TIPOS_FUENTE or f["contenido"] == "otro" or f["estado"] not in ("descargado", "descomprimido"):
            continue
        if not f["fase"]:
            print(f"  ! {f['id']} sin fase: {f['titulo'][:50]} ({f['url']})")
            continue
        # La misma copia en las dos webs: basta con una
        nombre = Path(f["ruta_local"]).name
        if (f["fase"], f["numero"], nombre) in vistos:
            continue
        vistos.add((f["fase"], f["numero"], nombre))
        grupos[(f["fase"], f["numero"])].append(f)

    base = TRABAJO / id_ed
    for clave in sorted(grupos, key=lambda c: (c[0], int(c[1] or 0))):
        fase, numero = clave
        carpeta = base / (f"{fase}-{numero}" if numero else f"_{fase}-completa")
        preparar_problema(clave, grupos[clave], ed, figuras_de, carpeta)
        print(f"  {carpeta.relative_to(RAIZ).as_posix():40s} {len(grupos[clave])} fuentes")

    # Esqueleto de edicion.yaml, si aún no existe
    yaml = RAIZ / "problemas" / id_ed / "edicion.yaml"
    if not yaml.exists():
        yaml.parent.mkdir(parents=True, exist_ok=True)
        paginas = ed["paginas"].split()
        yaml.write_text(
            f"id: {id_ed}\nnumero: {ed['numero']}\naño: {ed['año']}\nsede_regional: {ed['sede']}\n"
            f"url_origen: {paginas[0] if paginas else ''}\nnotas: \"\"\n", encoding="utf-8")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    inventario, ediciones = leer_inventario(), leer_ediciones()
    for id_ed in sys.argv[1:]:
        print(id_ed)
        preparar_edicion(id_ed, inventario, ediciones)


if __name__ == "__main__":
    main()
