# Template System Guide

This document explains how to create, maintain, and use slide templates in this folder.

The template system is designed for both human authors and AI agents.

It prioritises consistency, readability, maintainability, and brand flexibility.

---

## Folder Structure

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

## File Roles

### README.md

High-level overview.

Read this first when onboarding.

### TEMPLATE-SYSTEM.md

Operational manual.

Use this when creating or editing templates.

### 100-basic.html

Starter template.

Copy this file when creating a new template.

### 100-viewer.html

Simple browser-based viewer.

Use this to preview templates locally.

### 200-light/005-design-system.html

Visual design-system reference for light slides.

### 300-dark/005-design-system.html

Visual design-system reference for dark slides.

---

## Naming Convention

Use numeric prefixes to keep files sorted.

Recommended pattern:

```text
005-design-system.html
010-title-slide.html
020-section-divider.html
030-two-column.html
040-metric-dashboard.html
050-comparison.html
060-process.html
070-timeline.html
080-chart.html
090-closing.html
```

Use descriptive names.

Avoid vague names such as:

```text
slide1.html
template-new.html
test.html
final.html
```

---

## Template Metadata

Each template should include a metadata block near the top of the file.

Example:

```html
<!--
Template: Two Column Insight
Category: Content
Theme: Light
Use Case: Compare two ideas, options, or findings
Recommended Content:
- One slide title
- Two section headings
- 3–5 bullets per column
Notes:
- Use brand colour for emphasis only
- Avoid long paragraphs
-->
```

This helps humans and AI agents choose the correct template.

---

## Design Token System

Templates should use semantic design tokens.

Do not hardcode colours inside layouts.

Good:

```css
color: var(--brand-primary);
background: var(--surface-1);
border-color: var(--border);
```

Bad:

```css
color: #2563eb;
background: #f8fafc;
border-color: #e2e8f0;
```

Hardcoded colour values are allowed only inside the token definition section.

---

## Core Token Categories

### Neutral Tokens

Used for layout, readability, and structure.

```css
--surface-0
--surface-1
--surface-2

--text-primary
--text-secondary

--border
```

### Brand Tokens

Used for identity and selective emphasis.

```css
--brand-primary
--brand-secondary
--brand-tertiary
--brand-quaternary
```

### Semantic Tokens

Used when colour communicates meaning.

```css
--success
--warning
--danger
--info
```

### Chart Tokens

Used only for charts and data visualisation.

```css
--chart-1
--chart-2
--chart-3
--chart-4
--chart-5
--chart-6
```

---

## Recommended Token Block

Every standalone template should include a token block.

Light default:

```css
:root {
  --surface-0: #ffffff;
  --surface-1: #f8fafc;
  --surface-2: #eef2f7;

  --text-primary: #0f172a;
  --text-secondary: #64748b;

  --border: #e2e8f0;

  --brand-primary: #2563eb;
  --brand-secondary: #06b6d4;
  --brand-tertiary: #d97706;
  --brand-quaternary: #7c3aed;

  --success: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
  --info: #3b82f6;

  --chart-1: #2563eb;
  --chart-2: #06b6d4;
  --chart-3: #10b981;
  --chart-4: #f59e0b;
  --chart-5: #7c3aed;
  --chart-6: #ef4444;
}
```

Dark default:

```css
:root {
  --surface-0: #0f172a;
  --surface-1: #1a2332;
  --surface-2: #233044;

  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;

  --border: #334155;

  --brand-primary: #06b6d4;
  --brand-secondary: #22d3ee;
  --brand-tertiary: #4ade80;
  --brand-quaternary: #818cf8;

  --success: #22c55e;
  --warning: #f59e0b;
  --danger: #f87171;
  --info: #38bdf8;

  --chart-1: #06b6d4;
  --chart-2: #22d3ee;
  --chart-3: #4ade80;
  --chart-4: #f59e0b;
  --chart-5: #818cf8;
  --chart-6: #f87171;
}
```

---

## Brand Adaptation

To adapt a deck to a new brand, change token values only.

Do not change:

- layout
- spacing
- typography hierarchy
- component structure

Example Google-inspired token set:

