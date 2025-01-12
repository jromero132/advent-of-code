"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=10 ; task=2)
"""

import sys


def get_box(points: list[list[list, list]]) -> tuple[int, int, int, int]:
    min_x, min_y = points[0][0]
    max_x, max_y = points[0][0]
    for point in points[1:]:
        min_x = min(min_x, point[0][0])
        min_y = min(min_y, point[0][1])
        max_x = max(max_x, point[0][0])
        max_y = max(max_y, point[0][1])

    return min_x, max_x, min_y, max_y


def get_rect_area(points: list[list[list, list]]) -> int:
    min_x, max_x, min_y, max_y = get_box(points)
    return (max_x - min_x) * (max_y - min_y)


def main() -> None:
    points = []
    for line in sys.stdin:
        _, p, v = line.strip().split("=")
        p = [int(x) for x in p.split(">")[0][1:].split(", ")]
        v = [int(x) for x in v[1:-1].split(", ")]
        points.append([p, v])

    # I assume that the optimal position for the message is at the smallest rectangle area that contains all the points
    min_rect, seconds = get_rect_area(points), 0
    for i in range(2 * 10**4):  # This is the upper bound
        for point in points:
            point[0][0] += point[1][0]
            point[0][1] += point[1][1]

        if (new_area := get_rect_area(points)) < min_rect:
            min_rect = new_area
            seconds = i + 1

    print(seconds)


if __name__ == "__main__":
    main()
