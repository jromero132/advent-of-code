"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=2 ; task=2)
"""

import sys


def get_divisible_value(nums: list[int]) -> int:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] % nums[j] == 0:
                return nums[i] // nums[j]

            elif nums[j] % nums[i] == 0:
                return nums[j] // nums[i]

    return None  # Error


def main():
    ans = 0
    for line in sys.stdin:
        nums = [int(n) for n in line.split()]
        ans += get_divisible_value(nums)

    print(ans)


if __name__ == "__main__":
    main()
