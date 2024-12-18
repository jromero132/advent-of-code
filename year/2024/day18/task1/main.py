"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=18 ; task=1)
"""

import sys


def bfs(grid: list[list[bool]], start: tuple[int, int], end: tuple[int, int]) -> int:
    """
    Perform a breadth-first search to find the shortest path between two points in a grid.

    The function calculates the minimum number of steps required to navigate from a start point to an end point. The
    algorithm explores the grid by moving in four cardinal directions, tracking the minimum distance to each reachable
    cell. It stops when the end point is reached and returns the total distance traveled.

    Args:
        grid (list[list[bool]]): A 2D grid representing traversable and non-traversable cells.
        start (tuple[int, int]): The starting coordinates (row, column) in the grid.
        end (tuple[int, int]): The target coordinates (row, column) in the grid.

    Returns:
        int: The minimum number of steps from the start to the end point, or -1 if unreachable.

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
    return dist[end[0]][end[1]]


def main() -> None:
    memory_bytes = [tuple(int(x) for x in line.strip().split(",")) for line in sys.stdin]
    n, m = (7, 7) if len(memory_bytes) <= 25 else (71, 71)
    simulation = 12 if len(memory_bytes) <= 25 else 1024

    grid = [[True] * m for _ in range(n)]
    for x, y in memory_bytes[:simulation]:
        grid[y][x] = False

    print(bfs(grid, (0, 0), (n - 1, m - 1)))


if __name__ == "__main__":
    main()
