"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=1 ; task=2)
"""

import sys


def main():
    checked = set()
    for n in (int(line) for line in sys.stdin):
        checked.add(n)
        for m in checked:
            if 2020 - n - m in checked:
                print(n * m * (2020 - n - m))
                return


if __name__ == "__main__":
    main()
