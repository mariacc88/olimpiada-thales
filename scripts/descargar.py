"""Fase 0: descarga de fuentes e inventario.

Recorre la web actual (olimpiada.saemthales.es) y la antigua (thales.cica.es/olimpiada2),
descarga todo el material de cada edición de la Olimpiada Thales de 2º ESO en fuentes/raw/
y genera:

  fuentes/ediciones.csv   una fila por edición (año, sede, páginas de origen)
  fuentes/inventario.csv  una fila por material de origen (páginas, ficheros, enlaces externos)
  fuentes/informe.md      resumen por edición y lista de huecos

Es idempotente: lo ya descargado no se vuelve a pedir (salvo con --refrescar), y los
identificadores del inventario se conservan entre ejecuciones.

Uso:  python scripts/descargar.py [--refrescar]
"""

import csv
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "fuentes"
RAW = FUENTES / "raw"

NUEVA = "https://olimpiada.saemthales.es"
ANTIGUA = "https://thales.cica.es/olimpiada2"

PROFUNDIDAD_MAX = 2  # niveles de nodos de la web antigua a seguir desde la página de edición
PAUSA = 0.25         # segundos entre peticiones, por cortesía con el servidor
REFRESCAR = "--refrescar" in sys.argv

EXT_FICHEROS = {"pdf", "pps", "ppsx", "ppt", "pptx", "doc", "docx", "odt", "odp", "zip", "ggb", "htm", "html"}
EXT_IMAGENES = {"gif", "jpg", "jpeg", "png"}

# Términos de taxonomía de la web antigua -> identificadores de taxonomia.yaml
TERMINOS_BLOQUE = {36: "geometria", 38: "numeros", 39: "funciones", 40: "logica", 41: "estadistica"}
TERMINOS_DIFICULTAD = {42: "facil", 43: "medio", 44: "dificil"}

# Lo que se ha comprobado a mano al revisar el informe; se copia tal cual en informe.md
OBSERVACIONES = {
    "1985-I": "en la web, «¿Equivalencia geométrica?» figura como Regional 3; por el orden es el Regional 4.",
    "Figuras perdidas": "los ficheros que dan 404 se recuperan, si existe copia, del Internet Archive "
                        "(lo indica la columna notas del inventario). Los que siguen en «Errores de descarga» "
                        "no tienen copia: habrá que valorar en la Fase 1 si el problema se entiende sin ellos.",
    "2011-XXVII": "los problemas están en una única presentación de SlideShare (65 diapositivas, empieza por "
                  "«Los carros del supermercado»). Fase y número se asignan en la Fase 1.",
    "2014-XXX, 2015-XXXI, 2022-XXXVII": "un único material por fase (presentación o PDF de soluciones) con todos los problemas.",
    "2021-XXXVI": "edición online: 5 problemas por fase (no faltan).",
    "2024-XXXIX": "de la fase regional solo hay una crónica; no se han publicado los enunciados.",
    "2026-XLI": "solo hay bases y sedes; los problemas aún no se han publicado.",
}

CAMPOS_INVENTARIO = [
    "id", "edicion", "fase", "numero", "titulo", "tipo", "contenido", "estado",
    "url", "ruta_local", "origen", "bloques_thales", "dificultad_thales", "bytes", "notas",
]


# --- Utilidades -------------------------------------------------------------

ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50}


def romano_a_int(r):
    total = 0
    for a, b in zip(r, r[1:] + " "):
        v = ROMANOS[a]
        total += -v if b in ROMANOS and ROMANOS[b] > v else v
    return total


def año_de_edicion(n):
    # I = 1985, una por año; en 2020 no se celebró (XXXVI = 2021)
    return 1984 + n if n <= 35 else 1985 + n


def normalizar_url(href, base):
    url = urllib.parse.urljoin(base, html.unescape(href.strip()))
    url = re.sub(r"^(https?://[^/]+)\./", r"\1/", url)  # «thales.cica.es./…»
    url = url.replace("olimpiada2//", "olimpiada2/")
    url = re.sub(r"^http://(thales\.cica\.es|olimpiada\.saemthales\.es)", r"https://\1", url)
    url = url.replace("https://olimpiada.saemthales.es//", "https://olimpiada.saemthales.es/node/")
    return url.split("#")[0]


