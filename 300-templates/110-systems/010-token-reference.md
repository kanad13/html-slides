# Token Reference

This file documents the canonical token contract used by all layouts and example systems.

## Neutral

- `--surface-0`
- `--surface-1`
- `--surface-2`
- `--text-primary`
- `--text-secondary`
- `--border`

## Brand

- `--brand-primary`
- `--brand-secondary`
- `--brand-tertiary`
- `--brand-quaternary`

## Semantic

- `--success`
- `--warning`
- `--danger`
- `--info`

## Chart

- `--chart-1`
- `--chart-2`
- `--chart-3`
- `--chart-4`
- `--chart-5`
- `--chart-6`

## Supporting

- `--space-1` to `--space-8`
- `--radius-sm` to `--radius-xl`
- `--shadow-soft`

## Usage rule

Hardcoded colour values belong only inside token definition sections.

Layouts and components consume semantic tokens.

Derived visual treatments are allowed in layout CSS when they are composed from tokens.
Examples include gradients, transparent overlays, `color-mix()`, and emphasis effects that reference token values.
Avoid introducing raw hex, RGB, HSL, or named colour values outside token definition sections unless there is a documented browser/platform reason.

## External inspiration rule

External palettes, screenshots, company references, URLs, existing decks, user-provided hex values, or mood descriptions may be used as inspiration for a token pack.

They must not be applied directly throughout slide CSS.

Before slide generation, convert the chosen visual direction into the canonical token contract.

The required flow is:

1. Understand the visual inspiration.
2. Decide the intended theme direction.
3. Map the theme direction to token values.
4. Use those tokens in slide CSS and markup.
5. Document the theme source and assumptions in deck-context.md

## Custom token pack rule

A custom token pack is valid when:

- it defines the same canonical token names
- it keeps surface, text, border, brand, semantic, chart, spacing, radius, and shadow roles clear
- it supports the deck's audience and communication purpose
- it preserves readability and visual hierarchy
- it avoids random one-off styling across slides

A custom token pack may be created for a single deck.
It does not need to be promoted into the shared system folder unless it is expected to be reused across future decks.

## Semantic colour rule

Semantic colours should remain understandable as status indicators:

- --success should indicate positive, complete, healthy, or approved states
- --warning should indicate caution, risk, dependency, or attention
- --danger should indicate error, blocker, failure, or critical risk
- --info should indicate neutral information, guidance, or reference

Do not map semantic colours purely to brand colours if that makes status meaning unclear.

## Chart colour rule

Chart colours should be visually distinct from one another and usable on the chosen background.

When a custom brand-inspired theme is created:

- chart colours may be influenced by the brand direction
- chart colours do not need to exactly match brand colours
- chart colours should remain readable and distinguishable
- avoid using the same colour for unrelated meanings in the same deck

## Standalone slide rule

Generated slides should embed the resolved token values inside each standalone HTML slide by default.

Do not depend on a shared CSS file unless the user explicitly asks for that structure.
