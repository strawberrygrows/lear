#!/usr/bin/env node
/* The Edward Lear Trail — photo bundler.
   Run this ONCE, from the site folder, on a normal internet connection:
     node bundle.js
   It downloads every post's featured image (Lear's illustrated limericks)
   into ./images/ and writes ./images.json. The site then loads images
   locally instead of calling WordPress at runtime. Node 18+ required. */

const fs = require('fs');
const path = require('path');

const SITE = 'edwardleartrail.wordpress.com';
const OUT = path.join(__dirname, 'images');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const slugOf = u => (u || '').replace(/\/+$/, '').split('/').pop();

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const map = {};
  let posts = [];
  for (let page = 1; page <= 3; page++) {
    const api = `https://public-api.wordpress.com/rest/v1.1/sites/${SITE}/posts/?number=100&page=${page}&fields=URL,featured_image`;
    const r = await fetch(api);
    if (!r.ok) { console.error('API error', r.status); break; }
    const j = await r.json();
    posts = posts.concat(j.posts || []);
    if (!j.posts || j.posts.length < 100) break;
  }
  console.log(`Found ${posts.length} posts.`);
  let n = 0;
  for (const p of posts) {
    if (!p.featured_image) continue;
    const slug = slugOf(p.URL);
    const ext = (p.featured_image.split('.').pop().split('?')[0] || 'jpg').slice(0, 4);
    const file = `${slug}.${ext}`;
    try {
      const img = await fetch(p.featured_image + (p.featured_image.includes('?') ? '&' : '?') + 'w=800');
      if (!img.ok) { console.warn('skip', slug, img.status); continue; }
      fs.writeFileSync(path.join(OUT, file), Buffer.from(await img.arrayBuffer()));
      map[slug] = `images/${file}`;
      n++;
      process.stdout.write(`\r${n} images saved…`);
      await sleep(150); // be polite to WordPress
    } catch (e) { console.warn('\nfailed', slug, e.message); }
  }
  fs.writeFileSync(path.join(__dirname, 'images.json'), JSON.stringify(map, null, 1));
  console.log(`\nDone: ${n} images in ./images, index written to images.json.`);
})();
