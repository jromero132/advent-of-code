"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=3 ; task=2)
"""

import sys
from collections import defaultdict


def extract_number(row: str, start: int) -> tuple[int, int]:
    """Extract a number from the row starting at the given index."""
    end = start + 1
    while end < len(row) and row[end].isdigit():
        end += 1
    return int(row[start:end]), end


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    gear = defaultdict(list)
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].isdigit():
                num, end = extract_number(grid[i], j)
                for dj in range(j - 1, end + 1):
                    if i > 0 and 0 <= dj < len(grid[i]) and grid[i - 1][dj] == "*":
                        gear[(i - 1, dj)].append(num)

                    if i + 1 < len(grid) and 0 <= dj < len(grid[i]) and grid[i + 1][dj] == "*":
                        gear[(i + 1, dj)].append(num)

                if j > 0 and grid[i][j - 1] == "*":
                    gear[(i, j - 1)].append(num)

                if end < len(grid[i]) and grid[i][end] == "*":
                    gear[(i, end)].append(num)

                j = end

            else:
                j += 1

    print(sum(values[0] * values[1] for values in gear.values() if len(values) == 2))


if __name__ == "__main__":
    main()
