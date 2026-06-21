# HTML Deck Studio

**Portable presentations. No accounts. No servers. Files stay local.**

HTML Deck Studio is a local-first presentation system for people who want to present using HTML files instead of PowerPoint or some other tool.

In this repository, you'll find:

- A presentation viewer that allows you to present HTML slides and provides navigation, notes, overview, and fullscreen.
- An AI-assisted workflow for generating and updating HTML slide decks using a stable template system and tokenized themes.
- A PDF export tool that converts your HTML slides available for sharing or printing.

The best part: No installation, no build step, no lock-in. All content belongs to you, can be versioned in Git, and finely controlled with the full power of HTML, CSS, and JavaScript. You get to embeed Mermaid charts, D3 visualizations, or any web-native content. The viewer handles the presentation layer while you focus on crafting your narrative.

![](./400-assets/100.png)

## Three Ways to Use It

### 1. Just Present a Deck

Open [HTML Slides Viewer](./100-viewer.html), pick a folder of `.html` slides, and go. No installation, no internet, no dependencies. Full navigation, notes, overview, and fullscreen. Works on any machine, any time.

### 2. Generate Decks with AI

Give a coding agent the [Templates Folder](./300-templates/) as context. It creates complete standalone HTML slides with embedded tokens and CSS. Theme system included. Update your deck by regenerating slides.

### 3. Export to PDF

Convert your slide folder to a full-bleed 16:9 PDF for sharing or printing. Optional Python toolchain. Same files, production output.

## Why This Exists

- **Power and flexibility of HTML:** Create slides with any web content, custom layouts, and interactive features. You're not limited by a tool's capabilities.
- **AI-friendly:** The template system gives coding agents a stable structure for creating and updating decks. Your slides stay readable, diffable source.
- **Portable by design:** Each slide is a complete standalone HTML file with its own markup, CSS, and theme tokens. Move, share, or version them like any text file.

## Quick Start

### Present a Deck

1. Open [HTML Slides Viewer](./100-viewer.html) in a modern browser.
2. Click **Choose Folder**.
3. Select a folder containing `slide0100.html`, `slide0200.html`, and so on.
4. Present with arrow keys, toolbar buttons, overview mode, notes, or fullscreen.

### Generate a Deck With AI

Use the authoring system in [Templates Folder](./300-templates/) when asking an AI coding agent to create or update a deck.

Recommended starting points:

- [010-overview.md](./300-templates/010-overview.md)
- [020-system-guide.md](./300-templates/020-system-guide.md)
- [010-ai-workflow.md](./300-templates/130-workflows/010-ai-workflow.md)
- [020-output-contract.md](./300-templates/130-workflows/020-output-contract.md)

Generated decks should usually go in `500-output/<deck-name>/` with standalone slide files and a `deck-context.md`.

Name slide files with zero-padded 4-digit numbers: start at `slide0100.html`, then use `slide0200.html`, `slide0300.html`, and so on.

### Export a Deck to PDF

PDF export is intentionally separate from normal viewer use so the viewer remains dependency-free.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/pdf.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python 600-tools/export_pdf.py <deck-folder> --out output.pdf
```

The exporter renders each slide in Chromium and merges the pages into one full-bleed 16:9 PDF.

## Security and Privacy

The viewer is designed for local-first use.

- Selected files are read by the browser only after the user chooses them.
- Slide and asset files are represented with temporary object URLs.
- Old object URLs are revoked when a new deck is loaded.
- Slides render in sandboxed iframes so slide code is separated from the viewer chrome.
- The viewer does not upload selected slide files.

Important boundary: arbitrary HTML slides can still contain remote references. Use the validation tools and avoid remote runtime assets when you need fully offline or no-network behavior.

Read more in [120-security-model.md](./150-docs/120-security-model.md).

## Repository Map

Core folders:

- [100-viewer.html](./100-viewer.html) - local presentation viewer.
- [150-docs/](./150-docs/) - user guide, PDF export guide, security model, and development/testing guide.
- [200-demos/](./200-demos/) - reference demo deck built to the current slide contract.
- [300-templates/](./300-templates/) - AI authoring system, token references, layout catalog, and output rules.
- [500-output/](./500-output/) - recommended location for generated decks.
- [600-tools/](./600-tools/) - validation, smoke tests, CI helpers, and PDF export tooling.

## Documentation

Start with [150-docs/README.md](./150-docs/README.md).

- [100-user-guide.md](./150-docs/100-user-guide.md) - how to open, present, and navigate decks.
- [110-pdf-export.md](./150-docs/110-pdf-export.md) - setup, export commands, options, and troubleshooting.
- [120-security-model.md](./150-docs/120-security-model.md) - privacy boundaries and iframe/file handling.
- [130-development-and-tests.md](./150-docs/130-development-and-tests.md) - checks, CI, and maintenance rules.

The [300-templates/](./300-templates/) folder is deeper reference material for AI-assisted deck creation.

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

The GitHub Actions workflow in [.github/workflows/ci.yml](./.github/workflows/ci.yml) runs the same browser-enabled check suite on push and pull request.
