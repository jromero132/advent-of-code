"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=6 ; task=2)
"""

import itertools
import sys


def get_manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    """
    Calculate the Manhattan distance between two points in a 2D space.

    This function computes the distance between two points defined by their x and y coordinates using the Manhattan
    distance formula, which sums the absolute differences of their coordinates.

    Args:
        point1 (tuple[int, int]): The first point as a tuple of (x, y) coordinates.
        point2 (tuple[int, int]): The second point as a tuple of (x, y) coordinates.

    Returns:
        int: The Manhattan distance between the two points.

    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def main() -> None:
    coords = [tuple(int(x) for x in line.split(", ")) for line in sys.stdin]
    min_x, min_y, max_x, max_y = coords[0][0], coords[0][1], coords[0][0], coords[0][1]
    max_dist = 32 if len(coords) < 10 else 10000
    for x, y in coords[1:]:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(
        sum(
            sum(get_manhattan_distance((i, j), coord) for coord in coords) < max_dist
            for i, j in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1))
        ),
    )


if __name__ == "__main__":
    main()
