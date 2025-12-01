"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=1 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    dial = 50
    for line in sys.stdin:
        if line[0] == 'L':
            dial -= int(line[1:])

        else:
            dial += int(line[1:])

        dial %= 100
        ans += dial == 0

    print(ans)


if __name__ == "__main__":
    main()
