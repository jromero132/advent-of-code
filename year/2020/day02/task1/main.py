"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=2 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        line_parts = line.split()
        mi, ma = (int(x) for x in line_parts[0].split("-"))
        ans += mi <= line_parts[2].count(line_parts[1][0]) <= ma

    print(ans)


if __name__ == "__main__":
    main()
