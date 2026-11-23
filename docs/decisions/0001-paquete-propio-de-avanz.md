# 0001 — Paquete propio de Avanz

Estado: propuesta para la aprobación de la etapa 2 — 2026-11-23

## Contexto

Avanz es un cliente nuevo sin manual ni Figma. La recepción (etapa 0) y la
fuente de verdad del color (etapa 1, `docs/inventario-color.json`) quedaron
aprobadas con material provisional: capturas de la paleta en sRGB y Open Sans
tomada del sitio actual del banco. Este paquete no se clonó de otro cliente:
copia archivos del pipeline del estudio (runbooks/cliente-nuevo.md).

## Decisión

1. **Fuente.** `source/dtcg/marca.tokens.json` tiene los 9 colores oficiales
   y solo se cambia reabriendo la etapa 1. Lo demás de `source/dtcg/` lo
   escribe `herramientas/generar-dtcg.py`, que ancla cada rampa en su color
   oficial y corta si no lo reproduce exacto.
2. **Roles decididos por Ricardo (2026-11-23).**
   - `#FF7500` es marca: superficies e ilustración con texto negro (7,80).
     Nunca texto blanco.
   - Acción `#B85200` con texto blanco (4,95); hover `#A74A00`, press
     `#9E4500`. Son los stops 600–800 de `brand`.
   - Texto principal `neutral/950`; secundario `#646569`; borde de campo
     `#878C8E`; `#C6C6C6` solo divisores.
   - Servicios: petróleo `#27727B`, azul `#005E88` (absorbe `#295D7E`),
     naranja rojizo `#FA4616` con texto negro, rojo `#ED0026` solo como fondo
     o ilustración de servicio.
   - Error `#BC001C`, siempre con ícono y texto.
3. **Propuestas del estudio, sin color de marca detrás** (se aprueban con la
   etapa 2):
   - `success` verde (OKLCH h 150) y `warning` amarillo (h 92), lejos del
     naranja de marca (h 48) y del rojo (h 25).
   - `feedback/info` en neutros: azul y petróleo son de servicio.
   - Foco negro: pasa 3:1 sobre el fondo y sobre el botón de acción.
   - `text/tertiary` igual al secundario: con `#878C8E` no llega a 4,5.
4. **Solo tema claro** en v0.1.0. `check-units` y `check-contrast` leen el
   oscuro solo si existe.

## Consecuencias

- `#ED0026` (servicio) y `#BC001C` (error) tienen el mismo matiz (OKLCH h 25):
  sus tintes claros coinciden (`rojo/50` = `danger/50`). Se distinguen por
  claridad, ícono y texto, como pidió Ricardo. Si el banco quiere más
  separación, se mueve el matiz de `danger` acá.
- Si el banco confirma otro logo u otra paleta (el logo del sitio actual no
  usa `#FF7500`), se reabre la etapa 1 y se regenera.
- Cuando haya Figma, se importa `source/dtcg/` (ADR 0008 del estudio) y el
  generador se retira.
