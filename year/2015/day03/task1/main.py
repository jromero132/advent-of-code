"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=3 ; task=1)
"""

import sys


def main():
    santa_x, santa_y = 0, 0
    visited = {(santa_x, santa_y)}
    for c in sys.stdin.readline():
        match c:
            case "^":
                santa_y += 1

            case ">":
                santa_x += 1

            case "v":
                santa_y -= 1

            case "<":
                santa_x -= 1

            case _:  # Error
                pass

        visited.add((santa_x, santa_y))

    print(len(visited))


if __name__ == "__main__":
    main()
