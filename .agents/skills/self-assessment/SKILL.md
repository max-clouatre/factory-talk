---
name: self-assessment
description: The deck's eval. Runs audience-simulation and turns it into structured, slide-by-slide feedback with a short list of fixes. Use before a big change ships or when asked whether the talk is ready.
---

# Self-assessment

1. Run `.agents/skills/audience-simulation` on the current live deck.
2. Check the time budget: add up the notes' time windows and leave 10 to 20 percent for live overrun.
3. Check the standing rules in `AGENTS.md` against every slide and note.
4. Return feedback in exactly this format:

```
## Scores
Persona: n/10, one line each. Average and range.

## By slide
NN · Slide name
- Signal: high | low
- Issue: what the room will do or think, quoting the slide
- Raised by: which personas

## Rules check
Pass or fail per standing rule, with the slide that fails.

## Pacing
Planned total, likely total with overrun, minutes left for questions.

## Top fixes
Up to 5, high signal only, each as one concrete edit to index.html.

## Likely Q&A
The 5 most likely questions, each with a one-line answer.
```

5. Hand the top fixes to the speaker. Nothing ships from self-assessment until the speaker says which fixes go in; then each one goes through the intake flow in `AGENTS.md`.
