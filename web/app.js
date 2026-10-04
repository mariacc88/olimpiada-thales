/* Explorador del banco de problemas de la Olimpiada Matemática Thales.
   Lee datos/problemas.json (generado por scripts/construir.py), filtra, muestra
   los problemas y compone hojas en PDF en el navegador con typst.ts. */

"use strict";

const POR_PAGINA = 25;
const FASE = { provincial: "Fase provincial", regional: "Fase regional" };
const TYPST_VERSION = "0.7.0";
const TYPST_BUNDLE = `https://cdn.jsdelivr.net/npm/@myriaddreamin/typst.ts@${TYPST_VERSION}/dist/esm/contrib/all-in-one-lite.bundle.js`;
const TYPST_COMPILADOR = `https://cdn.jsdelivr.net/npm/@myriaddreamin/typst-ts-web-compiler@${TYPST_VERSION}/pkg/typst_ts_web_compiler_bg.wasm`;
const TYPST_RENDERIZADOR = `https://cdn.jsdelivr.net/npm/@myriaddreamin/typst-ts-renderer@${TYPST_VERSION}/pkg/typst_ts_renderer_bg.wasm`;

const estado = {
  datos: null,
  filtrados: [],
  mostrados: 0,
  hoja: leerHoja(),
};

const $ = (sel) => document.querySelector(sel);

/* ---------- Almacenamiento local (solo comodidad: la hoja de este navegador) ---------- */

function leerHoja() {
  try {
    const v = JSON.parse(localStorage.getItem("thales-hoja") || "[]");
    return Array.isArray(v) ? v : [];
  } catch {
    return [];
  }
}

function guardarHoja() {
  try {
    localStorage.setItem("thales-hoja", JSON.stringify(estado.hoja));
  } catch {
    /* sin almacenamiento: la hoja dura lo que la pestaña */
  }
}

/* ---------- Markdown con fórmulas ---------- */

function renderizar(md) {
  if (!md) return "";
  const formulas = [];
  const guardar = (tex, display) => {
    formulas.push({ tex, display });
    return `@@F${formulas.length - 1}@@`;
  };
  let texto = md.replace(/\$\$([\s\S]+?)\$\$/g, (_, t) => guardar(t, true));
  texto = texto.replace(/(^|[^\\$])\$([^$\n]+?)\$/g, (_, antes, t) => antes + guardar(t, false));
  let html = window.marked ? marked.parse(texto) : `<p>${texto}</p>`;
  html = html.replace(/@@F(\d+)@@/g, (_, i) => {
    const { tex, display } = formulas[Number(i)];
    try {
      return katex.renderToString(tex, { displayMode: display, throwOnError: false });
    } catch {
      return tex;
    }
  });
  return html;
}

/* ---------- Utilidades ---------- */

