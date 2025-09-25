"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=21 ; task=2)
"""

import sys
from collections import defaultdict


# Note: This approach assumes that the pattern of new points reached continues
# in a consistent manner, which is valid for the given puzzle input.

# This solution is based on the observation that the grid and the distances
# from the starting point repeat every `grid_len` steps. Therefore, we can
# calculate the number of new points reached at specific intervals and use
# a formula to compute the total number of unique points reached after
# TARGET_STEPS.

# The key insight is that the number of new points reached at each interval
# forms an arithmetic sequence. By identifying the first few terms of this
# sequence, we can derive a formula to calculate the total number of unique
# points reached after a large number of steps without simulating each step.

# The formula used is:
# total_points = a + b * x + (x * (x - 1) / 2) * (c - b)
# where:
# - a is the number of unique points reached in the first interval
# - b is the increase in unique points reached in the second interval
# - c is the increase in unique points reached in the third interval
# - x is the number of complete intervals in TARGET_STEPS

# Additional insight: It turns out that each square has a parity: a tile can
# either be reached in an even number of steps or an odd number of steps,
# but there are NO tiles that can be reached in an odd number of steps through
# one path, and an even number of steps through a different path.


def main() -> None:
    sr, sc = 0, 0
    grid = []
    for r, line in enumerate(sys.stdin):
        grid.append(line.strip("\n"))
        for c, ch in enumerate(grid[-1]):
            if ch == "S":
                sr, sc = r, c


    TARGET_STEPS = 26501365
    grid_len = len(grid)  # 131
    distance = defaultdict(set, {0: {(sr, sc)}})
    pts, steps = [], 0
    while len(pts) < 3:
        for r, c in distance[steps]:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr, cc = (r + dr) % grid_len, (c + dc) % grid_len
                if grid[rr][cc] != "#":
                    distance[steps + 1].add((r + dr, c + dc))

        if (steps - (grid_len // 2) + 1) % grid_len == 0:
            pts.append(len(distance[steps + 1]))

        steps += 1

    a = pts[0]
    b = pts[1] - pts[0]
    c = pts[2] - pts[1]
    x = TARGET_STEPS // grid_len  # grid_len // 2 == TARGET_STEPS % grid_len
    print(a + b * x + x * (x - 1) // 2 * (c - b))

if __name__ == "__main__":
    main()
