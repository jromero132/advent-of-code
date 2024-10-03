"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=2 ; task=1)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        line = line.split()
        mi, ma = (int(x) for x in line[0].split("-"))
        ans += mi <= line[2].count(line[1][0]) <= ma

    print(ans)


if __name__ == "__main__":
    main()
