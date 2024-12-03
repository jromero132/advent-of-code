"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=3 ; task=2)
"""

import itertools
import sys


def no_overlaps(
    grid: list[list[int]], rectangle: tuple[tuple[int, int], tuple[int, int], int]
) -> bool:
    """
    Check if a rectangle does not overlap with any other rectangle in the grid.

    This function determines whether all cells within the specified rectangle in the grid are not
    occupied by any other rectangle (indicated by a value of 1). It returns True if there are no
    overlaps, and False if any part of the rectangle overlaps with any other rectangle.

    Args:
        grid (list[list[int]]): A 2D list representing the grid of occupied spaces.
        rectangle (tuple[tuple[int, int], tuple[int, int]]): A tuple defining the top-left and
            bottom-right corners of the rectangle to check.

    Returns:
        bool: True if the rectangle does not overlap with any other rectangle in the grid.

    """
    return all(
        grid[i][j] == 1
        for i, j in itertools.product(
            range(rectangle[0][0], rectangle[1][0]),
            range(rectangle[0][1], rectangle[1][1]),
        )
    )


def main() -> None:
    max_x, max_y = 0, 0
    rectangles = []
    for line in sys.stdin:
        desc = line.split()
        rid = desc[0][1:]
        x, y = (int(n) for n in desc[2].strip(":").split(","))
        len_x, len_y = (int(n) for n in desc[3].split("x"))
        rectangles.append(((x, y), (x + len_x, y + len_y), rid))
        max_x = max(max_x, x + len_x)
        max_y = max(max_y, y + len_y)

    grid = [[0] * max_y for _ in range(max_x)]
    for rectangle in rectangles:
        for i, j in itertools.product(
            range(rectangle[0][0], rectangle[1][0]), range(rectangle[0][1], rectangle[1][1])
        ):
            grid[i][j] += 1

    for rectangle in rectangles:
        if no_overlaps(grid, rectangle):
            print(rectangle[2])
            break


if __name__ == "__main__":
    main()
