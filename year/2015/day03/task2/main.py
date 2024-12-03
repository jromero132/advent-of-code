"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=3 ; task=2)
"""

import sys


def main() -> None:
    idx, santa = 0, [[0, 0], [0, 0]]
    visited = {tuple(santa[idx])}
    for c in sys.stdin.readline():
        match c:
            case "^":
                santa[idx][1] += 1

            case ">":
                santa[idx][0] += 1

            case "v":
                santa[idx][1] -= 1

            case "<":
                santa[idx][0] -= 1

            case _:  # Error
                pass

        visited.add(tuple(santa[idx]))
        idx = (idx + 1) % len(santa)

    print(len(visited))


if __name__ == "__main__":
    main()
