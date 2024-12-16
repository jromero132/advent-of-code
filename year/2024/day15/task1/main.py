"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=15 ; task=1)
"""

import itertools
import sys


def main() -> None:
    grid, moves = sys.stdin.read().split("\n\n")
    grid = [list(row.strip()) for row in grid.split()]
    moves = moves.replace("\n", "")
    n, m = len(grid), len(grid[0])
    r, c = next(((i, row.index("@")) for i, row in enumerate(grid) if "@" in row))

    for move in moves:
        match move:
            case "^":
                dr, dc = -1, 0

            case ">":
                dr, dc = 0, 1

            case "v":
                dr, dc = 1, 0

            case "<":
                dr, dc = 0, -1

        # Try to push
        nr, nc = r + dr, c + dc  # new row, new column
        fr, fc = nr, nc  # final row, final column
        cnt = 0
        while grid[fr][fc] == "O":
            fr, fc = fr + dr, fc + dc
            cnt += 1

        if grid[fr][fc] == "#":  # Not a valid cell
            continue

        # Move the robot
        grid[r][c] = "."
        grid[nr][nc] = "@"

        # Move the boxes
        for i in range(1, dr * (fr - nr) + dc * (fc - nc) + 1):
            grid[nr + i * dr][nc + i * dc] = "O"

        r, c = nr, nc

    print(sum(100 * i + j for i, j in itertools.product(range(n), range(m)) if grid[i][j] == "O"))


if __name__ == "__main__":
    main()
