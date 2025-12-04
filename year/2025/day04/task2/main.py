"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=4 ; task=2)
"""

import sys


def main() -> None:
    grid = [[c for c in line] for line in sys.stdin.read().splitlines()]

    n, m = len(grid), len(grid[0])
    ans, cur = 0, -1

    # Performance does not matter for this one since the grid is 136 x 136 :)
    while cur != 0:
        cur = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    cnt = 0
                    for di in range(-1, 2, 1):
                        for dj in range(-1, 2, 1):
                            cnt += (0 <= i + di < n) and (0 <= j + dj < m) and grid[i + di][j + dj] == "@"

                    if cnt < 5:  # It should be less than 5 because when di = dj = 0 then it counts itself :)
                        cur += 1
                        # We can remove it here already, since at the end of this step, it will be removed anyways
                        # and it won't be counted in next step, for the next rolls.
                        # So it really does not matter if we remove it here or in another run after the for loops :)
                        grid[i][j] = '.'
        ans += cur
    print(ans)


if __name__ == "__main__":
    main()
