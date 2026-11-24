# 0003 — Sombras de dos capas y radios más redondos

Estado: propuesta para volver a aprobar la etapa 2 — 2026-11-23

## Contexto

Ricardo pidió llevar al portal un lenguaje con bordes más redondos y
sombras, a partir de una auditoría de estilos de un referente. Se consultó a
tres especialistas (dirección de arte, sistema de diseño y accesibilidad).
Coincidieron en tomar la estructura del referente (sombras en capas, escala de
radios, estados) y dejar los valores de Avanz: botón `brand/600`, borde de
campo `neutral/500`, foco negro.

## Decisión

1. **Sombras en dos capas** (contacto + ambiente), luz cenital, teñidas con
   `neutral/950` (`rgb(40 41 42)`) en lugar de negro puro. Tres niveles:
   `shadow/sm` tarjeta, `shadow/md` flotante (menú, aviso), `shadow/lg`
   destacado. `card/shadow` usa el valor de `shadow/sm`.
2. **Radios:** `button/radius` e `input/radius` pasan de `radius/md` (8) a
   `radius/lg` (12); `card/radius` de `radius/lg` (12) a `radius/xl` (16).
   La escala primitiva no cambia.
3. **Sombra en reposo de los botones:** `button/primary/shadow` y
   `button/secondary/shadow`; `button/primary/shadow-hover` se vuelve a
   teñir y crece para que el hover se note además del color.
4. **Sin cambios de color:** foco negro (`focus/ring-color`), borde de campo
   y secundario `neutral/500` (3,40:1) y el resto de la paleta quedan como
   están. Los 66 pares de contraste siguen en verde.

## Consecuencias

- Cambian valores publicados: versión 0.3.0 (minor) y se reabre la etapa 2.
  El inventario de color no cambia: la etapa 1 sigue aprobada.
- `@estudio/marca` necesita ganchos de sombra (0.6.0) para que el portal las
  use; sin ellos solo cambian los radios.
- Se reabre la etapa 3 del sitio: cambian páginas firmadas.
