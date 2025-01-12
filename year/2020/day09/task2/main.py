"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2020 ; day=9 ; task=2)
"""

import sys
from collections import defaultdict


def main() -> None:
    nums = [int(x) for x in sys.stdin.read().strip().split("\n")]
    valid = defaultdict(int)
    preamble = 5 if len(nums) <= 20 else 25
    for i in range(preamble):
        for j in range(i + 1, preamble):
            valid[nums[i] + nums[j]] += 1

    for i in range(preamble, len(nums)):
        if not valid[nums[i]]:
            target = nums[i]
            break

        for j in range(i - preamble + 1, i):
            valid[nums[i - preamble] + nums[j]] -= 1
            valid[nums[i] + nums[j]] += 1

    l, r, cur = 0, 0, 0
    while True:
        while cur + nums[r] > target:
            if l < r:
                cur -= nums[l]
            else:
                r += 1
            l += 1

        cur += nums[r]
        r += 1
        if cur == target and r - l >= 2:
            print(min(nums[l:r]) + max(nums[l:r]))
            break


if __name__ == "__main__":
    main()
