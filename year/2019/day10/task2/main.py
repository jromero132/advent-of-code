"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=10 ; task=2)
"""

import math
import sys
from collections import defaultdict, deque


def dot_product(v1: list[float], v2: list[float]) -> float:
    """
    Calculate the dot product of two vectors.

    The dot product is the sum of the products of the corresponding entries of the two vectors. Geometrically, it is
    the product of the Euclidean magnitudes of the two vectors and the cosine of the angle between them.

    Args:
        v1: The first vector.
        v2: The second vector.

    Returns:
        The dot product of v1 and v2.

    """
    return sum((a * b) for a, b in zip(v1, v2))


def length(v: list[float]) -> float:
    """
    Calculate the length (or magnitude) of a vector.

    The length of a vector is the square root of the sum of the squares of its components. It represents the distance
    of the vector from the origin.

    Args:
        v: The vector.

    Returns:
        The length of the vector.

    """
    return math.sqrt(dot_product(v, v))


def angle(v1: list[float], v2: list[float]) -> float:
    """
    Calculate the angle between two vectors.

    The angle is calculated using the arccosine of the dot product of the vectors divided by the product of their
    lengths. The function adjusts the angle based on the cross product to ensure it's in the correct quadrant.

    Args:
        v1: The first vector.
        v2: The second vector.

    Returns:
        The angle between the two vectors in radians.

    """
    angle = math.acos(dot_product(v1, v2) / (length(v1) * length(v2)))
    return angle if v1[0] * v2[1] - v1[1] * v2[0] >= 0 else 2 * math.pi - angle


def distance(v1: list[float], v2: list[float]) -> float:
    """
    Calculate the Euclidean distance between two vectors.

    The distance is calculated as the square root of the sum of the squared differences between corresponding elements
    of the vectors.  This represents the straight-line distance between the points represented by the vectors in
    n-dimensional space.

    Args:
        v1: The first vector.
        v2: The second vector.

    Returns:
        The Euclidean distance between v1 and v2.

    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))


def main() -> None:
    asteroids = [
        (j, i) for i, line in enumerate(sys.stdin) for j, c in enumerate(line.strip()) if c == "#"
    ]
    target = int(len(asteroids) * 0.8) if len(asteroids) <= 50 else 200  # For testing
    best, best_point, line = 0, None, None
    for i, (x1, y1) in enumerate(asteroids):
        sight = defaultdict(list)
        for j, (x2, y2) in enumerate(asteroids):
            if i == j:
                continue

            dx, dy = x2 - x1, y2 - y1
            gcd = math.gcd(dx, dy)
            sight[dx / gcd, dy / gcd].append((x2, y2))

        if best < len(sight):
            best = len(sight)
            best_point = (x1, y1)
            line = sight

    for points in line.values():
        points.sort(key=lambda x: distance(best_point, x))

    array = deque(sorted(line.items(), key=lambda p: angle((0, -1), p[0])))
    for _ in range(target - 1):
        line, points = array.popleft()
        if len(points) != 1:
            array.append((line, points[1:]))

    point = array.popleft()[1][0]
    print(int(point[0] * 100 + point[1]))


if __name__ == "__main__":
    main()
