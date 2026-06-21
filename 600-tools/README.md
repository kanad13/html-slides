# Tooling Guide

`600-tools/` contains optional scripts for maintaining this repo and exporting slides. These tools are not required for
normal viewer use.

## Scripts

- `check_viewer.mjs` - extracts and syntax-checks the inline viewer JavaScript in `100-viewer.html`.
- `validate_deck.py` - validates standalone slide decks against the output contract.
- `smoke_viewer.py` - runs a Playwright smoke test against the viewer and demo deck.
- `run_checks.py` - runs the standard local and CI checks.
- `export_pdf.py` - exports standalone HTML slides to a single PDF.

## Requirements

- `requirements/pdf.txt` - dependencies needed only for PDF export.
- `requirements/dev.txt` - development dependencies, including the PDF dependencies and browser smoke-test dependencies.

Use `requirements/pdf.txt` when you only need export. Use `requirements/dev.txt` when you are changing the viewer,
templates, tests, tools, or CI.

## Standard Commands

```bash
python3 600-tools/run_checks.py
```

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/dev.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python 600-tools/run_checks.py --browser
```

```bash
.venv/bin/python 600-tools/export_pdf.py 200-demos --out demo.pdf
```

Decks use insertion-safe numeric filenames beginning with `slide100.html`, then `slide200.html`, `slide300.html`, and so on. Use available values such as `slide110.html` or `slide150.html` for inserted material so PDF order stays correct without renumbering existing slides. Validate the numeric sequence with:

```bash
python3 600-tools/validate_deck.py 500-output/my-deck
```

Keep new required checks inside `run_checks.py` so local development and CI run the same suite.
