"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=14 ; task=1)
"""

import sys
from collections import defaultdict

from sortedcontainers import SortedDict


def set_rocks(
    grid: dict[tuple[int, int], SortedDict],
    p1: tuple[int, int],
    p2: tuple[int, int],
) -> None:
    """
    Set rocks in a grid based on two specified points.

    This function updates a grid by marking the positions of rocks between two points, either horizontally or
    vertically. It modifies the grid in place, setting the appropriate cells to indicate the presence of rocks.

    Args:
        grid (dict[tuple[int, int], SortedDict]): The grid where rocks will be set, represented as a dictionary of
            coordinates.
        p1 (tuple[int, int]): The first point defining the rock placement.
        p2 (tuple[int, int]): The second point defining the rock placement.

    """
    if p1[0] == p2[0]:
        for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            grid[p1[0]][i] = -1

    else:
        for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            grid[i][p1[1]] = -1


def fall(grid: dict[tuple[int, int], SortedDict], x: int, y: int) -> tuple[int, int] | None:
    """
    Determine the next position of falling sand in a grid.

    This function checks the grid to find the next available position for sand falling from a specified coordinate. It
    returns the new position if available, or None if the sand cannot fall further.

    Args:
        grid (dict[tuple[int, int], SortedDict]): The grid representing the environment where the sand falls.
        x (int): The x-coordinate from which the sand is falling.
        y (int): The y-coordinate from which the sand is falling.

    Returns:
        tuple[int, int] | None: The new position of the sand as a tuple of coordinates, or None if it cannot fall.

    """
    d = grid[x]
    if y in d:
        return None

    idx = d.bisect_left(y)
    return None if len(d) == idx else (x, d.peekitem(idx)[0] - 1)


def main() -> None:
    paths = [
        [[int(x) for x in point.split(",")] for point in path.strip().split(" -> ")]
        for path in sys.stdin
    ]

    sand_x, sand_y = 500, 0
    grid = defaultdict(SortedDict)

    for path in paths:
        for i in range(1, len(path)):
            set_rocks(grid, path[i - 1], path[i])

    while True:
        p = fall(grid, sand_x, sand_y)
        while p is not None:  # continuously drop the sand
            if p[1] + 1 not in grid[p[0] - 1]:
                p = fall(grid, p[0] - 1, p[1] + 1)

            elif p[1] + 1 not in grid[p[0] + 1]:
                p = fall(grid, p[0] + 1, p[1] + 1)

            else:
                break

        if p is None:
            break

        grid[p[0]][p[1]] = 1
        if p == (sand_x, sand_y):
            break

    print(sum(list(col.values()).count(1) for col in grid.values()))


if __name__ == "__main__":
    main()
