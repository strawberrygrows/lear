#!/usr/bin/env python3
"""Build the static reading page from paragraphs/<slug>/*.yaml.

    python3 scripts/build.py            -> site/index.html (full document)
    python3 scripts/build.py --fragment OUT.html
                                        -> same page without <!doctype>/<html>/<head>
                                           wrapper (for an Artifact preview)

Uses translation_final where the editor has filled it in, otherwise
translation_draft (marked as a draft on the page).
"""
import html
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SLUG = "discovery-of-eldorado"
PARA_DIR = ROOT / "paragraphs" / SLUG
TEMPLATE = ROOT / "scripts" / "template.html"


def inline_md(text):
    """Escape, then turn *x* into <em>x</em>."""
    t = html.escape(text, quote=False)
    return re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", t)


def load():
    meta = yaml.safe_load((PARA_DIR / f"{SLUG}-meta.yaml").read_text(encoding="utf-8"))
    paras = [yaml.safe_load(p.read_text(encoding="utf-8"))
             for p in sorted(PARA_DIR.glob(f"{SLUG}-p*.yaml"))]
    return meta, paras


def render_text(text, anns, start_n):
    """Render paragraph text with note markers after each annotation span."""
    out = inline_md(text.strip())
    notes = []
    n = start_n
    for a in anns:
        if a.get("type") == "query":
            continue  # queries are for the editor, not the reader
        n += 1
        span_html = inline_md(a["span"])
        marker = (f'<sup class="nref" id="nref-{n}"><a href="#note-{n}" '
                  f'aria-label="Note {n}">{n}</a></sup>')
        if span_html in out:
            out = out.replace(span_html, span_html + marker, 1)
        notes.append((n, a))
    return out, notes, n


def build_body(meta, paras):
    parts, endnotes = [], []
    n = 0
    any_draft = False
    current = None
    for i, p in enumerate(paras, 1):
        sec = p["section"]
        if sec["de"] != current:
            if current is not None:
                parts.append("</section>")
            current = sec["de"]
            parts.append(
                f'<section class="part">'
                f'<h2 class="part-head"><span class="en">{html.escape(sec["en"])}</span>'
                f'<span class="de" lang="de">{html.escape(sec["de"])}</span></h2>')
        final = (p.get("translation_final") or "").strip()
        text = final or p["translation_draft"]
        any_draft = any_draft or not final
        body, notes, n = render_text(text, p.get("annotations") or [], n)
        endnotes.extend((num, a, i) for num, a in notes)
        de = html.escape(p["source"]["raw"].strip(), quote=False)
        parts.append(
            f'<div class="pair" id="p{i:02d}">'
            f'<p class="en">{body}</p>'
            f'<p class="de" lang="de">{de}</p>'
            f'<a class="pnum" href="#p{i:02d}" aria-label="Paragraph {i}">{i}</a>'
            f'</div>')
    parts.append("</section>")

    notes_html = []
    for num, a, pi in endnotes:
        kind = "Allusion" if a["type"] == "quote" else "Note"
        notes_html.append(
            f'<li id="note-{num}"><span class="kind">{kind}</span> '
            f'<span class="span">{inline_md(a["span"])}</span>. '
            f'{inline_md(a["body"].strip())} '
            f'<a class="back" href="#nref-{num}" aria-label="Back to the text">↩</a></li>')
    return "\n".join(parts), "\n".join(notes_html), any_draft, len(paras), n


def main():
    meta, paras = load()
    story, notes, any_draft, count, n_notes = build_body(meta, paras)
    page = TEMPLATE.read_text(encoding="utf-8")
    status = ("Draft translation, awaiting editorial review" if any_draft
              else "Edited translation")
    for key, val in {
        "{{STORY}}": story,
        "{{NOTES}}": notes,
        "{{STATUS}}": status,
        "{{TITLE_EN}}": html.escape(meta["titleEn"]),
        "{{TITLE_DE}}": html.escape(meta["titleDe"]),
        "{{DATELINE_EN}}": html.escape(meta["datelineEn"]),
        "{{SOURCE_URL}}": html.escape(meta["source_url"]),
        "{{COUNT}}": str(count),
        "{{NOTE_COUNT}}": str(n_notes),
    }.items():
        page = page.replace(key, val)

    if "--fragment" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--fragment") + 1])
        frag = re.sub(r"(?s)^.*?<!--HEAD-->", "", page)
        frag = frag.replace("</head>", "").replace("<body>", "")
        frag = frag.replace("</body>", "").replace("</html>", "")
        out.write_text(frag.strip() + "\n", encoding="utf-8")
        print("wrote", out)
    else:
        out = ROOT / "site" / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
