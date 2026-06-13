# Presentation Template System v2

This folder contains the presentation template system used to create consistent, professional, AI-generated slides.

The system is token-based rather than colour-based.

That means layouts should stay stable while brand colours can change from deck to deck.

A Google-style deck, an OpenAI-style deck, and a neutral consulting deck should all be able to use the same templates by changing only token values.

---

## Files

```text
300-templates/
├── README.md
├── TEMPLATE-SYSTEM.md
├── 100-basic.html
├── 100-viewer.html
├── 200-light/
│   └── 005-design-system.html
└── 300-dark/
    └── 005-design-system.html
```

---

## Start Here

Use these files as follows:

- `README.md`
  High-level overview and philosophy.

- `TEMPLATE-SYSTEM.md`
  Operational guide for humans and AI agents creating new templates.

- `100-basic.html`
  Minimal starter template. Copy this when creating a new slide template.

- `100-viewer.html`
  Simple local viewer for browsing templates.

- `200-light/005-design-system.html`
  Light-theme visual design-system reference.

- `300-dark/005-design-system.html`
  Dark-theme visual design-system reference.

---

## Core Principle

Layouts are stable.

Brand tokens are interchangeable.

Do not redesign layouts for every brand.

Instead, update the token values:

```css
--brand-primary: #4285f4;
--brand-secondary: #ea4335;
--brand-tertiary: #fbbc05;
--brand-quaternary: #34a853;
```

The same layout should still work.

---

## Design Philosophy

The goal is not maximum visual variety.

The goal is:

- consistency
- readability
- professional appearance
- easy AI generation
- easy brand adaptation

Most slides should be visually calm.

Use colour for meaning, emphasis, and structure.

Avoid decorative colour usage that does not help the audience understand the message.

---

## Token Categories

The system uses four token categories.

### 1. Neutral Tokens

Used for structure and readability.

```css
--surface-0
--surface-1
--surface-2

--text-primary
--text-secondary

--border
```

Neutrals should make up roughly 80–90% of most slides.

---

### 2. Brand Tokens

Used for identity and emphasis.

```css
--brand-primary
--brand-secondary
--brand-tertiary
--brand-quaternary
```

Brand colours should usually make up 10–20% of a slide.

---

### 3. Semantic Tokens

Used when colour has meaning.

```css
--success
--warning
--danger
--info
```

Use these for statuses, risks, alerts, decisions, and KPI interpretation.

Do not use semantic colours only for decoration.

---

### 4. Chart Tokens

Used for data visualisation.

```css
--chart-1
--chart-2
--chart-3
--chart-4
--chart-5
--chart-6
```

Never invent chart colours inside individual slides.

---

## Recommended Colour Ratio

A good default ratio is:

```text
85% neutral
10% brand
5% semantic
```

This keeps slides professional and prevents rainbow-style decks.

---

## Brand Adaptation Examples

### Default Blue Theme

```css
--brand-primary: #2563eb;
--brand-secondary: #06b6d4;
--brand-tertiary: #d97706;
--brand-quaternary: #7c3aed;
```

### Google-Inspired Theme

```css
--brand-primary: #4285f4;
--brand-secondary: #ea4335;
--brand-tertiary: #fbbc05;
--brand-quaternary: #34a853;
```

### OpenAI-Inspired Theme

```css
--brand-primary: #10a37f;
--brand-secondary: #0e7c61;
--brand-tertiary: #202123;
--brand-quaternary: #6b7280;
```

### Microsoft-Inspired Theme

```css
--brand-primary: #0078d4;
--brand-secondary: #107c10;
--brand-tertiary: #ffb900;
--brand-quaternary: #d83b01;
```

---

## AI Agent Rules

When generating slides:

1. Use design tokens.
2. Do not hardcode colours.
3. Preserve typography hierarchy.
4. Preserve spacing rhythm.
5. Use brand colours sparingly.
6. Use semantic colours only when meaning exists.
7. Use chart tokens for charts.
8. Keep layouts readable at presentation distance.
9. Prefer fewer elements over more decoration.
10. Do not change layouts when adapting to a new brand.

---

## Most Important Rule

Layouts should never change when adapting to a new brand.

Only token values should change.
