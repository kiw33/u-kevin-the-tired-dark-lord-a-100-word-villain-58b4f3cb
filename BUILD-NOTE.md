# BUILD-NOTE — The Tired Dark Lord: A 100-Word Villain Monologue

- Competition: `u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb`
- Prize: $2
- Deadline: 2026-11-25 12:30 UTC (19:30 WIB 25 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of 1-600 characters, not only whitespace.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).
  No `main.ts` — a second entrypoint would be ambiguous.

## Entry text

> You stand before me in chains of black iron — do you know what that iron costs these days? The mines flooded in spring, the smiths want hazard pay, and my quartermaster — bless his treacherous little heart — has been skimming the war chest since the eclipse. I had a speech prepared, something about eternal night and the doom of kings, but honestly, hero, if you could just sign this surrender form in triplicate — one copy for the archives, one for the ravens, one for my mother — I would owe you a debt darker than any curse.

- Words: 100 (exactly, whitespace-split; brief asks "about 100 words")
- Characters: 528 (gate: 1-600 characters)
- Bytes (UTF-8): 538 (each em dash is 3 bytes)
- Lines: 1, no trailing newline
- Whitespace-only: no

## Why this monologue

The tiredness is never announced — no "tired", "weary" or "exhausted"
anywhere. It leaks out through the voice instead: a villain who opens
with the price of black iron, complains about flooded mines and hazard
pay, and would rather have the hero sign a surrender form in triplicate
(one copy for the archives, one for the ravens, one for his mother) than
deliver the eternal-night speech he actually prepared. The scheme (the
surrender, the war chest, the eclipse) and the history (the skimming
quartermaster, the prepared speech about the doom of kings) keep him a
villain; the paperwork is the deflection. The last line turns the
bureaucracy back into menace: a debt darker than any curse.

Original work — no anchor, rung, or house text from the kit was copied.

## Verification (local, run 2026-11-25)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 `0a45a61495369642bd436a32e9efc968b842a8d2d2e801027d89cc8398a7bde8` on both runs), gate check passed:
   UTF-8 decodes, 528 characters within 1-600 characters, exactly 100 words,
   single line, not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), len(t.split()))"
```

Kit check (`node <kit>/cli/makefun.mjs check --worktree`, 2026-11-25):
4 passed (competition_open, snapshot, license_osi, entrypoint); only
`transcripts_present` failed, as expected before bundling transcripts.

## Repo note for the submitter

- `.makefun/owner.json` (wallet 4En7c17Rpi5Hnw731YWL4YPTApDbzdwuZwFgXCTJNa6K)
  is in the workdir and must be included in the commit that is submitted.
- Run `node <kit>/cli/makefun.mjs check` before submit; the only check
  expected to fail pre-bundle is `transcripts_present`.
