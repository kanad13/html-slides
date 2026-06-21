# User Guide

## Open a Deck

1. Open `100-viewer.html` in a modern browser.
2. Choose **Choose Folder**.
3. Select the folder containing the slide files.

The viewer loads `.html` and `.htm` files, sorts them naturally, and shows them as a presentation. Use **Choose Files** if folder picking is unavailable in your browser.

## Deck Shape

A normal deck is a folder like this:

```text
my-deck/
├── slide100.html
├── slide200.html
├── slide300.html
└── deck-context.md
```

If a deck uses local images or media, keep them in the same deck folder:

```text
my-deck/
├── slide100.html
├── slide200.html
├── assets/
│   └── chart.png
└── deck-context.md
```

When using local assets, choose the folder so the browser grants access to the slide files and supporting files together.

## Present

Use the toolbar or keyboard:

| Action | Shortcut |
| --- | --- |
| Next slide | `Right Arrow` or `Space` |
| Previous slide | `Left Arrow` |
| First slide | `Home` |
| Last slide | `End` |
| Overview | `O` |
| Speaker notes | `N` |
| Presenter window | `P` |
| Slide list | `L` |
| Fullscreen/Zen | `Z` or `F` |
| Theme toggle | `M` |
| Open another deck | `D` |
| Help | `H` or `?` |
| Close overlay or exit | `Esc` |

## Speaker Notes

Slides can include hidden notes:

```html
<aside class="notes">Mention the customer feedback before moving to the roadmap.</aside>
```

The viewer extracts notes without executing slide scripts. Press `N` to show notes in the docked notes panel, or `P` to open the presenter window.

## Viewer Theme

The viewer theme toggle changes only the viewer chrome. It does not modify slide contents inside iframes.