function normalizar(s) {
  return (s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function origen(p) {
  const sede = p.sede ? ` (${p.sede})` : "";
  return `${p.edicion_numero} OMT · ${p.año}${sede} · ${FASE[p.fase]} · Problema ${p.numero}`;
}

function marcados(nombre) {
  return [...document.querySelectorAll(`input[name="${nombre}"]:checked`)].map((i) => i.value);
}

/* ---------- Filtros ---------- */

function prepararFiltros() {
  const { taxonomia, problemas } = estado.datos;
  const años = [...new Set(problemas.map((p) => p.año))].sort((a, b) => a - b);
  for (const [id, sel] of [["f-desde", 0], ["f-hasta", años.length - 1]]) {
    const s = $("#" + id);
    s.innerHTML = años.map((a) => `<option>${a}</option>`).join("");
    s.selectedIndex = sel;
  }

  const contar = (fn) => problemas.filter(fn).length;
  $("#f-dificultades").insertAdjacentHTML("beforeend", Object.entries(taxonomia.dificultades).map(([id, nombre]) =>
    `<label><input type="checkbox" name="dificultad" value="${id}"> ${nombre}
       <span class="cuenta">${contar((p) => p.dificultad === id)}</span></label>`).join(""));
  prepararArbolTemas(contar);

  document.querySelectorAll(".filtros input:not(.arbol input), .filtros select, #f-orden")
    .forEach((el) => el.addEventListener(el.type === "search" ? "input" : "change", aplicarFiltros));
  $("#limpiar").addEventListener("click", () => {
    $("#f-texto").value = "";
    $("#f-desde").selectedIndex = 0;
    $("#f-hasta").selectedIndex = $("#f-hasta").options.length - 1;
    document.querySelectorAll('input[name="fase"]').forEach((i) => (i.checked = true));
    document.querySelectorAll('input[name="dificultad"], #f-solucion, .arbol input').forEach((i) => (i.checked = false));
    actualizarArbol();
    aplicarFiltros();
  });
}

/* Árbol de temas: bloques con sus etiquetas (modelo jerárquico: cada etiqueta es de un bloque).
   - Marcar un bloque equivale a marcar todas sus etiquetas, e incluye además los problemas
     del bloque que no tienen etiqueta.
   - Desmarcar alguna etiqueta deja el bloque a medias (indeterminado) y estrecha la búsqueda.
   - Dentro del árbol todo se combina con «o». */
function prepararArbolTemas(contar) {
  const { taxonomia } = estado.datos;
  const html = Object.entries(taxonomia.bloques).map(([b, nombre]) => {
    // Solo se muestran las etiquetas que usa algún problema
    const etiquetas = Object.entries(taxonomia.etiquetas)
      .filter(([id, e]) => e.bloque === b && contar((p) => p.etiquetas.includes(id)))
      .map(([id, e]) => `<li><label><input type="checkbox" class="cb-etiqueta" value="${id}" data-bloque="${b}"> ${e.nombre}</label>
          <span class="cuenta">${contar((p) => p.etiquetas.includes(id))}</span></li>`).join("");
    const desplegar = etiquetas
      ? `<button type="button" class="desplegar" aria-expanded="false" aria-controls="etq-${b}" aria-label="Ver las etiquetas de ${nombre}">▸</button>`
      : '<span class="desplegar-hueco"></span>';
    return `<li class="nodo-bloque">
        <div class="fila">${desplegar}
          <label><input type="checkbox" class="cb-bloque" value="${b}"> ${nombre}</label>
          <span class="cuenta">${contar((p) => p.bloques.includes(b))}</span></div>
        ${etiquetas ? `<ul class="etiquetas" id="etq-${b}" hidden>${etiquetas}</ul>` : ""}
      </li>`;
  }).join("");
  const arbol = $("#f-temas");
  arbol.innerHTML = html;

  arbol.addEventListener("click", (e) => {
    const boton = e.target.closest(".desplegar");
    if (!boton) return;
    const abierto = boton.getAttribute("aria-expanded") === "true";
    boton.setAttribute("aria-expanded", String(!abierto));
    boton.textContent = abierto ? "▸" : "▾";
    $("#" + boton.getAttribute("aria-controls")).hidden = abierto;
  });
  arbol.addEventListener("change", (e) => {
    const cb = e.target;
    if (cb.classList.contains("cb-bloque")) {
      // El bloque arrastra a todas sus etiquetas
      arbol.querySelectorAll(`.cb-etiqueta[data-bloque="${cb.value}"]`).forEach((i) => (i.checked = cb.checked));
    } else if (cb.classList.contains("cb-etiqueta")) {
      const todas = [...arbol.querySelectorAll(`.cb-etiqueta[data-bloque="${cb.dataset.bloque}"]`)];
      arbol.querySelector(`.cb-bloque[value="${cb.dataset.bloque}"]`).checked = todas.every((i) => i.checked);
    }
    actualizarArbol();
    aplicarFiltros();
  });
}

/* Estado indeterminado de los bloques con solo parte de sus etiquetas marcadas */
function actualizarArbol() {
  document.querySelectorAll(".cb-bloque").forEach((cb) => {
    const etiquetas = [...document.querySelectorAll(`.cb-etiqueta[data-bloque="${cb.value}"]`)];
    const marcadas = etiquetas.filter((i) => i.checked).length;
    cb.indeterminate = !cb.checked && marcadas > 0;
  });
}

/* Devuelve una función que dice si un problema cumple el filtro de temas (null si no hay filtro) */
function filtroTemas() {
  const bloquesEnteros = [...document.querySelectorAll(".cb-bloque:checked")].map((i) => i.value);
  const etiquetas = [...document.querySelectorAll(".cb-etiqueta:checked")].map((i) => i.value);
  if (!bloquesEnteros.length && !etiquetas.length) return null;
  return (p) => p.bloques.some((b) => bloquesEnteros.includes(b)) || p.etiquetas.some((e) => etiquetas.includes(e));
}

function aplicarFiltros() {
  const palabras = normalizar($("#f-texto").value).split(/\s+/).filter(Boolean);
  const desde = Number($("#f-desde").value);
  const hasta = Number($("#f-hasta").value);
  const fases = marcados("fase");
  const temas = filtroTemas();
  const dificultades = marcados("dificultad");
  const conSolucion = $("#f-solucion").checked;

  estado.filtrados = estado.datos.problemas.filter((p) => {
    if (p.año < desde || p.año > hasta) return false;
    if (!fases.includes(p.fase)) return false;
    if (temas && !temas(p)) return false;
    if (dificultades.length && !dificultades.includes(p.dificultad)) return false;
    if (conSolucion && !p.tiene_solucion) return false;
    if (palabras.length) {
      p._texto ??= normalizar(`${p.titulo} ${p.enunciado} ${p.solucion}`);
      if (!palabras.every((w) => p._texto.includes(w))) return false;
    }
    return true;
  });
  if ($("#f-orden").value === "desc") estado.filtrados.reverse();

  const n = estado.filtrados.length;
  $("#resumen").textContent = n === 1 ? "1 problema" : `${n} problemas`;
  $("#lista").innerHTML = "";
  estado.mostrados = 0;
  mostrarMas();
}

/* ---------- Tarjetas de problema ---------- */

function tarjeta(p) {
  const { taxonomia } = estado.datos;
  const nodo = $("#plantilla-problema").content.firstElementChild.cloneNode(true);
  nodo.dataset.id = p.id;
  nodo.querySelector(".problema-titulo").textContent = p.titulo;
  nodo.querySelector(".problema-origen").textContent = origen(p);

  const insignias = [
    ...p.bloques.map((b) => `<li class="bloque">${taxonomia.bloques[b]}</li>`),
    `<li class="dif-${p.dificultad}">${taxonomia.dificultades[p.dificultad]}</li>`,
    ...p.etiquetas.map((e) => `<li>${taxonomia.etiquetas[e]?.nombre ?? e}</li>`),
  ];
  if (p.estado === "borrador") insignias.push('<li class="borrador" title="Transcripción y clasificación pendientes de revisión">Borrador</li>');
  nodo.querySelector(".insignias").innerHTML = insignias.join("");

  nodo.querySelector(".problema-enunciado").innerHTML = renderizar(p.enunciado);
  const sol = nodo.querySelector(".problema-solucion");
  if (p.tiene_solucion) {
    sol.addEventListener("toggle", () => {
      const div = sol.querySelector(".texto");
      if (sol.open && !div.innerHTML) div.innerHTML = renderizar(p.solucion);
    });
  } else {
    sol.remove();
    nodo.querySelector(".sin-solucion").hidden = false;
  }

  const boton = nodo.querySelector(".boton-anadir");
  actualizarBoton(boton, p.id);
  boton.addEventListener("click", () => alternarEnHoja(p.id));

  const enlaces = p.fuentes.map((u, i) => `<a href="${u}" target="_blank" rel="noopener">original${p.fuentes.length > 1 ? " " + (i + 1) : ""}</a>`);
  nodo.querySelector(".enlaces-origen").innerHTML = enlaces.length ? "Ver " + enlaces.join(" · ") : "";
  return nodo;
}

function mostrarMas() {
  const lote = estado.filtrados.slice(estado.mostrados, estado.mostrados + POR_PAGINA);
  const frag = document.createDocumentFragment();
  lote.forEach((p) => frag.appendChild(tarjeta(p)));
  $("#lista").appendChild(frag);
  estado.mostrados += lote.length;
  $("#ver-mas").hidden = estado.mostrados >= estado.filtrados.length;
}

function actualizarBoton(boton, id) {
  const dentro = estado.hoja.includes(id);
  boton.textContent = dentro ? "✓ En la hoja" : "Añadir a la hoja";
  boton.setAttribute("aria-pressed", String(dentro));
}

/* ---------- Mi hoja ---------- */

function alternarEnHoja(id) {
  const i = estado.hoja.indexOf(id);
  if (i >= 0) estado.hoja.splice(i, 1);
  else estado.hoja.push(id);
  cambioHoja();
}

function cambioHoja() {
  guardarHoja();
  document.querySelectorAll(".problema").forEach((art) => actualizarBoton(art.querySelector(".boton-anadir"), art.dataset.id));
  $("#contador-hoja").textContent = estado.hoja.length;
  pintarHoja();
}

function pintarHoja() {
  const porId = estado.porId;
  const items = estado.hoja.filter((id) => porId[id]);
  $("#hoja-vacia").hidden = items.length > 0;
  $("#hoja-opciones").hidden = items.length === 0;
  $("#hoja-lista").innerHTML = items.map((id, i) => {
    const p = porId[id];
    return `<li><div class="hoja-item">
      <span>${p.titulo}<small>${p.año} · ${FASE[p.fase]} · P${p.numero}</small></span>
      <button type="button" data-accion="subir" data-i="${i}" aria-label="Subir" ${i === 0 ? "disabled" : ""}>↑</button>
      <button type="button" data-accion="bajar" data-i="${i}" aria-label="Bajar" ${i === items.length - 1 ? "disabled" : ""}>↓</button>
      <button type="button" data-accion="quitar" data-i="${i}" aria-label="Quitar">×</button>
    </div></li>`;
  }).join("");
}

function prepararHoja() {
  const panel = $("#panel-hoja");
  const abrir = (visible) => {
    panel.hidden = !visible;
    $("#abrir-hoja").setAttribute("aria-expanded", String(visible));
  };
  $("#abrir-hoja").addEventListener("click", () => abrir(panel.hidden));
  $("#cerrar-hoja").addEventListener("click", () => abrir(false));
  document.addEventListener("keydown", (e) => e.key === "Escape" && abrir(false));
  $("#hoja-lista").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-accion]");
    if (!b) return;
    const i = Number(b.dataset.i);
    const h = estado.hoja;
    if (b.dataset.accion === "quitar") h.splice(i, 1);
    if (b.dataset.accion === "subir") [h[i - 1], h[i]] = [h[i], h[i - 1]];
    if (b.dataset.accion === "bajar") [h[i + 1], h[i]] = [h[i], h[i + 1]];
    cambioHoja();
  });
  $("#vaciar").addEventListener("click", () => {
    estado.hoja = [];
    cambioHoja();
  });
  $("#generar").addEventListener("click", generarPdf);
  $("#contador-hoja").textContent = estado.hoja.length;
  pintarHoja();
}