def url_pedible(url):
    p = urllib.parse.urlsplit(url)
    ruta = urllib.parse.quote(urllib.parse.unquote(p.path), safe="/~")
    consulta = urllib.parse.quote(urllib.parse.unquote(p.query), safe="=&/?")
    return urllib.parse.urlunsplit((p.scheme, p.netloc, ruta, consulta, ""))


def pedir(url):
    """Devuelve (bytes, None) o (None, error)."""
    time.sleep(PAUSA)
    req = urllib.request.Request(url_pedible(url), headers={"User-Agent": "Mozilla/5.0 (banco-problemas-thales)"})
    for intento in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read(), None
        except urllib.error.HTTPError as e:
            return None, f"HTTP {e.code}"
        except Exception as e:  # red: reintentar
            err = str(e)[:80]
            time.sleep(2 * (intento + 1))
    return None, err


def descargar(url, ruta):
    """Descarga a ruta si no existe. Devuelve (ok, error)."""
    if ruta.exists() and not REFRESCAR:
        return True, None
    datos, err = pedir(url)
    if datos is None:
        return False, err
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(datos)
    return True, None


def copia_archivada(url):
    """URL de la copia más cercana en el Internet Archive (contenido original, sin la barra de Wayback)."""
    sin_esquema = re.sub(r"^https?://", "", url)
    datos, _ = pedir("https://archive.org/wayback/available?url=" + urllib.parse.quote(sin_esquema, safe="/:"))
    if not datos:
        return None
    m = re.search(r'"timestamp":\s*"(\d+)"', decodificar(datos))
    if not m or '"available": true' not in decodificar(datos):
        return None
    return f"https://web.archive.org/web/{m.group(1)}id_/http://{sin_esquema}"


def decodificar(b):
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252", errors="replace")


def texto(fragmento):
    t = re.sub(r"<[^>]+>", " ", fragmento)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def nombre_seguro(nombre):
    nombre = urllib.parse.unquote(nombre)
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", nombre).strip(" .") or "fichero"


def extension(url):
    ruta = urllib.parse.unquote(urllib.parse.urlsplit(url).path)
    return ruta.rsplit(".", 1)[-1].lower() if "." in ruta.rsplit("/", 1)[-1] else ""


def id_nodo_antiguo(url):
    m = re.match(r"https://thales\.cica\.es/olimpiada2/?\?q=node/(\d+)$", url)
    return int(m.group(1)) if m else None


# --- Extracción de contenido de páginas ---------------------------------------

def segmento_nueva(s):
    m = re.search(r"<article.*?</article>", s, re.S)
    return m.group(0) if m else ""


def segmento_antigua(s):
    i = s.find('class="node')
    if i < 0:
        return ""
    i = s.rfind("<", 0, i)  # desde el principio de la etiqueta
    fines = [k for k in (s.find("mero de visitas", i), s.find('id="footer"', i), s.find("region-sidebar", i)) if k > 0]
    return s[i:min(fines)] if fines else s[i:]


def titulo_pagina(s):
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    return texto(m.group(1)).split(" | ")[0] if m else ""


RE_ENLACE = re.compile(
    r'<a\s[^>]*href="([^"]*)"[^>]*>(.*?)</a>'
    r'|<img\s[^>]*?src="([^"]*)"[^>]*>'
    r'|<iframe\s[^>]*?src="([^"]*)"[^>]*>'                                   # presentaciones incrustadas
    r'|<param\s[^>]*?value="([^"]*slidesharecdn[^"]*ssplayer[^"]*)"[^>]*>',  # visor flash antiguo de SlideShare
    re.S | re.I)


def url_slideshare_flash(valor):
    """El visor flash antiguo lleva el usuario y el título en la consulta: se convierte a la URL de la página."""
    q = urllib.parse.parse_qs(urllib.parse.urlsplit(html.unescape(valor)).query)
    if "userName" in q and "stripped_title" in q:
        return f"https://www.slideshare.net/{q['userName'][0]}/{q['stripped_title'][0]}"
    return ""


