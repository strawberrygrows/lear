#!/usr/bin/env python3
"""Create paragraphs/<slug>/*.yaml from a cleaned German source and a draft module.

    python3 scripts/make_paragraphs.py discovery_of_eldorado
    python3 scripts/make_paragraphs.py first_word_across_the_ocean

Never overwrites an existing paragraph file, because translation_draft is
immutable once written. The story's meta.yaml and the quote library entries
for the story are (re)written every time.
"""
import importlib
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "drafts"))


class Literal(str):
    pass


yaml.add_representer(
    Literal, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|"))


def dump(path, data):
    path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, width=88),
                    encoding="utf-8")


def main(module_name):
    D = importlib.import_module(module_name).D
    source = ROOT / "source" / D.source_file
    lines = [l.strip() for l in source.read_text(encoding="utf-8").splitlines() if l.strip()]
    title_de, dateline_de, body = lines[0], lines[1], lines[2:]

    paras, section = [], None
    for line in body:
        if line in D.sections:
            section = line
        else:
            if section is None:
                sys.exit(f"paragraph before first heading: {line[:40]!r}")
            paras.append((section, line))

    if len(paras) != len(D.paras):
        sys.exit(f"paragraph count mismatch: source {len(paras)}, drafts {len(D.paras)}")

    # DECISION-Z01: dashes only where Zweig has one, paragraph by paragraph.
    for i, ((_, de), (en, anns, _)) in enumerate(zip(paras, D.paras), 1):
        n_de, n_en = de.count("–") + de.count("—"), en.count("–")
        if n_de != n_en or "—" in en:
            sys.exit(f"p{i:02d}: dash count differs (source {n_de}, draft {n_en})")
        for a in anns:
            if a["span"] not in en:
                sys.exit(f"p{i:02d}: annotation span not in draft: {a['span']!r}")
            if "—" in a["body"] or " – " in a["body"]:
                sys.exit(f"p{i:02d}: dash in annotation body")

    out = ROOT / "paragraphs" / D.slug
    out.mkdir(parents=True, exist_ok=True)

    dump(out / f"{D.slug}-meta.yaml", {
        "slug": D.slug,
        "order": D.order,
        "titleEn": D.title_en,
        "titleDe": title_de,
        "datelineEn": D.dateline_en,
        "datelineDe": dateline_de,
        "author": "Stefan Zweig",
        "collection": "Sternstunden der Menschheit",
        "first_published": D.first_published,
        "blurb": D.blurb,
        "rights": D.rights,
        "source_text": "S. Fischer Verlag, 1951, via Projekt Gutenberg-DE",
        "source_url": D.source_url,
        "sections": [{"de": de, "en": en} for de, en in D.sections.items()],
    })

    for i, ((section, de), (en, anns, corr)) in enumerate(zip(paras, D.paras), 1):
        pid = f"{D.slug}-p{i:02d}"
        path = out / f"{pid}.yaml"
        if path.exists():
            continue
        dump(path, {
            "id": pid,
            "locus": f"{title_de}, paragraph {i}",
            "section": {"de": section, "en": D.sections[section]},
            "source_url": D.source_url,
            "status": "claude-drafted",
            "source": {"raw": Literal(de + "\n"), "ocr_corrections": corr},
            "translation_draft": Literal(en + "\n"),
            "translation_final": "",
            "annotations": [dict(id=j, **a, status="claude-drafted")
                            for j, a in enumerate(anns, 1)],
        })
        print("wrote", path.name)

    # Quote library: keep other stories' entries, replace this story's.
    lib_path = ROOT / "quotes" / "library.yaml"
    lib = yaml.safe_load(lib_path.read_text(encoding="utf-8")) if lib_path.exists() else {}
    entries = [q for q in (lib or {}).get("quotes", [])
               if not any(u.startswith(D.slug) for u in q.get("used_in", []))]
    ids = {q["id"] for q in entries}
    entries += [q for q in D.library if q["id"] not in ids]
    dump(lib_path, {"quotes": entries})
    print(f"{D.slug}: {len(paras)} paragraphs, library {len(entries)} entries")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
