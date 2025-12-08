"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=6 ; task=1)
"""

import sys
from math import prod


def main() -> None:
    array = [line.split() for line in sys.stdin.read().splitlines()]
    ans = 0
    for problem in map(list, zip(*array)):
        ans += sum(map(int, problem)) if problem.pop() == "+" else prod(map(int, problem))

    print(ans)


if __name__ == "__main__":
    main()
