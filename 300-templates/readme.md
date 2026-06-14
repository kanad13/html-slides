# Presentation Template System

This folder contains the reusable HTML slide template library used by the presentation system.

For browsing and presenting files locally, open the root viewer at [`../100-viewer.html`](../100-viewer.html).

For detailed operating rules, naming conventions, and template-authoring guidance, see [`TEMPLATE-SYSTEM.md`](TEMPLATE-SYSTEM.md).

---

## What is in this folder

```text
300-templates/
├── readme.md
├── TEMPLATE-SYSTEM.md
├── 100-basic.html
├── 200-light/
│   └── 005-design-system.html
│   └── 010-*.html
│   └── ...
│   └── 250-*.html
├── 300-dark/
│   └── 005-design-system.html
│   └── 010-*.html
│   └── ...
│   └── 250-*.html
```

---

## File roles

- [`100-basic.html`](100-basic.html)
  Legacy starter template and minimal token-based reference.

- [`200-light/005-design-system.html`](200-light/005-design-system.html)
  Canonical light-theme token and component reference.

- [`300-dark/005-design-system.html`](300-dark/005-design-system.html)
  Canonical dark-theme token and component reference.

- `200-light/010-250` and `300-dark/010-250`
  The main slide layout library. Prefer these when selecting a starting point for a new slide.

- [`TEMPLATE-SYSTEM.md`](TEMPLATE-SYSTEM.md)
  Complete rules for creating, adapting, and maintaining templates.

- [`../100-viewer.html`](../100-viewer.html)
  Root-level viewer for previewing and presenting slide files.

---

## Recommended workflow

- **Need a slide for content?** Start from the closest existing numbered template.
- **Need a brand-new layout?** Start from [`100-basic.html`](100-basic.html).
- **Need token guidance?** Use the light and dark design-system reference files.
- **Need to browse or present locally?** Open [`../100-viewer.html`](./../100-viewer.html).

---

## Core principle

Layouts stay stable.

Brands change through token values.

Do not redesign layouts for every brand.

---

## Most important rule

Layouts should never change when adapting to a new brand.

Only token values should change.
