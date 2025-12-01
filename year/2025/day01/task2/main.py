"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=1 ; task=2)
"""

import sys


def main() -> None:
    ans = 0
    dial = 50
    for line in sys.stdin:
        num = int(line[1:])

        if line[0] == 'L':
            ans += abs(dial - num) // 100 + (dial != 0 and dial <= num)
            dial = (dial - num) % 100

        else:
            ans += (dial + num) // 100
            dial = (dial + num) % 100

    print(ans)


if __name__ == "__main__":
    main()