/* ---------- PDF con Typst ---------- */

function cadena(s) {
  return '"' + String(s).replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"';
}

/* Debe producir lo mismo que componer() de scripts/hoja.py */
function componerHoja(problemas, titulo, soluciones, conOrigen) {
  const fase = { provincial: "Fase provincial", regional: "Fase regional" };
  const lineas = [
    '#import "/hoja.typ": hoja, problema, solucion, soluciones, sin-solucion',
    `#show: hoja.with(titulo: ${titulo ? cadena(titulo) : "none"})`,
    "",
  ];
  const cuerpoSolucion = (p) => (p.tiene_solucion ? `include "/typst/${p.id}-solucion.typ"` : "sin-solucion");
  problemas.forEach((p, k) => {
    const o = conOrigen ? cadena(`${p.edicion_numero} OMT · ${p.año} · ${fase[p.fase]} · Problema ${p.numero}`) : "none";
    lineas.push(`#problema(n: ${k + 1}, titulo: ${cadena(p.titulo)}, origen: ${o})[#include "/typst/${p.id}-enunciado.typ"]`);
    if (soluciones === "tras") lineas.push(`#solucion()[#${cuerpoSolucion(p)}]`);
  });
  if (soluciones === "final") {
    lineas.push("#soluciones()");
    problemas.forEach((p, k) => lineas.push(`#solucion(n: ${k + 1}, titulo: ${cadena(p.titulo)})[#${cuerpoSolucion(p)}]`));
  }
  return lineas.join("\n") + "\n";
}

