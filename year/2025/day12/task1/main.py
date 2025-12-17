"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=12 ; task=1)
"""

import sys

# This is a "Polyomino Packing problem", it is NP-complete in general.
# The only solution is brute-forcing with backtracking and early pruning.
# The idea is to add more and more pruning conditions until the solution works for the input of interest.
# NOTE: The solution works for the real input only, NOT the example!


def main() -> None:
    shapes = sys.stdin.read().split("\n\n")
    grids = shapes.pop()
    ans = 0
    for row in grids.splitlines():
        size, freq = row.split(": ")
        width, length = map(int, size.split("x"))
        total_freq = sum(map(int, freq.split()))
        ans += total_freq * 9 <= width * length
    print(ans)


if __name__ == "__main__":
    main()
