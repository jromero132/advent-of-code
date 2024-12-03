"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=3 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        sides = [int(x) for x in line.split()]
        ans += sum(sides) > 2 * max(sides)
    print(ans)


if __name__ == "__main__":
    main()
