"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=9 ; task=1)
"""

import sys


def dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """
    Calculate the distance between two points in a 2D space.

    This function computes the distance between two points represented as tuples of integers. It uses the Chebyshev
    distance metric, which is defined as the maximum of the absolute differences of their coordinates.

    Args:
        p1 (tuple[int, int]): The first point as a tuple of two integers.
        p2 (tuple[int, int]): The second point as a tuple of two integers.

    Returns:
        int: The Chebyshev distance between the two points.

    """
    return max(abs(x - y) for x, y in zip(p1, p2))


def add(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    """
    Add two points represented as tuples in a 2D space.

    This function takes two points, each represented as a tuple of integers, and returns a new tuple that represents
    the sum of the two points. The resulting point is calculated by adding the corresponding coordinates of the input
    points.

    Args:
        p1 (tuple[int, int]): The first point as a tuple of two integers.
        p2 (tuple[int, int]): The second point as a tuple of two integers.

    Returns:
        tuple[int, int]: A tuple representing the sum of the two points.

    """
    return tuple(x + y for x, y in zip(p1, p2))


def sign(x: int) -> int:
    """
    Determine the sign of a given integer.

    This function returns 1 if the input number is positive, -1 if it is negative, and 0 if the number is zero. It
    provides a simple way to assess the sign of an integer.

    Args:
        x (int): The integer whose sign is to be determined.

    Returns:
        int: The sign of the integer, which is 1, 0, or -1.

    """
    return 1 if x > 0 else (0 if x == 0 else -1)


def main() -> None:
    dir_move = {  # directions to move
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    knots = [(0, 0) for _ in range(2)]  # knots to be tracked

    pos = set(knots[:1])
    for instruction in sys.stdin:
        d, c = instruction.strip().split()
        d = dir_move[d]
        c = int(c)

        for _ in range(1, c + 1):
            knots[0] = add(knots[0], d)  # update head

            for i, j in zip(range(len(knots) - 1), range(1, len(knots))):  # update tail
                ht_dist = dist(knots[i], knots[j])
                if ht_dist == 2:
                    knots[j] = add(
                        knots[j],
                        (sign(knots[i][0] - knots[j][0]), sign(knots[i][1] - knots[j][1])),
                    )

            pos.add(knots[-1])  # update position of tail

    print(len(pos))


if __name__ == "__main__":
    main()
