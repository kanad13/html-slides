# Slide Deck Viewer

A single, dependency-free `viewer.html` file that turns any folder of standalone
HTML files into a swipeable slide deck. No server, no Node, no Python, no build
step — just open `viewer.html` in a browser.

## Repo structure

```
slide-deck-viewer/
├── viewer.html        # The viewer app — the only file you need to "run"
├── README.md
└── slides/            # Example deck (replace/edit/add/remove freely)
    ├── slide01.html
    ├── slide02.html
    └── slide03.html
```

You can rename, delete, or have multiple `slides*/` folders — the folder name
doesn't matter, since you pick it interactively each time.

## How it works

1. Open `viewer.html` directly (double-click it, `file://` is fine).
2. Click **Choose Folder** and select your slides folder (e.g. `slides/`).
3. The browser gives `viewer.html` a list of every file in that folder
   (this uses the standard `<input type="file" webkitdirectory>` picker —
   supported in Chrome, Edge, Brave, and Safari; not currently supported in
   Firefox).
4. The viewer:
   - Filters to `.html` / `.htm` files only.
   - Sorts them **alphabetically/numerically** by filename
     (`slide2.html` comes before `slide10.html`).
   - Creates an in-memory blob URL for each file and loads it into its own
     `<iframe>`.
   - Lays the iframes out side by side and lets you navigate between them.

Nothing is uploaded anywhere — `URL.createObjectURL` keeps everything local
to the browser tab. Click **Change folder** (top-left) to pick a different
deck without reloading the page.

## Navigation controls

- **Arrow keys** (← / →) or **spacebar** to advance
- **Swipe** left/right on touch devices
- **Click the dots** at the bottom to jump to a specific slide
- **Click the left/right edges** of the screen (invisible nav zones)
- **Slide counter** in the top-right shows position (e.g. `2 / 5`)

## Authoring slides

Each slide is a completely independent, self-contained HTML file:

- Use any CSS, inline `<style>`, fonts, images (as data URIs or relative
  paths *within the same folder*), JS, canvas animations, embedded SVGs —
  whatever you like.
- Aim for `height:100%` / `100vh` content so it fills the iframe cleanly
  (see the example slides for a minimal template).
- Filenames just need to sort in your intended order. Recommended pattern:
  `slide01.html`, `slide02.html`, ... `slide10.html`, etc. (zero-padding
  avoids `slide2` vs `slide10` ordering issues, though the viewer's numeric
  sort handles both correctly anyway).
- To reorder slides, just rename the files — no manifest or config to update.

## Design considerations / why it works this way

- **No server requirement**: Browsers block `fetch()`-based directory
  listings on `file://` for security reasons, and there's no way to read an
  arbitrary local folder via URL alone. The `webkitdirectory` file input is
  the standard, dependency-free workaround — it's a native browser API, not
  a library.
- **Folder picker instead of a hardcoded path**: A hardcoded absolute path
  baked into `viewer.html` would only work on one machine/one folder
  location. The picker keeps the viewer fully portable — drop it in any
  project, point it at any folder.
- **iframes instead of inlining HTML**: Keeps each slide's CSS/JS fully
  isolated (no class name collisions, no global script conflicts between
  slides), and means slide files are 100% standalone — you can also open any
  single `slideXX.html` directly in a browser to preview it in isolation.
- **Blob URLs**: `URL.createObjectURL(file)` lets the iframe load the
  selected file's actual content without any network request or server,
  while keeping everything sandboxed to the browser tab. URLs are revoked
  when you pick a new folder to avoid memory leaks.
- **Browser support note**: `webkitdirectory` is unfortunately not supported
  in Firefox as of this writing. If Firefox support becomes essential, an
  alternative is the File System Access API (`showDirectoryPicker()`), which
  Firefox also doesn't fully support yet — so the current approach is the
  most broadly compatible zero-dependency option for Chromium-based browsers
  and Safari.

## Possible future extensions (not included, to keep this minimal)

- Fullscreen / presenter mode toggle
- Thumbnail/overview grid of all slides
- Keyboard shortcut to jump to first/last slide (Home/End)
- Progress bar instead of dots for large decks
- Drag-and-drop folder support (in addition to the picker button)
