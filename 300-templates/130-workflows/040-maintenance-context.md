# Deck Context Sidecar

Each generated deck should include a `deck-context.md` file.

Its job is to preserve enough context so that a future AI agent or human can update the deck in a later session without rediscovering the original reasoning from scratch.

## Why this exists

Decks evolve across sessions.

The HTML slides alone often do not explain:

- why the deck was created
- what audience it targeted
- what arc was chosen
- which design choices were intentional
- what constraints shaped the deck
- what theme source or token strategy was used

That context should be saved with the deck.

## Required sections

A `deck-context.md` file should usually include:

### 1. Deck summary

- deck name
- date created
- date last updated
- purpose of the deck
- intended audience

### 2. Input summary

- source materials used
- prompt or brief summary
- assumptions made because information was missing

### 3. Narrative choices

- selected deck arc
- why that arc was chosen
- section structure used
- what was intentionally excluded

### 4. Theme brief

Document the deck's visual direction and token strategy.

Include:

- theme path used:
  - default light token pack
  - default dark token pack
  - custom token pack
- theme source:
  - user prompt
  - company or brand reference
  - screenshot
  - URL or online reference
  - existing deck
  - explicit hex values
  - mood words
  - inferred industry/audience style
- visual intent, such as mild, professional, technical, premium, bright, warm, or dark executive
- selected theme mode:
  - light
  - dark
  - hybrid-light
  - hybrid-dark
- important source colours or references
- token mapping rationale
- readability or contrast adjustments made
- semantic colour rationale
- chart colour rationale
- unresolved brand or style questions

If the deck uses external inspiration, state clearly whether it is:

- officially brand-guided, because the user provided official brand guidance
- brand-inspired, because the agent inferred style from public user-provided references
- mood-inspired, because the user provided descriptive direction rather than exact brand rules

### 5. Design choices

- layouts used and why
- notable visual constraints
- token or styling choices if relevant
- spacing, card, border, or shadow treatments if relevant

### 6. Slide map

A short list of slide numbers with their role.

Example:

- slide100.html — opener
- slide200.html — agenda
- slide300.html — current state
- slide400.html — recommendation

### 7. Update notes

- what changed in each later revision
- why it changed
- unresolved questions or follow-ups
- theme or token changes, if any

## Maintenance rule

When an agent updates a deck, it should update `deck-context.md` as part of the same change unless the user explicitly says not to.

If visual style, token values, or theme source changes, the Theme brief must be updated.
