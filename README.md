[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/h05meigames2/alien-field-notes-25nov26/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/h05meigames2/alien-field-notes-25nov26/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

# Alien Field Notes: The Two Day Earth Review

A one-line review of planet Earth, left by an alien tourist after a two-day visit. The locals built a network holding all human knowledge — and spent the whole visit arguing about whether their own planet is round.

> Locals built a network holding all human knowledge, then spent my whole two-day visit arguing whether their planet is round. 3/5 stars — the network works, the users don't.

## Run locally

Requires Python 3.13 (standard library only, no network access):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/alien-field-notes-out python3 main.py
cat /tmp/alien-field-notes-out/entry.txt
```

`main.py` validates the line (exactly one line, 1–200 characters) and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
