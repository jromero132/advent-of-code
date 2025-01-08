"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=25 ; task=1)
"""

import sys
from itertools import combinations


def main() -> None:
    schematics = sys.stdin.read().strip().split("\n\n")
    print(
        sum(
            not any(x1 == x2 == "#" for x1, x2 in zip(schematic1, schematic2))
            for schematic1, schematic2 in combinations(schematics, 2)
        ),
    )


if __name__ == "__main__":
    main()
