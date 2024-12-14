"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=14 ; task=1)
"""

import itertools
import math
import sys


def main() -> None:
    robots = [
        [[int(x) for x in s[2:].split(",")] for s in line.strip().split(" ")] for line in sys.stdin
    ]
    size = [11, 7] if len(robots) <= 15 else [101, 103]
    for _, (p, v) in itertools.product(range(100), robots):
        for i in range(len(size)):
            p[i] += v[i]
            if p[i] < 0 or p[i] >= size[i]:
                p[i] %= size[i]

    for i in range(len(size)):
        size[i] //= 2

    quadrants = [0] * 4
    for p, _ in robots:
        q, valid = 0, True
        for i in range(len(size)):
            valid &= p[i] != size[i]  # Middle horizontal and vertical lines
            q |= (p[i] > size[i]) << i

        if valid:
            quadrants[q] += 1

    print(math.prod(quadrants))


if __name__ == "__main__":
    main()
