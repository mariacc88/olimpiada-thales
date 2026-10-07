"""Fase 1: primera versión automática de problema.md para los problemas de la web antigua (HTML).

Parte del material de trabajo de preparar.py (trabajo/<edicion>/<fase>-<n>/) y escribe
problemas/<edicion>/<fase>-<n>/problema.md con:

  - el enunciado pasado a Markdown y limpio (comillas, saltos de línea, restos de pandoc);
  - las figuras convertidas a PNG: fig1.png, fig2.png… y, si es una miniatura de clip-art
    de la web antigua (/files/active/…), ilustracion.png;
  - metadatos sacados del inventario, con bloque y dificultad SIN RELLENAR a propósito:
    validar.py los marca como errores hasta que se revisa y clasifica cada problema.

No sobrescribe un problema.md que ya exista (salvo con --forzar).

Uso:  python scripts/extraer/desde_html.py 1986-II 1987-III … [--forzar]
"""

import csv
import re
import sys
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parents[2]
TRABAJO = RAIZ / "trabajo"
PROBLEMAS = RAIZ / "problemas"


def inventario():
    with open(RAIZ / "fuentes" / "inventario.csv", encoding="utf-8", newline="") as f:
        return {fila["id"]: fila for fila in csv.DictReader(f)}


def protegidos():
    """Problemas escritos a mano que no se regeneran ni con --forzar (fuentes/revisiones/no-regenerar.txt)."""
    f = RAIZ / "fuentes" / "revisiones" / "no-regenerar.txt"
    return set(f.read_text(encoding="utf-8").split()) if f.exists() else set()


def comillas(texto):
    """Comillas rectas por comillas latinas, por parejas dentro de cada párrafo."""
    def par(m):
        p = m.group(0)
        n = 0

        def alterna(_):
            nonlocal n
            n += 1
            return "«" if n % 2 else "»"
        return re.sub(r'"', alterna, p) if p.count('"') % 2 == 0 else p
    return re.sub(r"[^\n]+", par, texto)


def limpiar(md):
    md = re.sub(r"^:::.*$", "", md, flags=re.M)              # contenedores de pandoc
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = re.sub(r"\{[^{}]*(height|width|border)=[^{}]*\}", "", md)  # atributos de imagen
    md = re.sub(r"^\[\s*$", "", md, flags=re.M)                # envoltorios [ … ]{.image .preview}
    md = re.sub(r"^\s*\]\{[^}]*\}", "", md, flags=re.M)
    md = re.sub(r"\[([^\]]*)\]\{\.underline\}", r"\1", md)     # subrayados
    md = re.sub(r"(\w)\^([^\^\s]+)\^", r"$\1^{\2}$", md)      # superíndices de pandoc (3^3^)
    md = md.replace('\\"', '"').replace("\\'", "'")
    md = re.sub(r"\\([()\[\]*_.$<>-])", r"\1", md)             # escapes innecesarios
    md = re.sub(r"\\\n", "\n\n", md)                           # saltos de línea forzados
    md = re.sub(r"\\\s*$", "", md, flags=re.M)
    md = md.replace(" ", " ")                             # espacios duros de la web antigua
    md = re.sub(r"(?<=\S) {2,}(?=\S)", " ", md)                 # espacios repetidos dentro del texto
    md = re.sub(r"^[ \t]+$", "", md, flags=re.M)               # líneas con solo espacios
    md = re.sub(r"^[ \t]+(?=\S)", "", md, flags=re.M)          # sangrías (Markdown las tomaría por código)
    md = re.sub(r"\*{4,}", "", md)                             # negritas vacías
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"(!\[[^\]]*\]\([^)]+\))\n(?=\S)", r"\1\n\n", md)  # imagen pegada al párrafo siguiente
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = comillas(md)
    return md.strip()


def figura_local(url, carpeta_trabajo, inv):
    """Busca en imagenes/ el fichero descargado de esa URL (por nombre)."""
    nombre = url.rsplit("/", 1)[-1]
    for f in (carpeta_trabajo / "imagenes").glob(f"*-{nombre}"):
        return f
    return None


