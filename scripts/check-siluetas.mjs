#!/usr/bin/env node
/**
 * Siluetas de las portadas (ADR 0005): el texto tiene que pasar AA también
 * sobre la zona más oscura, donde se cruzan las copias. La opacidad de n
 * copias superpuestas se compone: 1 − (1 − α)^n. Lee build/tokens.css.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const css = readFileSync(path.join(root, "build/tokens.css"), "utf8");
const map = new Map([...css.matchAll(/--([a-z0-9-]+)\s*:\s*([^;]+);/g)].map(([, n, v]) => [n, v.trim()]));
const res = (n, d = 0) => {
  const v = map.get(n);
  const r = v?.match(/^var\(--([a-z0-9-]+)\)$/);
  return r && d < 20 ? res(r[1], d + 1) : v;
};
const rgb = (hex) => [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
const lum = (c) =>
  0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]);
function lin(v) {
  v /= 255;
  return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
}
const ratio = (a, b) => {
  const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p);
  return (x + 0.05) / (y + 0.05);
};

// Portada: fondo, textos que van encima y cuántas copias se cruzan.
const PORTADAS = [
  { id: "inicio", fondo: "surface-base", textos: ["text-primary", "text-secondary"], copias: 2 },
  { id: "logo", fondo: "surface-container", textos: ["text-primary", "text-secondary"], copias: 2 },
  { id: "color", fondo: "brand-main", textos: ["text-primary", "color-black"], copias: 2 },
  { id: "tipografia", fondo: "color-neutral-700", textos: ["text-inverse"], copias: 2 },
  { id: "sistema", fondo: "surface-inverse", textos: ["text-inverse"], copias: 1 },
];

let fallas = 0;
for (const p of PORTADAS) {
  const fondo = rgb(res(p.fondo));
  const tinta = rgb(res(`silueta-${p.id}-color`));
  const a = 1 - (1 - parseFloat(res(`silueta-${p.id}-opacity`))) ** p.copias;
  const cruce = fondo.map((f, i) => Math.round(f * (1 - a) + tinta[i] * a));
  for (const t of p.textos) {
    const r = ratio(rgb(res(t)), cruce);
    const ok = r >= 4.5;
    if (!ok) fallas++;
    console.log(`${ok ? "✓" : "✗"} ${p.id}: ${t} sobre el cruce de las siluetas ${r.toFixed(2)}:1`);
  }
}
if (fallas) {
  console.error(`check-siluetas: ${fallas} par(es) por debajo de 4,5:1`);
  process.exit(1);
}
console.log("check-siluetas: OK");
