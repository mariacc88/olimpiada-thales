# Banco de problemas de la Olimpiada Matemática Thales (2º ESO)

Plan de trabajo para construir una base de datos de todos los problemas de la Olimpiada Matemática Thales (2º de ESO), clasificados por tema y dificultad, con un explorador web público y generación de hojas en PDF.

---

## 1. Objetivo y alcance

- **Qué:** todos los problemas de las fases **provincial** y **regional** de la Olimpiada Matemática Thales para 2º de ESO, desde la I (Sevilla, 1985) hasta la última publicada.
- **Por cada problema:** edición, año, sede, fase, número, título, enunciado (con figuras y fórmulas), solución si existe, clasificación temática y dificultad.
- **Uso:** explorar y filtrar los problemas, y generar un PDF con los problemas elegidos, con o sin soluciones.
- **Publicación:** repositorio en GitHub y web estática en GitHub Pages.
- **Fuera de alcance por ahora:** la Olimpiada Alevín (primaria), la Juvenil, la sección «OM fuera de Andalucía» y los materiales publicados. La estructura permite añadirlos después con un campo `olimpiada`.

---

## 2. Fuentes

Hay dos webs:

| Web | Papel |
|---|---|
| `olimpiada.saemthales.es` (web actual) | Barra lateral «Ediciones anteriores» con una página por edición, y noticias en la portada (ediciones de 2024 en adelante). |
| `thales.cica.es/olimpiada2` (web antigua, aún activa) | Aloja casi todo el contenido real: páginas HTML de cada problema (1985–2002) y los ficheros (PDF, PPS, ZIP, DOC). |

La web antigua tiene una **taxonomía propia** en cada problema antiguo:
- Bloques temáticos (`?q=taxonomy/term/N`): Números/medidas (38), Geometría (36), Funciones/gráficas (39), Lógica (40), Estadística/Azar (41).
- Dificultad: Fácil (42), Medio (43), Difícil (44).

| Ediciones | Formato principal | Solución |
|---|---|---|
| I–XVIII (1985–2002) | Página HTML por problema en la web antigua, con figura GIF y etiquetas | Generalmente no |
| XIX–XXIII (2003–2007) | `.zip` que contienen `.pps` | Sí, dentro del PPS |
| XXIV–XXVI (2008–2010) | Mezcla de HTML, `.doc` y PDF | Variable |
| XXVII–XXVIII (2011–2012) | Página vacía en la web actual; hay que buscar en la antigua (términos 50 y 54) | Por determinar |
| XXIX–XXXV (2013–2019) | `.pps` / `.ppsx` por problema; algún `.ggb` | Sí |
| XXXVI–XXXVIII (2021–2023) | PDF por problema | Normalmente sí |
| XXXIX–XLI (2024–2026) | Noticias de la portada (no están en la barra lateral) | Por determinar |

**Incidencias conocidas:**
- En 2020 no hubo olimpiada (se suspendió por la pandemia).
- En el menú lateral, el enlace a la XXXI apunta a `//1642` y está roto; la página real es `/node/1642`.
- En 2023 los ficheros provinciales están mal nombrados: `OMT_XXVIII_*` en lugar de XXXVIII.
- Al convertir los PPS a PDF salen diapositivas repetidas por las animaciones, se pierden algunos símbolos especiales y aparecen restos de navegación («Comentario», «Menú»).

**Volumen estimado:** unos 40 ediciones × 2 fases × 4–8 problemas ≈ **450–550 problemas**.

---

## 3. Inventario y base de datos: la diferencia

Son dos cosas distintas, en dos momentos del proceso:

| | **Inventario** (Fase 0) | **Base de datos** (Fase 3) |
|---|---|---|
| Qué describe | Los **materiales de origen**: qué hay en la web, dónde está y qué fichero lo contiene | Los **problemas** ya limpios y clasificados: el producto final |
| Unidad | Un fichero o página de origen, que puede contener varios problemas (un ZIP o un PDF con soluciones de toda una fase) o ninguno (bases, carteles) | Un problema |
| Contenido | URL, ruta local, tipo de fichero, edición/fase/número deducidos, estado del procesamiento | Enunciado, solución, figuras, metadatos, clasificación |
| Cómo se crea | Automáticamente, con el script de descarga | Extracción más revisión y edición humanas |
| Para qué sirve | Saber qué falta, rastrear de dónde sale cada problema, poder rehacer la extracción | Explorar, filtrar e imprimir |

