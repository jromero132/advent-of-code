"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=14 ; task=2)
"""

import sys


def main() -> None:
    robots = [
        [[int(x) for x in s[2:].split(",")] for s in line.strip().split(" ")] for line in sys.stdin
    ]
    size = [11, 7] if len(robots) <= 15 else [101, 103]
    target_line = "O" * 4 if len(robots) <= 15 else "O" * 30
    step = 0
    while True:
        grid = [["."] * size[0] for _ in range(size[1])]
        for p, v in robots:
            for i in range(len(size)):
                p[i] += v[i]
                if p[i] < 0 or p[i] >= size[i]:
                    p[i] %= size[i]

            grid[p[1]][p[0]] = "O"

        step += 1
        if any(target_line in "".join(row) for row in grid):
            break

    print(step)


if __name__ == "__main__":
    main()
