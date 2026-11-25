#!/usr/bin/env python3
"""make.fun entry: The Tired Dark Lord: A 100-Word Villain Monologue
(u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb).

Writes one monologue of exactly 100 words, spoken by a fantasy villain
who is secretly just very tired, to /output/entry.txt. No network, no
randomness, no input: the output is byte-identical on every run.
"""

ENTRY = "You stand before me in chains of black iron \u2014 do you know what that iron costs these days? The mines flooded in spring, the smiths want hazard pay, and my quartermaster \u2014 bless his treacherous little heart \u2014 has been skimming the war chest since the eclipse. I had a speech prepared, something about eternal night and the doom of kings, but honestly, hero, if you could just sign this surrender form in triplicate \u2014 one copy for the archives, one for the ravens, one for my mother \u2014 I would owe you a debt darker than any curse."
# The single submitted monologue; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the monologue to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
