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
- If selected slides reference deck-local assets, map those selected assets to object URLs in memory rather than reading
  directly from arbitrary local paths.
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
- Use `300-templates/110-systems/100-light-default.html` and `300-templates/110-systems/110-dark-default.html` as the two default complete token packs.
- Use `300-templates/110-systems/020-theme-intake-and-tokenization.md` when a user provides brand, company, screenshot, URL, mood, existing deck, industry, or hex colour inspiration.
- Use `300-templates/130-workflows/` for deck creation, output, narrative arcs, and maintenance context.

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
- Use zero-padded 4-digit slide names: `slide0100.html`, `slide0200.html`, `slide0300.html`, and so on.
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
- External rendering libraries (such as Mermaid or Chart.js) may be embedded via CDN if documented in `deck-context.md`. This keeps slides portable when moved or shared.
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
- Keep `150-docs/` for human-facing docs. Number docs in intended reading order and keep
  `150-docs/README.md` as the guide into that folder.
- Keep `600-tools/` for optional repository tooling, checks, and PDF export. Normal viewer use must not depend on this
  folder.
- Keep Python requirement files under `600-tools/requirements/` so root-level files stay focused on primary repo entry
  points.
- If viewer behavior changes, update `README.md` in the same change.
- If template, token, workflow, or output behavior changes, update the relevant files under `300-templates/` and update `README.md` when the user-facing behavior changes.
- If a feature changes, update or add the relevant automated checks in the same change. Do not leave tests for a later
  cleanup pass.

## Testing Expectations

Before considering a viewer change done:

- Run a JavaScript syntax check by extracting the inline script from `100-viewer.html`.
- Run `git diff --check`.
- Run `python3 600-tools/run_checks.py`.
- Open the viewer in a browser and inspect the landing page.
- For UI changes, check both light and dark viewer themes.
- If deck behavior changes, test with a folder of at least two `.html` slides and one slide with `<aside class="notes">`.
- Run `python3 600-tools/run_checks.py --browser` when Playwright development dependencies are installed.

Before considering a template or generated-deck change done:

- Check that generated slides are standalone HTML files.
- Check that token names follow `300-templates/110-systems/010-token-reference.md`.
- Check that custom visual inspiration has been converted into tokens, not scattered as ad hoc component colours.
- Check that important text is readable on the selected background.
- Check that semantic and chart colours remain understandable.
- Check that `deck-context.md` records theme, narrative, and update decisions.
- Check that output follows `300-templates/130-workflows/020-output-contract.md`.
- Run `python3 600-tools/validate_deck.py <deck-folder>` when practical.

Before considering a tooling, PDF export, or CI change done:

- Update `600-tools/README.md` or `150-docs/130-development-and-tests.md` if commands, dependencies, or responsibilities
  change.
- Keep `.github/workflows/ci.yml` aligned with `python3 600-tools/run_checks.py --browser`; add required checks to
  `600-tools/run_checks.py` first so local and CI behavior stay consistent.
- For PDF export changes, export `200-demos` and verify the result is full-bleed with the expected page count.

## Things To Avoid

- React, Vue, Svelte, Astro, Vite, Webpack, or similar tooling.
- PDF export/conversion inside the normal viewer runtime. Optional offline export tooling may exist separately.
- Server-side slide generation.
- WebSocket presenter sync.
- Service workers unless there is a very strong reason and the offline/file behavior is preserved.
- Shared CSS requirements for generated decks unless explicitly requested by the user.
- Random hardcoded colour values in slide components.
