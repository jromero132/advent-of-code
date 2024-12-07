"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=6 ; task=1)
"""

import sys


def main() -> None:
    line = sys.stdin.read().strip()
    marker_size = 4
    print(
        next(
            (
                str(i)
                for i in range(marker_size, len(line) + 1)
                if len(set(line[i - marker_size : i])) == marker_size
            ),
            "-1",
        ),
    )


if __name__ == "__main__":
    main()
