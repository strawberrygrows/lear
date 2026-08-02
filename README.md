# The Edward Lear Trail — site handbook

## What you have

- **index.html** — the whole site in one file: map, quiz, miscellany. Works as-is by double-clicking it (it needs internet for map tiles and the limerick scans).
- **bundle.js** — optional script that downloads all the blog's limerick scans/photos next to the site so it doesn't lean on WordPress at runtime.
- **lear-trail-copy-review.md** — every word on the site, with Rachel's edits applied.
- **vendor/leaflet/** — the map library, served locally so the site doesn't depend on a CDN.

## Putting it on the internet

Deployed via **GitHub Pages**: every push to the default branch runs
`.github/workflows/deploy.yml` and republishes the site. For a custom
domain later, add it under Settings → Pages (same DNS dance as
antalszerb.com on Porkbun).

## Switching on the real Ordnance Survey backdrop

Out of the box the map uses OpenStreetMap. For the genuine article:

1. Go to **osdatahub.os.uk** → create a free account.
2. API Dashboard → **Add a project** → add the **OS Maps API** to it.
3. Copy the Project API Key into `CONFIG.OS_KEY` near the top of index.html.

Free tier is generous (transaction allowance far beyond what family browsing will use). Coverage is **Great Britain only** — the site automatically keeps OpenStreetMap underneath, so Ireland and the overseas pins still have a map; a layer switcher (top right of the map) lets your dad flip between views.

## Switching on the 1890s sheets

The National Library of Scotland's scanned Victorian OS one-inch maps — Lear-era Britain — are served via MapTiler:

1. **cloud.maptiler.com** → free account → Account → Keys → copy the key.
2. Paste into `CONFIG.MAPTILER_KEY` in index.html.

That adds an "1890s sheets (NLS)" option to the layer switcher. Free tier: 100,000 tiles/month, plenty. The NLS asks for attribution (already in the map credits) and non-commercial use (a birthday present qualifies handsomely).

## Bundling the photos

From the site folder, on your machine (Node 18+):

```
node bundle.js
```

Creates `images/` and `images.json`; the site notices them automatically and stops calling WordPress. Upload those alongside index.html when you host. Until then the site fetches images live from the blog, which also works fine.

## Still to do together

1. You send the birthday message text (or edit the placeholder in index.html directly — search for `BIRTHDAY MESSAGE`).
2. You return the copy file with edits; I apply them.
3. Open index.html on your phone and laptop and shout at me about anything broken or ugly.
