"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=17 ; task=1)
"""

import heapq
import sys


def get_heat_loss(
    grid: list[list[int]],
    src: tuple[int, int],
    dst: tuple[int, int],
    min_steps: int,
    max_steps: int,
) -> int:
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [(0, src, d) for d in dirs]
    visited = set()
    n, m = len(grid), len(grid[0])

    while queue:
        heat, (r, c), old_dir = heapq.heappop(queue)

        if (r, c) == dst:
            return heat

        if ((r, c), old_dir) in visited:
            continue

        visited.add(((r, c), old_dir))
        for dr, dc in dirs:
            if old_dir[0] + dr != 0 and old_dir[1] + dc != 0:  # turning left or right
                nr, nc = r + dr * (min_steps - 1), c + dc * (min_steps - 1)
                if 0 <= nr < n and 0 <= nc < m:  # inside grid
                    path_heat = heat + sum(
                        grid[r + i * dr][c + i * dc] for i in range(1, min_steps)
                    )
                    for _ in range(min_steps, max_steps + 1):
                        nr, nc = nr + dr, nc + dc
                        if nr in (-1, n) or nc in (-1, m):
                            break

                        path_heat += grid[nr][nc]
                        heapq.heappush(queue, (path_heat, (nr, nc), (dr, dc)))

    return -1


def main() -> None:
    grid = [[int(x) for x in line] for line in sys.stdin.read().strip().split("\n")]
    print(get_heat_loss(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1), 1, 3))


if __name__ == "__main__":
    main()