El inventario es la «lista de trabajo» y la trazabilidad. La base de datos es el contenido. Cada problema guarda en `fuentes` los identificadores del inventario de los que procede.

---

## 4. Estructura del proyecto

```
Thales/
├── PLAN.md                     ← este documento
├── README.md                   ← presentación pública del repositorio
├── LICENSE / AVISO.md          ← licencia del código y atribución del contenido a SAEM Thales
├── taxonomia.yaml              ← bloques, dificultades y etiquetas finas permitidas
│
├── fuentes/
│   ├── inventario.csv          ← (en git) un registro por material de origen
│   └── raw/                    ← (NO en git) copia local de todo lo descargado
│       ├── web-actual/         ← HTML de las páginas de edición
│       ├── web-antigua/        ← HTML de los nodos de problemas y de la taxonomía
│       └── ficheros/           ← PDF, PPS, PPSX, ZIP, DOC, GGB tal como se descargan
│
├── problemas/                  ← (en git) LA BASE DE DATOS: fuente de verdad
│   ├── 1985-I/
│   │   ├── edicion.yaml        ← datos de la edición
│   │   ├── provincial-1/
│   │   │   ├── problema.md     ← metadatos + enunciado + solución
│   │   │   └── fig1.png
│   │   └── regional-1/ …
│   ├── 2016-XXXII/ …
│   └── …
│
├── requirements.txt            ← dependencias de Python (pyyaml, pillow, pymupdf)
├── scripts/
│   ├── descargar.py            ← Fase 0: rastrea las dos webs y rellena inventario y raw/
│   ├── extraer/
│   │   ├── preparar.py         ← Fase 1: reúne texto, páginas e imágenes de cada problema en trabajo/
│   │   └── recortar.py         ← Fase 1: recorta una figura de una fuente a 300 ppp
│   ├── clasificar.py           ← Fase 2 (pendiente): exporta/importa la tabla de revisión
│   ├── comun.py                ← lectura de problemas y taxonomía, compartida por los demás
│   ├── validar.py              ← comprueba metadatos, figuras referenciadas, etiquetas válidas
│   ├── construir.py            ← Fase 3: genera el índice JSON y los fragmentos Typst
│   └── hoja.py                 ← genera en local un PDF con los problemas elegidos
│
├── plantillas/
│   └── hoja.typ                ← plantilla Typst de la hoja de problemas (A4)
│
├── web/                        ← Fase 4: explorador estático
│   ├── index.html
│   ├── app.js
│   └── estilo.css
│
├── trabajo/                    ← (NO en git) intermedios: PDF convertidos, páginas renderizadas, borradores
│
└── .github/workflows/
    └── publicar.yml            ← valida, construye y despliega en GitHub Pages
```

### 4.1. Identificadores

- Edición: `AAAA-ROMANO`, por ejemplo `2016-XXXII`.
- Problema: `AAAA-fase-N`, por ejemplo `2016-regional-3`. Es estable y legible, y sirve para la URL, los ficheros y las referencias cruzadas.

### 4.2. `edicion.yaml`

```yaml
id: 2016-XXXII
numero: XXXII
año: 2016
sede_regional: Sevilla
fecha_provincial: 2016-03-12
fecha_regional: 2016-05-18
url_origen: https://olimpiada.saemthales.es/node/1640
notas: ""
```

### 4.3. `problema.md`

```markdown
---
id: 2016-provincial-1
edicion: 2016-XXXII
fase: provincial            # provincial | regional
numero: 1
titulo: El robot
bloques: [logica]           # identificadores de taxonomia.yaml (uno o varios)
bloques_thales: []          # el bloque que le asignó la web antigua, si lo tiene (informativo)
etiquetas: [deduccion]      # taxonomía fina, identificadores de taxonomia.yaml
dificultad: medio           # facil | medio | dificil
origen_clasificacion: propuesta   # propuesta | revisada
tiene_solucion: true
fuentes: [F0123]            # ids del inventario
estado: borrador            # borrador | revisado
notas: ""
---

## Enunciado

Texto en Markdown, con fórmulas en LaTeX ($a^2+b^2=c^2$) y figuras:

![Plano de las habitaciones](fig1.png)

## Solución

…
```

