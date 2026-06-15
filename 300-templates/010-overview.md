# HTML Slide Template Library

This folder is the slide-authoring and slide-generation reference for this repo.

It exists so an AI coding agent or a human can quickly build, update, and maintain standalone HTML slide decks.

The system supports three theme paths:

1. Use the default light token pack.
2. Use the default dark token pack.
3. Create a deck-specific custom token pack from user-provided inspiration, such as mood words, company references, screenshots, URLs, existing decks, or hex values.

In all cases, final slides should use the canonical token contract.

## Start here

- Read `020-system-guide.md` for the system rules and authoring priorities.
- Use `100-basic.html` as the default standalone slide scaffold.
- Read `110-systems/010-token-reference.md` for the canonical token contract.
- Use `110-systems/100-light-default.html` or `110-systems/110-dark-default.html` when no custom theme is needed.
- Use `110-systems/020-theme-intake-and-tokenization.md` when the user gives brand, mood, screenshot, URL, or colour inspiration.
- Browse `120-layouts/010-layout-catalog.md` for structural options.
- Use `130-workflows/010-ai-workflow.md` for slide creation and maintenance workflow.

## Folder map

```text
300-templates/
├── 010-overview.md
├── 020-system-guide.md
├── 100-basic.html
├── 110-systems/
│   ├── 010-token-reference.md
│   ├── 020-theme-intake-and-tokenization.md
│   ├── 100-light-default.html
│   └── 110-dark-default.html
├── 120-layouts/
│   └── 010-layout-catalog.md
└── 130-workflows/
    ├── 010-ai-workflow.md
    ├── 020-output-contract.md
    ├── 030-deck-arcs.md
    └── 040-maintenance-context.md
```

## Default workflow

- Clarify the audience, goal, and raw input.
- Choose a deck arc from `130-workflows/030-deck-arcs.md`.
- Choose a theme path:
  - default light token pack,
  - default dark token pack,
  - or custom token pack created from user inspiration.
- If using external inspiration, convert it into the canonical token contract before creating slides.
- Pick a small set of layout shapes from the catalog.
- Build the actual slides as standalone HTML files.
- Embed all token values and CSS inside each standalone slide unless the user explicitly asks for a different structure.
- Output the deck in `500-output/` together with `deck-context.md`.
- On later revisions, update both the slides and the context sidecar.
