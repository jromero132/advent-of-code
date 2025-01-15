"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=11 ; task=1)
"""

import sys


def main() -> None:
    galaxies = [[i, j] for i, line in enumerate(sys.stdin) for j, c in enumerate(line) if c == "#"]

    # Double the rows
    galaxies.sort()
    offset = 0
    for i in range(1, len(galaxies)):
        offset += max(0, galaxies[i][0] + offset - galaxies[i - 1][0] - 1)
        galaxies[i][0] += offset

    # Double the columns
    galaxies.sort(key=lambda x: x[1])
    offset = 0
    for i in range(1, len(galaxies)):
        offset += max(0, galaxies[i][1] + offset - galaxies[i - 1][1] - 1)
        galaxies[i][1] += offset

    print(
        sum(
            abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            for i in range(len(galaxies))
            for j in range(i + 1, len(galaxies))
        ),
    )


if __name__ == "__main__":
    main()
