"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=20 ; task=1)
"""

import sys


def bfs(grid: list[list[str]], start: tuple[int, int]) -> dict[tuple[int, int], int]:
    """
    Perform a breadth-first search (BFS) traversal on a grid from a starting point.

    The function explores the grid by moving in four cardinal directions, tracking the minimum distance to each visited
    cell. It stops when no new cells can be reached.

    Args:
        grid (list[list[str]]): A 2D grid representing the map with traversable and blocked cells.
        start (tuple[int, int]): The starting coordinates (row, column) for the BFS traversal.

    Returns:
        dict[tuple[int, int], int]: A dictionary mapping grid coordinates to their minimum distance from the start.

    """
    dirs_to_move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    r, c = start
    dist, queue, i = {(r, c): 0}, [(r, c)], 0
    while i < len(queue):
        r, c = queue[i]
        for dr, dc in dirs_to_move:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] != "#" and (nr, nc) not in dist:
                dist[nr, nc] = dist[r, c] + 1
                queue.append((nr, nc))
        i += 1
    return dist


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    target = 10 if len(grid) <= 15 else 100  # For test cases
    start, end = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    dist_s = bfs(grid, start)  # Best path from start cell
    dist_e = bfs(grid, end)  # Best path from end cell
    total_dist = dist_s[end]
    # For any two cells, if:
    #   - best path from start cell + best from end cell + distance between the 2 cells + target <= total distance
    #     then we can cheat between these two cells if their distance is less than 2
    print(
        sum(
            d1 + d + d2 + target <= total_dist
            for (r1, c1), d1 in dist_s.items()
            for (r2, c2), d2 in dist_e.items()
            if (d := abs(r1 - r2) + abs(c1 - c2)) <= 2
        ),
    )


if __name__ == "__main__":
    main()
