"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=6 ; task=1)
"""

import sys


def main() -> None:
    grid = list(sys.stdin)
    n, m = len(grid), len(grid[0])
    r, c = 0, 0
    while grid[r][c] != "^":
        c += 1
        if c == m:
            r += 1
            c = 0

    visited = [[set() for _ in range(m)] for _ in range(n)]
    dr, dc = -1, 0
    while (dr, dc) not in visited[r][c]:
        visited[r][c].add((dr, dc))
        nr, nc = r + dr, c + dc
        if nr in (-1, n) or nc in (-1, m):
            break

        if grid[nr][nc] == "#":
            dr, dc = dc, -dr

        else:
            r, c = nr, nc

    print(sum(len(visited[i][j]) > 0 for i in range(n) for j in range(m)))


if __name__ == "__main__":
    main()
