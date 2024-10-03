"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=2 ; task=2)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        p1 = ord(line[0]) - ord("A")  # 0=rock ; 1=paper ; 2=scissors
        result = (1 - ord(line[2]) + ord("X")) % 3  # 0=tie ; 1=p1 wins ; 2=p2 wins
        p2 = (3 + p1 - result) % 3  # 0=rock ; 1=paper ; 2=scissors
        ans += p2 + 1 + 3 * ((1 - result) % 3)

    print(ans)


if __name__ == "__main__":
    main()
