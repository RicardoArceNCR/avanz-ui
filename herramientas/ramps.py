"""Rampas 50-950 en OKLCH ancladas a los hex de marca.

Una tabla comun de claridad (LT) hace que el mismo stop signifique lo mismo
en todas las familias: todo X/700 sirve como texto sobre Crema, todo X/300-400
sirve como texto sobre Noche. Las anclas se respetan exactas; los stops
vecinos absorben la diferencia con un decaimiento gaussiano.
"""
import math
from color import oklch, gamut_map

STOPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
LT = {50: .975, 100: .935, 200: .875, 300: .805, 400: .745, 500: .685,
      600: .600, 700: .520, 800: .440, 900: .360, 950: .280}
CM = {50: .14, 100: .30, 200: .50, 300: .70, 400: .86, 500: 1, 600: 1,
      700: .95, 800: .82, 900: .64, 950: .48}


def ramp(anchors):
    A = {s: oklch(h) for s, h in anchors.items()}
    idx = {s: i for i, s in enumerate(STOPS)}
    main = max(A, key=lambda s: A[s][1])
    Cm = A[main][1]
    ks = sorted(A)
    out = {}
    for s in STOPS:
        if s in anchors:
            out[s] = anchors[s].upper()
            continue
        L = LT[s]
        for a, (La, Ca, Ha) in A.items():
            L += (La - LT[a]) * math.exp(-((abs(idx[s] - idx[a])) / 1.2) ** 2)
        if len(ks) == 1:
            H = A[ks[0]][2]
        else:
            lo = max([k for k in ks if k <= s] or [ks[0]])
            hi = min([k for k in ks if k >= s] or [ks[-1]])
            if lo == hi:
                H = A[lo][2]
            else:
                t = (idx[s] - idx[lo]) / (idx[hi] - idx[lo])
                dh = ((A[hi][2] - A[lo][2] + 180) % 360) - 180
                H = (A[lo][2] + t * dh) % 360
        C = Cm * CM[s]
        for a, (La, Ca, Ha) in A.items():
            if a != main:
                w = math.exp(-((abs(idx[s] - idx[a])) / 0.9) ** 2)
                C = C * (1 - w) + Ca * (CM[s] / CM[a]) * w
        out[s] = gamut_map(L, C, H)
    return out


NL = {50: .972, 100: .930, 200: .872, 300: .800, 400: .710, 500: .625,
      600: .525, 700: .450, 800: .335, 900: .282, 950: .245}


def neutral_ramp(paper, ink, Lt=NL, c_light=.0080, c_dark=.0090):
    """Grises = tinta Noche sobre papel Crema, con croma < 0.01 para pasar
    la regla 'neutral es neutral' de check-ramps. Lado claro con el matiz
    calido del papel, lado oscuro con el violeta de la tinta; el croma cae
    casi a cero en el medio para no pasar por rosados."""
    Lp, Cp, Hp = oklch(paper)
    Li, Ci, Hi = oklch(ink)
    out = {}
    for s in STOPS:
        L = Lt[s]
        t = min(1, max(0, (Lp - L) / (Lp - Li)))
        C = c_light * (1 - t) ** 2 + c_dark * t ** 2
        H = Hp if t < .5 else Hi
        out[s] = gamut_map(L, C, H)
    return out
