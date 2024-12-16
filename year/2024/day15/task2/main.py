"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=15 ; task=2)
"""

import itertools
import sys


def main() -> None:
    initial_grid, moves = sys.stdin.read().split("\n\n")
    grid = []
    for row in initial_grid.split():
        grid.append([])
        for c in row.strip():
            match c:
                case "#":
                    grid[-1].extend(("#", "#"))

                case "O":
                    grid[-1].extend(("[", "]"))

                case ".":
                    grid[-1].extend((".", "."))

                case "@":
                    grid[-1].extend(("@", "."))

    moves = moves.replace("\n", "")
    n, m = len(grid), len(grid[0])
    r, c = next(((i, row.index("@")) for i, row in enumerate(grid) if "@" in row))
    for move in moves:
        match move:
            case "^":
                dr, dc = -1, 0

            case ">":
                dr, dc = 0, 1

            case "v":
                dr, dc = 1, 0

            case "<":
                dr, dc = 0, -1

        # Try to push
        queue, i, hit_wall = [(r, c)], 0, False
        checked = set(queue)
        while i < len(queue):
            nr, nc = queue[i][0] + dr, queue[i][1] + dc

            if grid[nr][nc] == "#":  # Hit the wall, so we can't push
                hit_wall = True
                break

            if grid[nr][nc] in "[]" and (nr, nc) not in checked:
                q = [(nr, nc)]
                if move in "^v":
                    q.append((nr, nc + (1 if grid[nr][nc] == "[" else -1)))

                queue.extend(q)
                checked.update(q)

            i += 1

        if not hit_wall:  # Move the boxes from the farthest first and finally move the robot
            for nr, nc in queue[::-1]:
                grid[nr][nc], grid[nr + dr][nc + dc] = (
                    grid[nr + dr][nc + dc],
                    grid[nr][nc],
                )  # Basic push/switching pos
            r, c = r + dr, c + dc

    print(sum(100 * i + j for i, j in itertools.product(range(n), range(m)) if grid[i][j] == "["))


if __name__ == "__main__":
    main()
