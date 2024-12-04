"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=4 ; task=2)
"""

import itertools
import sys


def get_matches(grid: list[str]) -> int:
    """
    Count the occurrences of specific word patterns in a grid.

    This function checks for the presence of the words "MAS" and "SAM" in a 2D grid by examining specific diagonal
    arrangements of characters, so they form an X pattern. It returns the total count of such occurrences.

    Args:
        grid (list[str]): A 2D list representing the grid of characters.

    Returns:
        int: The number of occurrences of the specified word patterns in the grid.

    """
    words = ("MAS", "SAM")
    return sum(
        (
            grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1] in words
            and grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] in words
        )
        for i, j in itertools.product(range(1, len(grid) - 1), range(1, len(grid[0]) - 1))
    )


def main() -> None:
    grid = list(sys.stdin)
    print(get_matches(grid))


if __name__ == "__main__":
    main()
