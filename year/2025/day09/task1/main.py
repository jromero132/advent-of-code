"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=9 ; task=1)
"""

import sys
from itertools import product


def main() -> None:
    points = [tuple(map(int, line.split(","))) for line in sys.stdin.read().splitlines()]

    ans = 0
    for (x1, y1), (x2, y2) in product(points, points):
        ans = max(ans, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

    print(ans)


if __name__ == "__main__":
    main()
