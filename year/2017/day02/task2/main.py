"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=2 ; task=2)
"""

import sys


def get_divisible_value(nums: list[int]) -> int:
    """Find the first pair of numbers in the list that are divisible.

    This function iterates through a list of integers to identify the first pair of numbers where
    one number is divisible by the other. It returns the result of the division of the larger number
    by the smaller number.

    Args:
        nums (list[int]): A list of integers to check for divisibility.

    Returns:
        int: The result of the division of the two divisible numbers, or None if no such pair
            exists.
    """
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
