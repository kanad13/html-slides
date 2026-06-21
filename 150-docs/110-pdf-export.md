# PDF Export

PDF export converts a folder of standalone HTML slides into one full-bleed 16:9 PDF.

The exporter uses Playwright and Chromium because browser rendering gives the closest match to what the viewer presents.
This is an optional local toolchain; normal viewer use still requires no Python, Node, server, or build step.

## Setup

From the repo root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/pdf.txt
.venv/bin/python -m playwright install chromium
```

## Export

```bash
.venv/bin/python 600-tools/export_pdf.py 200-demos --out demo.pdf
```

For generated decks:

```bash
.venv/bin/python 600-tools/export_pdf.py 500-output/my-deck --out 500-output/my-deck.pdf
```

## Options

- `--out <file>` - output PDF path.
- `--width 1536` - browser viewport width in CSS pixels.
- `--height 864` - browser viewport height in CSS pixels.
- `--paper-width 16in` - PDF page width.
- `--paper-height 9in` - PDF page height.
- `--settle-ms 250` - wait after each slide loads before printing.
- `--headed` - run Chromium visibly for debugging.

## Full-Bleed Output

The default export target is `16in x 9in` with zero margins. Slides should include:

```css
@page {
  size: 16in 9in;
  margin: 0;
}

html,
body {
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```

If a PDF shows a white border or an unexpected second page, check that:

- the exporter is using matching paper dimensions;
- the slide uses full-page layout such as `width: 100vw` and `height: 100vh`;
- the slide body has no default margin;
- the slide height is constrained to the PDF page size during printing;
- the PDF viewer is not adding its own page background or preview padding.

## What Export Does Not Do

The exporter does not upload files, convert slides through a server, or require the viewer to change its runtime model.
It renders selected local slide files in Chromium and merges the printed pages.