Convenciones fijadas en el piloto:

- **Figuras:** `fig1.png`, `fig2.png`… para el enunciado y `fig-solucion.png`, `fig-solucion1.png`… para la solución. El texto alternativo describe la figura; la web lo usa para accesibilidad y el PDF lo oculta.
- **Ilustraciones decorativas** (fotos, dibujos que no aportan datos) se incluyen como `ilustracion.png`, tras el primer párrafo del enunciado. Se imprimen pequeñas (4,5 cm como máximo en su lado mayor) y en la web se muestran a 220 px. No se incluyen las imágenes de plantilla que se repiten en todas las diapositivas o en los membretes (logotipos, retrato de Thales, fondos), ni las de las portadas de las presentaciones.
- **Tablas y cuadrículas** se transcriben como tablas Markdown, no como imagen. Si no tienen cabecera, se deja la primera fila vacía (`| | | |`) y la web y el PDF la ocultan.
- **Listas con números no consecutivos** (definiciones de crucigramas, etc.) se escriben como viñetas con el número en negrita, porque Markdown renumera las listas.
- **Soluciones:** se transcriben fieles al original pero condensadas: cuando el original desarrolla un recuento paso a paso en muchas diapositivas, se recoge el razonamiento y el resultado, y se indica en `notas`. Las erratas evidentes del original se corrigen y se anota.
- **Clasificación:** `bloques_thales` conserva lo que dijo la web antigua; `bloques`, `etiquetas` y `dificultad` son la propuesta que se revisa.

### 4.4. `taxonomia.yaml`

Cada valor tiene un **identificador** (el que se escribe en `problema.md`) y un **nombre visible** (el que muestra la web). Las etiquetas finas se agrupan bajo su bloque para ordenar los filtros, pero su identificador es único en todo el fichero.

```yaml
bloques:                      # los cinco de la web antigua de Thales
  geometria:
    nombre: Geometría
    etiquetas:
      areas: Áreas y perímetros
      pitagoras: Teorema de Pitágoras
  logica:
    nombre: Lógica
    etiquetas:
      deduccion: Deducción a partir de pistas
  # … numeros, funciones, estadistica
dificultades:
  facil: Fácil
  medio: Medio
  dificil: Difícil
```

Las etiquetas actuales son de muestra; las instrucciones para editarlas están al principio del propio fichero. `validar.py` rechaza cualquier bloque, etiqueta o dificultad que no figure aquí. Así la clasificación se mantiene consistente.

---

## 5. Fases

### Fase 0. Descarga e inventario
- `descargar.py` recorre:
  - Las páginas de edición de la barra lateral y las noticias de la portada (2024 en adelante).
  - El nodo gemelo de cada página en la web antigua (mismo número de nodo), que a menudo tiene más contenido.
  - Los nodos enlazados de la web antigua, hasta dos niveles.
- De cada nodo de problema antiguo recoge fase, número, título, figuras, y el bloque y la dificultad que le asignó Thales.
- Descarga los ficheros enlazados (PDF, PPS, PPSX, PPT, DOC, ZIP, GGB…) y descomprime los ZIP.
- Las presentaciones de SlideShare (2011–2013), enlazadas o incrustadas, se descargan diapositiva a diapositiva como JPG de 2048 px.
- Genera tres ficheros:
  - `fuentes/ediciones.csv`: una fila por edición.
  - `fuentes/inventario.csv`: una fila por material, con las columnas `id, edicion, fase, numero, titulo, tipo, contenido, estado, url, ruta_local, origen, bloques_thales, dificultad_thales, bytes, notas`.
  - `fuentes/informe.md`: cobertura por edición, observaciones, errores y enlaces externos.
- Es idempotente: no descarga de nuevo lo que ya existe y conserva los identificadores `F0001…` entre ejecuciones. Con `--refrescar` lo vuelve a pedir todo.
- **Entregable:** `inventario.csv` completo y un informe de huecos (ediciones o problemas sin material localizado).

