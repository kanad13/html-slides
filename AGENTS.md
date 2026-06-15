# Development Guardrails

This repo has two related but separate responsibilities:

1. **`100-viewer.html`** is a portable, single-file HTML presentation viewer.
2. **`300-templates/`** is the slide-authoring and AI-generation reference for creating standalone HTML slide decks.

Future changes should preserve both contracts:

- the viewer remains local-first, dependency-free, and usable by opening `100-viewer.html` directly in a browser;
- generated slides remain standalone HTML files with all required markup, token values, and CSS embedded inline by default.

## Non-Negotiable Constraints

- `100-viewer.html` must remain usable by opening it directly in a browser.
- Do not require Python, Node, npm, a web server, a package manager, or a browser extension for normal viewer use.
- Do not add external runtime dependencies, CDN scripts, web fonts, tracking, analytics, or remote assets.
- Do not upload, sync, or transmit selected slide files anywhere.
- Keep slide files isolated in iframes so one slide cannot break the viewer or another slide.
- Keep the folder/file picker flow. Static HTML cannot scan arbitrary local folders without user selection.
- Keep the viewer useful offline.
- Generated decks should remain usable as local standalone HTML files.
- Do not introduce a shared CSS dependency for generated decks unless the user explicitly asks for that structure.

## Viewer Runtime Contract

- `100-viewer.html` contains all runtime code: markup, CSS, and JavaScript.
- The viewer should stay theme-agnostic. It should not need to understand whether a slide uses the default light token pack, the default dark token pack, or a deck-specific custom token pack.
- The viewer should load selected `.html` or `.htm` files, sort them naturally, isolate them in iframes, and extract lightweight metadata such as title and speaker notes.
- The viewer theme toggle affects only the viewer UI chrome, not the slide contents inside iframes.
- Do not make the viewer dependent on files inside `300-templates/` or `500-output/`.

## Browser API Choices

- Use browser-native APIs only.
- Folder selection should continue to use `<input type="file" webkitdirectory directory multiple>`.
- File fallback should continue to use a plain multi-file input.
- Use `URL.createObjectURL(file)` for selected slide files and revoke old URLs when replacing a deck.
- Use `localStorage` only for lightweight preferences such as viewer theme and last slide number.
- Treat drag-and-drop folder loading as a browser-dependent enhancement. Picker buttons must remain the reliable fallback.

## UI/UX Principles

- The viewer should feel like a presentation tool, not a file browser.
- Important modes need visible buttons and matching keyboard shortcuts.
- Avoid hidden-only interactions unless they are convenience extras.
- Notes, sidebars, and overview should not trap basic slide navigation.
- Large decks must remain usable; avoid dot-only navigation.
- Keep the first screen clear for non-technical users.
- Preserve an obvious path back to choosing another deck.

## Template and Slide Authoring Contract

- `300-templates/` defines the authoring system, not viewer runtime behavior.
- Use `300-templates/100-basic.html` as the default standalone slide scaffold.
- Use `300-templates/110-systems/010-token-reference.md` as the canonical token contract.
- Use `300-templates/110-systems/110-light-default.html` and `300-templates/110-systems/110-dark-default.html` as the two default complete token packs.
- Use `300-templates/110-systems/020-theme-intake-and-tokenization.md` when a user provides brand, company, screenshot, URL, mood, existing deck, industry, or hex colour inspiration.
- Use `300-templates/130-workflows/` for deck creation, output, narrative arts, and maintenance context.

## Token and Theme Rules

The framework supports three theme paths:

1. default light token pack;
2. default dark token pack;
3. deck-specific custom token pack.

Custom token packs may be inspired by:

- company or brand references;
- screenshots or visual examples;
- URLs or online style references;
- existing slides or decks;
- user-provided hex values;
- mood words or visual adjectives;
- industry, audience, or event context.

Rules:

- External inspiration is allowed. Direct external styling is not.
- All visual inspiration must be converted into the canonical token contract before slide generation.
- Layouts and slide components should consume tokens rather than random hardcoded colours.
- Hardcoded colour values belong inside token definition sections, except for documented browser/platform reasons.
- Derived visual treatments such as gradients, transparency overlays, and colour-alpha() are acceptable when composed from tokens.
- Semantic colours must remain understandable as status indicators.
- Chart colours must remain visually distinct and readable on the selected background.
- If user-provided colours create readability problems, adjust derived token values and document the adjustment in `deck-context.md`.

## Generated Deck Output Rules

- Generated decks belong in `500-output/`, preferably one subfolder per deck.
- Use zero-padded slide names such as `slide01.html`, `slide02.html`, `slide03.html`.
- Each slide must be a complete standalone HTML document.
- Each slide should include:
  - `<!DOCTYPE html>`;
  - `<html lang="...">`;
  - charset and viewport metadata;
  - a meaningful `<title>`;
  - inline token definitions;
  - inline CSS;
  - slide markup;
  - optional `<aside class="notes">`.
- By default, embed all token values and CSS inside each slide.
- Do not create or require a deck-level shared CSS file unless the user explicitly asks for it.
- Every generated deck should usually include `deck-context.md`.

## Deck Context Rules

`deck-context.md` preserves enough context for a future AI agent or human to update the deck without rediscovering the original reasoning.

When creating or materially updating a deck, record:

- deck purpose and intended audience;
- source materials and assumptions;
- selected deck arc and narrative choices;
- theme path and theme source;
- custom token strategy, if any;
- important source colours or references;
- readability or contrast adjustments;
- semantic and chart colour rationale;
- layouts used and why;
- slide map;
- update notes and unresolved questions.

If visual style, token values, or theme source changes, update the theme brief in `deck-context.md` in the same change.

## Code Organization

- Keep `100-viewer.html` understandable to someone editing plain HTML/CSS/JS.
- Use section comments in `100-viewer.html` so future edits can find the right area quickly.
- Prefer small, named functions over large anonymous blocks.
- Avoid clever abstractions.
- If viewer behavior changes, update `README.md` in the same change.
- If template, token, workflow, or output behavior changes, update the relevant files under `300-templates/` and update `README.md` when the user-facing behavior changes.

## Testing Expectations

Before considering a viewer change done:

- Run a JavaScript syntax check by extracting the inline script from `100-viewer.html`.
- Run `git diff --check`.
- Open the viewer in a browser and inspect the landing page.
- for UI changes, check both light and dark viewer themes.
- If deck behavior changes, test with a folder of at least two `.html` slides and one slide with `<aside class="notes">`.

Before considering a template or generated-deck change done:

- Check that generated slides are standalone HTML files.
- Check that token names follow `300-templates/110-systems/010-token-reference.md`.
- Check that custom visual inspiration has been converted into tokens, not scattered as ad hoc component colours.
- Check that important text is readable on the selected background.
- Check that semantic and chart colours remain understandable.
- Check that `deck-context.md` records theme, narrative, and update decisions.
- Check that output follows `300-templates/130-workflows/020-output-contract.md`.

## Things To Avoid

- React, Vue, Svelte, Astro, Vite, Webpack, or similar tooling.
- Markdown-to-slide pipelines inside this repo.
- PDF export/conversion.
- Server-side slide generation.
- WebSocket presenter sync.
- Service workers unless there is a very strong reason and the offline/file behavior is preserved.
- External runtime assets, fonts, scripts, analytics, or tracking.
- Shared CSS requirements for generated decks unless explicitly requested by the user.
- Random hardcoded colour values in slide components.
- Claiming official brand compliance unless the user provided official brand guidance.
