"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=2 ; task=2)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        line = line.split()
        i, j = (int(x) - 1 for x in line[0].split("-"))
        ans += (line[2][i] == line[1][0]) != (line[2][j] == line[1][0])

    print(ans)


if __name__ == "__main__":
    main()
