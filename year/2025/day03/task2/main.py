"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=3 ; task=2)
"""

import sys


def main() -> None:
    N_TURNS = 12
    ans = 0
    for line in sys.stdin.read().splitlines():
        digits = []
        for i in range(N_TURNS - 1, -1, -1):
            digits.append(max(line[:-i]) if i != 0 else max(line))
            line = line[line.index(digits[-1]) + 1:]

        ans += int("".join(digits))
    print(ans)


if __name__ == "__main__":
    main()