def enlaces_con_contexto(seg, fase=""):
    """Recorre el segmento en orden y devuelve (href, texto_enlace, fase_contexto, es_img)."""
    pos = 0
    for m in RE_ENLACE.finditer(seg):
        previo = texto(seg[pos:m.start()])
        if "provincial" in previo.lower():
            fase = "provincial"
        if "regional" in previo.lower():
            fase = "regional"
        pos = m.end()
        if m.group(3):
            yield m.group(3), "", fase, True
        elif m.group(4) or m.group(5):
            # Sin texto de enlace: el título del problema suele ir justo antes de lo incrustado
            href = m.group(4) or url_slideshare_flash(m.group(5))
            yield href, previo[-80:], fase, False
        else:
            t = texto(m.group(2))
            f = "provincial" if "provincial" in t.lower() else "regional" if "regional" in t.lower() else fase
            yield m.group(1), t, f, False


RE_NUM_TEXTO = re.compile(r"(?:problema|cuesti[oó]n|n\.?\s*[ºo°]|\bp)\s*\.?\s*(\d{1,2})\b\s*[:.\-–]?\s*(.*)", re.I)


def deducir_problema(texto_enlace, url, fase_ctx):
    """Intenta deducir (fase, numero, titulo) de un enlace a fichero."""
    fase, numero, titulo = fase_ctx, "", ""
    m = RE_NUM_TEXTO.search(texto_enlace) or re.search(r"(?:^|\s)(\d{1,2})\s*[.)\-–]\s+(\D.*)$", texto_enlace)
    if m:
        numero, titulo = m.group(1), m.group(2).strip(" .-–()").replace("( PowerPoint)", "").strip()
    nombre = urllib.parse.unquote(url.rsplit("/", 1)[-1]).lower()
    letra_num = None
    if m := re.match(r"\d+([pr])(\d+)\b", nombre) or re.search(r"_([pr])(\d+)[._]", nombre):
        letra_num = m.groups()                    # 32p1.pps, XXXVI_P1_….pdf
    elif m := re.match(r"\d{2}(\d)([pr])", nombre):
        letra_num = m.group(2), m.group(1)        # 251r.pps, 191pr.zip: edición + número + fase
    if letra_num:
        fase = fase or ("provincial" if letra_num[0] == "p" else "regional")
        numero = numero or letra_num[1]
    if "prov" in nombre and not fase:
        fase = "provincial"
    if "regional" in nombre and not fase:
        fase = "regional"
    return fase, numero, titulo or texto_enlace


def deducir_contenido(texto_enlace, url):
    t = (texto_enlace + " " + urllib.parse.unquote(url)).lower()
    if re.search(r"bases|premio|paco ?anillo|cartel|clasificad|inscrip|consentim|sedes|diploma|acta", t):
        return "otro"
    if re.search(r"soluci|resoluci|resuelt", t):
        return "solucion"
    return "?"


# --- Inventario ---------------------------------------------------------------

class Inventario:
    def __init__(self, ruta):
        self.ruta = ruta
        self.filas = {}      # clave (url) -> fila
        self.ids_previos = {}
        if ruta.exists():
            with open(ruta, encoding="utf-8", newline="") as f:
                for fila in csv.DictReader(f):
                    self.ids_previos[fila["url"]] = fila["id"]
        self.siguiente = 1 + max((int(i[1:]) for i in self.ids_previos.values()), default=0)

    def añadir(self, url, **campos):
        if url in self.filas:
            return self.filas[url]
        id_ = self.ids_previos.get(url)
        if not id_:
            id_ = f"F{self.siguiente:04d}"
            self.siguiente += 1
        fila = {c: "" for c in CAMPOS_INVENTARIO}
        fila.update(campos, id=id_, url=url)
        self.filas[url] = fila
        return fila

    def guardar(self):
        filas = sorted(self.filas.values(), key=lambda f: f["id"])
        with open(self.ruta, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS_INVENTARIO)
            w.writeheader()
            w.writerows(filas)


# --- Descubrimiento de ediciones ---------------------------------------------