```css
--brand-primary: #4285f4;
--brand-secondary: #ea4335;
--brand-tertiary: #fbbc05;
--brand-quaternary: #34a853;

--chart-1: #4285f4;
--chart-2: #ea4335;
--chart-3: #fbbc05;
--chart-4: #34a853;
--chart-5: #9334e6;
--chart-6: #00acc1;
```

---

## Colour Usage Strategy

Recommended ratio:

```text
85% neutral
10% brand
5% semantic
```

Use neutral surfaces for most structure.

Use brand colours for:

- slide labels
- emphasis lines
- selected icons
- important numbers
- key highlights

Use semantic colours for:

- success
- risk
- warning
- errors
- decision status
- positive or negative KPI interpretation

Avoid using semantic colours as generic decoration.

---

## Typography Rules

Use a simple hierarchy.

### H1

Slide title.

Recommended:

```css
font-size: 3rem;
font-weight: 800;
letter-spacing: -0.04em;
```

### H2

Section heading.

Recommended:

```css
font-size: 1.35rem;
font-weight: 700;
```

### Body

Normal slide text.

Recommended:

```css
font-size: 1rem;
line-height: 1.65;
```

### Eyebrow

Small section label.

Recommended:

```css
font-size: 0.76rem;
font-weight: 800;
text-transform: uppercase;
letter-spacing: 0.16em;
color: var(--brand-primary);
```

---

## Layout Rules

Every slide should have:

1. One primary message.
2. Clear visual hierarchy.
3. Consistent spacing.
4. Limited colour usage.
5. Enough whitespace.
6. Text that is readable at presentation distance.

If a slide feels busy:

1. Remove decoration.
2. Reduce colour.
3. Reduce text.
4. Simplify layout.

---

## Spacing System

Use a consistent spacing scale.

```css
--space-1: 0.25rem;
--space-2: 0.5rem;
--space-3: 0.75rem;
--space-4: 1rem;
--space-5: 1.5rem;
--space-6: 2rem;
--space-7: 3rem;
--space-8: 4rem;
```

Do not manually invent spacing values unless the layout requires a specific exception.

---

## Component Patterns

Recommended reusable components:

- card
- metric card
- badge
- callout
- two-column grid
- three-card grid
- chart block
- section label
- accent line

Components should use tokens.

Example:

```css
.card {
  background: var(--surface-1);
  border: 1px solid var(--border);
  border-radius: 1.25rem;
  padding: var(--space-6);
}
```

---

## Chart Rules

Charts should use chart tokens.

Good:

```css
.bar-1 {
  background: var(--chart-1);
}
.bar-2 {
  background: var(--chart-2);
}
.bar-3 {
  background: var(--chart-3);
}
```

Bad:

```css
.bar-1 {
  background: red;
}
.bar-2 {
  background: blue;
}
.bar-3 {
  background: green;
}
```

Charts should be readable without relying only on colour.

Use labels, values, or legends.

---

## Accessibility Rules

Check:

- text contrast
- font size
- line height
- spacing
- semantic colour usage
- chart readability
- slide readability at distance

Avoid:

- tiny text
- low-contrast grey text
- colour-only meaning
- dense paragraphs
- crowded charts

---

## AI Generation Workflow

When generating a new slide:

1. Identify slide purpose.
2. Select the closest template.
3. Insert content.
4. Use existing typography hierarchy.
5. Use token-based colours.
6. Use brand colour sparingly.
7. Use semantic colour only when meaning exists.
8. Keep the primary message obvious.
9. Avoid adding unnecessary decoration.
10. Validate readability.

---

## Template Creation Workflow

When creating a new template:

1. Copy `100-basic.html`.
2. Rename according to the naming convention.
3. Update metadata.
4. Keep the token block.
5. Build layout using tokenised components.
6. Test with default brand tokens.
7. Test with a different brand palette.
8. Test in both light and dark themes where applicable.
9. Add the template to the viewer.
10. Document any special usage rules.

---

## Quality Checklist

Before committing a template:

```text
[ ] Uses design tokens
[ ] No hardcoded colours outside token definitions
[ ] Clear slide hierarchy
[ ] Readable at presentation distance
[ ] Works with different brand palettes
[ ] Uses semantic colours only for meaning
[ ] Uses chart colours only for charts
[ ] Includes metadata block
[ ] Has consistent spacing
[ ] Avoids unnecessary decoration
```

---

## Most Important Rule

Layouts should never change when adapting to a new brand.

Only token values should change.
