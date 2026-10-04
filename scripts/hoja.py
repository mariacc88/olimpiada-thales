"""Genera en local una hoja de problemas en PDF con Typst.

Necesita los datos construidos (python scripts/construir.py) y Typst instalado.

Ejemplos:
  python scripts/hoja.py 2016-regional-3 1985-provincial-5 -o hoja.pdf
  python scripts/hoja.py 2023-provincial-1 2023-provincial-2 --soluciones final --titulo "Repaso"
  python scripts/hoja.py --bloque geometria --dificultad facil -o geometria.pdf

Opciones de soluciones: no (por defecto), final (al final de la hoja), tras (después de cada problema).
La misma composición la hace el explorador web en el navegador (web/app.js, función componerHoja).
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

from comun import RAIZ

DATOS = RAIZ / "web" / "datos"
FASE = {"provincial": "Fase provincial", "regional": "Fase regional"}


def cadena(s):
    """Literal de cadena de Typst."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def origen(p):
    return f"{p['edicion_numero']} OMT · {p['año']} · {FASE[p['fase']]} · Problema {p['numero']}"


def componer(problemas, titulo=None, soluciones="no", con_origen=True):
    """Devuelve el código Typst de la hoja. Debe producir lo mismo que componerHoja() de web/app.js."""
    lineas = ['#import "/hoja.typ": hoja, problema, solucion, soluciones, sin-solucion',
              f"#show: hoja.with(titulo: {cadena(titulo) if titulo else 'none'})", ""]

    def cuerpo_solucion(p):
        return f'include "/typst/{p["id"]}-solucion.typ"' if p["tiene_solucion"] else "sin-solucion"

    for n, p in enumerate(problemas, 1):
        o = cadena(origen(p)) if con_origen else "none"
        lineas.append(f'#problema(n: {n}, titulo: {cadena(p["titulo"])}, origen: {o})'
                      f'[#include "/typst/{p["id"]}-enunciado.typ"]')
        if soluciones == "tras":
            lineas.append(f"#solucion()[#{cuerpo_solucion(p)}]")
    if soluciones == "final":
        lineas.append("#soluciones()")
        for n, p in enumerate(problemas, 1):
            lineas.append(f"#solucion(n: {n}, titulo: {cadena(p['titulo'])})[#{cuerpo_solucion(p)}]")
    return "\n".join(lineas) + "\n"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("ids", nargs="*", help="identificadores de problema (p. ej. 2016-regional-3)")
    a.add_argument("--bloque", help="todos los problemas de un bloque")
    a.add_argument("--dificultad", help="filtra por dificultad")
    a.add_argument("--edicion", help="filtra por edición (p. ej. 2016-XXXII)")
    a.add_argument("--soluciones", choices=["no", "final", "tras"], default="no")
    a.add_argument("--titulo", default="Problemas de la Olimpiada Matemática Thales")
    a.add_argument("--sin-origen", action="store_true", help="no indicar edición y fase de cada problema")
    a.add_argument("-o", "--salida", default="hoja.pdf")
    args = a.parse_args()

    if not (DATOS / "problemas.json").exists():
        sys.exit("Faltan los datos: ejecuta antes python scripts/construir.py")
    todos = json.loads((DATOS / "problemas.json").read_text(encoding="utf-8"))["problemas"]
    por_id = {p["id"]: p for p in todos}
    if args.ids:
        desconocidos = [i for i in args.ids if i not in por_id]
        if desconocidos:
            sys.exit(f"No existen: {', '.join(desconocidos)}")
        elegidos = [por_id[i] for i in args.ids]
    else:
        elegidos = [p for p in todos
                    if (not args.bloque or args.bloque in p["bloques"])
                    and (not args.dificultad or p["dificultad"] == args.dificultad)
                    and (not args.edicion or p["edicion"] == args.edicion)]
    if not elegidos:
        sys.exit("No hay problemas que cumplan esos criterios.")

    principal = DATOS / "_hoja.typ"
    principal.write_text(componer(elegidos, args.titulo, args.soluciones, not args.sin_origen), encoding="utf-8")
    salida = Path(args.salida).resolve()
    r = subprocess.run(["typst", "compile", "--root", str(DATOS), str(principal), str(salida)],
                       capture_output=True, text=True, encoding="utf-8")
    principal.unlink()
    if r.returncode:
        sys.exit(r.stderr)
    print(f"{salida} ({len(elegidos)} problemas)")


if __name__ == "__main__":
    main()
