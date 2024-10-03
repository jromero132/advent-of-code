"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=3 ; task=2)
"""

import sys
from math import sqrt


def get_coords(pos: int) -> tuple[int, int]:
    if pos == 1:
        return 0, 0

    # The interval for `pos` goes from (2n - 1)² + 1 to (2n + 1)².
    r = int(sqrt(pos - 1) + 1) // 2  # Distance to the border box
    first = (2 * r - 1) ** 2 + 1  # First number in the border box
    pos_in_border = pos - first  # Position of the number in the border box
    border = pos_in_border // (2 * r)  # 0=right ; 1=top ; 2=left ; 3=bottom
    pos_in_side = pos_in_border % (2 * r)  # Position of the number in its side of the border box
    match border:
        case 0:  # Right
            return r, pos_in_side - r + 1

        case 1:  # Top
            return r - pos_in_side - 1, r

        case 2:  # Left
            return -r, r - pos_in_side - 1

        case 3:  # Bottom
            return pos_in_side - r + 1, -r


def main():
    target = int(sys.stdin.readline())
    grid = {(0, 0): 1}
    last, pos = 1, 1

    while last <= target:
        pos += 1
        x, y = get_coords(pos)
        grid[(x, y)] = last = sum(
            grid.get((x + i, y + j), 0) for i in range(-1, 2) for j in range(-1, 2)
        )

    print(last)


if __name__ == "__main__":
    main()
