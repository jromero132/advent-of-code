"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=9 ; task=1)
"""

import sys


def is_low_point(grid: list[list[int]], r: int, c: int) -> bool:
    """
    Determine if a specific point in a grid is a low point.

    This function checks whether the value at a given position in a 2D grid is lower than its adjacent values. A low
    point is defined as a value that is less than all of its directly neighboring values.

    Args:
        grid (list[list[int]]): A 2D list representing the grid of integer values.
        r (int): The row index of the point to check.
        c (int): The column index of the point to check.

    Returns:
        bool: True if the point is a low point, False otherwise.

    """
    dir_move = [  # directions to move
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]
    n, m = len(grid), len(grid[0])
    ans = True
    for dr, dc in dir_move:
        nr, nc = r + dr, c + dc
        ans &= nr < 0 or nr >= n or nc < 0 or nc >= m or grid[r][c] < grid[nr][nc]
    return ans


def main() -> None:
    grid = [[int(x) for x in line.strip()] for line in sys.stdin]  # get the information
    print(
        sum(
            grid[i][j] + 1
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if is_low_point(grid, i, j)
        ),
    )


if __name__ == "__main__":
    main()
