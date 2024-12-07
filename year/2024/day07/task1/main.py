"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=7 ; task=1)
"""

import sys


def main() -> None:
    lines = [line.strip() for line in sys.stdin]
    ans = 0
    for line in lines:
        expected, nums = line.split(": ")
        expected = int(expected)
        nums = [int(num) for num in nums.split()]
        n = len(nums) - 1
        for mask in range(2**n):
            res = nums[0]
            for bit in range(n):
                res = res * nums[bit + 1] if (1 << bit) & mask else res + nums[bit + 1]
                if res > expected:
                    break

            if res == expected:
                ans += expected
                break
    print(ans)


if __name__ == "__main__":
    main()
