# @avanz/ui

Tokens de diseño de Avanz. `source/dtcg/` es la fuente de verdad; el paquete
publica el CSS que consume el sitio. El sitio no redefine la paleta.

**Estado:** v0.6.0. Los colores principales salen del manual del cliente
(«Manual Logo Book», p. 04: Pantones 2018 C, 137 C, 186 C y Cool Gray 10 C);
los grises medio y claro y los colores de servicio siguen saliendo de capturas
hasta que el banco los confirme. Tipografía del manual: Kohinoor en títulos
(licencia web pendiente; no se publica sin ella) y Open Sans en lectura
(ADR 0006).

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
| `source/dtcg/marca.tokens.json` | Los colores oficiales (etapa 1) | Solo reabriendo la etapa 1 |
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
