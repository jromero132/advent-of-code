"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=7 ; task=2)
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
        for mask in range(3**n):
            res = nums[0]
            for bit in range(n):
                match mask % 3:
                    case 0:
                        res = res + nums[bit + 1]

                    case 1:
                        res = res * nums[bit + 1]

                    case 2:
                        res = int(str(res) + str(nums[bit + 1]))

                if res > expected:
                    break

                mask //= 3

            if res == expected:
                ans += expected
                break
    print(ans)


if __name__ == "__main__":
    main()
