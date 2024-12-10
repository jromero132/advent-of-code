"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=10 ; task=2)
"""

import itertools
import sys


def main() -> None:
    dirs_to_move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    grid = [
        [-1 if x == "." else int(x) for x in line.strip()] for line in sys.stdin
    ]  # '.' = -1 for sample inputs
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    queue = []
    for i, j in itertools.product(range(n), range(m)):
        if grid[i][j] == 0:
            queue.append((i, j))
            dp[i][j] = 1

    p, ans = 0, 0
    while p < len(queue):
        r, c = queue[p]

        if grid[r][c] == 9:
            ans += dp[r][c]

        p += 1
        for dr, dc in dirs_to_move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == grid[r][c] + 1:
                if dp[nr][nc] == 0:
                    queue.append((nr, nc))

                dp[nr][nc] += dp[r][c]

    print(ans)


if __name__ == "__main__":
    main()
