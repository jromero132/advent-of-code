"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=16 ; task=1)
"""

import sys
from collections import defaultdict


def main() -> None:
    grid = sys.stdin.read().strip().split("\n")
    n, m = len(grid), len(grid[0])
    queue, i = [((0, 0), (0, 1))], 0
    visited = defaultdict(list)
    visited[queue[0][0]].append(queue[0][1])
    while i < len(queue):
        (r, c), (dr, dc) = queue[i]
        next_steps = []
        match grid[r][c]:
            case "|":
                if dr == 0:
                    next_steps.extend((((r - 1, c), (-1, 0)), ((r + 1, c), (1, 0))))

                else:
                    next_steps.append(((r + dr, c + dc), (dr, dc)))

            case "-":
                if dc == 0:
                    next_steps.extend((((r, c - 1), (0, -1)), ((r, c + 1), (0, 1))))

                else:
                    next_steps.append(((r + dr, c + dc), (dr, dc)))

            case "/":
                next_steps.append(((r - dc, c - dr), (-dc, -dr)))

            case "\\":
                next_steps.append(((r + dc, c + dr), (dc, dr)))

            case ".":
                next_steps.append(((r + dr, c + dc), (dr, dc)))

        for (nr, nc), nd in next_steps:
            if 0 <= nr < n and 0 <= nc < m and nd not in visited[nr, nc]:
                visited[nr, nc].append(nd)
                queue.append(((nr, nc), nd))

        i += 1

    print(len(visited))


if __name__ == "__main__":
    main()
