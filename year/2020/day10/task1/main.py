"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=10 ; task=1)
"""

import sys


def main() -> None:
    adapters = [0, *sorted(int(x) for x in sys.stdin.read().strip().split("\n"))]
    jolt1, jolt3 = 0, 0
    for a1, a2 in zip(adapters, adapters[1:]):
        jolt1 += a2 - a1 == 1
        jolt3 += a2 - a1 == 3

    print(jolt1 * (jolt3 + 1))


if __name__ == "__main__":
    main()
