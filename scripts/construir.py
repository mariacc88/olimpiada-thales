"""Fase 3: construye los datos de la web a partir de problemas/.

Genera en web/datos/ (no se versiona; se regenera siempre):

  problemas.json             índice con metadatos, enunciado y solución (Markdown) de cada problema
  fig/<id>/…                 figuras de cada problema
  typst/<id>-enunciado.typ   fragmentos Typst para componer hojas en PDF
  typst/<id>-solucion.typ
  hoja.typ                   plantilla de la hoja (copia de plantillas/hoja.typ)

Uso:  python scripts/construir.py
"""

import csv
import json
import re
import shutil
import subprocess
import sys
from datetime import date

from PIL import Image

from comun import RAIZ, figuras, leer_ediciones, leer_problemas, leer_taxonomia
from validar import validar

DATOS = RAIZ / "web" / "datos"
ANCHO_MAX_CM = 15.0
ANCHO_ILUSTRACION_CM = 4.5  # las imágenes decorativas (ilustracion*.png) se imprimen pequeñas


def urls_inventario():
    with open(RAIZ / "fuentes" / "inventario.csv", encoding="utf-8", newline="") as f:
        return {fila["id"]: fila["url"] for fila in csv.DictReader(f)}


def ancho_impresion_cm(ruta):
    """Tamaño natural de una figura en papel: los recortes de PDF están a 300 ppp; las imágenes
    pequeñas de la web antigua, a 96 ppp."""
    px, alto = Image.open(ruta).size
    if ruta.name.startswith("ilustracion"):
        # el lado mayor no pasa de ANCHO_ILUSTRACION_CM (las fotos verticales también quedan pequeñas)
        return min(round(px / 96 * 2.54, 1), round(ANCHO_ILUSTRACION_CM * min(1, px / alto), 1))
    ppp = 300 if px >= 600 else 96
    return min(ANCHO_MAX_CM, round(px / ppp * 2.54, 1))


def a_typst(markdown, id_, anchos):
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "typst", "--wrap=preserve"],
                       input=markdown.encode("utf-8"), capture_output=True, check=True)
    t = r.stdout.decode("utf-8")
    # Rutas de las figuras relativas a la raíz del proyecto Typst (web/datos) y con su ancho natural
    t = re.sub(r'image\("([^"]+)"',
               lambda m: f'image("/fig/{id_}/{m.group(1)}", width: {anchos.get(m.group(1), ANCHO_MAX_CM)}cm',
               t)
    # Tablas de Markdown con la cabecera vacía (cuadrículas): sin fila de cabecera
    t = re.sub(r"table\.header\((?:\[\],\s*)+\),\s*table\.hline\(\),\s*", "", t)
    return t


def construir():
    tax = leer_taxonomia()
    ediciones = leer_ediciones()
    urls = urls_inventario()
    if DATOS.exists():
        shutil.rmtree(DATOS)
    (DATOS / "typst").mkdir(parents=True)
    shutil.copy(RAIZ / "plantillas" / "hoja.typ", DATOS / "hoja.typ")

    problemas = []
    for carpeta, meta, sec, _ in leer_problemas():
        id_ = meta["id"]
        ed = ediciones[meta["edicion"]]
        anchos = {}
        for fig in set(figuras(sec.get("enunciado")) + figuras(sec.get("solución"))):
            destino = DATOS / "fig" / id_ / fig
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(carpeta / fig, destino)
            anchos[fig] = ancho_impresion_cm(destino)

        def para_web(md):
            return re.sub(r"(!\[[^\]]*\]\()([^)\s]+)", lambda m: f"{m.group(1)}datos/fig/{id_}/{m.group(2)}", md or "")

        enunciado, solucion = sec.get("enunciado", ""), sec.get("solución", "")
        (DATOS / "typst" / f"{id_}-enunciado.typ").write_text(a_typst(enunciado, id_, anchos), encoding="utf-8")
        if solucion:
            (DATOS / "typst" / f"{id_}-solucion.typ").write_text(a_typst(solucion, id_, anchos), encoding="utf-8")

        problemas.append({
            "id": id_,
            "edicion": ed["id"],
            "edicion_numero": ed["numero"],
            "año": ed["año"],
            "sede": ed.get("sede_regional", ""),
            "fase": meta["fase"],
            "numero": meta["numero"],
            "titulo": meta["titulo"],
            "bloques": meta["bloques"],
            "etiquetas": meta["etiquetas"],
            "dificultad": meta["dificultad"],
            "tiene_solucion": meta["tiene_solucion"],
            "estado": meta["estado"],
            "notas": meta.get("notas") or "",
            "fuentes": [urls[f] for f in meta["fuentes"] if f in urls],
            "figuras": sorted(f"fig/{id_}/{f}" for f in anchos),
            "enunciado": para_web(enunciado),
            "solucion": para_web(solucion),
        })

    problemas.sort(key=lambda p: (p["año"], p["fase"] != "provincial", p["numero"]))
    datos = {
        "generado": date.today().isoformat(),
        "taxonomia": tax,
        "ediciones": {k: {"numero": v["numero"], "año": v["año"], "sede": v.get("sede_regional", "")}
                      for k, v in ediciones.items()},
        "problemas": problemas,
    }
    (DATOS / "problemas.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(problemas)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errores, _, _ = validar()
    if errores:
        print("\n".join(f"ERROR  {e}" for e in errores))
        sys.exit("Corrige los errores (scripts/validar.py) antes de construir.")
    n = construir()
    print(f"{n} problemas → {DATOS.relative_to(RAIZ).as_posix()}/")


if __name__ == "__main__":
    main()
