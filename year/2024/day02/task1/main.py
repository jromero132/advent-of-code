"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=2 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        nums = [int(x) for x in line.split()]
        ans += all(1 <= nums[i] - nums[i - 1] <= 3 for i in range(1, len(nums))) or all(
            -3 <= nums[i] - nums[i - 1] <= -1 for i in range(1, len(nums))
        )

    print(ans)


if __name__ == "__main__":
    main()
