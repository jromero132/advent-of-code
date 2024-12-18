"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=18 ; task=1)
"""

import sys


def bfs(grid: list[list[bool]], start: tuple[int, int], end: tuple[int, int]) -> bool:
    """
    Determine if a path exists between two points in a grid using breadth-first search.

    The function checks whether a traversable route can be found from a start point to an end point. The algorithm
    explores the grid by moving in four cardinal directions, tracking reachable cells and determining path connectivity.
    It returns a boolean indicating whether the end point is accessible from the start point.

    Args:
        grid (list[list[bool]]): A 2D grid representing traversable and non-traversable cells.
        start (tuple[int, int]): The starting coordinates (row, column) in the grid.
        end (tuple[int, int]): The target coordinates (row, column) in the grid.

    Returns:
        bool: True if a path exists between start and end points, False otherwise.

    """
    dirs_to_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, m = len(grid), len(grid[0])
    queue, dist, i = [start], [[-1] * m for _ in range(n)], 0
    dist[start[0]][start[1]] = 0
    while i < len(queue):
        r, c = queue[i]
        if (r, c) == end:
            break
        for dr, dc in dirs_to_move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

        i += 1
    return dist[end[0]][end[1]] != -1


def main() -> None:
    memory_bytes = [tuple(int(x) for x in line.strip().split(",")) for line in sys.stdin]
    n, m = (7, 7) if len(memory_bytes) <= 25 else (71, 71)
    left, right = 0, len(memory_bytes)
    while left < right:  # Binary search
        middle = (left + right) // 2
        grid = [[True] * m for _ in range(n)]
        for x, y in memory_bytes[:middle]:
            grid[y][x] = False

        if bfs(grid, (0, 0), (n - 1, m - 1)):
            left = middle + 1

        else:
            right = middle
    print(",".join(str(n) for n in memory_bytes[left - 1]))


if __name__ == "__main__":
    main()
