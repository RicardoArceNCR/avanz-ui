# 0006 — Marca del manual del cliente

Estado: propuesta para volver a aprobar las etapas 0, 1 y 2 — 2026-11-24.
Supera a la [0002](0002-segoe-ui-y-estados-de-boton.md) en tipografía;
actualiza la [0001](0001-paquete-propio-de-avanz.md) (error y gris) y la
[0004](0004-ambar-de-portada.md) (ámbar).

## Contexto

El 2026-11-24 llegó material del banco (copiado en
`docs/avanz/cliente-2026-11-24/` del sitio, ignorado por git):

- **Manual Logo Book, p. 04 «Colores Pantones»**
  (`manual-p04-colores-pantones.pdf`, sha256 `ac183696…cc646`): White
  `#FFFFFF`; 2018 C `#FF7500`; 137 C `#FFA300`; 186 C `#C8102E` (su CMYK dice
  M:200, errata probable); Cool Gray 10 C `#63666A`.
- **Logo** (`logo-avanz.svg`): el mismo dibujo que el del sitio del banco, con
  rellenos `#F68628`, `#FAA41A`, `#DA1A32` y `#474C55` (conversión CMYK, no
  los HTML del manual).
- **Fuentes:** Open Sans (TTF v1.10, Apache 2.0) y Kohinoor (Indian Type
  Foundry, comercial, licencia de escritorio, fsType 4).

Ricardo aprobó aplicar la auditoría de marca y, para la tipografía, pidió
textualmente: «utiliza las fuentes que te envié, las licencias lo vemos al
final, no te preocupes».

## Decisión

### Color

1. `color/marca/naranja` `#FF7500` no cambia de valor; su fuente pasa al
   manual (2018 C).
2. `color/marca/ambar` `#FFA401` → `#FFA300` (137 C). Deja de ser «solo del
   banner»: es color oficial de superficie, con texto negro (10,49:1). Nunca
   texto, foco ni botón (blanco 2,00; acción `#B85200` encima 2,47; gris
   secundario 2,88). Esos dos pares quedan registrados como prohibidos
   (mínimo 0) en `contrast-pairs.json`. No es el único diferenciador junto al
   naranja (1,35:1). Sigue sin rampa.
3. `color/marca/gris-oscuro` `#646569` → `#63666A` (Cool Gray 10 C). Ancla
   `neutral/700`; con blanco pasa de 5,82 a 5,77:1. La rampa neutral se
   regenera anclada en él.
4. **Nuevo `color/marca/rojo` `#C8102E` (186 C):** solo logo, ilustración y
   piezas; nunca interfaz. **Sin rampa** (como el ámbar): no tiene consumidor
   de interfaz y unos rosados del 186 competirían con `danger/50–100`.
5. **Error `danger/700` `#BC001C` → `#A40040`.** El error anterior y el 186 C
   eran casi el mismo color (1,13:1, ΔEok 3,2). `#A40040` es carmesí
   (OKLCH L 0,46 C 0,19 H 10): se sigue leyendo como rojo de error y se separa
   del logo por matiz y claridad (ΔEok 8,6; protan/deutan 7,5/8,6) y del rojo
   de servicio `#ED0026` (ΔEok 15,9). Blanco encima 7,92:1; texto 700 sobre
   `danger/50` 7,36 y sobre `/100` 6,46; `feedback/error` 8,91. Regla nueva:
   el error queda a ΔEok ≥ 8 del rojo de marca. Siempre con ícono y texto.
6. Los grises medio y claro y los colores de servicio (petróleo, azul,
   naranja rojizo, `#ED0026`) **no se borran**: el manual recibido no los
   trae; siguen con fuente «capturas», pendientes de confirmar con el banco.

### Tipografía

7. `brand/font-display` = **Kohinoor** (títulos) y `brand/font-body` =
   **Open Sans** (lectura, etiquetas y botones). El sitio las sirve en WOFF2
   desde sus archivos, con respaldo de métricas ajustadas a Arial. Pesos:
   Kohinoor Medium 500, Demi 600 (el archivo declara 450) y Bold 700, más Demi
   Italic; Open Sans 400, 600 y 700.
8. **Licencia web de Kohinoor pendiente.** La de los archivos es de
   escritorio: no se publica el sitio sin la licencia web (queda en la
   recepción del sitio como pendiente, para el final, por decisión de
   Ricardo). Kohinoor no tiene cifras tabulares: las cifras van en Open Sans
   con `tabular-nums`.
9. `button/font-weight` 700 → 600 (Open Sans SemiBold existe; la 0002 lo
   había subido a 700 porque Segoe UI no tenía Semibold).

## Consultas

- **Color y accesibilidad** (subagente, 2026-11-24): eligió `#A40040` entre
  cinco candidatos (H 0–20, L 0,46–0,50) por ser el que más se separa del
  186 C sin dejar de leerse rojo (H ≥ 8; magenta pierde la convención de
  error) y el que mejor distingue el error de la acción naranja con
  daltonismo. Confirmó el 186 C sin rampa y los pares prohibidos del ámbar.
- **Tipografía y Next.js** (subagente, 2026-11-24): `@font-face` manual en
  `globals.css` (el sitio no usa `next/font`); sin `local()` para Kohinoor;
  métricas de respaldo medidas con fontTools; Open Sans desde los WOFF2 de
  fontsource (OFL, con GPOS y `tnum`) en lugar de los TTF v1.10, que traen el
  kerning en la tabla `kern` vieja; sin Light ni itálica de Open Sans (el
  portal no las usa).

## Consecuencias

- Cambian `marca.tokens.json` (etapa 1) y el valor de tokens publicados:
  versión **0.6.0** (minor). Se reabren las etapas 0, 1 y 2 (y la 3 del
  sitio, que sube al tag nuevo).
- El conflicto del logo (inventario) se cierra: el logo vigente es el del
  manual, con los rellenos de su conversión CMYK.
