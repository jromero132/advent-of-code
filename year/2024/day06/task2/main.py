"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=6 ; task=2)
"""

import itertools
import sys

memo: list[list[bool]] = None


def get_travel(
    grid: list[str],
    origin: tuple[int, int],
    d: tuple[int, int],
    obj: tuple[int, int],
) -> bool:
    """
    Simulate movement on a grid and checks if the travel path is valid.

    This function takes an initial position and direction, moving through the grid while avoiding obstacles and tracking
    visited positions. It determines if the final position remains within the grid boundaries.

    Args:
        grid (list[str]): A 2D grid represented as a list of strings, where each string is a row.
        origin (tuple[int, int]): The starting coordinates in the grid as a tuple (row, column).
        d (tuple[int, int]): The initial direction of movement as a tuple (delta_row, delta_column).
        obj (tuple[int, int]): The target coordinates to reach on the grid.

    Returns:
        bool: True if the final position is within the grid boundaries, False otherwise.

    """
    n, m = len(grid), len(grid[0])
    visited = [[set() for _ in range(m)] for _ in range(n)]
    extra_visited = []
    r, c = origin
    dr, dc = d
    while (dr, dc) not in visited[r][c]:
        visited[r][c].add((dr, dc))
        nr, nc = r + dr, c + dc
        if (nr in (-1, n) or nc in (-1, m)) and (nr, nc) != obj:
            extra_visited.append((nr, nc))
            break

        if (nr, nc) == obj or grid[nr][nc] == "#":
            dr, dc = dc, -dr

        else:
            r, c = nr, nc

    return 0 <= nr < n and 0 <= nc < m, visited, extra_visited


def main() -> None:
    grid = list(sys.stdin)
    n, m = len(grid), len(grid[0])
    r, c = 0, 0
    while grid[r][c] != "^":
        c += 1
        if c == m:
            r += 1
            c = 0

    # (-1, 0) because it starts facing up ; (-1, -1) is for no initial obstacle
    _, travel, extra_steps = get_travel(grid, (r, c), (-1, 0), (-1, -1))
    print(
        sum(
            get_travel(grid, (r, c), (-1, 0), (i, j))[0]
            for i, j in itertools.product(range(n), range(m))
            if len(travel[i][j]) > 0 and (i, j) != (r, c)
        )  # normal positions
        + sum(get_travel(grid, (r, c), (-1, 0), pos)[0] for pos in extra_steps),  # border positions
    )


if __name__ == "__main__":
    main()
