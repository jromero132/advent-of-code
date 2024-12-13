"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=13 ; task=1)
"""

import sys

INFINITY = 201  # Since no button will be pressed more than 100 times


def solve(button_a: tuple[int, int], button_b: tuple[int, int], prize: tuple[int, int]) -> int:
    """
    Solve a linear equation system to find the fewest tokens to spend.

    Calculates the minimum number of tokens required to reach a specific prize coordinate using two buttons. The
    function handles both determinant and non-determinant scenarios for solving the linear equation.

    Args:
        button_a (tuple[int, int]): Coordinates of the first button (x, y).
        button_b (tuple[int, int]): Coordinates of the second button (x, y).
        prize (tuple[int, int]): Target coordinates to reach (x, y).

    Returns:
        int: The minimum number of button presses to reach the prize, or 0 if no valid solution exists.

    """
    xa, ya = button_a
    xb, yb = button_b
    xp, yp = prize

    # Equations
    # a * xa + b * xb = xp
    # a * ya + b * yb = yp

    # Calculate determinant: D = xa * yb - xb * ya
    determinant = xa * yb - xb * ya

    if determinant == 0:
        # Find all possible solutions, this might take some time, it all depends on the equation type
        ans = INFINITY
        for a in range(xp // xa + 1):
            b = (xp - a * xa) // xb
            if a * xa + b * xb == xp:
                ans = min(ans, a * 3 + b)
        return ans

    # Inverse matrix
    # (xa xb) = (1 / (xa * yb - xb * ya))(yb -xb)
    # (ya yb)                            (-ya xa)

    # Find solutions
    # ((1 / D)(yb -xb))(xp) = (yb * xp - xb * yp) / D = (a)
    # (      )(-ya xa))(yp)   (xa * yp - ya * xp) / D = (b)

    a = (yb * xp - xb * yp) // determinant
    b = (xa * yp - ya * xp) // determinant
    return a * 3 + b if min(a, b) >= 0 and (a * xa + b * xb, a * ya + b * yb) == (xp, yp) else 0


def main() -> None:
    games = sys.stdin.read().strip().split("\n\n")
    ans = 0
    for game in games:
        button_a_str, button_b_str, prize_str = game.split("\n")
        button_a = tuple(int(x.split("+")[1]) for x in button_a_str.split(": ")[1].split(", "))
        button_b = tuple(int(x.split("+")[1]) for x in button_b_str.split(": ")[1].split(", "))
        prize = tuple(int(x.split("=")[1]) for x in prize_str.split(": ")[1].split(", "))
        ans += solve(button_a, button_b, prize)
    print(ans)


if __name__ == "__main__":
    main()
