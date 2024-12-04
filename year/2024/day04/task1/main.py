"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=4 ; task=1)
"""

import itertools
import sys


def get_matches(grid: list[str], word: str) -> int:
    """
    Count the occurrences of a specified word in a grid in multiple directions.

    This function searches for the given word in a 2D grid of characters, checking horizontally, vertically, and
    diagonally. It returns the total number of times the word is found.

    Args:
        grid (list[str]): A 2D list representing the grid of characters.
        word (str): The word to search for in the grid.

    Returns:
        int: The number of occurrences of the word in the grid.

    """
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1)]
    ans = 0
    for i, j, d in itertools.product(range(len(grid)), range(len(grid[0])), dirs):
        ni, nj, p = i, j, 0
        while (
            0 <= ni < len(grid)
            and 0 <= nj < len(grid[ni])
            and p < len(word)
            and grid[ni][nj] == word[p]
        ):
            ni += d[0]
            nj += d[1]
            p += 1

        ans += p == len(word)
    return ans


def main() -> None:
    grid = list(sys.stdin)
    print(get_matches(grid, "XMAS") + get_matches(grid, "SAMX"))


if __name__ == "__main__":
    main()
