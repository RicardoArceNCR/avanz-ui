# Changelog

Formato: [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/). Versiones:
[SemVer](https://semver.org/lang/es/). Un cambio de valor de un token publicado
es minor; renombrar o quitar un token es major.

## [0.2.0] — 2026-11-23

### Cambiado

- Tipografía: `brand/font-display` y `brand/font-body` pasan de Open Sans a
  Segoe UI (decisión de Ricardo; licencia web pendiente, etapa 4).
- `button/font-weight` 600 → 700: Segoe UI no tiene Semibold.
- `button/danger` pasa a contorno (fondo blanco, texto y borde `danger/700`).
  El relleno rojo queda en `button/danger-solid`, para confirmaciones.
- `button/disabled/text` `neutral/400` → `neutral/700`: deshabilitado
  legible (4,83:1).

### Agregado

- `button/primary/shadow-hover`: el hover no depende solo del color.
- `button/danger-solid/*`.
- Pares de contraste del botón destructivo con relleno, su borde y el
  deshabilitado.

## [0.1.0] — 2026-11-23

### Agregado

- Colores oficiales de Avanz (`color/marca/*`), provisionales desde capturas.
- Rampas OKLCH 50–950: `neutral`, `brand`, `petroleo`, `azul`, `rojizo`,
  `rojo`, `danger`, `success` y `warning`, ancladas en los colores oficiales.
- Semánticos, componentes (botón, campo, tarjeta, etiqueta), tipografía en
  Open Sans, espacio, radios, sombras, movimiento y capas.
- `theme-bridge.css` para Tailwind v4 y shadcn. Solo tema claro.
- 61 pares de contraste que bloquean el build, sin excepciones.
