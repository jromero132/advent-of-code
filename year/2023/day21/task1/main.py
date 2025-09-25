"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=21 ; task=1)
"""

import sys
from collections import defaultdict


def main() -> None:
    sr, sc = 0, 0
    grid = []
    for r, line in enumerate(sys.stdin):
        grid.append(line.strip("\n"))
        for c, ch in enumerate(grid[-1]):
            if ch == "S":
                sr, sc = r, c


    TARGET_STEPS = 6 if len(grid) < 15 else 64
    distance = defaultdict(set, {0: {(sr, sc)}})
    q = [(sr, sc, 0)]
    while q:
        r, c, steps = q.pop(0)
        if steps == TARGET_STEPS:
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(grid) \
            and 0 <= cc < len(grid[0]) \
            and grid[rr][cc] != "#" \
            and steps + 1 <= TARGET_STEPS \
            and (rr, cc) not in distance[steps + 1]:
                distance[steps + 1].add((rr, cc))
                q.append((rr, cc, steps + 1))

    print(len(distance[TARGET_STEPS]))


if __name__ == "__main__":
    main()
