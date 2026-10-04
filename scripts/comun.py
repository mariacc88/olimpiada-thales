"""Lectura de la base de datos de problemas (problemas/*/*/problema.md) y de la taxonomía."""

import re
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
PROBLEMAS = RAIZ / "problemas"

FASES = ("provincial", "regional")
ESTADOS = ("borrador", "revisado")
ORIGENES = ("propuesta", "revisada")
OBLIGATORIOS = ("id", "edicion", "fase", "numero", "titulo", "bloques", "etiquetas", "dificultad",
                "origen_clasificacion", "tiene_solucion", "fuentes", "estado")


def leer_taxonomia():
    t = yaml.safe_load((RAIZ / "taxonomia.yaml").read_text(encoding="utf-8"))
    bloques = {k: v["nombre"] for k, v in t["bloques"].items()}
    etiquetas = {}
    for b, v in t["bloques"].items():
        for e, nombre in (v.get("etiquetas") or {}).items():
            etiquetas[e] = {"nombre": nombre, "bloque": b}
    return {"bloques": bloques, "etiquetas": etiquetas, "dificultades": t["dificultades"]}


def leer_ediciones():
    ediciones = {}
    for f in sorted(PROBLEMAS.glob("*/edicion.yaml")):
        e = yaml.safe_load(f.read_text(encoding="utf-8"))
        ediciones[e["id"]] = e
    return ediciones


def partir(md):
    """Separa la cabecera YAML y las secciones «## Enunciado» y «## Solución»."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", md, re.S)
    if not m:
        raise ValueError("falta la cabecera YAML entre líneas ---")
    meta = yaml.safe_load(m.group(1))
    cuerpo = m.group(2)
    secciones = {}
    for s in re.split(r"^## ", cuerpo, flags=re.M)[1:]:
        titulo, _, texto = s.partition("\n")
        secciones[titulo.strip().lower()] = texto.strip()
    return meta, secciones


def leer_problemas():
    """Lista de (carpeta, meta, secciones). Los errores de lectura se devuelven como meta=None."""
    resultado = []
    for f in sorted(PROBLEMAS.glob("*/*/problema.md")):
        try:
            meta, secciones = partir(f.read_text(encoding="utf-8"))
            resultado.append((f.parent, meta, secciones, None))
        except Exception as e:  # noqa: BLE001
            resultado.append((f.parent, None, None, str(e)))
    return resultado


def figuras(texto):
    """Rutas de las imágenes referenciadas en un texto Markdown."""
    return re.findall(r"!\[[^\]]*\]\(([^)\s]+)", texto or "")
