"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=12 ; task=1)
"""

import sys

DIRS_TO_MOVE = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
)


def get_region_measurements(
    grid: list[str],
    r: int,
    c: int,
    checked: list[list[bool]],
) -> tuple[int, int]:
    """
    Calculate the area and perimeter of a connected region in a grid.

    The function identifies and measures a contiguous region of identical grid elements.

    Args:
        grid (list[str]): 2D grid representing the map or region.
        r (int): Starting row coordinate.
        c (int): Starting column coordinate.
        checked (list[list[bool]]): 2D boolean grid tracking visited cells.

    Returns:
        tuple[int, int]: A tuple containing the area and perimeter of the region.

    Notes:
        - Uses breadth-first search to explore connected cells.
        - Considers a cell part of the region if it has the same value as the starting cell.

    """
    n, m = len(grid), len(grid[0])
    queue = [(r, c)]
    checked[r][c] = True
    area, perimeter = 0, 0
    while area < len(queue):
        r, c = queue[area]
        area += 1
        for dr, dc in DIRS_TO_MOVE:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == grid[r][c]:
                if not checked[nr][nc]:
                    queue.append((nr, nc))
                    checked[nr][nc] = True

            else:
                perimeter += 1

    return area, perimeter


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    n, m = len(grid), len(grid[0])
    checked = [[False] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not checked[i][j]:
                area, perimeter = get_region_measurements(grid, i, j, checked)
                ans += area * perimeter
    print(ans)


if __name__ == "__main__":
    main()
