# Demo Deck Context

## Deck Summary

- Deck name: HTML Deck Studio Demo
- Purpose: Showcase the framework's three user paths and core features with clear, accessible narrative
- Intended audience: New users and potential adopters of HTML Deck Studio
- Date created: 2026-06-16
- Date last updated: 2026-06-21

## Input Summary

- Source materials: Updated README.md, AGENTS.md constraints, template system, token reference, and user workflows
- Assumptions: New readers need to understand what the framework does, not its internal implementation details

## Narrative Choices

- Selected deck arc: User-focused feature showcase with three parallel paths (Present, Generate, Export)
- Rationale: The original technical deep-dive worked for developers. This version introduces users to the value and workflow
- Section structure: Welcome, Three Paths, Present (demo viewer), Generate (AI workflow), Token System overview, Light vs Dark themes, PDF Export, Why use this, Getting Started
- Approach: Each slide focuses on one user need, with clear next steps and practical examples

## Theme Brief

- Theme path: default light token pack
- Theme source: `300-templates/110-systems/100-light-default.html`
- Visual intent: approachable, bright, energetic, welcoming to non-technical users
- Theme mode: light
- Important source colors: Standard light token pack values
- Token strategy: Each slide embeds the complete light token set; CSS consumes tokens
- Readability adjustments: No custom adjustments; default light tokens provide good contrast and hierarchy
- Semantic color rationale: Default semantic colors (success, warning, danger, info) preserve meaning
- Chart color rationale: Not demonstrated in this deck, but chart tokens are present for consistency

## Design Choices

- Layouts used: Full-bleed opener, title-lead-grid card, step-by-step workflow, feature preview, token grid, two-column theme comparison, quick-reference list
- Reasoning: Mix of layouts keeps the presentation scannable without overwhelming navigation. Each layout serves a communication job
- Styling: All raw colors are confined to token definitions in :root. No hardcoded hex values in component CSS

## Slide Map

- slide0100.html - Welcome: Portable presentations, no lock-in (opener with three core principles)
- slide0200.html - Three Ways to Use It (Present, Generate, Export)
- slide0300.html - Present: Open a folder of slides and present immediately (3-step workflow)
- slide0400.html - Generate: Use AI to create and update decks (prompt example + output)
- slide0500.html - Token System: Tokenized color and spacing (token overview grid)
- slide0600.html - Light & Dark Themes: Two built-in themes plus custom capability
- slide0700.html - Export to PDF: Share slides as full-bleed PDF (command example)
- slide0800.html - Why HTML Deck Studio: Four key benefits (local, inspectable, AI-friendly, production-ready)
- slide0900.html - Getting Started: Next steps for users (4-step onboarding)

## Update Notes

- 2026-06-16: Original deck from scratch, dark theme, focused on technical contract and internal standards
- 2026-06-21: Complete regeneration to light theme with user-focused narrative. Changed target audience from developers to new users. Reframed each slide around user workflows instead of technical implementation details. Maintains all token system and framework integrity while prioritizing clarity and accessibility

## Unresolved Questions / Future Considerations

- Consider video walkthrough of the viewer interface
- Consider adding example deck screenshots or recorded demos
- Consider creating a complementary "advanced" deck for developers and template authors
