"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=18 ; task=1)
"""

import sys


def get_polygon_area(vertices: list[tuple[int]]) -> float:  # shoelace theorem
    n = len(vertices)
    return (
        abs(
            sum(
                vertices[i][0] * vertices[(i + 1) % n][1]
                - vertices[(i + 1) % n][0] * vertices[i][1]
                for i in range(n)
            ),
        )
        / 2
    )


def get_polygon_perimeter(vertices: list[tuple[int]]) -> int:
    return sum(
        abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
        for v1, v2 in zip(vertices, vertices[1:] + [vertices[0]])
    )


def get_total_points(points: list[tuple[int]]) -> int:  # Pick's theorem
    return int(get_polygon_area(points) + get_polygon_perimeter(points) / 2) + 1


def main() -> None:
    polygon = [(0, 0)]
    for line in sys.stdin:
        d, n, _ = line.split()
        n = int(n)
        match d:
            case "R":
                polygon.append((polygon[-1][0] + n, polygon[-1][1]))

            case "D":
                polygon.append((polygon[-1][0], polygon[-1][1] + n))

            case "L":
                polygon.append((polygon[-1][0] - n, polygon[-1][1]))

            case "U":
                polygon.append((polygon[-1][0], polygon[-1][1] - n))

    print(get_total_points(polygon))


if __name__ == "__main__":
    main()