let typstListo = null;

function cargarTypst() {
  typstListo ??= new Promise((resolver, rechazar) => {
    const s = document.createElement("script");
    s.type = "module";
    s.src = TYPST_BUNDLE;
    s.onload = () => {
      window.$typst.setCompilerInitOptions({ getModule: () => TYPST_COMPILADOR });
      window.$typst.setRendererInitOptions({ getModule: () => TYPST_RENDERIZADOR });
      resolver(window.$typst);
    };
    s.onerror = () => rechazar(new Error("No se pudo cargar el generador de PDF."));
    document.head.appendChild(s);
  });
  return typstListo;
}

async function bytes(ruta) {
  const r = await fetch(ruta);
  if (!r.ok) throw new Error(`No se encuentra ${ruta}`);
  return new Uint8Array(await r.arrayBuffer());
}

async function generarPdf() {
  const problemas = estado.hoja.map((id) => estado.porId[id]).filter(Boolean);
  if (!problemas.length) return;
  const titulo = $("#h-titulo").value.trim();
  const soluciones = document.querySelector('input[name="soluciones"]:checked').value;
  const conOrigen = $("#h-origen").checked;
  const boton = $("#generar");
  const aviso = (t) => ($("#estado-pdf").textContent = t);

  boton.disabled = true;
  try {
    aviso("Preparando el generador de PDF (la primera vez tarda unos segundos)…");
    const typst = await cargarTypst();
    aviso("Reuniendo los problemas…");
    await typst.resetShadow();
    await typst.mapShadow("/hoja.typ", await bytes("datos/hoja.typ"));
    for (const p of problemas) {
      await typst.mapShadow(`/typst/${p.id}-enunciado.typ`, await bytes(`datos/typst/${p.id}-enunciado.typ`));
      if (p.tiene_solucion && soluciones !== "no") {
        await typst.mapShadow(`/typst/${p.id}-solucion.typ`, await bytes(`datos/typst/${p.id}-solucion.typ`));
      }
      for (const f of p.figuras) await typst.mapShadow(`/${f}`, await bytes(`datos/${f}`));
    }
    aviso("Componiendo el PDF…");
    const pdf = await typst.pdf({ mainContent: componerHoja(problemas, titulo, soluciones, conOrigen) });
    if (!pdf) throw new Error("Typst no ha devuelto ningún PDF.");
    const url = URL.createObjectURL(new Blob([pdf], { type: "application/pdf" }));
    const a = document.createElement("a");
    a.href = url;
    a.download = (normalizar(titulo).replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "hoja-thales") + ".pdf";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 60000);
    aviso(`PDF generado con ${problemas.length} ${problemas.length === 1 ? "problema" : "problemas"}.`);
  } catch (e) {
    console.error(e);
    aviso(`No se ha podido generar el PDF: ${e.message || e}`);
  } finally {
    boton.disabled = false;
  }
}

/* ---------- Arranque ---------- */

async function iniciar() {
  try {
    const r = await fetch("datos/problemas.json");
    estado.datos = await r.json();
  } catch {
    $("#resumen").textContent = "No se han podido cargar los problemas.";
    return;
  }
  estado.porId = Object.fromEntries(estado.datos.problemas.map((p) => [p.id, p]));
  estado.hoja = estado.hoja.filter((id) => estado.porId[id]);
  $("#total").textContent = `${estado.datos.problemas.length} problemas`;
  $("#generado").textContent = estado.datos.generado;
  if (window.matchMedia("(max-width: 820px)").matches) $(".filtros-plegable").open = false;
  prepararFiltros();
  prepararHoja();
  $("#ver-mas").addEventListener("click", mostrarMas);
  aplicarFiltros();
}

document.addEventListener("DOMContentLoaded", iniciar);
