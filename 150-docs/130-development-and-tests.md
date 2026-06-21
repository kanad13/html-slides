# Development and Tests

This repo has two primary contracts:

- `100-viewer.html` is a single-file local viewer.
- `300-templates/` defines the AI slide-generation system.

Changes should keep those contracts separate.

## Standard Checks

Run this before considering a change done:

```bash
python3 600-tools/run_checks.py
```

This runs:

- viewer static checks;
- demo deck validation;
- `git diff --check`.

Run the browser-enabled suite when Playwright is installed:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/dev.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python 600-tools/run_checks.py --browser
```

## What to Update With Each Feature

- Viewer behavior change: update or add viewer checks, then run `python3 600-tools/run_checks.py --browser`.
- Generated deck contract change: update `600-tools/validate_deck.py`, relevant `300-templates/` docs, and demo deck if needed.
- PDF export change: run `600-tools/export_pdf.py` on `200-demos` and inspect page size/full-bleed output.
- Documentation change for user-facing behavior: update `README.md` and the relevant file in `150-docs/`.
- Template or workflow change: update the relevant file in `300-templates/` and keep `deck-context.md` expectations aligned.

## CI

`.github/workflows/ci.yml` runs on push and pull request.

It currently:

1. checks out the repo;
2. installs Node and Python;
3. installs development requirements from `600-tools/requirements/dev.txt`;
4. installs Chromium for Playwright;
5. runs `python 600-tools/run_checks.py --browser`.

Keep CI aligned with `600-tools/run_checks.py`. If a new required check is added locally, add it to `run_checks.py` first so CI picks it up from the same command.

## Tooling Layout

`600-tools/` contains repo-maintenance and export tooling:

- `check_viewer.mjs` - static viewer checks.
- `validate_deck.py` - generated deck validator.
- `smoke_viewer.py` - Playwright browser smoke test for the viewer and demo deck.
- `run_checks.py` - standard local/CI check runner.
- `export_pdf.py` - optional PDF exporter.
- `requirements/` - Python dependency sets for dev and PDF export.

Normal viewer use must not depend on these tools.
