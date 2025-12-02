"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=2 ; task=2)
"""

import sys
from itertools import accumulate
from bisect import bisect_left


def main() -> None:
    invalid_ids_set = set()
    for i in range(1, 10**6):
        str_i = str(i)

        for r in range(2, 10 // len(str_i) + 1):
            invalid_ids_set.add(int(str_i * r))

    invalid_ids = sorted(invalid_ids_set)
    pref_sum = [0, *accumulate(invalid_ids)]

    pairs = sys.stdin.read().strip().split(",")
    ans = 0
    for pair in pairs:
        l, r = map(int, pair.split("-"))
        pos_l = bisect_left(invalid_ids, l)
        pos_r = bisect_left(invalid_ids, r + 1)
        ans += pref_sum[pos_r] - pref_sum[pos_l]
    print(ans)


if __name__ == "__main__":
    main()
