"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=4 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        parts = line.split()
        ans += len(parts) == len(set(parts))

    print(ans)


if __name__ == "__main__":
    main()
