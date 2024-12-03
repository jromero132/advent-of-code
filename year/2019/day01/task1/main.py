"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=1 ; task=1)
"""

import sys


def main() -> None:
    print(sum(int(module) // 3 - 2 for module in sys.stdin))


if __name__ == "__main__":
    main()
