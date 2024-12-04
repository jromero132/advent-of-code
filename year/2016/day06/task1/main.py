"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=6 ; task=1)
"""

import sys
from collections import Counter


def main() -> None:
    grid = list(sys.stdin)
    counter = [Counter(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
    print("".join(c.most_common(1)[0][0] for c in counter))


if __name__ == "__main__":
    main()
