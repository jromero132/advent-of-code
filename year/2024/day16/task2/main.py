"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=16 ; task=2)
"""

import heapq
import itertools
import sys
from collections import defaultdict


def dijkstra(grid: list[str], sr: int, sc: int) -> int:
    """
    Find the number of unique tiles visited at the minimum distance in a grid using a modified Dijkstra's algorithm.

    The function calculates the minimum distance and tracks unique tiles reached. The algorithm explores grid paths with
    complex movement rules, allowing forward movement, counterclockwise, and clockwise rotations. It uses a priority
    queue to track distances, unique tiles, and explores different movement strategies efficiently.

    Args:
        grid (list[str]): A 2D grid representing the map with traversable and blocked cells.
        sr (int): Starting row coordinate.
        sc (int): Starting column coordinate.

    Returns:
        int: The number of unique tiles visited at the minimum distance.

    """
    queue = [(0, (sr, sc), (0, 1), {(sr, sc)})]
    distance = defaultdict(lambda: float("inf"))
    ans, min_dist = set(), float("inf")
    while queue:
        dist, node, d, tiles = heapq.heappop(queue)
        distance[node, d] = dist

        if grid[node[0]][node[1]] == "E":
            if dist < min_dist:
                min_dist, ans = dist, tiles

            elif dist == min_dist:
                ans |= tiles

            continue

        # There are only 3 options to analyze
        nr, nc = node[0] + d[0], node[1] + d[1]
        if grid[nr][nc] != "#" and dist + 1 < distance[(nr, nc), d]:
            heapq.heappush(queue, (dist + 1, (nr, nc), d, tiles | {(nr, nc)}))  # Move forward

        d2 = (-d[1], d[0])
        if dist + 1000 < distance[(node, d2)]:
            heapq.heappush(queue, (dist + 1000, node, d2, tiles))  # Move counterclockwise

        d3 = (d[1], -d[0])
        if dist + 1000 < distance[(node, d3)]:
            heapq.heappush(queue, (dist + 1000, node, d3, tiles))  # Move clockwise

    return len(ans)


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    sr, sc = next(
        (
            (i, j)
            for i, j in itertools.product(range(len(grid)), range(len(grid[0])))
            if grid[i][j] == "S"
        ),
    )
    print(dijkstra(grid, sr, sc))


if __name__ == "__main__":
    main()
