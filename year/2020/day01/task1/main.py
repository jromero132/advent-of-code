"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=1 ; task=1)
"""

import sys


def main() -> None:
    checked = set()
    for n in (int(line) for line in sys.stdin):
        checked.add(n)
        if 2020 - n in checked:
            print(n * (2020 - n))
            break


if __name__ == "__main__":
    main()
