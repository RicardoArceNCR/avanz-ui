# 0004 — Ámbar de la portada

Estado: propuesta para volver a aprobar las etapas 1 y 2 — 2026-11-23

## Contexto

El banner del sitio del banco (`docs/avanz/banner-bg-desktop.jpg` del sitio)
es un fondo ámbar `#FFA401` con capas del naranja de marca `#FF7500` al 34 %:
donde se cruzan dos capas da `#FF9400` y tres, `#FF8901`. Ricardo decidió
llevarlo a la portada del portal, animado con Three.js (ruta B, «Ensamble en
capas»). El ámbar no estaba en la paleta de las capturas.

## Decisión

1. **`color/marca/ambar` = `#FFA401`**, provisional, medido en el banner (la
   zona lisa es un solo valor). Entra al inventario con fuente «banner».
2. **Sin rampa:** es un fondo, no un color de interfaz. El generador lo
   exceptúa de la regla «todo color de marca está en una rampa».
3. **Semánticos:** `surface/ambar` y `text/on-ambar` (negro, 10,56:1). El par
   bloquea el build.
4. **Componente `portada`:** `bg` (ámbar), `capa` (`brand/500`),
   `capa-opacity` 0,34, `text` negro y `logo-bg` blanco. El logo no va sobre
   el ámbar: sus letras `#646569` dan 2,93:1.
5. **Nunca en controles:** `#B85200` sobre ámbar da 2,49:1. Sobre la portada,
   botón y brillo van en negro.

## Consecuencias

- Cambia `marca.tokens.json` (etapa 1) y se agregan tokens: versión 0.4.0;
  se reabren las etapas 1 y 2.
- `check-units` acepta `--*-opacity` como ratio.
- El banner pasa a la recepción del sitio como `fondos`, provisional.