def descubrir_ediciones():
    """Devuelve lista de dicts con id, numero, año, sede, urls de las páginas de edición."""
    ediciones = {}
    ruta = RAW / "web-actual" / "portada-0.html"
    descargar(NUEVA + "/", ruta)
    portada = decodificar(ruta.read_bytes())

    # 1) Barra lateral «Ediciones anteriores»
    for href, txt in re.findall(r'<a href="(https://olimpiada\.saemthales\.es/[^"]+)">([^<]*OMT[^<]*)</a>', portada):
        txt = html.unescape(txt).replace("\xa0", " ")
        m = re.match(r"\s*([IVXL]+)\s+OMT\s*\(([^,]+),\s*(\d+)\)", txt)
        if not m:
            continue
        num = romano_a_int(m.group(1))
        url = normalizar_url(href, NUEVA)
        ediciones[num] = {"romano": m.group(1), "n": num, "año": año_de_edicion(num),
                          "sede": m.group(2).strip(), "paginas": [url]}

    # 2) Noticias de la portada: ediciones recientes que aún no están en la barra lateral
    pagina = 0
    while True:
        ruta = RAW / "web-actual" / f"portada-{pagina}.html"
        ok, _ = descargar(f"{NUEVA}/?page={pagina}", ruta)
        if not ok:
            break
        s = decodificar(ruta.read_bytes())
        noticias = re.findall(r'href="(/node/\d+)" rel="bookmark"[^>]*>\s*(?:<span[^>]*>)?([^<]+)', s)
        if not noticias:
            break
        for href, titulo in noticias:
            t = html.unescape(titulo).strip()
            if re.search(r"alev[ií]n|juvenil|primaria|nacional", t, re.I):
                continue
            m = re.search(r"\b([IVXL]+)\s+OLIMPIADA MATEM[ÁA]TICA THALES", t, re.I)
            if not m:
                continue
            num = romano_a_int(m.group(1).upper())
            url = normalizar_url(href, NUEVA)
            if num in ediciones and ediciones[num]["sede"]:
                continue  # ya está en la barra lateral: basta con esa página
            e = ediciones.setdefault(num, {"romano": m.group(1).upper(), "n": num, "año": año_de_edicion(num),
                                           "sede": "", "paginas": []})
            if url not in e["paginas"]:
                e["paginas"].append(url)
        if f"?page={pagina + 1}" not in s:
            break
        pagina += 1

    # 3) Cada nodo de la web actual tiene su gemelo en la antigua (mismo número de nodo)
    for e in ediciones.values():
        e["id"] = f"{e['año']}-{e['romano']}"
        for url in list(e["paginas"]):
            m = re.search(r"/node/(\d+)$", url)
            if m:
                e["paginas"].append(f"{ANTIGUA}/?q=node/{m.group(1)}")
    return [ediciones[k] for k in sorted(ediciones)]


# --- Rastreo -----------------------------------------------------------------

