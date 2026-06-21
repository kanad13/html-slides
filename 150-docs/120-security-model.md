# Security and Privacy Model

HTML Deck Studio is local-first. The viewer is designed to present user-selected files without uploading them.

## File Access

The viewer uses browser-native file inputs:

- folder input for deck folders;
- multi-file input as a fallback;
- drag-and-drop as a browser-dependent enhancement.

The browser grants access only to files the user selects. Static HTML cannot scan arbitrary local folders without that selection.

## Object URLs

Selected slide and asset files are represented with `URL.createObjectURL(file)`. Old object URLs are revoked when a new deck replaces the current one.

This keeps file handling in the browser tab and avoids direct arbitrary local path access.

## Iframe Isolation

Slides render in sandboxed iframes with `allow-scripts`.

This means:

- slide JavaScript can run inside the slide frame;
- slide content is separated from the viewer chrome;
- the viewer does not grant same-origin access to selected slide frames.

The viewer extracts lightweight metadata such as titles and notes with `DOMParser` before creating the iframe URL. That metadata extraction does not execute slide scripts.

## Network Boundary

The viewer does not upload selected files.

However, a slide is HTML. If a slide file contains remote images, fonts, scripts, stylesheets, CSS URLs, or application code that makes network requests, the browser may request those remote resources when the slide renders.

For fully offline or no-network decks:

- avoid remote runtime references;
- keep assets deck-local;
- run `python3 600-tools/validate_deck.py <deck-folder>`;
- review slide HTML before presenting untrusted decks.

## Hosted Viewer Note

A static hosted viewer can still preserve the no-upload file-selection model, but arbitrary uploaded slide HTML needs a stricter policy if the promise is "nothing leaves the browser." Hosted mode is intentionally not implemented in this repo yet.
