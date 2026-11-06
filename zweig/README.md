# Stefan Zweig in English: *The Discovery of Eldorado*

A new English translation of Stefan Zweig's *Die Entdeckung Eldorados*, from *Sternstunden der Menschheit* (1927), made by the same method as the Antal Szerb project (`strawberrygrows/antal-szerb`): LLM draft, human editorial revision, paragraph by paragraph, every change in git.

This folder is self-contained so it can be moved to its own repository.

## Layout

```
source/die-entdeckung-eldorados.txt   Cleaned German text (S. Fischer 1951, via Projekt Gutenberg-DE)
paragraphs/discovery-of-eldorado/     One YAML per paragraph (Szerb schema) + meta.yaml + SUMMARY.md
quotes/library.yaml                   Allusions and their canonical English
apparatus/decisions.md                Zweig-specific rulings (Z01–Z07); Szerb rules apply otherwise
scripts/translation_data.py           The first draft, used once to create the YAML
scripts/make_paragraphs.py            Creates the YAML; never overwrites (translation_draft is immutable)
scripts/build.py, template.html       Builds the reading page
site/index.html                       The built page (static, no dependencies)
```

## Editing

Edit `translation_final` in a paragraph YAML (leave `translation_draft` alone), set `status: rachel-edited`, then rebuild:

```bash
python3 scripts/build.py
```

The page uses `translation_final` where it is filled in, otherwise the draft, and shows a "Draft translation" badge while any paragraph is still a draft. It needs Python 3 and PyYAML. `site/` can be served by GitHub Pages, Netlify, or any static host.

## Principles (inherited from the Szerb project)

- Repetition, refrains and alliteration preserved; sentences and paragraphs break where Zweig breaks them.
- **Dashes only where Zweig has one** (Szerb DECISION-009 → Z01); checked by script.
- Canonical English for quotations and allusions (Authorised Version for Exodus 3:8).
- British spelling; curly quotes, single primary, double nested; spaced en-dash.
- Foreign words kept and italicised; `*markdown italics*` in YAML.
- Four annotation types (`source`, `note`, `quote`, `query`); `note` under 80 words; `query` only for real impasses.

## Rights

- **Zweig** died on 22 February 1942. His works have been in the public domain since 1 January 2013 in the UK, the EU, Switzerland, Austria and other life-plus-70 countries.
- **United States:** copyright depends on first publication, not death. *Die Entdeckung Eldorados* was first published in 1927 and so has been public domain in the US since 1 January 2023. Chapters first published in the enlarged 1943 edition stay in US copyright until the end of 2038. If any of Zweig's revisions to this text first appeared in 1943, those revisions would technically stay protected in the US as well. For US sale, collate against the 1927 Insel text.
- **Existing English translations** (Eden and Cedar Paul, 1940; Anthea Bell, 2013) are in copyright. They were not used and should not be consulted while drafting.
- **The new translation** is the translator's own copyright work.
- **The transcription:** the German text is public domain, but check Projekt Gutenberg-DE's terms of use before reproducing their transcription wholesale on a public site. A scan of the 1927 edition is the safest source of record.
