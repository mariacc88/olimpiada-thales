"""Comprueba la base de datos de problemas antes de construir.

Errores (impiden construir): metadatos que faltan o no válidos, valores fuera de taxonomia.yaml,
identificadores repetidos o que no casan con la carpeta, figuras que no existen, secciones que faltan.
Avisos: lo que conviene revisar pero no rompe nada.

Uso:  python scripts/validar.py
"""

import sys
from collections import Counter

from comun import (ESTADOS, FASES, OBLIGATORIOS, ORIGENES, figuras, leer_ediciones, leer_problemas,
                   leer_taxonomia)


def validar():
    tax = leer_taxonomia()
    ediciones = leer_ediciones()
    errores, avisos = [], []
    ids = Counter()

    for carpeta, meta, sec, fallo in leer_problemas():
        donde = carpeta.relative_to(carpeta.parents[1]).as_posix()
        if fallo:
            errores.append(f"{donde}: {fallo}")
            continue

        def error(msg):
            errores.append(f"{donde}: {msg}")

        faltan = [c for c in OBLIGATORIOS if c not in meta]
        if faltan:
            error(f"faltan campos: {', '.join(faltan)}")
            continue
        ids[meta["id"]] += 1

        ed = meta["edicion"]
        if ed not in ediciones:
            error(f"la edición {ed} no tiene edicion.yaml")
        elif carpeta.parent.name != ed:
            error(f"edicion: {ed} no coincide con la carpeta {carpeta.parent.name}")
        if meta["fase"] not in FASES:
            error(f"fase no válida: {meta['fase']}")
        if carpeta.name != f"{meta['fase']}-{meta['numero']}":
            error(f"la carpeta debería llamarse {meta['fase']}-{meta['numero']}")
        if ed in ediciones and meta["id"] != f"{ediciones[ed]['año']}-{meta['fase']}-{meta['numero']}":
            error(f"id {meta['id']} no sigue el formato año-fase-número")

        for b in meta["bloques"] or []:
            if b not in tax["bloques"]:
                error(f"bloque desconocido: {b}")
        if not meta["bloques"]:
            error("sin bloque temático")
        for e in meta["etiquetas"] or []:
            if e not in tax["etiquetas"]:
                error(f"etiqueta desconocida: {e} (añádela a taxonomia.yaml)")
            elif tax["etiquetas"][e]["bloque"] not in (meta["bloques"] or []):
                # Modelo jerárquico: los bloques de un problema incluyen siempre los de sus etiquetas
                error(f"la etiqueta {e} es del bloque {tax['etiquetas'][e]['bloque']}, que falta en bloques")
        if meta["dificultad"] not in tax["dificultades"]:
            error(f"dificultad no válida: {meta['dificultad']}")
        if meta["origen_clasificacion"] not in ORIGENES:
            error(f"origen_clasificacion no válido: {meta['origen_clasificacion']}")
        if meta["estado"] not in ESTADOS:
            error(f"estado no válido: {meta['estado']}")
        if not isinstance(meta["tiene_solucion"], bool):
            error("tiene_solucion debe ser true o false")

        if not sec.get("enunciado"):
            error("falta la sección «## Enunciado»")
        tiene = bool(sec.get("solución"))
        if meta["tiene_solucion"] is True and not tiene:
            error("tiene_solucion: true pero falta la sección «## Solución»")
        if meta["tiene_solucion"] is False and tiene:
            error("hay sección «## Solución» pero tiene_solucion: false")

        for texto in (sec.get("enunciado"), sec.get("solución")):
            for fig in figuras(texto):
                if not (carpeta / fig).exists():
                    error(f"la figura {fig} no existe")
        usadas = set(figuras(sec.get("enunciado")) + figuras(sec.get("solución")))
        for img in carpeta.glob("*.png"):
            if img.name not in usadas:
                avisos.append(f"{donde}: la imagen {img.name} no se usa")
        if meta["estado"] == "borrador":
            avisos.append(f"{donde}: pendiente de revisión")

    for i, n in ids.items():
        if n > 1:
            errores.append(f"id repetido: {i} ({n} veces)")
    return errores, avisos, sum(ids.values())


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errores, avisos, n = validar()
    borradores = sum("pendiente de revisión" in a for a in avisos)
    otros = [a for a in avisos if "pendiente de revisión" not in a]
    for a in otros:
        print(f"AVISO  {a}")
    for e in errores:
        print(f"ERROR  {e}")
    print(f"{n} problemas · {len(errores)} errores · {len(otros)} avisos · {borradores} pendientes de revisión")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
