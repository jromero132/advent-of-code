"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=2 ; task=2)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        line_parts = line.split()
        i, j = (int(x) - 1 for x in line_parts[0].split("-"))
        ans += (line_parts[2][i] == line_parts[1][0]) != (line_parts[2][j] == line_parts[1][0])

    print(ans)


if __name__ == "__main__":
    main()
