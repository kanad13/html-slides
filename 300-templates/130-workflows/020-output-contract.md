# Output Contract

This file defines the required output contract for generated decks.

## Output location

Generated slide decks belong in `500-output/`.

Use one subfolder per deck.

Example:

```
500-output/
└─ project-update-q3/
   ├─ slide0100.html
   ├─ slide0200.html
   ├─ slide0300.html
   └─ deck-context.md
```

Do not place long-lived generated decks directly at the root of `500-output/` unless the user explicitly asks for a flat output.

## Required deck files

Every generated deck should usually include:

- `slide0100.html`, `slide0200.html`, `slide0300.html`, ...
- `deck-context.md`

Optional:

- supporting local assets stored in a deck-local subfolder such as `assets/`

## Slide naming

- Use zero-padded 4-digit numbers: `slide0100.html`, `slide0200.html`, `slide0300.html`, and so on.
- This ensures consistent sorting in all file browsers and tools, even when decks grow beyond 999 slides.
- Reserve gaps for inserts. For example, place a new framing slide between `slide0100.html` and `slide0200.html` at `slide0110.html` or `slide0150.html`.
- Never renumber the whole deck merely to insert a slide. Stable filenames preserve the intended viewer and PDF order, reduce noisy diffs, and make future edits safe.
- Keep the sequence numeric and strictly increasing. Record intentional additions in `deck-context.md`.

## Slide contract

Each slide must be a standalone HTML document.

Each slide should include:

- `<!DOCTYPE html>`
- `<html lang="...">`
- charset and viewport metadata
- a meaningful `<title>`
- inline token definitions
- inline CSS
- slide markup
- optional `<aside class="notes">`

When PDF export is expected, each slide should also include print-friendly sizing and exact colour rendering hints, for
example:

```css
@page {
  size: 16in 9in;
  margin: 0;
}

html,
body {
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```

## Theme and token contract

Each deck should use one clear theme strategy:

1. default light token pack
2. default dark token pack
3. deck-specific custom token pack

A custom token pack may be created from user-provided inspiration such as:

- company or brand reference
- screenshot
- URL or online style reference
- existing slide or deck
- mood words
- explicit hex values
- industry or audience context

Regardless of source, all theme values must be mapped into the canonical token contract before slide generation.

Slides and components should consume tokens rather than random hardcoded colours.

## Standalone theme rule

By default, custom token values should be embedded inline in every standalone slide.

Do not create a shared deck-level CSS file unless the user explicitly asks for that structure.

This keeps each slide portable, editable, and compatible with the local viewer.

## Images and libraries

Standalone slides are preferred.
Embed images and external libraries directly in the slide when possible, for maximum portability.

```html
<body>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
    mermaid.initialize({ startOnLoad: true });
  </script>
</body>
```

- This approach helps keep slides portable when they are moved or shared, as long as the CDN is accessible.
- Document the external dependency in `deck-context.md`.

## Optional PDF export

PDF export is allowed as an optional toolchain outside normal viewer use.

Recommended command:

```bash
python3 600-tools/export_pdf.py 500-output/<deck-name> --out 500-output/<deck-name>.pdf
```

This does not change the viewer runtime contract. Opening and presenting `100-viewer.html` must remain dependency-free.

## Deck consistency rules

Within one deck:

- keep one primary theme direction unless the user asks otherwise
- reuse a small set of layouts rather than changing layout on every slide
- keep typography, spacing, and card treatments consistent
- keep token values consistent across slides
- prefer content clarity over decorative density

## Default generation assumptions

Unless the user says otherwise:

- create a deck subfolder inside `500-output/`
- use standalone HTML slides
- embed all required CSS and token values inside each slide
- use `300-templates/100-basic.html` as the base scaffold
- choose layouts from `300-templates/120-layouts/010-layout-catalog.md`
- use the default light or dark token pack if no visual direction is provided
- create a custom token pack if the user provides brand, mood, screenshot, URL, existing deck, or hex colour inspiration
- write a `deck-context.md` file alongside the slides

## Update behavior

When updating an existing deck:

- preserve existing numbering when practical
- edit in place when only small changes are needed
- add new slides by extending the sequence
- preserve the existing token strategy unless a theme change is requested
- if the theme changes, update token values consistently across affected slides
- update `deck-context.md` to record why changes were made
