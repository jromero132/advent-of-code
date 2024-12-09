"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=7 ; task=1)
"""

import sys


def main() -> None:
    bottom, above = set(), set()
    for line in sys.stdin:
        program_def = line.strip().split(" -> ")
        program = program_def[0]
        programs_above = program_def[1] if len(program_def) == 2 else ""
        bottom.add(program.split()[0])
        for p in programs_above.split(", "):
            above.add(p)

    print((bottom - above).pop())


if __name__ == "__main__":
    main()
