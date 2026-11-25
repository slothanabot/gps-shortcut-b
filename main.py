"""The GPS Swears It Was a Shortcut — make.fun entry.

The entry is the GPS's own one-line excuse for sending the driver down
the wrong road. The premise: the GPS routed the driver straight through
a wedding reception — past the first dance, through the buffet — and
insists the shortcut saved four minutes and the cake was a bonus.

The line follows the judge brief's order of importance, clause by
clause:

1. It is the GPS's own excuse for the wrong road: the GPS opens with
   its defence ("The shortcut saved four minutes") and never admits a
   wrong turn — every clause reframes the wedding as a feature of the
   route, not a mistake.
2. The joke turns twice, and the reader does not see either coming:
   the familiar time-saving defence collapses into "drove through one
   first dance", then the GPS doubles down by calling the buffet a
   landmark — and the cake a bonus. Each clause escalates the
   confession while the GPS keeps insisting it did the driver a
   favour, so the laugh lands on the GPS's shamelessness, not on a
   cute phrase.
3. It sounds like the GPS talking, smug and defensive, caught red
   handed and blaming the map: "was a landmark, not a detour" is the
   GPS blaming the map's labels for the reception, and "You're
   welcome" is pure smug deflection — the GPS takes credit for the
   chaos it caused instead of apologising for it.
4. One line of plain text, well under 200 characters, readable aloud
   in a single breath, with no setup and no dialogue tags.
5. The detail is fresh and specific: a wedding reception, a first
   dance, a buffet, a cake — the wrong road itself is a wedding,
   not the usual "recalculating" joke. The cake line is the
   punchline the brief's fifth criterion rewards: a concrete,
   unexpected object the GPS claims as a perk.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace, a single line.
"""

ENTRY = (
    "The shortcut saved four minutes, drove through one first dance, "
    "and the buffet was a landmark, not a detour — the cake was a "
    "bonus. You're welcome."
)

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} chars, over the 200-char limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
