"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=2 ; task=2)
"""

import sys


def main():
    horizontal, depth, aim = 0, 0, 0
    for line in sys.stdin:
        move, steps = line.split()
        steps = int(steps)
        match move:
            case "forward":
                horizontal += steps
                depth += aim * steps

            case "down":
                aim += steps

            case "up":
                aim -= steps

            case _:  # Error
                pass

    print(horizontal * depth)


if __name__ == "__main__":
    main()
