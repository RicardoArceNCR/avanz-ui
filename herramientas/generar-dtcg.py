#!/usr/bin/env python3
"""
generar-dtcg.py — escribe las colecciones DTCG de Avanz en source/dtcg/.

Avanz no tiene Figma: source/dtcg/ se escribe con este script (ADR 0008 del
estudio: un DTCG escrito por otra herramienta también sirve). Forma: la del
export nativo de Figma de divergentes-ui ($type en cada token; color como
objeto con colorSpace, components, alpha y hex; números sin unidad).

NO toca source/dtcg/marca.tokens.json: son los colores oficiales aprobados en
la etapa 1. Este script los lee y ancla las rampas en ellos; si una rampa no
reproduce exacto su color oficial, corta.

  python3 herramientas/generar-dtcg.py && npm run verify

Las decisiones de rol son de Ricardo (2026-11-23, docs/arranque.md del sitio)
y están en docs/decisions/0001-paquete-propio-de-avanz.md.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'herramientas'))
from color import gamut_map  # noqa: E402
from ramps import ramp, STOPS  # noqa: E402

OUT = os.path.join(ROOT, 'source', 'dtcg')
MARCA = json.load(open(os.path.join(OUT, 'marca.tokens.json'), encoding='utf-8'))['color']['marca']
M = {k: v['$value']['hex'].upper() for k, v in MARCA.items()}


# ─── Rampas ─────────────────────────────────────────────────────────────────
# Anclas: color oficial (de marca.tokens.json) o decisión de Ricardo. El stop
# de cada ancla es el más cercano en claridad OKLCH (tabla LT de ramps.py).
ANCLAS = {
    'neutral': {300: M['gris-claro'], 500: M['gris-medio'], 700: M['gris-oscuro']},
    # Acción #B85200, hover #A74A00 y press #9E4500: decisión de Ricardo,
    # mismo matiz que #FF7500 (OKLCH h 48), más oscuros.
    'brand': {500: M['naranja'], 600: '#B85200', 700: '#A74A00', 800: '#9E4500'},
    'petroleo': {700: M['servicio-petroleo']},
    'azul': {800: M['servicio-azul']},
    'rojizo': {500: M['servicio-naranja-rojizo']},
    'rojo': {600: M['servicio-rojo']},
    # Error #BC001C: decisión de Ricardo, aparte del rojo de servicio.
    'danger': {700: '#BC001C'},
    # Propuesta del estudio, no colores de marca: éxito verde y aviso
    # amarillo, lejos del naranja de marca (h 48) y del rojo (h 25).
    'success': {600: gamut_map(0.56, 0.13, 150)},
    'warning': {300: gamut_map(0.86, 0.15, 92)},
}
RAMPAS = {fam: ramp(a) for fam, a in ANCLAS.items()}
for fam, anclas in ANCLAS.items():
    for stop, hx in anclas.items():
        assert RAMPAS[fam][stop] == hx.upper(), f'{fam}/{stop} no reproduce {hx}'
for nombre, hx in M.items():
    if nombre == 'servicio-azul-retirado':
        continue  # se unifica con servicio-azul (decisión de Ricardo)
    assert any(hx in r.values() for r in RAMPAS.values()), f'{nombre} {hx} no está en ninguna rampa'


def col(hx, alpha=1):
    h = hx.lstrip('#')
    comps = [round(int(h[i:i + 2], 16) / 255, 6) for i in (0, 2, 4)]
    return {'$type': 'color', '$value': {'colorSpace': 'srgb', 'components': comps, 'alpha': alpha, 'hex': '#' + h.upper()}}


def ref(path, tipo='color'):
    return {'$type': tipo, '$value': '{' + path + '}'}


def num(v):
    return {'$type': 'number', '$value': v}


def txt(v):
    return {'$type': 'string', '$value': v}


def c(fam, stop):
    return ref(f'color.{fam}.{stop}')


W = ref('color.white')
K = ref('color.black')  # texto negro sobre #FF7500 y #FA4616 (decisión de Ricardo)


def escribir(nombre, datos):
    with open(os.path.join(OUT, f'{nombre}.tokens.json'), 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
        f.write('\n')


# ─── primitivos ─────────────────────────────────────────────────────────────
primitivos = {
    'color': {
        'white': col('#FFFFFF'),
        'black': col('#000000'),
        **{fam: {str(s): col(r[s]) for s in STOPS} for fam, r in RAMPAS.items()},
    },
    'typography': {
        'size': {k: num(v) for k, v in [('2xs', 10), ('xs', 12), ('sm', 14), ('md', 16), ('lg', 18), ('xl', 20),
                                         ('2xl', 24), ('3xl', 28), ('4xl', 32), ('5xl', 40), ('6xl', 48), ('7xl', 56)]},
        'weight': {k: num(v) for k, v in [('regular', 400), ('medium', 500), ('semibold', 600), ('bold', 700), ('extrabold', 800)]},
        'leading': {k: num(v) for k, v in [('tight', 1.2), ('snug', 1.35), ('normal', 1.5), ('relaxed', 1.65), ('loose', 1.8)]},
        'tracking': {k: num(v) for k, v in [('tight', -0.02), ('normal', 0), ('wide', 0.02), ('wider', 0.04), ('caps', 0.08)]},
    },
    'radius': {k: num(v) for k, v in [('none', 0), ('xs', 2), ('sm', 4), ('md', 8), ('lg', 12), ('xl', 16), ('2xl', 24), ('full', 9999)]},
    'border': {k: num(v) for k, v in [('none', 0), ('sm', 1), ('md', 1.5), ('lg', 2), ('xl', 3)]},
}

# ─── semanticos ─────────────────────────────────────────────────────────────
def fb(fam, icon=700):
    return {'bg': c(fam, 50), 'border': c(fam, 300), 'text': c(fam, 800), 'icon': c(fam, icon)}


def servicio(fam, stop, texto):
    return {'bg': c(fam, stop), 'text': texto, 'subtle': c(fam, 50), 'strong': c(fam, 800)}


semanticos = {
    'background': {'page': W, 'base': W, 'subtle': c('neutral', 50), 'strong': c('neutral', 100)},
    'surface': {'base': W, 'raised': W, 'container': c('neutral', 50), 'subtle': c('neutral', 50),
                'inverse': c('neutral', 950), 'brand': c('brand', 500)},
    'text': {'primary': c('neutral', 950), 'secondary': c('neutral', 700), 'tertiary': c('neutral', 700),
             'disabled': c('neutral', 400), 'inverse': W, 'brand': c('brand', 600), 'on-brand': W,
             'on-brand-surface': K},
    'border': {'default': c('neutral', 300), 'subtle': c('neutral', 100), 'strong': c('neutral', 500),
               'brand': c('brand', 500), 'inverse': W},
    'divider': {'default': c('neutral', 300), 'strong': c('neutral', 500)},
    'brand': {'main': c('brand', 500), 'subtle': c('brand', 50), 'strong': c('brand', 700),
              'action': c('brand', 600), 'action-hover': c('brand', 700), 'action-press': c('brand', 800),
              'font-display': txt('Segoe UI'), 'font-body': txt('Segoe UI')},
    'servicio': {'petroleo': servicio('petroleo', 700, W), 'azul': servicio('azul', 800, W),
                 'rojizo': servicio('rojizo', 500, K), 'rojo': servicio('rojo', 600, W)},
    'feedback': {'success': fb('success'), 'warning': fb('warning', 600), 'error': fb('danger'),
                 # Info sin color propio: azul y petróleo son de servicio.
                 'info': {'bg': c('neutral', 50), 'border': c('neutral', 300), 'text': c('neutral', 950), 'icon': c('neutral', 700)}},
    # Foco negro: pasa 3:1 sobre el fondo y sobre el botón de acción.
    'focus': {'ring-color': K, 'ring-offset': W},
    'interaction': {'link': {'default': c('brand', 700), 'hover': c('brand', 800), 'visited': c('brand', 800)}},
}

# ─── componentes ────────────────────────────────────────────────────────────
componentes = {
    'button': {
        'font-weight': num(700),  # Segoe UI no tiene Semibold
        'radius': ref('radius.md', 'number'),
        # Hover: además del color, una sombra (especialistas, 2026-11-23).
        'primary': {'bg': c('brand', 600), 'bg-hover': c('brand', 700), 'bg-press': c('brand', 800), 'text': W, 'border': c('brand', 600),
                    'shadow-hover': txt('0px 1px 2px rgba(0, 0, 0, 0.12), 0px 2px 4px rgba(0, 0, 0, 0.10)')},
        'secondary': {'bg': W, 'bg-hover': c('neutral', 50), 'bg-press': c('neutral', 100), 'text': c('neutral', 950), 'border': c('neutral', 500)},
        'ghost': {'bg': W, 'bg-hover': c('neutral', 50), 'bg-press': c('neutral', 100), 'text': c('brand', 700), 'border': W},
        # Destructivo con contorno: relleno rojo solo en la confirmación (danger-solid),
        # nunca junto al primario. Disabled gris legible (especialistas, 2026-11-23).
        'danger': {'bg': W, 'bg-hover': c('danger', 50), 'bg-press': c('danger', 100), 'text': c('danger', 700), 'border': c('danger', 700)},
        'danger-solid': {'bg': c('danger', 700), 'bg-hover': c('danger', 800), 'bg-press': c('danger', 900), 'text': W, 'border': c('danger', 700)},
        'disabled': {'bg': c('neutral', 100), 'text': c('neutral', 700), 'border': c('neutral', 100)},
        'size': {s: {'height': num(h), 'padding-x': num(p)} for s, h, p in [('sm', 32, 12), ('md', 40, 16), ('lg', 48, 24)]},
    },
    'input': {
        'bg': W, 'bg-focus': W, 'bg-disabled': c('neutral', 50),
        'border': c('neutral', 500), 'border-hover': c('neutral', 700), 'border-focus': c('brand', 600),
        'border-error': c('danger', 700), 'border-success': c('success', 700), 'border-disabled': c('neutral', 200),
        'text': c('neutral', 950), 'placeholder': c('neutral', 700), 'label': c('neutral', 800), 'text-disabled': c('neutral', 400),
        'radius': ref('radius.md', 'number'), 'padding-x': num(12), 'padding-y': num(10),
    },
    'card': {
        'bg': W, 'border': c('neutral', 200), 'text': c('neutral', 950), 'bg-hover': c('neutral', 50), 'border-hover': c('neutral', 300),
        'radius': ref('radius.lg', 'number'), 'padding': num(24),
        'shadow': txt('0px 1px 2px rgba(0, 0, 0, 0.06), 0px 1px 3px rgba(0, 0, 0, 0.10)'),
    },
    'pill': {
        'radius': num(9999),
        'base': {'bg': c('neutral', 50), 'text': c('neutral', 800), 'border': c('neutral', 300)},
        'brand': {'bg': c('brand', 50), 'text': c('brand', 800)},
        'success': {'bg': c('success', 50), 'text': c('success', 800)},
        'warning': {'bg': c('warning', 50), 'text': c('warning', 800)},
        'error': {'bg': c('danger', 50), 'text': c('danger', 800)},
        'sm': {'padding-x': num(8)}, 'md': {'padding-x': num(12)},
    },
}


# ─── tipografía ─────────────────────────────────────────────────────────────
# Segoe UI (decisión de Ricardo, 2026-11-23; licencia web en la etapa 4). Sin
# Semibold: botones y etiquetas en Bold. Escala sobria para banca: display sin
# mayúsculas forzadas; labels en caja normal, sin tracking.
def estilo(size, lh, ls=None):
    d = {'size': num(size), 'line-height': num(lh)}
    if ls is not None:
        d['letter-spacing'] = num(ls)
    return d


tipografia = {'typography': {'styles': {
    'display': {'hero': estilo(56, 64, -1.12), 'xl': estilo(48, 56, -0.96), 'lg': estilo(40, 48, -0.6),
                'md': estilo(36, 44, -0.36), 'sm': estilo(32, 40, -0.32)},
    'heading': {'h1': estilo(28, 36, -0.28), 'h2': estilo(24, 32), 'h3': estilo(20, 28), 'h4': estilo(18, 26), 'h5': estilo(16, 24)},
    'body': {'lg': estilo(18, 28), 'md': estilo(16, 24), 'sm': estilo(14, 20), 'xs': estilo(12, 18),
             'lg-bold': estilo(18, 28), 'md-bold': estilo(16, 24), 'sm-bold': estilo(14, 20)},
    'label': {'lg': estilo(16, 20), 'md': estilo(14, 18), 'sm': estilo(12, 16), 'xs': estilo(11, 14)},
    'overline': {'lg': estilo(14, 18, 1.12), 'sm': estilo(12, 16, 0.96)},
    'code': {'md': estilo(14, 22), 'sm': estilo(12, 18)},
}}}

# ─── Colecciones genéricas (sin datos de marca) ─────────────────────────────
spacing = {'spacing': {str(k): num(v) for k, v in [(0, 0), (1, 4), (2, 8), (3, 12), (4, 16), (5, 20), (6, 24),
                                                     (8, 32), (10, 40), (12, 48), (16, 64), (20, 80), (24, 96)]}}
motion = {'motion': {
    'duration': {k: num(v) for k, v in [('instant', 50), ('fast', 100), ('normal', 150), ('slow', 250), ('slower', 400)]},
    'easing': {k: txt(v) for k, v in [('standard', 'cubic-bezier(0.4, 0, 0.2, 1)'), ('enter', 'cubic-bezier(0, 0, 0.2, 1)'),
                                       ('exit', 'cubic-bezier(0.4, 0, 1, 1)'), ('spring', 'cubic-bezier(0.34, 1.56, 0.64, 1)')]},
}}
opacity = {'opacity': {k: num(v) for k, v in [('ghost', 0.04), ('hairline', 0.08), ('subtle', 0.16), ('mid', 0.42), ('soft', 0.5),
                                              ('medium', 0.6), ('strong', 0.72), ('high', 0.8), ('full', 1)]}}
breakpoints = {'breakpoint': {k: num(v) for k, v in [('sm', 640), ('md', 768), ('lg', 1024), ('xl', 1280), ('2xl', 1536)]}}
shadow = {k: txt(v) for k, v in [('sm', '0px 1px 2px rgba(0, 0, 0, 0.06), 0px 1px 3px rgba(0, 0, 0, 0.10)'),
                                 ('md', '0px 4px 6px -1px rgba(0, 0, 0, 0.10), 0px 2px 4px -2px rgba(0, 0, 0, 0.10)'),
                                 ('lg', '0px 10px 15px -3px rgba(0, 0, 0, 0.10), 0px 4px 6px -4px rgba(0, 0, 0, 0.10)')]}
zindex = {k: num(v) for k, v in [('dropdown', 1000), ('sticky', 1020), ('overlay', 1030), ('modal', 1040), ('toast', 1050), ('tooltip', 1060)]}

for nombre, datos in [('primitivos', primitivos), ('semanticos', semanticos), ('componentes', componentes),
                      ('tipografia', tipografia), ('spacing', spacing), ('motion', motion), ('opacity', opacity),
                      ('breakpoints', breakpoints), ('shadow', shadow), ('z-index', zindex)]:
    escribir(nombre, datos)
print('source/dtcg: 10 colecciones escritas; marca.tokens.json sin tocar')
for fam, r in RAMPAS.items():
    print(f'  {fam:9}', ' '.join(r[s] for s in STOPS))
