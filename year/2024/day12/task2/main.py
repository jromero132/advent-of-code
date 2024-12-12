"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=12 ; task=2)
"""

import sys

DIRS_TO_MOVE = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
)  # Keep this in clockwise or counterclockwise order


def get_region_measurements(
    grid: list[str],
    r: int,
    c: int,
    checked: list[list[bool]],
) -> tuple[int, int]:
    """
    Calculate the area and number of sides of a connected region in a grid.

    The function identifies and measures a contiguous region of identical grid elements with corner detection.

    Args:
        grid (list[str]): 2D grid representing the map or region.
        r (int): Starting row coordinate.
        c (int): Starting column coordinate.
        checked (list[list[bool]]): 2D boolean grid tracking visited cells.

    Returns:
        tuple[int, int]: A tuple containing the area and number of sides of the region.

    Notes:
        - Uses breadth-first search to explore connected cells.
        - Considers a cell part of the region if it has the same value as the starting cell.
        - Calculates both internal and external corners for precise calculation of the number of sides.

    """
    n, m = len(grid), len(grid[0])
    queue = [(r, c)]
    checked[r][c] = True
    area = 0
    while area < len(queue):
        r, c = queue[area]
        area += 1
        for dr, dc in DIRS_TO_MOVE:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == grid[r][c] and not checked[nr][nc]:
                queue.append((nr, nc))
                checked[nr][nc] = True

    # Number of sides is the number of corners. In order to easily calculate the number of corners, the directions to
    # move array must be in clockwise or counterclockwise order.
    dirs_to_check = (*DIRS_TO_MOVE, DIRS_TO_MOVE[0])
    sides = 0
    cells = set(queue)
    for r, c in queue:
        # Two consecutive neighbours does not exist, i.e. a cell is an external corner if:
        #   - above and right cells are not in the area
        #   - right and bottom cells are not in the area
        #   - bottom and left cells are not in the area
        #   - left and above cells are not in the area
        external_corner_check = []

        # Two consecutive cells does exist but the diagonal cell does not exist, i.e. a cell is an internal corner if:
        #   - above and right cells are in the area but above-right cells is not
        #   - right and bottom cells are in the area but right-bottom cells is not
        #   - bottom and left cells are in the area but bottom-left cells is not
        #   - left and above cells are in the area but left-above cells is not
        internal_corner_check = []

        for i, (dr, dc) in enumerate(dirs_to_check):
            external_corner_check.append((r + dr, c + dc))
            if i < len(DIRS_TO_MOVE):
                internal_corner_check.append(
                    (r + dr + dirs_to_check[i + 1][0], c + dc + dirs_to_check[i + 1][1]),
                )

        for i in range(len(DIRS_TO_MOVE)):
            cell1 = external_corner_check[i]
            cell2 = external_corner_check[i + 1]
            cell3 = internal_corner_check[i]
            sides += cell1 not in cells and cell2 not in cells  # external corner
            sides += cell1 in cells and cell2 in cells and cell3 not in cells  # internal corner

    return area, sides


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    n, m = len(grid), len(grid[0])
    checked = [[False] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not checked[i][j]:
                area, sides = get_region_measurements(grid, i, j, checked)
                ans += area * sides
    print(ans)


if __name__ == "__main__":
    main()
