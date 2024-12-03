"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=2 ; task=2)
"""

import sys


def is_safe_report(nums: list[int]) -> bool:
    """
    Check if a list of numbers represents a safe report.

    A report is considered safe if the differences between consecutive numbers are either all between 1 and 3
    (inclusive) in ascending order, or all between -3 and -1 (inclusive) in descending order.

    Args:
        nums (list[int]): A list of integers to check.

    Returns:
        bool: True if the report is safe, False otherwise.

    """
    return all(1 <= nums[i] - nums[i - 1] <= 3 for i in range(1, len(nums))) or all(
        -3 <= nums[i] - nums[i - 1] <= -1 for i in range(1, len(nums))
    )


def main() -> None:
    ans = 0
    for line in sys.stdin:
        nums = [int(x) for x in line.split()]
        for i in range(len(nums) + 1):
            if is_safe_report(nums[:i] + nums[i + 1 :]):
                ans += 1
                break

    print(ans)


if __name__ == "__main__":
    main()
