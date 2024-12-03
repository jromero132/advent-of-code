"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=2 ; task=2)
"""

import sys


def is_safe_report(nums):
    return all(1 <= nums[i] - nums[i - 1] <= 3 for i in range(1, len(nums))) or all(
        -3 <= nums[i] - nums[i - 1] <= -1 for i in range(1, len(nums))
    )


def main():
    ans = 0
    for line in sys.stdin:
        nums = [int(x) for x in line.split()]
        for i in range(0, len(nums) + 1):
            if is_safe_report(nums[:i] + nums[i + 1 :]):
                ans += 1
                break

    print(ans)


if __name__ == "__main__":
    main()