### Fase 1. Extracción
- `preparar.py <edición>…` reúne en `trabajo/<edición>/<fase>-<n>/` todo el material de cada problema:
  - un `borrador.md` con los metadatos propuestos y el texto extraído de cada fuente;
  - `paginas/`: las páginas renderizadas;
  - `imagenes/`: las imágenes incrustadas y las figuras de la web antigua.
  - Según el formato:
    - **HTML antiguo:** el cuerpo del nodo se pasa a Markdown con pandoc, con sus figuras y el bloque de Thales.
    - **PDF:** texto por página con PyMuPDF, páginas renderizadas e imágenes incrustadas.
    - **PPS/PPSX/PPT/DOC:** se convierten a PDF con LibreOffice y se omiten las diapositivas que solo añaden elementos a la siguiente (animaciones).
    - **GeoGebra (`.ggb`):** se extraen sus textos (enunciado y solución) y sus imágenes.
    - **SlideShare:** las diapositivas descargadas como imagen.
- Después Claude redacta `problemas/<edición>/<fase>-<n>/problema.md`:
  - Lee el texto extraído y las páginas como imagen.
  - Separa enunciado y solución, pasa las fórmulas a LaTeX y reconstruye los símbolos perdidos.
  - Recorta las figuras con `recortar.py`. La opción `--sin-fondo` quita el fondo de las diapositivas.
- Todo queda con `estado: borrador`.

### Fase 2. Clasificación
- La web antigua solo asignó bloque a parte de los problemas anteriores a 2010 y casi nunca dificultad. Ese dato se guarda en `bloques_thales` y sirve de referencia.
- Claude propone bloque, etiquetas y dificultad para todos (`origen_clasificacion: propuesta`).
- `clasificar.py` exporta una tabla CSV con id, título, enunciado abreviado y la clasificación propuesta. Se revisa a mano (por ejemplo en una hoja de cálculo) y se reimporta (`origen_clasificacion: revisada`).
- Cuando esté definida la taxonomía fina, se añade a `taxonomia.yaml` y se repite el ciclo de propuesta y revisión con las etiquetas.

### Fase 3. Base de datos y construcción
- La fuente de verdad son los ficheros de `problemas/`: se leen, se editan a mano y se versionan con git.
- `construir.py` genera, sin guardarlos en git:
  - `web/datos/problemas.json`: índice con metadatos, enunciado y solución en Markdown y rutas de las figuras.
  - `web/datos/fig/<id>/…`: las figuras.
  - `web/datos/typst/<id>-enunciado.typ` y `<id>-solucion.typ`: cada parte convertida a Typst con pandoc. A cada figura se le da su tamaño natural en papel (300 ppp para los recortes, 96 ppp para las imágenes pequeñas de la web antigua; como máximo 15 cm).
- `validar.py` se ejecuta antes de construir: comprueba metadatos obligatorios, figuras que existen, etiquetas válidas e identificadores únicos.

### Fase 4. Explorador web (GitHub Pages)
- Una página estática, sin servidor, en HTML y JavaScript, con KaTeX para las fórmulas.
- **Filtros:** año o rango de años, fase, bloque, etiqueta, dificultad, «con solución» y búsqueda de texto.
- **Vista de cada problema:** enunciado con figuras y solución desplegable; enlace a la fuente original.
- **Cesta de selección:** se marcan problemas y se genera un PDF con opciones:
  - Con o sin soluciones.
  - Soluciones al final o tras cada problema.
  - Mostrar o no la edición y la fase.
  - Título de la hoja.
- **Generación del PDF:** se hace en el propio navegador con **typst.ts 0.7** (Typst compilado a WebAssembly) usando `plantillas/hoja.typ`. No hace falta servidor y la maquetación es de calidad tipo LaTeX.
  - La primera vez descarga el compilador y las fuentes desde jsDelivr (unos segundos).
  - Comprobado en el piloto: el PDF del navegador sale igual que el de Typst en local.
  - **Alternativa local:** `hoja.py 2016-regional-3 1999-provincial-2 … --soluciones final` genera el mismo PDF con Typst instalado.
  - `componer()` de `hoja.py` y `componerHoja()` de `web/app.js` deben producir el mismo documento: si se cambia una, hay que cambiar la otra.
