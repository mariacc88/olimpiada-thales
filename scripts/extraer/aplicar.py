"""Aplica a problemas/ la revisión de un lote: clasificación, correcciones de texto y renombrados.

La revisión de cada lote se escribe como un fichero YAML en fuentes/revisiones/ (versionado), por ejemplo:

  1986-II/regional-1:
    clasificar: [[numeros], [proporcionalidad], medio]   # bloques, etiquetas, dificultad
    reemplazar: [["texto viejo", "texto nuevo"], …]      # sustituciones literales en el problema
    renombrar: [[fig1.png, ilustracion.png], …]          # ficheros de imagen (y sus referencias)
    alt: [[ilustracion.png, "Ilustración: un fantasma"]] # texto alternativo de una imagen
    notas: "…"                                           # sustituye el campo notas
    titulo: "…"                                          # sustituye el título
    enunciado: |                                         # reescribe el enunciado entero
      …

  1986-II/regional-8:
    desde: F0046            # crea el problema a partir de otro nodo HTML del inventario
    clasificar: …

Uso:  python scripts/extraer/aplicar.py fuentes/revisiones/revision-1986-1987.yaml
"""

import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))


def poner_campo(texto, campo, valor):
    return re.sub(rf"^{campo}: .*$", lambda _: f"{campo}: {valor}", texto, count=1, flags=re.M)


def lista(v):
    return "[" + ", ".join(v) + "]"


def comillas_yaml(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def crear_desde(destino_rel, fuente):
    """Genera problema.md desde un nodo concreto del inventario (para números mal puestos en la web)."""
    import desde_html
    inv = desde_html.inventario()
    trabajo = RAIZ / "trabajo" / destino_rel
    borrador_original = None
    # Se reutiliza el borrador de la carpeta de trabajo de ese nodo
    for b in (RAIZ / "trabajo").glob(f"{destino_rel.split('/')[0]}/*/borrador.md"):
        if f"## Fuente {fuente} · nodo-problema" in b.read_text(encoding="utf-8"):
            borrador_original = b
            break
    if not borrador_original:
        sys.exit(f"No encuentro el borrador del nodo {fuente}")
    texto = borrador_original.read_text(encoding="utf-8")
    # Borrador solo con esa fuente
    partes = re.split(r"(?=^## Fuente )", texto, flags=re.M)
    propia = [p for p in partes if p.startswith(f"## Fuente {fuente}")][0].split("\n---\n")[0]
    trabajo.mkdir(parents=True, exist_ok=True)
    (trabajo / "imagenes").mkdir(exist_ok=True)
    for img in (borrador_original.parent / "imagenes").glob("*"):
        (trabajo / "imagenes" / img.name).write_bytes(img.read_bytes())
    (trabajo / "borrador.md").write_text(partes[0] + propia, encoding="utf-8")
    print(f"  {destino_rel}: {desde_html.convertir(destino_rel, inv, forzar=True)}")


def aplicar(revision):
    for rel, cambios in revision.items():
        carpeta = RAIZ / "problemas" / rel
        if "desde" in cambios:
            crear_desde(rel, cambios["desde"])
        ruta = carpeta / "problema.md"
        s = ruta.read_text(encoding="utf-8")
        if "clasificar" in cambios:
            bloques, etiquetas, dificultad = cambios["clasificar"]
            s = poner_campo(s, "bloques", lista(bloques))
            s = poner_campo(s, "etiquetas", lista(etiquetas))
            s = poner_campo(s, "dificultad", dificultad)
        if "enunciado" in cambios:  # reescritura completa del enunciado
            cab, _, resto = s.partition("## Enunciado")
            _, sep, despues = resto.partition("\n## ")
            s = cab + "## Enunciado\n\n" + cambios["enunciado"].strip() + "\n" + (f"\n## {despues}" if sep else "")
        for viejo, nuevo in cambios.get("reemplazar", []):
            if viejo not in s:
                print(f"  ! {rel}: no encuentro «{viejo[:50]}»")
            s = s.replace(viejo, nuevo)
        for viejo, nuevo in cambios.get("renombrar", []):
            if nuevo is None:
                (carpeta / viejo).unlink(missing_ok=True)
                s = re.sub(rf"\n*!\[[^\]]*\]\({re.escape(viejo)}\)\n*", "\n\n", s)
                continue
            if not (carpeta / viejo).exists():
                print(f"  ! {rel}: no existe {viejo}")
                continue
            (carpeta / viejo).rename(carpeta / nuevo)
            s = s.replace(f"]({viejo})", f"]({nuevo})")
        for img, alt in cambios.get("alt", []):
            s = re.sub(rf"!\[[^\]]*\]\({re.escape(img)}\)", lambda _: f"![{alt}]({img})", s)
        if "notas" in cambios:
            s = poner_campo(s, "notas", comillas_yaml(cambios["notas"]))
        if "titulo" in cambios:
            s = poner_campo(s, "titulo", comillas_yaml(cambios["titulo"]))
        if cambios.get("borrar_fuente_extra"):
            s = poner_campo(s, "fuentes", lista([re.search(r"^fuentes: \[(F\d+)", s, re.M).group(1)]))
        s = re.sub(r"\n{3,}", "\n\n", s)
        ruta.write_text(s, encoding="utf-8")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    for f in sys.argv[1:]:
        aplicar(yaml.safe_load(Path(f).read_text(encoding="utf-8")))
        print(f"aplicado {f}")


if __name__ == "__main__":
    main()
