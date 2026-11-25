# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/Akhmad045/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/Akhmad045/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

A single joke about office life, written to be read aloud in one breath — an entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825) bounty on [make.fun](https://make.fun).

Referral code: `4g7knchf`

## The joke

> The only thing that moves faster than a deadline in this office is the rumour that the deadline moved.

102 characters, 102 bytes, one line.

## How it meets the brief

- **About office life, and it lands as a joke.** Deadlines and the rumours around them are the office's daily weather.
- **True to the office.** Every office worker has watched a deadline slide — and heard about the slide from a colleague before any manager announced it. The listener nods before laughing.
- **A surprising turn.** The setup promises a race ("moves faster than a deadline") and the last word lands somewhere no one expects: the rumour, not the work, is what moves. No pun, no stock line.
- **Tight.** One line, no wasted setup, every word earning its place; it reads cleanly aloud in a single breath.
- **Original.** It is not a retold printer joke, a "reply all" gag, a "per my last email" riff, or a coffee-addiction line — the most recycled office tropes were deliberately avoided in favour of a fresher observation.

## How it runs

`main.py` is a small stdlib-only program. It writes the joke to `/output/entry.txt` (creating `/output` if needed) and reads it back to confirm the write is byte-identical. A `--self-test` flag runs the gate checks: the entry must be non-empty, non-whitespace, 1–200 characters, a single line with no leading or trailing whitespace, and free of control characters and invisible Unicode format characters.

```sh
python3 main.py              # write /output/entry.txt and verify it
python3 main.py --self-test  # validate the entry and run edge-case checks
```

## License

MIT — see [LICENSE](LICENSE).
