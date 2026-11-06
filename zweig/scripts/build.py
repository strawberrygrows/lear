#!/usr/bin/env python3
"""Build the static site from paragraphs/<slug>/*.yaml.

    python3 scripts/build.py
        -> site/index.html (contents) and site/<slug>.html (one per story)

    python3 scripts/build.py --preview DIR
        -> the same pages in DIR, with index.html stripped of its
           <!doctype>/<html>/<head> wrapper (for an Artifact preview)

Each story page uses translation_final where the editor has filled it in,
otherwise translation_draft (marked as a draft on the page).
"""
import html
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


def inline_md(text):
    """Escape, then turn *x* into <em>x</em>."""
    t = html.escape(text, quote=False)
    return re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", t)


def plain(text):
    return re.sub(r"\*([^*\n]+)\*", r"\1", text)


def fill(template, values):
    for key, val in values.items():
        template = template.replace("{{" + key + "}}", val)
    left = re.findall(r"\{\{[A-Z_]+\}\}", template)
    if left:
        sys.exit(f"unfilled placeholders: {left}")
    return template


def load_stories():
    stories = []
    for d in sorted(p for p in (ROOT / "paragraphs").iterdir() if p.is_dir()):
        meta_path = d / f"{d.name}-meta.yaml"
        if not meta_path.exists():
            continue
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
        paras = [yaml.safe_load(p.read_text(encoding="utf-8"))
                 for p in sorted(d.glob(f"{d.name}-p*.yaml"))]
        stories.append((meta, paras))
    return sorted(stories, key=lambda s: s[0]["order"])


def render_text(text, anns, start_n):
    """Render paragraph text with note markers after each annotation span."""
    out = inline_md(text.strip())
    notes, n = [], start_n
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


def build_story(meta, paras):
    parts, endnotes = [], []
    n, any_draft, current, dashes = 0, False, None, 0
    for i, p in enumerate(paras, 1):
        sec = p["section"]
        if sec["de"] != current:
            if current is not None:
                parts.append("</section>")
            current = sec["de"]
            parts.append(
                f'<section class="part">'
                f'<h2 class="part-head"><span class="en">{inline_md(sec["en"])}</span>'
                f'<span class="de" lang="de">{html.escape(sec["de"])}</span></h2>')
        final = (p.get("translation_final") or "").strip()
        text = final or p["translation_draft"]
        any_draft = any_draft or not final
        dashes += p["source"]["raw"].count("–")
        body, notes, n = render_text(text, p.get("annotations") or [], n)
        endnotes.extend(notes)
        de = html.escape(p["source"]["raw"].strip(), quote=False)
        parts.append(
            f'<div class="pair" id="p{i:02d}">'
            f'<p class="en">{body}</p>'
            f'<p class="de" lang="de">{de}</p>'
            f'<a class="pnum" href="#p{i:02d}" aria-label="Paragraph {i}">{i}</a>'
            f'</div>')
    parts.append("</section>")

    notes_html = []
    for num, a in endnotes:
        kind = "Allusion" if a["type"] == "quote" else "Note"
        notes_html.append(
            f'<li id="note-{num}"><span class="kind">{kind}</span> '
            f'<span class="span">{inline_md(a["span"])}</span>. '
            f'{inline_md(a["body"].strip())} '
            f'<a class="back" href="#nref-{num}" aria-label="Back to the text">↩</a></li>')
    return {
        "STORY": "\n".join(parts),
        "NOTES": "\n".join(notes_html),
        "STATUS": ("Draft translation, awaiting editorial review" if any_draft
                   else "Edited translation"),
        "COUNT": str(len(paras)),
        "NOTE_COUNT": str(n),
        "DASHES": str(dashes),
        "_draft": any_draft,
    }


def pager(stories, idx):
    links = []
    if idx > 0:
        m = stories[idx - 1][0]
        links.append(f'<a href="{m["slug"]}.html">← {html.escape(m["titleEn"])}</a>')
    links.append('<a href="index.html">Contents</a>')
    if idx < len(stories) - 1:
        m = stories[idx + 1][0]
        links.append(f'<a href="{m["slug"]}.html">{html.escape(m["titleEn"])} →</a>')
    return " ".join(links)


def strip_wrapper(page):
    frag = re.sub(r"(?s)^.*?<!--HEAD-->", "", page)
    for tag in ("</head>", "<body>", "</body>", "</html>"):
        frag = frag.replace(tag, "")
    return frag.strip() + "\n"


def main():
    css = (SCRIPTS / "style.css").read_text(encoding="utf-8")
    story_t = (SCRIPTS / "story.html").read_text(encoding="utf-8")
    index_t = (SCRIPTS / "index.html").read_text(encoding="utf-8")
    stories = load_stories()

    preview = "--preview" in sys.argv
    out_dir = Path(sys.argv[sys.argv.index("--preview") + 1]) if preview else ROOT / "site"
    out_dir.mkdir(parents=True, exist_ok=True)

    contents = []
    for idx, (meta, paras) in enumerate(stories):
        v = build_story(meta, paras)
        is_draft = v.pop("_draft")
        v.update({
            "CSS": css,
            "TITLE_EN": html.escape(meta["titleEn"]),
            "TITLE_DE": html.escape(meta["titleDe"]),
            "DATELINE_EN": html.escape(meta["datelineEn"]),
            "DESCRIPTION": html.escape(f"Stefan Zweig, ‘{meta['titleDe']}’: {plain(meta['blurb'])}"),
            "RIGHTS": inline_md(meta["rights"]),
            "SOURCE_URL": html.escape(meta["source_url"]),
            "PAGER": pager(stories, idx),
        })
        (out_dir / f"{meta['slug']}.html").write_text(fill(story_t, v), encoding="utf-8")
        print("wrote", f"{meta['slug']}.html")
        state = "draft" if is_draft else "edited"
        contents.append(
            f'<li><span class="num">{idx + 1}</span><div>'
            f'<h2><a href="{meta["slug"]}.html">{html.escape(meta["titleEn"])}</a></h2>'
            f'<p class="de" lang="de">{html.escape(meta["titleDe"])}</p>'
            f'<p class="line">{html.escape(meta["datelineEn"])}</p>'
            f'<p class="blurb">{inline_md(meta["blurb"])}</p>'
            f'<p class="meta">{len(paras)} paragraphs · {state}</p>'
            f'</div></li>')

    index = fill(index_t, {"CSS": css, "CONTENTS": "\n".join(contents)})
    if preview:
        index = strip_wrapper(index)
    (out_dir / "index.html").write_text(index, encoding="utf-8")
    print("wrote index.html")


if __name__ == "__main__":
    main()
