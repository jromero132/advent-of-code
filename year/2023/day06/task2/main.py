"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=6 ; task=2)
"""

import sys
from math import ceil, floor, sqrt


def get_quadratic_equation_solutions(time: int, distance: int) -> tuple[int, int] | None:
    """
    Calculate the solutions for a quadratic equation based on time and distance.

    This function determines the roots of a quadratic equation derived from the given time and distance. If the
    discriminant is negative, it indicates no real solutions exist, and the function returns None.

    Args:
        time (int): The time variable in the quadratic equation.
        distance (int): The distance variable in the quadratic equation.

    Returns:
        tuple[int, int] | None: A tuple containing the two solutions if they exist, or None if there are no real
            solutions.

    Raises:
        ValueError: If the inputs are not valid integers.

    """
    d = time**2 - 4 * distance
    if d < 0:
        return None
    d = sqrt(d)
    x1 = ceil((time - d) / 2)
    x2 = floor((time + d) / 2)
    if x1 * x1 - time * x1 + distance == 0:
        x1 += 1
    if x2 * x2 - time * x2 + distance == 0:
        x2 -= 1
    return x1, x2


def main() -> None:
    time, distance = sys.stdin.readlines()
    time, distance = int("".join(time.split()[1:])), int("".join(distance.split()[1:]))
    sol = get_quadratic_equation_solutions(time, distance)
    print(sol[1] - sol[0] + 1)


if __name__ == "__main__":
    main()
