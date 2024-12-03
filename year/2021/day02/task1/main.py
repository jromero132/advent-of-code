"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=2 ; task=1)
"""

import sys


def main() -> None:
    horizontal, depth = 0, 0
    for line in sys.stdin:
        move, steps = line.split()
        steps = int(steps)
        match move:
            case "forward":
                horizontal += steps

            case "down":
                depth += steps

            case "up":
                depth -= steps

            case _:  # Error
                pass

    print(horizontal * depth)


if __name__ == "__main__":
    main()
