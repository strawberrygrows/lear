"""Helpers for the one-off draft modules in scripts/drafts/."""


class Draft:
    def __init__(self, slug, source_file, source_url, title_en, dateline_en, order,
                 first_published, blurb, rights, sections):
        self.slug, self.source_file, self.source_url = slug, source_file, source_url
        self.title_en, self.dateline_en, self.order = title_en, dateline_en, order
        self.first_published, self.blurb, self.rights = first_published, blurb, rights
        self.sections = sections
        self.paras = []
        self.library = []

    def para(self, draft, annotations=None, corrections=None):
        self.paras.append((draft.strip(), annotations or [], corrections or []))


def note(span, body):
    return {"type": "note", "span": span, "body": body.strip()}


def quote(span, ref, body):
    return {"type": "quote", "span": span, "quote_library_ref": ref, "body": body.strip()}


def query(span, body):
    return {"type": "query", "span": span, "body": body.strip()}
