#!/usr/bin/env node
/* Writes imagedims.json: { "images/<file>": [width, height], ... }
   The site uses this to reserve each popup picture's exact box before
   the file loads, so popups open instantly without any layout jump.
   Run after bundle.js. No dependencies; parses jpg/png/gif/webp headers. */

const fs = require('fs');
const path = require('path');

function jpegSize(b){
  let i = 2;
  while (i < b.length - 9) {
    if (b[i] !== 0xFF) { i++; continue; }
    const m = b[i + 1];
    if (m === 0xD8 || (m >= 0xD0 && m <= 0xD9)) { i += 2; continue; }
    const len = b.readUInt16BE(i + 2);
    if ((m >= 0xC0 && m <= 0xCF) && m !== 0xC4 && m !== 0xC8 && m !== 0xCC)
      return [b.readUInt16BE(i + 7), b.readUInt16BE(i + 5)];
    i += 2 + len;
  }
  return null;
}
function pngSize(b){ return [b.readUInt32BE(16), b.readUInt32BE(20)]; }
function gifSize(b){ return [b.readUInt16LE(6), b.readUInt16LE(8)]; }
function webpSize(b){
  const fourcc = b.toString('ascii', 12, 16);
  if (fourcc === 'VP8X') return [1 + b.readUIntLE(24, 3), 1 + b.readUIntLE(27, 3)];
  if (fourcc === 'VP8 ') return [b.readUInt16LE(26) & 0x3FFF, b.readUInt16LE(28) & 0x3FFF];
  if (fourcc === 'VP8L') {
    const n = b.readUInt32LE(21);
    return [1 + (n & 0x3FFF), 1 + ((n >> 14) & 0x3FFF)];
  }
  return null;
}
function sizeOf(file){
  const b = fs.readFileSync(file);
  if (b[0] === 0xFF && b[1] === 0xD8) return jpegSize(b);
  if (b[0] === 0x89 && b[1] === 0x50) return pngSize(b);
  if (b[0] === 0x47 && b[1] === 0x49) return gifSize(b);
  if (b.toString('ascii', 0, 4) === 'RIFF' && b.toString('ascii', 8, 12) === 'WEBP') return webpSize(b);
  return null;
}

const dir = path.join(__dirname, 'images');
const out = {};
let missed = 0;
for (const f of fs.readdirSync(dir).sort()) {
  try {
    const d = sizeOf(path.join(dir, f));
    if (d && d[0] > 0 && d[1] > 0) out[`images/${f}`] = d;
    else { missed++; console.error('no dimensions:', f); }
  } catch (e) { missed++; console.error('failed:', f, e.message); }
}
fs.writeFileSync(path.join(__dirname, 'imagedims.json'), JSON.stringify(out));
console.error(`imagedims.json: ${Object.keys(out).length} entries, ${missed} missed.`);
