"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=10 ; task=1)
"""

import math
import sys


def main() -> None:
    asteroids = [
        (j, i) for i, line in enumerate(sys.stdin) for j, c in enumerate(line.strip()) if c == "#"
    ]
    best = 0
    for i, (x1, y1) in enumerate(asteroids):
        sight = set()
        for j, (x2, y2) in enumerate(asteroids):
            if i == j:
                continue

            dx, dy = x2 - x1, y2 - y1
            gcd = math.gcd(dx, dy)
            sight.add((dx / gcd, dy / gcd))

        best = max(best, len(sight))

    print(best)


if __name__ == "__main__":
    main()
