"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=16 ; task=1)
"""

import heapq
import itertools
import sys
from collections import defaultdict


def dijkstra(grid: list[str], sr: int, sc: int, er: int, ec: int) -> int:
    queue = [(0, (sr, sc), (0, 1))]
    distance = defaultdict(lambda: float("inf"))
    while queue:
        dist, node, d = heapq.heappop(queue)
        distance[node, d] = dist

        if grid[node[0]][node[1]] == "E":
            continue

        # There are only 3 options to analyze
        nr, nc = node[0] + d[0], node[1] + d[1]
        if grid[nr][nc] != "#" and dist + 1 < distance[(nr, nc), d]:
            heapq.heappush(queue, (dist + 1, (nr, nc), d))  # Move forward

        d2 = (-d[1], d[0])
        if dist + 1000 < distance[(node, d2)]:
            heapq.heappush(queue, (dist + 1000, node, d2))  # Move counterclockwise

        d3 = (d[1], -d[0])
        if dist + 1000 < distance[(node, d3)]:
            heapq.heappush(queue, (dist + 1000, node, d3))  # Move clockwise

    return min(distance[(er, ec), (i, j)] for i, j in ((-1, 0), (0, 1), (1, 0), (0, -1)))


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    sr, sc, er, ec = -1, -1, -1, -1
    for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
        if grid[i][j] == "S":
            sr, sc = i, j

        elif grid[i][j] == "E":
            er, ec = i, j

    print(dijkstra(grid, sr, sc, er, ec))


if __name__ == "__main__":
    main()
