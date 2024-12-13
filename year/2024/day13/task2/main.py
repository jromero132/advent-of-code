"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=13 ; task=2)
"""

import sys

INFINITY = 201  # Since no button will be pressed more than 100 times


def solve(button_a: tuple[int, int], button_b: tuple[int, int], prize: tuple[int, int]):
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
        prize = tuple(
            int(x.split("=")[1]) + 10000000000000 for x in prize_str.split(": ")[1].split(", ")
        )
        ans += solve(button_a, button_b, prize)
    print(ans)


if __name__ == "__main__":
    main()
