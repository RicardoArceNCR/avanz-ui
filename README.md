# @avanz/ui

Tokens de diseño de Avanz. `source/dtcg/` es la fuente de verdad; el paquete
publica el CSS que consume el sitio. El sitio no redefine la paleta.

**Estado:** v0.1.0, provisional. Sin manual ni Figma: los colores oficiales
salen de capturas de la paleta convertidas a sRGB; la tipografía es Segoe UI,
con licencia web pendiente. Se confirman con el manual o el banco antes de publicar
(etapa 4 del proceso del estudio).

## Uso

```sh
pnpm add "git+https://github.com/RicardoArceNCR/avanz-ui.git#v0.1.0"
```

```css
@import "@avanz/ui/tokens.css";
@import "@avanz/ui/theme-bridge.css"; /* Tailwind v4 + API shadcn */
```

Solo tema claro en v0.1.0.

## Cómo cambia

| Archivo | Qué es | Quién lo toca |
| --- | --- | --- |
| `source/dtcg/marca.tokens.json` | Los 9 colores oficiales (etapa 1) | Solo reabriendo la etapa 1 |
| `herramientas/generar-dtcg.py` | Rampas, roles y componentes, anclados en `marca` | Etapa 2 |
| `source/dtcg/*.tokens.json` | Salida del generador, versionada | Nadie a mano |
| `scripts/contrast-pairs.json` | Pares que bloquean el build | Etapa 2 |

```sh
npm run dtcg      # regenera source/dtcg (menos marca)
npm run verify    # dtcg → Style Dictionary → unidades, rampas y contraste
npm run sistema   # sistema/sistema.html: paleta, roles, tipografía y contraste
```

`build/` y `source/*.json` se versionan: el CI falla si no corresponden a
`source/dtcg`.

Decisiones: [docs/decisions](docs/decisions/). Inventario de color:
[docs/inventario-color.json](docs/inventario-color.json).
