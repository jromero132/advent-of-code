"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=2 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        nums = [int(n) for n in line.split()]
        ans += max(nums) - min(nums)

    print(ans)


if __name__ == "__main__":
    main()
