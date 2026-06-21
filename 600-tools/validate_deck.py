#!/usr/bin/env python3
"""Validate standalone HTML deck output against this repo's basic contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_TOKENS = [
    "--surface-0",
    "--surface-1",
    "--surface-2",
    "--text-primary",
    "--text-secondary",
    "--border",
    "--brand-primary",
    "--brand-secondary",
    "--brand-tertiary",
    "--brand-quaternary",
    "--success",
    "--warning",
    "--danger",
    "--info",
    "--chart-1",
    "--chart-2",
    "--chart-3",
    "--chart-4",
    "--chart-5",
    "--chart-6",
    "--space-1",
    "--space-2",
    "--space-3",
    "--space-4",
    "--space-5",
    "--space-6",
    "--space-7",
    "--space-8",
    "--radius-sm",
    "--radius-md",
    "--radius-lg",
    "--radius-xl",
    "--shadow-soft",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", type=Path, help="Deck directory containing slideNN.html files")
    parser.add_argument("--require-notes", action="store_true", help="Require every slide to include aside.notes")
    parser.add_argument("--allow-shared-css", action="store_true", help="Allow linked stylesheets")
    parser.add_argument("--no-context", action="store_true", help="Do not require deck-context.md")
    args = parser.parse_args()

    errors: list[str] = []
    deck_dir = args.deck
    if not deck_dir.is_dir():
        return fail([f"{deck_dir} is not a directory"])

    slides = sorted(deck_dir.glob("slide*.html"), key=natural_key)
    if not slides:
        return fail([f"{deck_dir} does not contain slide*.html files"])

    actual = [slide.name for slide in slides]
    validate_spaced_numbering(slides, errors)

    if not args.no_context and not (deck_dir / "deck-context.md").is_file():
        errors.append("deck-context.md is required beside the slide files")

    for slide in slides:
        errors.extend(validate_slide(slide, args.require_notes, args.allow_shared_css))

    if errors:
        return fail(errors)

    print(f"deck validation passed: {deck_dir} ({len(slides)} slides)")
    return 0


def validate_slide(slide: Path, require_notes: bool, allow_shared_css: bool) -> list[str]:
    html = slide.read_text(encoding="utf-8")
    errors: list[str] = []

    checks = [
        (r"^\s*<!DOCTYPE html>", "missing <!DOCTYPE html>"),
        (r"<html\s+[^>]*lang=", "missing <html lang=...>"),
        (r"<meta\s+[^>]*charset=", "missing charset metadata"),
        (r"<meta\s+[^>]*name=['\"]viewport['\"]", "missing viewport metadata"),
        (r"<title>\s*[^<\s][^<]*</title>", "missing meaningful <title>"),
        (r"<style[\s>]", "missing inline <style>"),
        (r":root\s*{", "missing :root token section"),
    ]
    for pattern, message in checks:
        if not re.search(pattern, html, re.IGNORECASE | re.MULTILINE):
            errors.append(f"{slide}: {message}")

    if require_notes and not re.search(r"<aside\s+[^>]*class=['\"][^'\"]*\bnotes\b", html, re.IGNORECASE):
        errors.append(f"{slide}: missing <aside class=\"notes\">")

    for token in REQUIRED_TOKENS:
        if token not in html:
            errors.append(f"{slide}: missing token {token}")

    if not allow_shared_css and re.search(r"<link\s+[^>]*rel=['\"]stylesheet['\"]", html, re.IGNORECASE):
        errors.append(f"{slide}: linked stylesheets are not allowed by default")

    remote_patterns = [
        r"\b(?:src|href|poster)=['\"]https?://",
        r"@import\s+(?:url\()?['\"]?https?://",
        r"url\(\s*['\"]?https?://",
    ]
    for pattern in remote_patterns:
        if re.search(pattern, html, re.IGNORECASE):
            errors.append(f"{slide}: remote runtime reference found")
            break

    outside_root = remove_root_blocks(html)
    if re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(", outside_root):
        errors.append(f"{slide}: raw colour value found outside :root token definitions")

    return errors


def remove_root_blocks(html: str) -> str:
    return re.sub(r":root\s*{[^{}]*(?:{[^{}]*}[^{}]*)*}", "", html, flags=re.IGNORECASE | re.DOTALL)


def natural_key(path: Path) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def validate_spaced_numbering(slides: list[Path], errors: list[str]) -> None:
    """Accept deliberately spaced integer slide names while retaining deterministic order."""
    numbers: list[int] = []
    for slide in slides:
        match = re.fullmatch(r"slide(\d+)\.html", slide.name, re.IGNORECASE)
        if not match:
            errors.append(f"{slide.name}: expected a numeric slide filename such as slide100.html")
            continue
        numbers.append(int(match.group(1)))
    # Existing demo decks may retain the legacy contiguous format. New deck instructions use slide100.html onward.
    if numbers and numbers[0] != 100:
        legacy_expected = list(range(1, len(numbers) + 1))
        if numbers != legacy_expected:
            errors.append("slide numbering must start at slide100.html, or use the legacy contiguous sequence")
    if len(numbers) == len(slides) and any(next_num <= current for current, next_num in zip(numbers, numbers[1:])):
        errors.append("slide numbers must increase")


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
