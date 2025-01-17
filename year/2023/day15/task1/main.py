"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=15 ; task=1)
"""

import sys


def main() -> None:
    sequences = sys.stdin.read().strip().replace("\n", "").split(",")
    ans = 0
    for sequence in sequences:
        h = 0
        for c in sequence:
            h = (h + ord(c)) * 17 % 256

        ans += h

    print(ans)


if __name__ == "__main__":
    main()