class Rastreador:
    def __init__(self, inv):
        self.inv = inv
        self.visitados = set()
        self.presentaciones = {}  # clave de la presentación en SlideShare -> fila del inventario

    def ruta_pagina(self, url):
        m = re.search(r"/node/(\d+)$", url)
        if m and url.startswith(NUEVA):
            return RAW / "web-actual" / f"node-{m.group(1)}.html"
        n = id_nodo_antiguo(url)
        if n:
            return RAW / "web-antigua" / f"node-{n}.html"
        return None

    def pagina(self, url, ed, profundidad, origen=""):
        if url in self.visitados:
            return
        self.visitados.add(url)
        ruta = self.ruta_pagina(url)
        es_antigua = url.startswith(ANTIGUA)
        ok, err = descargar(url, ruta)
        fila = self.inv.añadir(url, edicion=ed["id"], tipo="pagina-edicion" if profundidad == 0 else "nodo",
                               origen=origen, ruta_local=ruta.relative_to(RAIZ).as_posix())
        if not ok:
            fila.update(estado="error", notas=err)
            return
        s = decodificar(ruta.read_bytes())
        seg = segmento_antigua(s) if es_antigua else segmento_nueva(s)
        titulo = titulo_pagina(s)
        fila.update(estado="descargado", titulo=titulo, bytes=str(ruta.stat().st_size))
        if not texto(seg):
            fila.update(contenido="vacia")
            return

        # ¿Es un nodo de problema de la web antigua? («I OMT: Provincial 1: Marinerías.»)
        es_problema = False
        m = re.match(r"([IVXL]+)\s+OMT\s*:\s*(Provincial|Regional)\s*(\d+)\s*:?\s*(.*?)\.?$", titulo, re.I)
        if es_antigua and m:
            es_problema = True
            terminos = [int(t) for t in re.findall(r"taxonomy/term/(\d+)", seg)]
            fila.update(fase=m.group(2).lower(), numero=m.group(3), titulo=m.group(4), contenido="enunciado",
                        tipo="nodo-problema",
                        bloques_thales=" ".join(TERMINOS_BLOQUE[t] for t in terminos if t in TERMINOS_BLOQUE),
                        dificultad_thales=" ".join(TERMINOS_DIFICULTAD[t] for t in terminos if t in TERMINOS_DIFICULTAD))
        if "node-acidfree" in seg[:200]:
            fila.update(contenido="otro", notas="álbum de fotos")
            return

        fase_pagina = "regional" if "regional" in titulo.lower() else "provincial" if "provincial" in titulo.lower() else ""
        for href, txt, fase_ctx, es_img in enlaces_con_contexto(seg, fase_pagina):
            if not href or href.startswith(("mailto:", "javascript:")):
                continue
            u = normalizar_url(href, url)
            if not u.startswith("http"):
                continue  # p. ej. rutas file:// que se colaron al editar la web
            ext = extension(u)
            if "taxonomy/term" in u:
                continue
            if es_img or ext in EXT_IMAGENES:
                if es_problema:  # las figuras de los problemas antiguos
                    self.fichero(u, ed, fila, "", fila["fase"], fila["numero"], "figura", "imagen")
                continue
            if id_nodo_antiguo(u):
                if profundidad < PROFUNDIDAD_MAX:
                    self.pagina(u, ed, profundidad + 1, fila["id"])
                continue
            if ext in EXT_FICHEROS and ("thales.cica.es" in u or "saemthales.es" in u):
                fase, num, tit = deducir_problema(txt, u, fase_ctx)
                if es_problema:
                    fase, num = fila["fase"], fila["numero"]
                self.fichero(u, ed, fila, tit, fase, num, deducir_contenido(txt, u), ext)
            elif re.search(r"slideshare\.net/(?!thecroaker)", u):
                if re.match(r"https?://(www\.)?slideshare\.net/[^/]*/?$", u):
                    continue  # portada o perfil de usuario
                fase, num, tit = deducir_problema(txt, u, fase_ctx)
                self.slideshare(u, ed, fila, tit, fase, num)
            elif re.search(r"geogebra\.org/(student|m|material)", u):
                fase, num, tit = deducir_problema(txt, u, fase_ctx)
                self.inv.añadir(u, edicion=ed["id"], fase=fase, numero=num, titulo=tit or txt, tipo="externo",
                                contenido="?", estado="externo", origen=fila["id"])

    def fichero(self, url, ed, origen, titulo, fase, numero, contenido, tipo):
        if url in self.inv.filas:
            return
        nombre = nombre_seguro(urllib.parse.urlsplit(url).path.rsplit("/", 1)[-1])
        ruta = RAW / "ficheros" / ed["id"] / nombre
        fila = self.inv.añadir(url, edicion=ed["id"], fase=fase, numero=numero, titulo=titulo, tipo=tipo,
                               contenido=contenido, origen=origen["id"], ruta_local=ruta.relative_to(RAIZ).as_posix())
        ok, err = descargar(url, ruta)
        notas = ""
        if not ok and err == "HTTP 404":
            copia = copia_archivada(url)
            if copia:
                ok, err = descargar(copia, ruta)
                notas = f"recuperado de archive.org: {copia}"
        if not ok:
            fila.update(estado="error", notas=err, ruta_local="")
            return
        fila.update(estado="descargado", bytes=str(ruta.stat().st_size), notas=notas)
        if tipo == "zip":
            self.descomprimir(fila, ruta, ed)

    def slideshare(self, url, ed, origen, titulo, fase, numero):
        """Descarga las diapositivas de una presentación de SlideShare como JPG de 2048 px."""
        url = re.sub(r"^http://", "https://", url)
        if url in self.inv.filas:
            return
        slug = re.sub(r"[^\w-]+", "-", url.split("slideshare.net/", 1)[1]).strip("-")
        pagina = RAW / "slideshare" / f"{slug}.html"
        fila = self.inv.añadir(url, edicion=ed["id"], fase=fase, numero=numero, titulo=titulo, tipo="slideshare",
                               contenido="?", origen=origen["id"])
        ok, err = descargar(url, pagina)
        if not ok:
            fila.update(estado="error", notas=err)
            return
        s = decodificar(pagina.read_bytes())
        m = re.search(r"(https://image\.slidesharecdn\.com/([^\"'\s\\/]+))/\d+/([^\"'\s\\/]+?)-1-\d+\.jpg", s)
        if not m:
            fila.update(estado="error", notas="no se encuentran las diapositivas")
            return
        base, clave, nombre = m.groups()
        # La misma presentación puede aparecer enlazada e incrustada, con URLs distintas
        if clave in self.presentaciones:
            previa = self.presentaciones[clave]
            for campo in ("fase", "numero", "titulo"):
                previa[campo] = previa[campo] or fila[campo]
            del self.inv.filas[url]
            return
        self.presentaciones[clave] = fila
        carpeta = RAW / "ficheros" / ed["id"] / f"slideshare-{clave}"
        fila["ruta_local"] = carpeta.relative_to(RAIZ).as_posix()
        total = re.search(r'"totalSlides":(\d+)', s)
        n = int(total.group(1)) if total else len(set(re.findall(re.escape(nombre) + r"-(\d+)-\d+\.jpg", s)))
        fallos = 0
        for i in range(1, n + 1):
            ok, _ = descargar(f"{base}/75/{nombre}-{i}-2048.jpg", carpeta / f"{i:03d}.jpg")
            fallos += not ok
        tam = sum(p.stat().st_size for p in carpeta.glob("*.jpg"))
        fila.update(estado="descargado" if not fallos else "error", bytes=str(tam),
                    notas=f"{n} diapositivas" + (f", {fallos} sin descargar" if fallos else ""))

    def descomprimir(self, fila_zip, ruta, ed):
        destino = ruta.with_suffix("")
        try:
            with zipfile.ZipFile(ruta) as z:
                for info in z.infolist():
                    if info.is_dir():
                        continue
                    nombre = info.filename
                    if not info.flag_bits & 0x800:  # nombres en cp437 sin marca UTF-8
                        nombre = nombre.encode("cp437").decode("cp850", errors="replace")
                    destino_f = destino / nombre_seguro(Path(nombre).name)
                    if not destino_f.exists() or REFRESCAR:
                        destino_f.parent.mkdir(parents=True, exist_ok=True)
                        destino_f.write_bytes(z.read(info))
                    self.inv.añadir(f"{fila_zip['url']}#{nombre}", edicion=ed["id"], fase=fila_zip["fase"],
                                    numero=fila_zip["numero"], titulo=fila_zip["titulo"],
                                    tipo=extension(nombre) or "?", contenido=fila_zip["contenido"],
                                    estado="descomprimido", origen=fila_zip["id"],
                                    ruta_local=destino_f.relative_to(RAIZ).as_posix(), bytes=str(info.file_size))
        except zipfile.BadZipFile:
            fila_zip.update(estado="error", notas="zip corrupto")


