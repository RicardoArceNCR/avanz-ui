# 0002 — Segoe UI y estados de botón

Estado: propuesta para volver a aprobar las etapas 1 y 2 — 2026-11-23

> Superada en tipografía por la [0006](0006-marca-del-manual-del-cliente.md): Kohinoor y Open Sans del manual; `button/font-weight` vuelve a 600. Los estados de botón siguen vigentes.

## Contexto

Con el portal armado, Ricardo decidió usar Segoe UI (Regular, Italic y Bold,
archivos entregados por él) en lugar de Open Sans, y licenciarla antes de
publicar. Además preguntó si el botón principal debía ser el naranja de marca
`#FF7500`. Se consultó a dos especialistas (dirección de arte y
accesibilidad).

## Decisión

1. **Tipografía:** `brand/font-*` = Segoe UI. No hay Semibold: el botón pasa
   a 700. La licencia web se exige en la etapa 4 y su kit reemplaza los
   archivos que sirve el sitio.
2. **Botón principal:** sigue en `#B85200` (`brand/600`) con texto blanco.
   Los dos especialistas coinciden: `#FF7500` con texto negro no llega a 3:1
   contra el blanco (1.4.11), da APCA Lc 52,6 con texto de 16 px y se confunde
   con el naranja rojizo de servicio `#FA4616`. `#FF7500` queda para marca,
   nunca en controles.
3. **Hover con sombra** (`button/primary/shadow-hover`): de reposo a hover
   el color cambia 1,17:1, poco para notarse solo.
4. **Destructivo con contorno** (`button/danger`); relleno solo en la
   confirmación (`button/danger-solid`). El error `#BC001C` y el primario son
   cálidos y oscuros: rellenos uno junto al otro se confunden.
5. **Deshabilitado legible:** texto `neutral/700` sobre `neutral/100`
   (4,83:1).

## Consecuencias

- Cambian `source/dtcg` y el inventario: se reabren las etapas 1 y 2 y la
  versión pasa a 0.2.0 (minor: cambian valores y se agregan tokens).
- El sitio sube a `#v0.2.0` después del tag.
