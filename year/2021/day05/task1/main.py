"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=5 ; task=1)
"""

import sys
from collections.abc import Generator


def translate(lines: list[list[list[int]]]) -> tuple[int, int]:
    """Translate a list of vent lines into a list of dimensions by normalizing their coordinates.

    This function takes a list of vent lines coordinates, calculates the minimum and maximum values
    for each dimension, and adjusts the coordinates to start from zero. It returns a list which is
    the maximum X and Y values of the box, so now all the segments of the vents are in the box
    (0, 0) x (X, Y).

    Args:
        lines (list[list[list[int]]]): A nested list containing integer coordinates representing
            vent segments.

    Returns:
        tuple[int, int]: A tuple of integers representing the maximum X and Y values of the box, so
            now all the segments of the vents are in the box (0, 0) x (X, Y).
    """
    min_vals = list(lines[0][0])
    max_vals = list(lines[0][0])

    for line in lines:  # get minimum and maximum x, y values
        for vent in line:
            for i in range(len(vent)):
                min_vals[i] = min(min_vals[i], vent[i])
                max_vals[i] = max(max_vals[i], vent[i])

    for line in lines:  # update cells based on the minimum x, y values
        for point in line:
            for i in range(len(min_vals)):
                point[i] -= min_vals[i]

    return (
        ma - mi + 1 for ma, mi in zip(max_vals, min_vals)
    )  # max x, y values so the box is (0, 0) x (x, y)


def generate(v1: list[int], v2: list[int]) -> Generator[int, None, None]:
    """Generate a sequence of points between two given vent coordinates.

    This function yields points starting from the first coordinate and incrementally moves towards
    the second coordinate. It continues to yield points until the two coordinates are equal,
    effectively generating all intermediate points.

    Args:
        v1 (list[int]): The starting coordinate as a list of integers.
        v2 (list[int]): The ending coordinate as a list of integers.

    Yields:
        list[int]: The next point in the sequence of coordinates between v1 and v2.
    """
    sign = [1 if v1[i] <= v2[i] else -1 for i in range(len(v1))]
    yield v1
    while v1 != v2:
        for i in range(len(v1)):  # Generate next point, and try to move diagonally first
            if v1[i] != v2[i]:
                v1[i] += sign[i]
        yield v1


def main():
    lines = [
        [[int(n) for n in point.split(",")] for point in line.split(" -> ")] for line in sys.stdin
    ]
    n, m = translate(lines)
    field = [[0] * m for _ in range(n)]

    for v1, v2 in lines:
        if v1[0] == v2[0] or v1[1] == v2[1]:
            for i, j in generate(v1, v2):
                field[i][j] += 1

    print(sum(cell >= 2 for row in field for cell in row))


if __name__ == "__main__":
    main()
