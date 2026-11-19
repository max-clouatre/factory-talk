# Change request

Every change to the deck comes in through this shape, whoever asks and whichever session picks it up. Copy it, fill it in, then follow the intake flow in `AGENTS.md`.

- **Ask, in plain words:** what should change, as the requester said it.
- **Slide(s):** number and name, from the slide bar (STN 07/19).
- **Why:** what the room should get from it.
- **Time:** does it add time? If so, where does that time come from?
- **Done when:** what someone sees on the live slide once it's right.

Before shipping:

- [ ] `python3 checks/validate.py` passes
- [ ] Speaker notes updated in `aside.notes`
- [ ] One commit to `main`, message says what and why
- [ ] Opened on the live page at presentation size and looked at
