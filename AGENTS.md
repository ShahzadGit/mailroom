# AGENTS.md

## Project

Mailroom is a command-line tool for one newsletter: IMCG, Humak (Admissions).
It reads the subscribers, checks an issue, and sends it to a practice mail server.

## Rules

- Use uv for everything (install, add packages, run scripts, run tests). Do not use pip, venv, or python directly.
- Never use a real person's email address. Use `@example.com`, and `@resend.dev` for practice sends.
- Commit and push after every step.
- Behaviors first. I give the expected answers, you write them as pytest tests in `test_mailroom.py` (one test per behavior, named for the behavior), show them failing with `uv run pytest`, then write the code.
- I decide the test cases and their answers. Never change an expected answer to make a test pass.
- Never read today's date inside the logic. Pass the run date in. Only the command line may read today's date.
- When something breaks, show me the full error before changing anything.
- Count text length the way Python's `len()` counts (code points). An emoji with a skin tone, like 👍🏽, counts as 2.

## How I learn

- I am an intermediate Python programmer. Describe the code to me concisely in simple words.
- Write only with what I have learned. If something new would really help, stop and tell me its name in one line.
- When the code uses something new, show me that piece first and ask me to predict what it does.
  Stay quiet while I guess. Then run it, and explain a line only when I ask.
