"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=2 ; task=1)
"""

import sys


def main():
    two_letters, three_letters = 0, 0
    for line in sys.stdin:
        cnt = {}
        for c in line:
            cnt[c] = cnt.get(c, 0) + 1

        two_letters += any(v == 2 for v in cnt.values())
        three_letters += any(v == 3 for v in cnt.values())

    print(two_letters * three_letters)


if __name__ == "__main__":
    main()
