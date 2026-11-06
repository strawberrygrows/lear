#!/usr/bin/env python3
"""One-off: create paragraphs/<slug>/*.yaml from the cleaned German source and
translation_data.py. Refuses to overwrite existing paragraph files, because
translation_draft is immutable once written."""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import translation_data as T  # noqa: E402

SLUG = "discovery-of-eldorado"
SOURCE = ROOT / "source" / "die-entdeckung-eldorados.txt"
SOURCE_URL = ("https://projekt-gutenberg.org/authors/stefan-zweig/books/"
              "sternstunden-der-menschheit/chapter/9/")


class Literal(str):
    pass


def literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(Literal, literal_representer)


def dump(path, data):
    path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, width=88),
                    encoding="utf-8")


def main():
    lines = [l.strip() for l in SOURCE.read_text(encoding="utf-8").splitlines() if l.strip()]
    title_de, dateline_de, body = lines[0], lines[1], lines[2:]

    paras, section = [], None
    for line in body:
        if line in T.SECTIONS:
            section = line
        else:
            paras.append((section, line))

    if len(paras) != len(T.P):
        sys.exit(f"paragraph count mismatch: source {len(paras)}, drafts {len(T.P)}")

    # DECISION-Z01: dashes only where Zweig has one, paragraph by paragraph.
    for i, ((_, de), (en, anns, _)) in enumerate(zip(paras, T.P), 1):
        n_de, n_en = de.count("–") + de.count("—"), en.count("–")
        if n_de != n_en or "—" in en:
            sys.exit(f"p{i:02d}: dash count differs (source {n_de}, draft {n_en})")
        for a in anns:
            if a["span"] not in en:
                sys.exit(f"p{i:02d}: annotation span not in draft: {a['span']!r}")
            if "—" in a["body"]:
                sys.exit(f"p{i:02d}: em-dash in annotation body")

    out = ROOT / "paragraphs" / SLUG
    out.mkdir(parents=True, exist_ok=True)

    dump(out / f"{SLUG}-meta.yaml", {
        "titleEn": T.TITLE_EN,
        "titleDe": title_de,
        "datelineEn": T.DATELINE_EN,
        "datelineDe": dateline_de,
        "author": "Stefan Zweig",
        "collection": "Sternstunden der Menschheit",
        "first_published": "1927, Insel-Bücherei 165 (Leipzig: Insel-Verlag)",
        "source_text": "S. Fischer Verlag, 1951, via Projekt Gutenberg-DE",
        "source_url": SOURCE_URL,
        "sections": [{"de": de, "en": en} for de, en in T.SECTIONS.items()],
    })

    for i, ((section, de), (en, anns, corr)) in enumerate(zip(paras, T.P), 1):
        pid = f"{SLUG}-p{i:02d}"
        path = out / f"{pid}.yaml"
        if path.exists():
            print(f"skip {path.name}: exists (translation_draft is immutable)")
            continue
        dump(path, {
            "id": pid,
            "locus": f"Die Entdeckung Eldorados, paragraph {i}",
            "section": {"de": section, "en": T.SECTIONS[section]},
            "source_url": SOURCE_URL,
            "status": "claude-drafted",
            "source": {"raw": Literal(de + "\n"), "ocr_corrections": corr},
            "translation_draft": Literal(en + "\n"),
            "translation_final": "",
            "annotations": [dict(id=j, **a, status="claude-drafted")
                            for j, a in enumerate(anns, 1)],
        })
        print("wrote", path.name)

    lib = ROOT / "quotes" / "library.yaml"
    lib.parent.mkdir(exist_ok=True)
    if not lib.exists():
        dump(lib, {"quotes": T.QUOTE_LIBRARY})
        print("wrote quotes/library.yaml")


if __name__ == "__main__":
    main()
