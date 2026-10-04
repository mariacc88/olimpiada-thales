# Olimpiada Matemática Thales: banco de problemas

Base de datos de los problemas de la Olimpiada Matemática Thales (2.º de ESO, Andalucía), clasificados por tema y dificultad, con un explorador web y generación de hojas en PDF.

> 🚧 En construcción. El plan de trabajo está en [PLAN.md](PLAN.md).

Los problemas, sus soluciones y sus ilustraciones son obra de la [Sociedad Andaluza de Educación Matemática Thales](https://thales.cica.es) y proceden de [olimpiada.saemthales.es](https://olimpiada.saemthales.es/), que los publica bajo licencia Creative Commons (enlaza a CC BY-NC-SA 2.5 ES y a CC BY 3.0 ES). Aquí se reproducen con atribución, sin fines comerciales y con enlace a cada original. Este proyecto no está vinculado a la SAEM Thales.

## Trabajar en local

Requisitos: Python 3.12 o posterior y [pandoc](https://pandoc.org) 3.10. Para generar PDF desde la terminal hace falta además [Typst](https://typst.app); para extraer problemas nuevos (Fase 1), LibreOffice.

Preparar el entorno (solo la primera vez):

```sh
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt     # en Linux/macOS: .venv/bin/pip
```

### Ver la web

```sh
.venv/Scripts/python scripts/construir.py         # genera web/datos/ a partir de problemas/
python -m http.server 8765 --directory web        # sirve la web
```

Abre <http://localhost:8765> en el navegador; `Ctrl+C` en la terminal para pararla.

- `construir.py` solo hace falta repetirlo cuando cambia algo en `problemas/` o en `taxonomia.yaml`. Si solo se toca `web/` (HTML, CSS, JS), basta con recargar la página.
- La web tiene que servirse así: abriendo `web/index.html` con doble clic no puede cargar los datos.
- `construir.py` valida antes los problemas y se detiene si hay errores. Se pueden comprobar por separado con `.venv/Scripts/python scripts/validar.py`.

### Generar una hoja en PDF desde la terminal

```sh
.venv/Scripts/python scripts/hoja.py 2016-regional-3 2023-provincial-1 --soluciones final -o hoja.pdf
.venv/Scripts/python scripts/hoja.py --bloque geometria --dificultad facil -o geometria.pdf
```

`--soluciones` admite `no` (por defecto), `final` o `tras` (después de cada problema). La web hace lo mismo desde el botón «Mi hoja».

### Añadir o editar problemas

Cada problema es un fichero `problemas/<edición>/<fase>-<número>/problema.md` con sus figuras al lado. El formato y las convenciones están en [PLAN.md](PLAN.md) (sección 4.3); los valores permitidos de bloques, etiquetas y dificultad, en [taxonomia.yaml](taxonomia.yaml).

Los comandos de descarga de fuentes y extracción están en [PLAN.md](PLAN.md) (sección 6).

## Publicación

Cada push a `main` valida, construye y publica la web en GitHub Pages ([.github/workflows/publicar.yml](.github/workflows/publicar.yml)).