def convertir(problema, inv, forzar):
    trabajo = TRABAJO / problema
    destino = PROBLEMAS / problema
    if (destino / "problema.md").exists() and (not forzar or problema in protegidos()):
        return "ya existe" + (" (protegido)" if forzar else "")
    borrador = (trabajo / "borrador.md").read_text(encoding="utf-8")
    fuentes = re.findall(r"^## Fuente (F\d+) · nodo-problema", borrador, re.M)
    if not fuentes:
        return "sin nodo HTML"
    fila = inv[fuentes[0]]
    # Texto de la primera fuente (si hay dos nodos con el mismo número, se avisa en notas)
    bloque = borrador.split(f"## Fuente {fuentes[0]}", 1)[1]
    bloque = re.split(r"^---$|^## Fuente ", bloque, maxsplit=1, flags=re.M)[0]
    cuerpo = bloque.split("\n", 2)[2] if bloque.count("\n") >= 2 else ""
    cuerpo = re.sub(r"^https://thales\.cica\.es\S*\s*", "", cuerpo.strip())

    destino.mkdir(parents=True, exist_ok=True)
    for viejo in destino.glob("*.png"):  # al regenerar, fuera las imágenes de la versión anterior
        viejo.unlink()
    notas = []
    n_fig = 0
    n_ilus = 0
    vistas = set()

    def imagen(m):
        nonlocal n_fig, n_ilus
        alt, url = m.group(1), m.group(2)
        if url in vistas:  # la misma imagen repetida (p. ej. varias ovejas): una basta
            return ""
        vistas.add(url)
        local = figura_local(url, trabajo, inv)
        # Clip-art de la web antigua: miniaturas de /files/active/ y personajes de Matelandia
        decorativa = "/files/active/" in url or "/Matelandia/" in url
        if not local:
            if decorativa:
                notas.append(f"ilustración perdida: {url}")
                return ""
            notas.append(f"figura perdida: {url}")
            return f"\n\n**[FIGURA PERDIDA]**\n\n"
        if decorativa:
            n_ilus += 1
            nombre = "ilustracion.png" if n_ilus == 1 else f"ilustracion{n_ilus}.png"
            alt = f"Ilustración: {alt}" if alt else "Ilustración"
        else:
            n_fig += 1
            nombre = f"fig{n_fig}.png"
            alt = alt or "Figura"
        im = Image.open(local)
        im.convert("RGBA" if im.mode in ("P", "RGBA", "LA") else "RGB").save(destino / nombre)
        return f"\n\n![{alt}]({nombre})\n\n"

    # Miniaturas enlazadas a la imagen grande: [![alt](pequeña)](grande) → la grande
    cuerpo = re.sub(r"\[!\[([^\]]*)\]\([^)]*\)\]\(([^)\s]+)[^)]*\)", lambda m: f"![{m.group(1)}]({m.group(2)})", cuerpo)
    cuerpo = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)[^)]*\)", imagen, cuerpo)
    cuerpo = limpiar(cuerpo)
    if len(fuentes) > 1:
        notas.append(f"hay {len(fuentes)} nodos con este número en la web: {', '.join(fuentes)}")

    edicion = problema.split("/")[0]
    fase, numero = problema.split("/")[1].split("-")
    titulo = fila["titulo"].strip().rstrip(".")
    if any(c in titulo for c in ':¿?#"'):
        titulo = '"' + titulo.replace('"', "'") + '"'
    bloques_thales = fila["bloques_thales"].split()
    meta = f"""---
id: {edicion.split('-')[0]}-{fase}-{numero}
edicion: {edicion}
fase: {fase}
numero: {numero}
titulo: {titulo}
bloques: []
bloques_thales: [{', '.join(bloques_thales)}]
etiquetas: []
dificultad: {fila['dificultad_thales'] or ''}
origen_clasificacion: propuesta
tiene_solucion: false
fuentes: [{', '.join(fuentes)}]
estado: borrador
notas: "{'; '.join(notas)}"
---

## Enunciado

{cuerpo}
"""
    (destino / "problema.md").write_text(meta, encoding="utf-8")
    return f"ok ({n_fig} fig.{', ' + '; '.join(notas) if notas else ''})"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    forzar = "--forzar" in sys.argv
    inv = inventario()
    for ed in [a for a in sys.argv[1:] if not a.startswith("--")]:
        for carpeta in sorted((TRABAJO / ed).iterdir(), key=lambda c: (c.name.split("-")[0], int(c.name.split("-")[-1]) if c.name.split("-")[-1].isdigit() else 0)):
            if carpeta.name.startswith("_"):
                continue
            print(f"{ed}/{carpeta.name}: {convertir(f'{ed}/{carpeta.name}', inv, forzar)}")


if __name__ == "__main__":
    main()
