#!/usr/bin/env python3
"""Validation station: checks index.html against the standing rules in AGENTS.md.

Runs locally (python3 checks/validate.py) and on every push (.github/workflows/validate.yml).
Exits non-zero and lists every failure. Standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
TITLE = "Applied AI Architect"
BANNED = ["fnbo", "first national", "campaigner", "french canadian", "lead engineer", "(draft"]
TOTAL_MIN = 20 * 60
QUESTIONS_BY = 17 * 60 + 15

failures = []


def fail(msg):
    failures.append(msg)


def secs(t):
    m, s = t.split(":")
    return int(m) * 60 + int(s)


# 1. Public repo: nothing about the employer, no retired wording.
low = HTML.lower()
for word in BANNED:
    if word in low:
        fail(f"banned wording on the page: '{word}'")

# 2. Speaker title, everywhere.
if HTML.count(TITLE) < 2:
    fail(f"speaker title '{TITLE}' should appear on the title slide and About me")

# 3. Slides: numbering, notes, time windows, steps, cues.
slides = re.findall(r'<!-- (\d+) · [^>]*-->\s*<section class="slide[^"]*"([^>]*)>(.*?)</section>', HTML, re.S)
sections = re.findall(r'<section class="slide', HTML)
if len(slides) != len(sections):
    fail(f"{len(sections)} slides but {len(slides)} have a numbered comment right above them")

prev_end = 0
for i, (num, attrs, body) in enumerate(slides, 1):
    name = re.search(r'data-name="([^"]*)"', attrs)
    label = f"slide {i} ({name.group(1) if name else '?'})"
    if int(num) != i:
        fail(f"{label}: numbered comment says {num}")
    notes = re.search(r'<aside class="notes">(.*?)</aside>', body, re.S)
    if not notes:
        fail(f"{label}: no speaker notes")
        continue
    window = re.search(r"(\d+:\d\d) to (\d+:\d\d)", notes.group(1))
    if not window:
        fail(f"{label}: notes have no time window like '1:30 to 3:00'")
        continue
    start, end = secs(window.group(1)), secs(window.group(2))
    if start != prev_end:
        fail(f"{label}: starts at {window.group(1)}, but the previous slide ends at {prev_end // 60}:{prev_end % 60:02d}")
    if end <= start:
        fail(f"{label}: time window runs backwards")
    prev_end = end
    steps = re.search(r'data-steps="(\d+)"', attrs)
    used = [int(n) for n in re.findall(r'data-step="(\d+)"', body)]
    declared = int(steps.group(1)) if steps else 0
    if used and max(used) != declared:
        fail(f"{label}: data-steps is {declared} but the highest data-step is {max(used)}")
    if declared and not used:
        fail(f"{label}: data-steps is {declared} but nothing on the slide steps in")
    if "data-cue=" not in attrs:
        fail(f"{label}: no chapter card (data-cue)")
    if i < len(slides) and "data-next=" not in attrs:
        fail(f"{label}: no next-slide line (data-next)")

if prev_end > QUESTIONS_BY:
    fail(f"talk content runs to {prev_end // 60}:{prev_end % 60:02d}; questions must start by 17:15")
if prev_end > TOTAL_MIN:
    fail("talk runs past 20:00")

# 4. Legibility: the 18pt floor is set for presentation-size screens, and no inline style undercuts it.
floor = re.search(r"@media \(min-width: 1100px\) \{(.*?)\n\}", HTML, re.S)
if not floor or "max(18pt" not in floor.group(1):
    fail("missing the 18pt body floor for presentation-size screens")
else:
    for sel in (".eyebrow", ".tree", ".cue"):
        if sel not in floor.group(1):
            fail(f"18pt floor does not cover {sel}")
for px in re.findall(r'style="[^"]*font-size:\s*(\d+)px', HTML):
    if int(px) < 24:
        fail(f"inline font-size {px}px is under 18pt")

if failures:
    print(f"FAIL: {len(failures)} rule(s) broken")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print(f"OK: {len(slides)} slides, content ends at {prev_end // 60}:{prev_end % 60:02d}, all standing rules hold")
