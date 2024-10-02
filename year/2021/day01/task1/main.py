"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=1 ; task=1)
"""

import sys


def main():
    ans = 0
    prev = int(sys.stdin.readline())
    for cur in (int(x) for x in sys.stdin):
        ans += prev < cur
        prev = cur

    print(ans)


if __name__ == "__main__":
    main()
