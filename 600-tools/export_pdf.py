#!/usr/bin/env python3
"""Export a folder of standalone HTML slides to a single PDF."""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

try:
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover - exercised by users without PDF deps
    print("Playwright is not installed. Run: python3 -m pip install -r 600-tools/requirements/pdf.txt", file=sys.stderr)
    raise SystemExit(2)

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:  # pragma: no cover - exercised by users without PDF deps
    print("pypdf is not installed. Run: python3 -m pip install -r 600-tools/requirements/pdf.txt", file=sys.stderr)
    raise SystemExit(2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", type=Path, help="Directory containing slideNN.html files")
    parser.add_argument("--out", type=Path, required=True, help="Output PDF path")
    parser.add_argument("--width", type=int, default=1536, help="Browser viewport width in CSS pixels")
    parser.add_argument("--height", type=int, default=864, help="Browser viewport height in CSS pixels")
    parser.add_argument("--paper-width", default="16in", help="PDF page width with CSS unit")
    parser.add_argument("--paper-height", default="9in", help="PDF page height with CSS unit")
    parser.add_argument("--settle-ms", type=int, default=250, help="Wait after load before printing each slide")
    parser.add_argument("--headed", action="store_true", help="Run with a visible browser")
    args = parser.parse_args()
    try:
        args.paper_width = css_dimension(args.paper_width)
        args.paper_height = css_dimension(args.paper_height)
    except ValueError as error:
        parser.error(str(error))

    deck_dir = args.deck.resolve()
    slides = sorted(deck_dir.glob("slide*.html"), key=natural_key)
    if not slides:
        print(f"No slide*.html files found in {deck_dir}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="html-deck-pdf-") as tmp:
        tmp_dir = Path(tmp)
        rendered = render_slides(slides, tmp_dir, args)
        merge_pdfs(rendered, args.out)

    print(f"exported {len(slides)} slides to {args.out}")
    return 0


def render_slides(slides: list[Path], tmp_dir: Path, args: argparse.Namespace) -> list[Path]:
    rendered: list[Path] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not args.headed)
        page = browser.new_page(viewport={"width": args.width, "height": args.height}, device_scale_factor=1)
        for index, slide in enumerate(slides, start=1):
            page.goto(slide.resolve().as_uri(), wait_until="load")
            try:
                page.wait_for_load_state("networkidle", timeout=1500)
            except PlaywrightTimeoutError:
                pass
            page.wait_for_timeout(args.settle_ms)
            page.emulate_media(media="print")
            page.add_style_tag(content=f"""
              @page {{ size: {args.paper_width} {args.paper_height}; margin: 0; }}
              html, body {{ width: {args.paper_width} !important; height: {args.paper_height} !important; margin: 0; overflow: hidden !important; }}
              .slide {{ width: {args.paper_width} !important; height: {args.paper_height} !important; margin: 0; overflow: hidden !important; }}
              .standard {{ grid-template-rows: 4.15rem minmax(0, 1fr) !important; }}
              html, body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
            """)
            out = tmp_dir / f"slide-{index:04d}.pdf"
            page.pdf(
                path=str(out),
                width=args.paper_width,
                height=args.paper_height,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                print_background=True,
                prefer_css_page_size=True,
                display_header_footer=False,
            )
            rendered.append(out)
        browser.close()
    return rendered


def merge_pdfs(paths: list[Path], output: Path) -> None:
    writer = PdfWriter()
    for path in paths:
        reader = PdfReader(str(path))
        overflow = reader.pages[1:]
        if any((page.extract_text() or "").strip() for page in overflow):
            raise RuntimeError(f"{path.name} produced content beyond its first PDF page")
        writer.add_page(reader.pages[0])
    with output.open("wb") as handle:
        writer.write(handle)


def natural_key(path: Path) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def css_dimension(value: str) -> str:
    value = str(value).strip()
    if not re.fullmatch(r"(?:\d+(?:\.\d+)?|\.\d+)(?:px|in|cm|mm)", value):
        raise ValueError(f"invalid CSS dimension: {value!r}")
    return value


if __name__ == "__main__":
    raise SystemExit(main())
