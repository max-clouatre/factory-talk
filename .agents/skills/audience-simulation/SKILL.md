---
name: audience-simulation
description: Simulate the meetup audience reading the deck, slide by slide, with speaker notes. Use to find where a real room tunes out, pushes back or gets confused.
---

# Audience simulation

## The panel

Ten personas, picked to match a Midwest AI engineering meetup: regulated industries, consultancies and startups.

1. Skeptical staff engineer, 15 years in, enterprise Java shop
2. Engineering manager with 8 reports
3. Product manager at a SaaS company
4. Delivery lead / scrum master at a consultancy
5. Platform and developer-experience engineer who owns CI
6. Security and compliance lead in a regulated industry
7. Startup founder, 3 engineers, heavy agent user
8. Junior developer, 1 year in
9. Non-technical VP of operations, brought by their team
10. The meetup organizer, who asked speakers for real implementation stories

## How to run it

1. Load the live `index.html`, including every `aside.notes`.
2. For each persona, separately, before reading any other persona's output: walk the deck in order, as that person, reading each slide and what the speaker will say.
3. Each persona logs:
   - **Tunes out:** the slide where they stop listening, and why
   - **Remembers:** the one line they'd repeat at work tomorrow
   - **Pushback:** what they'd argue with, quoting the slide
   - **Confused:** words or jumps they couldn't follow
   - **Q&A:** the question they'd ask
   - **Score:** out of 10
4. Only then, tally across personas.

## Signal

- **High:** raised independently by 3 or more personas, or a single issue that breaks credibility with a technical room.
- **Low:** one or two personas, no credibility risk. Note it; don't chase it.
- Bold hot takes are only an issue if a persona misreads the meaning, never just for being spicy.
- All ten are one model playing roles. Treat agreement as a strong hint, not proof.
