# Slide System Guide

This file is the main instruction set for building slides from `300-templates`.

## What the system is

The system separates five things:

- **tokens** - colours, spacing, radius, shadow, and related design variables
- **theme sources** - default token packs or external inspiration converted into tokens
- **layouts** - structural arrangements of content regions
- **deck workflows** - how decks are created, updated, and documented across sessions
- **slides** - real standalone HTML files with actual content

## What this system is for

This is a personal HTML slide system for AI-assisted deck creation and maintenance.

It is not a corporate multi-user design system.

The normal workflow is:

- give an AI coding agent the repo and source material
- ask it to create or update a deck
- choose either a default token pack or a custom tokenized theme
- generate standalone slide files in `500-output/`
- keep a `deck-context.md` file beside the slides so future sessions retain context

## Theme model

The system supports two default complete token packs:

- **Light default** - use for general-purpose decks with a light background.
- **Dark default** - use for general-purpose decks with a dark background.

The system also supports **deck-specific custom token packs**.

A custom token pack may be created from:

- user-described mood or style
- company or brand reference
- screenshot or visual example
- URL or online style reference
- existing slide or deck sample
- explicit hex values
- industry or audience context

External inspiration is allowed as input.
Direct external styling is not.

All visual inspiration must be converted into the canonical token contract before slide generation.
Layouts and slide components should consume tokens, not arbitrary one-off colours.

### Rules that matter

- Keep each slide as a standalone HTML file.
- Use the token names from `110-systems/010-token-reference.md`.
- Use `110-systems/100-light-default.html` or `110-systems/110-dark-default.html` when no custom visual direction is needed.
- Use `110-systems/020-theme-intake-and-tokenization.md` when the user gives brand, mood, screenshot, URL, company, or colour inspiration.
- Choose layout structure based on content and communication need first.
- Adjust token values to express theme and visual tone once the content structure is right.
- Reuse a small number of layouts within one deck.
- Update deck context when a deck is created or materially changed.
- Record custom theme decisions in deck-context.md.

## Normal workflow

- Determine audience, purpose, and available input.
- Choose a deck arc from `130-workflows/030-deck-arcs.md`.
- Use `100-basic.html` as the default scaffold.
- Select fitting structures from `120-layouts/010-layout-catalog.md`.
- Choose a theme path:
  - copy token values from the default light system,
  - copy token values from the default dark system,
  - or create a custom token pack using the theme intake and tokenization workflow.
- Build the slides as full standalone HTML documents.
- Embed token definitions and slide CSS inline in each slide by default.
- Output them following `130-workflows/020-output-contract.md`.
- Write or update `deck-context.md` using `130-workflows/040-maintenance-context.md`.

## Required token contract

### Minimum tokens for most slides

- `--surface-0`
- `--surface-1`
- `--surface-2`
- `--text-primary`
- `--text-secondary`
- `--border`
- `--brand-primary`
- `--space-1` to `--space-8`
- `--radius-sm` to `--radius-xl`
- `--shadow-soft`

### Extended tokens for richer slides

#### Additional brand

- `--brand-secondary`
- `--brand-tertiary`
- `--brand-quaternary`

#### Semantic

- `--success`
- `--warning`
- `--danger`
- `--info`

#### Chart

- `--chart-1`
- `--chart-2`
- `--chart-3`
- `--chart-4`
- `--chart-5`
- `--chart-6`

## Custom theme expectations

When creating a custom theme:

- map the visual direction into the canonical token names
- keep text/background contrast readable
- keep semantic colours recognizable as status colours
- keep chart colours visually distinct from one another
- do not use brand colours as status colours unless they remain understandable
- avoid hardcoding external inspiration colours directly into components
- document the source and reasoning in deck-context.md

## Slide file expectations

A real slide file should usually include:

- `<!DOCTYPE html>`
- `<html lang="...">`
- charset and viewport metadata
- inline token definitions
- `<style>` that consumes those tokens
- `<slide markup>`
- optional `<aside class="notes">`

## Deck-level expectations

A real deck should usually have:

- a coherent arc
- a limited set of repeated layout patterns
- an opener and a close or clear final implication
- titles that make slide purpose obvious
- a clear theme direction
- deck-context.md documenting why the deck was built the way it was

## Simple quality check

Before considering a slide or deck done:

- the deck arc fits the audience and task
- each slide has one clear communication job
- tokens are used consistently
- layout choice follows content need rather than decoration
- the deck does not rely on random hardcoded colours across components
- custom theme values are mapped into the canonical token contract
- text and important visual elements remain readable
- hierarchy is obvious
- slides are readable without zooming in
- output files follow the output contract
