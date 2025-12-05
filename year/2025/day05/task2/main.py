"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=5 ; task=2)
"""

import sys


def main() -> None:
    inp_ranges, _ = sys.stdin.read().split("\n\n")
    inp_ranges = sorted([*map(int, i.split("-"))] for i in inp_ranges.splitlines())

    ranges = [inp_ranges[0]]
    for l, r in inp_ranges[1:]:
        if l <= ranges[-1][1]:
            ranges[-1][1] = max(ranges[-1][1], r)

        else:
            ranges.append([l, r])

    print(sum(r - l + 1 for l, r in ranges))


if __name__ == "__main__":
    main()
