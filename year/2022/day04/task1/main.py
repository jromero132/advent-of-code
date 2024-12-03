"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=4 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for s1, s2 in (line.split(",") for line in sys.stdin):
        r1 = [int(x) for x in s1.split("-")]
        r2 = [int(x) for x in s2.split("-")]

        # check if one section fully overlaps the other
        ans += (r1[0] <= r2[0] and r2[1] <= r1[1]) or (r2[0] <= r1[0] and r1[1] <= r2[1])

    print(ans)


if __name__ == "__main__":
    main()
