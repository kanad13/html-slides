# HTML Deck Studio

HTML Deck Studio is a local-first presentation system built on a simple idea: slides should be portable, standalone HTML files that work anywhere—in a browser, in version control, in PDF, or shared with others. No accounts, no servers, no lock-in.

## The Problem

Most presentation tools make you choose: either you get portability (slides as files) or you get features (cloud editing, rich formatting, AI collaboration). HTML Deck Studio does both. Your slides stay as inspectable, diffable HTML while you get a full presentation experience.

## What You Get

**Three components working together:**

1. **`100-viewer.html`** — Open any folder of `.html` slides and present immediately. No installation, no build step, works offline.
2. **`300-templates/`** — A stable contract for creating slides with AI agents. Token-based theming, consistent layouts, and reusable components.
3. **Optional PDF export** — Turn your slide folder into a print-ready, full-bleed 16:9 PDF using the local Python toolchain.

## Why this exists

- **Local-first and private:** selecting a deck does not upload it.
- **Portable by design:** each slide carries its own markup, tokens, and CSS.
- **AI-ready, not AI-locked:** templates and deck context give coding agents a stable system to extend.
- **Presentation-ready:** the viewer provides navigation, overview, notes, presenter mode, and fullscreen.
- **Shareable:** an optional local toolchain creates a full-bleed PDF without changing normal viewer use.

## Core workflow

1. Create complete HTML slide files, with the flexibility of HTML, CSS, and JavaScript.
2. Present those files together in the browser. Normal use needs no installation, hosting, or internet connection.
3. Optionally, export the deck to PDF for sharing or printing.

## Good fits

- Executive updates, strategy narratives, customer stories, and workshop decks that need polished PDF sharing.
- Sensitive or offline presentations where files must remain on the presenter’s machine.
- Teams that want slides to be inspectable, diffable source files rather than opaque binaries.
- AI-generated or frequently updated decks that need a clear visual and content contract.

## Three Paths

**Just present?** Open `100-viewer.html`, pick your slide folder, and go.

**Generate decks with AI?** Use `300-templates/` to guide your agent. Slides come out as complete HTML with theme tokens baked in.

**Need a PDF?** Use the optional export toolchain. One command, full-bleed output.

## Quick Start

### Present a Deck

1. Open `100-viewer.html` in a modern browser.
2. Click **Choose Folder**.
3. Select a folder containing `slide0100.html`, `slide0200.html`, and so on.
4. Present with arrow keys, toolbar buttons, overview mode, notes, or fullscreen.

If your browser does not support folder picking, use **Choose Files** and select the slide files. If the deck uses local assets such as `assets/chart.png`, choose the full folder so those assets are included.

### Export a Deck to PDF

PDF export is intentionally separate from normal viewer use so the viewer remains dependency-free.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/pdf.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python 600-tools/export_pdf.py 200-demos --out demo.pdf
```

The exporter renders each slide in Chromium and merges the pages into one full-bleed 16:9 PDF.

### Generate a Deck With AI

Use the authoring system in `300-templates/` when asking an AI coding agent to create or update a deck.

Recommended starting points:

- `300-templates/010-overview.md`
- `300-templates/020-system-guide.md`
- `300-templates/130-workflows/010-ai-workflow.md`
- `300-templates/130-workflows/020-output-contract.md`

Generated decks should usually go in `500-output/<deck-name>/` with standalone slide files and a `deck-context.md`.

Name slide files with zero-padded 4-digit numbers: start at `slide0100.html`, then use `slide0200.html`, `slide0300.html`, and so on. Insert future material with an available number such as `slide0110.html`; this preserves PDF order without renaming existing files and ensures consistent sorting even as decks grow.

## Security and Privacy

The viewer is designed for local-first use.

- Selected files are read by the browser only after the user chooses them.
- Slide and asset files are represented with temporary object URLs.
- Old object URLs are revoked when a new deck is loaded.
- Slides render in sandboxed iframes so slide code is separated from the viewer chrome.
- The viewer does not upload selected slide files.

Important boundary: arbitrary HTML slides can still contain remote references. Use the validation tools and avoid remote runtime assets when you need fully offline or no-network behavior.

Read more in `150-docs/120-security-model.md`.

## Repository Map

Core folders:

- `100-viewer.html` - local presentation viewer.
- `150-docs/` - user guide, PDF export guide, security model, and development/testing guide.
- `200-demos/` - reference demo deck built to the current slide contract.
- `300-templates/` - AI authoring system, token references, layout catalog, and output rules.
- `500-output/` - recommended location for generated decks.
- `600-tools/` - validation, smoke tests, CI helpers, and PDF export tooling.

## Documentation

Start with `150-docs/README.md`.

- `150-docs/100-user-guide.md` - how to open, present, and navigate decks.
- `150-docs/110-pdf-export.md` - setup, export commands, options, and troubleshooting.
- `150-docs/120-security-model.md` - privacy boundaries and iframe/file handling.
- `150-docs/130-development-and-tests.md` - checks, CI, and maintenance rules.

The `300-templates/` folder is deeper reference material for AI-assisted deck creation.

## Development Checks

Run the standard checks before considering viewer, demo, template, or tooling changes done:

```bash
python3 600-tools/run_checks.py
```

Run the browser smoke test when the optional development dependencies are installed:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/dev.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python 600-tools/run_checks.py --browser
```

The GitHub Actions workflow in `.github/workflows/ci.yml` runs the same browser-enabled check suite on push and pull request.

## Design Principles

- Normal viewer use must stay dependency-free.
- Generated slides should be standalone HTML by default.
- Visual style should be tokenized, not scattered across components.
- PDF export can use an optional local toolchain because accurate HTML/CSS rendering needs a browser engine.
- Tests and docs should change with features, not after features.
