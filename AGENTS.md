# Factory Talk

This repo is a small factory with one product: a 20-minute talk, "Build the Factory, Not the Feature", for the AI Engineer Omaha meetup.

The product is `index.html`, a single self-contained slide deck. GitHub Pages serves it from `main`, so every push to `main` is a release.

Any agent working here reads this file first, then the skills it names.

## Standing rules

These hold for every change, from every session, without being restated.

- **One buzzword.** "Factory" is the only one, and it means one thing: the shared system your team builds, that builds your product. Don't introduce "harness", "agentic" or friends on screen.
- **Speaker title** is "Applied AI Architect", everywhere.
- **Public repo.** Nothing about the speaker's employer, its projects, people or numbers. Keep every example a general pattern.
- **Time budget.** 20 minutes total. Each slide's notes carry its time window; questions start no later than 17:15. If a change adds time, take it from somewhere else in the same change.
- **Legibility.** 18pt minimum for anything on a slide. Keep the print layout working.
- **Voice and look** follow `.agents/skills/brand-voice`.

## Intake flow

1. **Request comes in** as plain words: "add a slide after 4", "sharpen hot take 3".
2. **Apply it** to `index.html`. Match the existing slide markup and CSS, put speaker notes in `aside.notes`, and keep the slide-number comments and time windows in order.
3. **Check it** against the standing rules: one buzzword, no employer details, 18pt, time budget still adds up, keyboard controls (arrows, N, T, R) still work.
4. **Ship it.** One commit per request, with a message that says what changed and why, pushed to `main`. Pages is live about a minute later.
5. **Verify live.** Open the deployed slide at presentation size and look at it before reporting back.

Bigger changes (new slides, reordering, cuts) also run `.agents/skills/self-assessment` before and after.

## Skills

| Skill | Use it when |
|---|---|
| `.agents/skills/brand-voice` | Writing or rewording anything on a slide or in the notes |
| `.agents/skills/audience-simulation` | You need to know how a real room will read the deck |
| `.agents/skills/self-assessment` | Before a big change ships, or when asked "is this ready?" |

## The improvement loop

Self-assessment feedback is not a to-do list. Changes that fix an issue raised by 3 or more personas, or a single credibility risk, go into the deck. When a fix reveals a rule that should always hold, add it to the standing rules above, so the next change follows it for free.
