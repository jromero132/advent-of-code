"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=6 ; task=1)
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
    for x, y in coords[1:]:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    areas, infinite_areas = {coord: 0 for coord in coords}, set()
    for i, j in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        min_dist, cur_idx = get_manhattan_distance((i, j), coords[0]), 0
        for k in range(1, len(coords)):
            cur_dist = get_manhattan_distance((i, j), coords[k])

            if cur_dist < min_dist:
                min_dist, cur_idx = cur_dist, k

            elif cur_dist == min_dist:
                cur_idx = -1

        if cur_idx != -1:
            areas[coords[cur_idx]] += 1
            if j in (min_y, max_y) or i in (min_x, max_x):
                infinite_areas.add(coords[cur_idx])

    print(max(v for k, v in areas.items() if k not in infinite_areas))


if __name__ == "__main__":
    main()
