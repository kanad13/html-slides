# Demo Deck Context

## Deck Summary

- Deck name: HTML Deck Studio Demo
- Purpose: Demonstrate the current viewer, generation contract, token system, and optional tooling direction.
- Intended audience: Users and future AI agents maintaining this repository.
- Date created: 2026-06-16
- Date last updated: 2026-06-16

## Input Summary

- Source materials: Repository README, AGENTS.md, template system, token reference, output contract, and maintenance context guidance.
- Assumptions: The demo should act as a standards-compliant reference deck rather than a loose feature showcase.

## Narrative Choices

- Selected deck arc: Teaching arc.
- Rationale: The deck explains the system rules and expected workflow in a sequence that builds from output contract to validation and optional export.
- Section structure: intro, standalone contract, token system, theme intake, layout selection, viewer runtime, maintenance context, quality gates, PDF export.
- Excluded: Online hosted viewer behavior, because it is intentionally deferred.

## Theme Brief

- Theme path: default dark token pack.
- Theme source: `300-templates/110-systems/110-dark-default.html`.
- Visual intent: technical, precise, and high-contrast.
- Theme mode: dark.
- Important source colors: copied from the default dark token pack.
- Token strategy: each slide embeds the same resolved token values in `:root`; component CSS consumes tokens.
- Readability adjustments: no custom adjustments beyond default dark token choices.
- Semantic color rationale: default semantic colors preserve recognizable success, warning, danger, and info meanings.
- Chart color rationale: chart tokens are present even though this demo deck does not include charts.

## Design Choices

- Layouts used: classic opener, title-body, card grids, process flow, split explanation, checklist, and command panel.
- Reasoning: The deck uses a small set of repeatable structures to keep content scannable and coherent.
- Styling: raw color values are confined to token definitions; derived treatments use token-based `color-mix()` and gradients.

## Slide Map

- slide0100.html - opener and purpose
- slide0200.html - standalone slide contract
- slide0300.html - token roles
- slide0400.html - theme intake flow
- slide0500.html - layout choice
- slide0600.html - viewer runtime contract
- slide0700.html - deck context
- slide0800.html - quality gates
- slide0900.html - PDF export
- slide09.html - optional PDF export

## Update Notes

- 2026-06-16: Rebuilt from scratch to align demos with the repository token and output standards.
