# Theme Intake and Tokenization

This file defines how an AI agent or human should turn visual inspiration into a tokenized slide theme.

The goal is to support flexible user requests without weakening the token system.

Users may describe a style in natural language, name a company, provide screenshots, share URLs, give existing slide examples, or specify hex values.
The final output must still be a complete token pack that follows the canonical token contract.

## Core principle

External inspiration is allowed.
Direct external styling is not.

The required model is:

```text
inspiration source
→ visual interpretation
→ canonical token mapping
→ standalone HTML slides
→ deck-context.md documentation
```

## Supported theme inputs

A theme can be based on one or more of the following:

- user-described mood or style
- company or brand name
- public website or online visual reference
- screenshot or image reference
- existing deck or slide sample
- explicit hex values
- industry or domain context
- audience context
- event or presentation context

Examples:

- "Make it look professional but warm."
- "Use a style inspired by our company website."
- "Use these colours: ■ #1F2A24, ■ #8A9A5B, □ #F4EFE6."
- "Use something close to this screenshot."
- "Create a bright innovation-style deck."
- "Make it feel like an executive technology briefing."

## Default token packs

The system includes two default complete token packs:

- light default
- dark default

Use them when:

- the user gives no special visual direction
- speed and predictability matter more than custom styling
- the deck should stay close to the framework baseline
- the user asks for a simple light or dark deck

## Custom token packs

Create a custom token pack when:

- the user gives explicit style or colour direction
- the deck should reflect a company, brand, event, or visual reference
- the user provides screenshots, URLs, existing slides, or hex values
- the default light/dark themes do not fit the desired tone

A custom token pack may be deck-specific.\
It does not need to become a permanent shared system theme.

## Tokenization workflow

### 1. Identify the theme source

Determine where the visual direction comes from:

- default framework theme
- user mood words
- company or brand reference
- screenshot
- URL
- existing deck
- explicit colours
- inferred industry style

If multiple sources conflict, prefer explicit user instructions over inferred style.

### 2. Interpret the visual intent

Translate the input into a concise visual intent.

Examples:

- mild and neutral
- executive and serious
- bright and energetic
- technical and precise
- premium and understated
- warm and approachable
- dark and high-contrast
- minimal and document-like

This visual intent should guide token choices.

### 3. Choose the theme mode

Decide whether the deck should be:

- light
- dark
- hybrid-light
- hybrid-dark

Definitions:

- **light**: mostly light surfaces and dark text
- **dark**: mostly dark surfaces and light text
- **hybrid-light**: light deck with strong dark sections or accents
- **hybrid-dark**: dark deck with selected light cards or panels

Use one primary mode per deck unless the user explicitly asks for multiple modes.

### 4. Map inspiration to token roles

Convert inspiration colours into token roles.

Minimum mapping:

- background and main slide surface → --surface-0
- secondary panels/cards → --surface-1
- tertiary areas or muted blocks → --surface-2
- main readable text → --text-primary
- secondary text → --text-secondary
- dividers and card borders → --border
- main accent or brand colour → --brand-primary
- supporting accent colours → --brand-secondary, --brand-tertiary, --brand-quaternary
- status colours → --success, --warning, --danger, --info
- charts → --chart-1 to --chart-6

Do not assume the user's first colour is always the primary brand token.\
Infer roles from contrast, mood, and stated preference.

### 5. Fill missing tokens

User input is often incomplete.

If the user provides only one or two colours, generate the missing supporting tokens while preserving:

- readability
- hierarchy
- visual coherence
- semantic status meaning
- chart distinctness

Generated supporting colours should feel compatible with the user-provided direction.

### 6. Preserve semantic meaning

Semantic colours should stay understandable.

Do not force company or brand colours into semantic roles if doing so makes success, warning, danger, or info states unclear.

For example:

- green brand colour can still be --brand-primary
- but --success should remain clearly positive
- \--danger should remain clearly critical
- \--warning should remain clearly cautionary

### 7. Preserve chart usability

Chart colours should be distinguishable on the selected background.

When possible:

- use brand-inspired chart colours
- avoid colours that are too similar to each other
- avoid chart colours that conflict with status colours in the same slide
- avoid using only decorative colours when data comparison is important

### 8. Check readability

Before generating slides, check that the theme supports:

- readable title text
- readable body text
- readable cards and labels
- visible borders or separation where needed
- sufficient contrast for important visual elements
- legible chart labels and table content

If a user-provided colour causes readability problems, adjust the derived token value and document the adjustment.

### 9. Apply tokens consistently

Once the token pack is selected or generated:

- embed the resolved token values in each standalone slide
- use token names in layout and component CSS
- avoid ad hoc hardcoded colours in slide components
- keep the same token values across the deck unless a deliberate section-level variation is documented

### 10. Document the theme

Record theme decisions in deck-context.md.

Include:

- theme source
- visual intent
- selected mode
- important source colours or references
- token strategy
- readability adjustments
- chart colour rationale
- semantic colour rationale
- unresolved questions

## Company and brand references

When a user gives a company or brand name:

- use the company reference as visual inspiration only unless official brand guidelines are provided
- do not claim the deck uses official brand guidelines unless the user supplied them
- prefer "brand-inspired custom token direction" when using public visual references
- adjust colours for readability where needed
- document assumptions in deck-context.md

## Screenshot or image references

When a user provides a screenshot or image:

- identify the dominant surface style
- identify accent colours
- identify contrast level
- identify card, border, and shadow treatment
- infer whether the style is light, dark, or hybrid
- convert the visual direction into tokens
- do not attempt pixel-perfect copying unless explicitly requested

## URL or online references

When a user provides a URL or asks for external inspiration:

- inspect the visual direction where possible
- identify reusable colour and style signals
- convert those signals into the token contract
- do not depend on remote assets in the generated deck
- do not use external fonts, scripts, images, or CDNs unless explicitly allowed elsewhere

## Hex value inputs

When a user provides hex values:

- treat them as source colours, not automatically as complete tokens
- infer likely roles based on colour character and user wording
- ask a clarification only if the intended role is materially ambiguous
- generate missing neutral, semantic, and chart tokens
- adjust derived values if needed for readability

Example:

```text
Input:
■ #1F2A24,  ■ #8A9A5B,  □ #F4EFE6

Possible interpretation:
- ■ #1F2A24 → dark surface or text anchor
- ■ #8A9A5B → olive brand accent
- □ #F4EFE6 → warm light surface
```

## Mood word inputs

When a user gives mood words, translate them into token behaviour.

Examples:

```text
mild
→ low saturation, soft surfaces, restrained accents

bright
→ vivid accents, high energy, careful contrast control

professional
→ conservative neutrals, strong hierarchy, limited accent use

premium
→ restrained palette, deep or warm neutrals, subtle contrast

technical
→ precise cool accents, clean surfaces, strong data readability

warm
→ cream, sand, bronze, olive, or muted orange direction

dark executive
→ charcoal/navy surfaces, high text contrast, restrained accent colours
```

## Output rule

By default, generated slides must remain standalone.

This means:

- each slide includes the resolved token values inline
- each slide includes the CSS needed to render itself
- no shared theme CSS file is required
- the viewer can load each slide independently

Use a shared deck-level CSS file only if the user explicitly asks for it.

## Anti-patterns

Avoid:

- copying external palettes directly into random components
- using a different custom palette on every slide
- treating brand colours as semantic status colours without checking meaning
- sacrificing readability to preserve exact inspiration colours
- creating a theme that only works on one slide type
- depending on remote assets, web fonts, or CDN resources
- claiming official brand compliance without official brand input
