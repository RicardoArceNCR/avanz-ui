# 0005 — Siluetas en las portadas

Estado: propuesta para volver a aprobar la etapa 2 — 2026-11-24

## Contexto

Ricardo cambió la portada del inicio: en lugar del ámbar del banner (ADR
0004), fondo blanco con siluetas grises a la izquierda; y las portadas de
capítulo, cada una en su color, con siluetas a la derecha. La forma es la de
Ricardo (dos copias del mismo pétalo, una girada sobre la otra), perfeccionada
por el estudio. Se consultó a tres especialistas (dirección de arte,
desarrollo y accesibilidad).

## Decisión

1. **`silueta/<portada>/color` y `/opacity`** para inicio, logo, color,
   tipografía y sistema: tono sobre tono, sin colores nuevos.

   | Portada | Fondo | Silueta | Opacidad por copia |
   | --- | --- | --- | --- |
   | inicio | `surface/base` | `neutral/950` | 0,05 |
   | logo | `surface/container` | `neutral/950` | 0,045 |
   | color | `brand/main` | negro | 0,04 |
   | tipografía | `neutral/700` | negro | 0,15 |
   | sistema | `surface/inverse` | blanco | 0,06 (una copia) |

2. **El texto pasa AA sobre el cruce.** Donde se pisan dos copias la opacidad
   se compone (1 − (1 − α)²). `scripts/check-siluetas.mjs` mide cada texto de
   cada portada contra ese cruce y corta el build por debajo de 4,5:1. En
   Color, el texto principal `#28292A` es el que limita (4,63:1).
3. **El ámbar queda sin uso en el portal.** `color/marca/ambar`,
   `surface/ambar`, `text/on-ambar` y `portada/*` se conservan para no romper a
   quien los use; quitarlos sería major.

## Consecuencias

- Se agregan tokens: versión 0.5.0; se reabre la etapa 2. El inventario no
  cambia.
