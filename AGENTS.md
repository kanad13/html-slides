# Development Guardrails

This project is intentionally a portable, single-file HTML presentation viewer. Future changes should preserve that contract.

## Non-Negotiable Constraints

- `viewer.html` must remain usable by opening it directly in a browser.
- Do not require Python, Node, npm, a web server, a build step, a package manager, or a browser extension for normal use.
- Do not add external runtime dependencies, CDN scripts, web fonts, tracking, analytics, or remote assets.
- Do not upload, sync, or transmit selected slide files anywhere.
- Keep slide files isolated in iframes so one slide cannot break the viewer or another slide.
- Keep the folder/file picker flow. Static HTML cannot scan arbitrary local folders without user selection.
- Keep the viewer useful offline.

## Browser API Choices

- Use browser-native APIs only.
- Folder selection should continue to use `<input type="file" webkitdirectory directory multiple>`.
- File fallback should continue to use a plain multi-file input.
- Use `URL.createObjectURL(file)` for selected slide files and revoke old URLs when replacing a deck.
- Use `localStorage` only for lightweight preferences such as theme and last slide number.

## UI/UX Principles

- The viewer should feel like a presentation tool, not a file browser.
- Important modes need visible buttons and matching keyboard shortcuts.
- Avoid hidden-only interactions unless they are convenience extras.
- Notes, sidebars, and overview should not trap basic slide navigation.
- Large decks must remain usable; avoid dot-only navigation.
- Keep the first screen clear for non-technical users.

## Code Organization

- `viewer.html` contains all runtime code: markup, CSS, and JavaScript.
- Use section comments in `viewer.html` so future edits can find the right area quickly.
- Prefer small, named functions over adding large anonymous blocks.
- Avoid clever abstractions; this file should be understandable to someone editing plain HTML/CSS/JS.
- If behavior changes, update `README.md` in the same change.

## Testing Expectations

Before considering a change done:

- Run a JavaScript syntax check by extracting the inline script from `viewer.html`.
- Run `git diff --check`.
- Open the viewer in a browser and inspect the landing page.
- For UI changes, check both light and dark themes.
- If deck behavior changes, test with a folder of at least two `.html` slides and one slide with `<aside class="notes">`.

## Things To Avoid

- React, Vue, Svelte, Astro, Vite, Webpack, or similar tooling.
- Markdown-to-slide pipelines inside this repo.
- PDF export/conversion.
- Server-side slide generation.
- WebSocket presenter sync.
- Service workers unless there is a very strong reason and the offline/file behavior is preserved.
