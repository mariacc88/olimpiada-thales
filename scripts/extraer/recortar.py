"""Recorta una figura de una fuente del inventario y la guarda como PNG.

Las coordenadas son fracciones (0–1) de la página o imagen: izquierda, arriba, derecha, abajo.
Así se pueden leer directamente sobre las páginas de trabajo/…/paginas/, sea cual sea su tamaño.

  Fuente PDF o presentación (se renderiza a 300 ppp):
    python scripts/extraer/recortar.py F0852 3 0.10 0.20 0.60 0.85 problemas/2016-XXXII/provincial-1/fig1.png

  Fuente imagen (jpg, gif, png, o diapositiva de SlideShare), con página «-»:
    python scripts/extraer/recortar.py F0006 - 0 0 1 1 problemas/1985-I/provincial-3/fig1.png
    python scripts/extraer/recortar.py ruta/a/imagen.jpg - 0.1 0.1 0.9 0.9 destino.png

Opciones:
  --dpi N      resolución para fuentes PDF (por defecto 300)
  --diapositiva N   con fuentes de SlideShare, número de diapositiva
  --sin-fondo  con fuentes PDF, sustituye por blanco las imágenes que ocupan más del 30 %
               de la página (fondos de diapositiva o marcas de agua) y conserva figuras, dibujos y texto
"""

import argparse
import csv
import sys
from pathlib import Path

import pymupdf
from PIL import Image

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from preparar import CONVERTIBLES, a_pdf  # noqa: E402


def fila_inventario(id_):
    with open(RAIZ / "fuentes" / "inventario.csv", encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            if fila["id"] == id_:
                return fila
    sys.exit(f"No existe {id_} en el inventario")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("fuente", help="id del inventario (F0123) o ruta a una imagen")
    p.add_argument("pagina", help="número de página (PDF) o «-» para imágenes")
    p.add_argument("caja", nargs=4, type=float, metavar=("IZQ", "ARR", "DER", "ABA"))
    p.add_argument("destino")
    p.add_argument("--dpi", type=int, default=300)
    p.add_argument("--diapositiva", type=int)
    p.add_argument("--sin-fondo", action="store_true",
                   help="PDF: sustituye por blanco las imágenes que ocupan más del 30 %% de la página (fondos)")
    a = p.parse_args()
    x0, y0, x1, y1 = a.caja
    destino = Path(a.destino)
    destino.parent.mkdir(parents=True, exist_ok=True)

    if a.fuente.startswith("F") and a.fuente[1:].isdigit():
        fila = fila_inventario(a.fuente)
        ruta = RAIZ / fila["ruta_local"]
        if fila["tipo"] == "slideshare":
            ruta = ruta / f"{a.diapositiva:03d}.jpg"
        elif fila["tipo"] in CONVERTIBLES:
            ruta = a_pdf(ruta)
    else:
        ruta = Path(a.fuente)

    if ruta.suffix.lower() == ".pdf":
        pagina = pymupdf.open(ruta)[int(a.pagina) - 1]
        r = pagina.rect
        clip = pymupdf.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height, r.x0 + x1 * r.width, r.y0 + y1 * r.height)
        if a.sin_fondo:
            # Los fondos de diapositiva son imágenes que ocupan casi toda la página: se sustituyen por blanco
            blanco = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, 1, 1), 0)
            blanco.set_pixel(0, 0, (255, 255, 255))
            for info in pagina.get_image_info(xrefs=True):
                caja = pymupdf.Rect(info["bbox"])
                if info["xref"] and caja.get_area() > 0.3 * r.get_area():
                    pagina.replace_image(info["xref"], pixmap=blanco)
        pagina.get_pixmap(dpi=a.dpi, clip=clip).save(destino)
    else:
        img = Image.open(ruta).convert("RGB")
        w, h = img.size
        img.crop((round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h))).save(destino)
    print(f"{destino} ({Image.open(destino).size[0]}×{Image.open(destino).size[1]} px)")


if __name__ == "__main__":
    main()
