# AI Slide Workflow

This folder defines how an AI coding agent should create, update, and maintain slide decks in this repo.

## Scope

Use this workflow for personal HTML slide generation in this repo.

This is not a corporate multi-user design system. It is a lightweight, local-first slide workflow for a single user who may return across multiple sessions.

## Workflow set

- [`010-ai-workflow.md`](010-ai-workflow.md) — end-to-end creation and maintenance workflow
- [`020-output-contract.md`](020-output-contract.md) — required output files and naming rules
- [`030-deck-arcs.md`](030-deck-arcs.md) — reusable deck arc patterns based on communication best practices
- [`040-maintenance-context.md`](040-maintenance-context.md) — deck context sidecar file for future updates
- [`020-theme-intake-and-tokenization.md`](../110-systems/020-theme-intake-and-tokenization.md) – workflow for turning visual inspiration into tokens

## Creation workflow

### 1. Understand the task

Before creating slides, determine:

- who the audience is
- what outcome the deck should achieve
- what source material is available
- whether the deck is informative, persuasive, analytical, explanatory, or mixed
- what constraints exist for length, tone, and theme
- whether the user provided visual inspiration, such as a company name, screenshot, URL, existing deck, mood words, or hex values

If important information is missing, state assumptions clearly in `deck-context.md`.

### 2. Shape the deck before writing slides

Before writing any HTML:

- choose a deck arc from [`030-deck-arcs.md`](030-deck-arcs.md)
- define the section flow
- decide roughly how many slides are needed
- assign one communication job to each slide

Do not start from decorative layout choices.

Start from message, audience, and arc.

### 3. Choose theme path and token strategy

Choose one of three theme paths:

1. **Default light token pack**
   - Use when the user wants a normal light deck or gives no special visual direction.

2. **Default dark token pack**
   - Use when the user wants a dark deck or the content benefits from a high-contrast dark presentation style.

3. **Custom token pack**
   - Use when the user provides brand, company, screenshot, URL, mood, existing deck, industry, or hex colour inspiration.

When creating a custom token pack:

- follow [`../110-systems/020-theme-intake-and-tokenization.md`](../110-systems/020-theme-intake-and-tokenization.md)
- convert external inspiration into the canonical token contract
- do not scatter external colours directly across slide components
- preserve readability and visual hierarchy
- keep semantic colours understandable
- keep chart colours distinct
- document the theme source and token choices in `deck-context.md`

### 4. Choose system ingredients

- use [`../100-basic.html`](../100-basic.html) as the default scaffold
- choose a theme direction from [110-systems](../110-systems/)
- choose layouts from [120-layouts](../120-layouts/)

### 5. Generate output

- write the deck into `500-output/` following [`020-output-contract.md`](020-output-contract.md)
- create standalone HTML slides
- embed token definitions and CSS inline in each slide by default
- create `deck-context.md`
- keep slides scannable and locally editable

## Maintenance workflow

When updating an existing deck:

### 1. Read before editing

Review:

- existing slide files
- `deck-context.md`
- the user's requested changes
- the existing theme brief, if present

### 2. Preserve intent where possible

Try to preserve:

- the existing arc unless the user wants a reframing
- the current numbering unless renumbering is truly needed
- the visual system unless the user wants a redesign
- the existing token strategy unless the theme is part of the requested change

### 3. Handle theme changes deliberately

If the user asks for a visual redesign or new brand/style direction:

- identify whether the request changes the token pack
- update the token values consistently across all slides
- avoid mixing old and new token values in the same deck unless a deliberate section-level theme change is introduced and documented
- preserve standalone slide behaviour
- update the theme brief in `deck-context.md` with the new theme source, token strategy, and any assumptions or adjustments made during the redesign

### 4. Record change context

Update `deck-context.md` with:

- what changed
- why it changed
- what assumptions were introduced
- any unresolved follow-up items
- theme changes, if any

## Authoring priorities

When trade-offs appear, prefer this order:

- message clarity
- audience fit
- coherent arc
- slide readability
- deck consistency
- token consistency
- visual refinement

## Anti-patterns

Avoid these failure modes:

- choosing layouts before understanding the content
- using a different visual style on every slide
- overfilling slides with report text
- inventing unsupported facts to complete a narrative
- updating slides without updating context
- treating layouts as rigid templates instead of communication tools
- using external inspiration colours directly in components instead of tokenizing them
- claiming official brand compliance without official brand input
