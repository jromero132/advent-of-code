"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=2 ; task=2)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        p1 = ord(line[0]) - ord("A")
        result = (1 - ord(line[2]) + ord("X")) % 3
        p2 = (3 + p1 - result) % 3
        ans += p2 + 1 + (3, 0, 6)[result]

    print(ans)


if __name__ == "__main__":
    main()
