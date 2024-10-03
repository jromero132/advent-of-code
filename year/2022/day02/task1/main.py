"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=2 ; task=1)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        p1 = ord(line[0]) - ord("A")
        p2 = ord(line[2]) - ord("X")
        result = (3 + p1 - p2) % 3
        ans += p2 + 1 + 3 * ((1 - result) % 3)

    print(ans)


if __name__ == "__main__":
    main()
