"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=4 ; task=1)
"""

import sys


def main():
    ans = 0
    for line in sys.stdin:
        _, card = line.split(":")
        winning_nums, nums = (set(part.strip().split()) for part in card.split("|"))
        n = len(nums.intersection(winning_nums))
        ans += 0 if n == 0 else 2 ** (n - 1)

    print(ans)


if __name__ == "__main__":
    main()
