"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=14 ; task=2)
"""

import itertools
import sys


def rotate_right(grid: tuple[str]) -> tuple[str]:
    ans = [["" for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
        ans[j][len(grid) - i - 1] = grid[i][j]
    return tuple("".join(row) for row in ans)


def rotate_left(grid: tuple[str]) -> tuple[str]:
    ans = [["" for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
        ans[len(grid[0]) - j - 1][i] = grid[i][j]
    return tuple("".join(row) for row in ans)


def tilt_north(grid: tuple[str]) -> tuple[str]:
    rocks = [-1] * len(grid[0])
    ans = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "#":
                rocks[j] = i
                ans[i][j] = "#"

            elif c == "O":
                rocks[j] += 1
                ans[rocks[j]][j] = "O"

    return tuple("".join(row) for row in ans)


def tilt_west(grid: tuple[str]) -> tuple[str]:
    return rotate_left(tilt_north(rotate_right(grid)))


def tilt_south(grid: tuple[str]) -> tuple[str]:
    return rotate_left(rotate_left(tilt_north(rotate_left(rotate_left(grid)))))


def tilt_east(grid: tuple[str]) -> tuple[str]:
    return rotate_right(tilt_north(rotate_left(grid)))


def main() -> None:
    grid = tuple(sys.stdin.read().strip().split("\n"))
    dirs = [tilt_north, tilt_west, tilt_south, tilt_east]
    cache, rev_cache = {}, {}
    for i in range(10**9):
        for func in dirs:
            grid = func(grid)

        if grid in cache:
            break

        cache[grid] = i
        rev_cache[i] = grid

    cycle_start = cache[grid]
    cycle_len = i - cache[grid]
    remaining_cycles = (10**9 - cycle_start - 1) % cycle_len

    grid = rev_cache[cycle_start + remaining_cycles]
    print(
        sum(
            len(grid) - i
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == "O"
        ),
    )


if __name__ == "__main__":
    main()
