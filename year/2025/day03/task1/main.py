"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=3 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin.read().splitlines():
        digit1 = max(line[:-1])
        digit2 = max(line[line.index(digit1) + 1:])
        ans += int(digit1 + digit2)

    print(ans)


if __name__ == "__main__":
    main()