- **Despliegue:** `publicar.yml` valida, construye y publica en GitHub Pages en cada push a `main`. Fija la versión de pandoc (3.10, la misma que en local), porque la salida Typst cambia entre versiones.

### Fase 5. Revisión
Lista de comprobación por problema, que cambia `estado` a `revisado`:
- [ ] Enunciado completo y fiel al original.
- [ ] Figuras presentes, legibles y bien recortadas.
- [ ] Fórmulas correctas.
- [ ] Solución completa, o `tiene_solucion: false`.
- [ ] Metadatos y clasificación correctos.

El explorador puede ocultar los borradores o marcarlos como tales.

---

## 6. Flujo de trabajo y comandos

Requisitos en local: Python 3.12+, pandoc 3.10, LibreOffice (solo para la Fase 1) y Typst (solo para `hoja.py`).

```sh
python -m venv .venv && .venv/Scripts/pip install -r requirements.txt   # una vez

python scripts/descargar.py                                    # Fase 0 (idempotente)
.venv/Scripts/python scripts/extraer/preparar.py 2016-XXXII    # Fase 1: material de trabajo
.venv/Scripts/python scripts/extraer/recortar.py F0855 2 0.07 0.19 0.25 0.35 problemas/…/fig1.png --sin-fondo
.venv/Scripts/python scripts/validar.py                        # comprobar la base de datos
.venv/Scripts/python scripts/construir.py                      # generar web/datos/
python -m http.server 8765 --directory web                     # ver la web en http://localhost:8765
.venv/Scripts/python scripts/hoja.py 2016-regional-3 2023-provincial-1 --soluciones final -o hoja.pdf
```

---

## 7. Orden de ejecución

1. **Andamiaje:** estructura de carpetas, `taxonomia.yaml`, repositorio git y `.gitignore`.
2. **Fase 0 completa:** inventario de todo y lista de huecos.
3. **Piloto con tres ediciones de formatos distintos:**
   - 1985-I (HTML antiguo, con clasificación).
   - 2016-XXXII (PPS y un GGB).
   - 2023-XXXVIII (PDF con soluciones).

   Se les aplican las fases 1, 2, 3 y 4 de principio a fin, con el explorador y la generación de PDF funcionando. **Aquí se valida el formato de `problema.md` y la plantilla de la hoja antes de escalar.**
4. **Escalado por lotes,** de más fácil a más difícil:
   1. HTML antiguo (1985–2002).
   2. PDF (2021–2026).
   3. PPS sueltos (2013–2019).
   4. ZIP/PPS y DOC (2003–2010).
   5. Huecos de 2011–2012.
5. **Clasificación fina,** cuando esté definida la taxonomía.
6. **Publicación:** repositorio público y GitHub Pages.

---

## 8. Riesgos y decisiones pendientes

- **Derechos del contenido.** Los problemas son de SAEM Thales. La web antigua indica una licencia Creative Commons, aunque los enlaces muestran tanto BY 3.0 ES como BY-NC-SA 2.5 ES; la web nueva no indica licencia. **Decisión:** se publica con una atribución explícita en el pie de la web y en el README (autoría de Thales, licencia, uso sin fines comerciales, enlace a cada original y aviso de que el proyecto no está vinculado a Thales). Se respeta la lectura más restrictiva (BY-NC-SA). Cuando el banco esté más completo y pulido, se escribirá a la Sociedad Thales.
- **Copia local de las fuentes.** Los ficheros originales (cientos de MB) no se suben al repositorio. Si se quiere conservarlos, mejor guardarlos aparte (disco o almacenamiento externo), ya que la web antigua podría desaparecer.
- **Figuras.** Son la parte más costosa y la más propensa a errores. El recorte se hace de forma semiautomática y requiere revisión.
- **Dificultad.** El criterio de Thales es relativo a la prueba (fácil/medio/difícil dentro de la olimpiada). Las propuestas para problemas nuevos intentarán imitarlo, pero son subjetivas.
- **Problemas interactivos (GeoGebra).** Se guarda el enlace o fichero `.ggb` y una figura estática; no se reproducen de forma interactiva.
