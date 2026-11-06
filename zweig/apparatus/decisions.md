# Editorial Decisions: Zweig translations

These follow the Antal Szerb project's rules (`strawberrygrows/antal-szerb`: CLAUDE.md, STYLE.md, apparatus/decisions.md, apparatus/house-style-decisions.md) wherever they apply. Entries below record only where a Zweig text needs its own ruling. The editor's rulings take precedence.

---

### DECISION-Z01: Dashes only where Zweig has one
**Date:** 2026-11-06
**Context:** Szerb DECISION-009, applied to German. Zweig's dash is the *Gedankenstrich* (–).
**Ruling:** A dash appears in the English only where the German has one, rendered as a spaced en-dash (UK house style). `scripts/make_paragraphs.py` checks this per paragraph and refuses to write a draft whose dash count differs from the source. *Die Entdeckung Eldorados* has ten.
**Scope:** All Zweig texts, permanent.

### DECISION-Z02: Voice
**Date:** 2026-11-06
**Context:** The Szerb voice (interwar British literary scholarship) is calibrated for essays. Zweig's *Sternstunden* are narrative miniatures in the historical present, built on long comma-chains, refrains and exclamation.
**Ruling:** Keep the interwar British register (British spelling, slightly Latinate vocabulary, no modern idiom) but follow Zweig's syntax rather than Eliot's: keep the historical present; keep his comma-chains and comma splices rather than repunctuating into semicolons, except where English would otherwise misparse; keep every refrain identical on each occurrence (*der reichste Mann der Welt* = 'the richest man in the world'); keep leitmotif words consistent (*magisch* = 'magical/magic'; *gigantisch* = 'gigantic'; *Feuerwoge* = 'wave of fire').
**Scope:** All Zweig texts.

### DECISION-Z03: Zweig's spelling of personal names
**Date:** 2026-11-06
**Context:** Zweig writes *Johann August Suter* (the historical John Augustus Sutter) and *Alverado* (Juan Bautista Alvarado).
**Ruling:** Keep the name form Zweig chose deliberately for his protagonist (Suter), with a note on first occurrence. Correct plain misspellings of secondary historical figures silently (Alvarado), with a note.
**Scope:** All Zweig texts.

### DECISION-Z04: Place-names
**Date:** 2026-11-06
**Context:** Zweig Germanises or misspells places: *Neuyork*, *San Franzisko*, *Sakramento*, *Monte Rey*, *Van Couver*, *Le Hâvre*, *Kap Hoorn*.
**Ruling:** Extend Szerb DECISION-008: give all non-German place-names in their standard English form silently. Period names that are not errors stay (*Sandwich Islands*). Zweig's spelling of obscure places is kept where the correct form is uncertain or the variant is his (*Rynenberg*), with a note.
**Scope:** All Zweig texts.

### DECISION-Z05: Zweig's history is not corrected
**Date:** 2026-11-06
**Context:** *Die Entdeckung Eldorados* follows Blaise Cendrars's novel *L'Or* (1925) and departs from the historical record (the deaths of Suter's wife and sons, Judge Thompson, the date and place of Suter's death, the telegraph in 1848).
**Ruling:** Translate what Zweig wrote. Do not correct his history. Where a departure would mislead a reader, add a short `note`.
**Scope:** All Zweig texts.

### DECISION-Z06: Numbers
**Date:** 2026-11-06
**Context:** Zweig mixes figures and words (*31 Jahre alt*, *fünfundvierzig Jahre alt*, *17 221 Farmer*, *25 Millionen Dollar*).
**Ruling:** Ages and small numbers spelled out in English prose style; large exact figures and money left in figures as Zweig gives them, with British thousands comma (17,221). Dates as day–month–year (7 July, 15 March 1855).
**Scope:** All Zweig texts.

### DECISION-Z07: Period terms for peoples
**Date:** 2026-11-06
**Context:** Zweig (1927) writes *Rothäute*, *Kanaken*, *Farbigen*, *Eingeborenen*.
**Ruling:** Render in period-appropriate English without sharpening or softening beyond the original: 'Red Indians', 'Kanakas', 'coloured men', 'natives'. Noted on first occurrence. The editor may revise.
**Scope:** All Zweig texts.

### DECISION-Z08: Ships' names
**Date:** 2026-11-06
**Context:** Zweig puts ships' names in quotation marks (»Agamemnon«, »Niagara«, »Great Eastern«).
**Ruling:** Italicise ships' names, as English convention requires (*Agamemnon*). No quotation marks.
**Scope:** All Zweig texts.

### DECISION-Z09: English quoted by Zweig
**Date:** 2026-11-06
**Context:** Zweig often quotes English sources in English and then gives his own German translation of the same words (*The Times*, Morse), and uses English words in his German (*Rush*, *Newspaper Boys*, headlines).
**Ruling:** Keep the English exactly as Zweig gives it, quirks included ('an universal jubilee'). Omit Zweig's German gloss where it only repeats the English, with a note. Where Zweig quotes an English-language source in German only (the Valentia prayer), look for the original; if it is not found, translate fresh and raise a `query`.
**Scope:** All Zweig texts.
