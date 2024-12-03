"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=3 ; task=1)
"""

import sys
from math import sqrt


def main() -> None:
    pos = int(sys.stdin.readline())
    if pos == 1:
        print(0)
        return

    # The interval for `pos` goes from (2n - 1)² + 1 to (2n + 1)².
    r = int(sqrt(pos - 1) + 1) // 2  # Distance to the border box
    first = (2 * r - 1) ** 2 + 1  # First number in the border box
    pos_in_border = pos - first + 1  # Position of the number in the border box
    pos_in_side = pos_in_border % (2 * r)  # Position of the number in its side of the border box

    # The radius will be traveled always.
    # Plus some extra steps according to the distance from the position in the side to the radius,
    # because the center will always in at position radius inside any side of the border box.
    # E.g.:
    #   - Border box: 10...25
    #   - Side of border box: 10...13 ; 14...17 ; 18...21 ; 22...25
    print(r + abs(pos_in_side - r))


if __name__ == "__main__":
    main()