# --- Informe -----------------------------------------------------------------

def escribir_ediciones(ediciones):
    with open(FUENTES / "ediciones.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "numero", "año", "sede", "paginas"])
        for e in ediciones:
            w.writerow([e["id"], e["romano"], e["año"], e["sede"], " ".join(e["paginas"])])


def escribir_informe(ediciones, inv):
    por_ed = defaultdict(list)
    for f in inv.filas.values():
        por_ed[f["edicion"]].append(f)

    tipos_problema = {"nodo-problema", "pdf", "pps", "ppsx", "ppt", "pptx", "doc", "docx", "ggb", "htm", "html",
                      "externo", "slideshare"}
    lineas = [
        "# Informe de la Fase 0: descarga e inventario",
        "",
        "Generado por `scripts/descargar.py`. Resume lo descargado en `fuentes/raw/` y registrado en `inventario.csv`.",
        "",
        "Leyenda de la columna «Problemas localizados»: `P` = fase provincial, `R` = regional, número = problema. "
        "Un número aparece si hay al menos un material (página, fichero o enlace) asociado a ese problema. "
        "La asociación es automática y aproximada: se verifica en la Fase 1.",
        "",
        "| Edición | Sede | Materiales | Tipos | Problemas localizados | Avisos |",
        "|---|---|---|---|---|---|",
    ]
    for e in ediciones:
        filas = por_ed.get(e["id"], [])
        tipos = Counter(f["tipo"] for f in filas if f["tipo"] not in ("pagina-edicion", "nodo", "imagen"))
        prob = defaultdict(set)
        completas = set()  # materiales que cubren una fase entera (una presentación o un PDF por fase)
        for f in filas:
            if f["fase"] and f["tipo"] in tipos_problema and f["contenido"] != "otro":
                if f["numero"]:
                    prob[f["fase"]].add(int(f["numero"]))
                elif f["tipo"] != "externo":
                    completas.add(f["fase"])
        loc = "; ".join(f"{fase[0].upper()} " + (",".join(map(str, sorted(prob[fase]))) if prob[fase] else "")
                        + (" (+ material de fase completa)" if fase in completas else "")
                        for fase in sorted(set(prob) | completas)) or "—"
        avisos = []
        n_err = sum(f["estado"] == "error" for f in filas)
        n_ext = sum(f["estado"] == "externo" for f in filas)
        if n_err:
            avisos.append(f"{n_err} errores")
        if n_ext:
            avisos.append(f"{n_ext} enlaces externos")
        if not prob and not completas:
            avisos.append("**sin problemas localizados**")
        if any(f["tipo"] == "pagina-edicion" and f["contenido"] == "vacia" for f in filas):
            avisos.append("alguna página de edición vacía")
        tipos_txt = ", ".join(f"{t} {n}" for t, n in sorted(tipos.items()))
        lineas.append(f"| {e['id']} | {e['sede']} | {len(filas)} | {tipos_txt} | {loc} | {'; '.join(avisos)} |")

    lineas += ["", "## Observaciones (revisión manual)", ""]
    lineas += [f"- **{ed}**: {obs}" for ed, obs in OBSERVACIONES.items()]

    errores = [f for f in inv.filas.values() if f["estado"] == "error"]
    externos = [f for f in inv.filas.values() if f["estado"] == "externo"]
    lineas += ["", f"## Errores de descarga ({len(errores)})", ""]
    lineas += [f"- `{f['id']}` {f['edicion']}: {f['notas']} — {f['url']}" for f in errores] or ["Ninguno."]
    lineas += ["", f"## Enlaces externos no descargados ({len(externos)})", ""]
    lineas += [f"- `{f['id']}` {f['edicion']} {f['fase']} {f['numero']} «{f['titulo']}» — {f['url']}" for f in externos] or ["Ninguno."]

    total = len(inv.filas)
    tam = sum(int(f["bytes"] or 0) for f in inv.filas.values() if f["estado"] == "descargado")
    lineas += ["", "## Totales", "", f"- Registros en el inventario: {total}",
               f"- Tamaño descargado: {tam / 1e6:.0f} MB",
               f"- Por tipo: " + ", ".join(f"{t} {n}" for t, n in Counter(f['tipo'] for f in inv.filas.values()).most_common())]
    (FUENTES / "informe.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")


# --- Programa principal --------------------------------------------------------

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    RAW.mkdir(parents=True, exist_ok=True)
    inv = Inventario(FUENTES / "inventario.csv")
    ediciones = descubrir_ediciones()
    print(f"{len(ediciones)} ediciones encontradas")
    rast = Rastreador(inv)
    for e in ediciones:
        antes = len(inv.filas)
        for url in e["paginas"]:
            rast.pagina(url, e, 0)
        print(f"  {e['id']:<16} {len(inv.filas) - antes:4d} materiales", flush=True)
        inv.guardar()  # guardado parcial, por si se interrumpe
    escribir_ediciones(ediciones)
    inv.guardar()
    escribir_informe(ediciones, inv)
    print("Listo: fuentes/inventario.csv, fuentes/ediciones.csv, fuentes/informe.md")


if __name__ == "__main__":
    main()
