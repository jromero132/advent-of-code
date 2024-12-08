"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=8 ; task=1)
"""

import itertools
import sys
from collections import defaultdict


def main() -> None:
    lines = [line.strip() for line in sys.stdin]
    antennas = defaultdict(list)
    n, m = len(lines), len(lines[0])
    for i, j in itertools.product(range(n), range(m)):
        if lines[i][j].isalnum():
            antennas[lines[i][j]].append((i, j))

    ans = set()
    for locations in antennas.values():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                r = locations[i][0] - locations[j][0]
                c = locations[i][1] - locations[j][1]

                nr, nc = locations[i][0] + r, locations[i][1] + c
                if 0 <= nr < n and 0 <= nc < m:
                    ans.add((nr, nc))

                nr, nc = locations[j][0] - r, locations[j][1] - c
                if 0 <= nr < n and 0 <= nc < m:
                    ans.add((nr, nc))

    print(len(ans))


if __name__ == "__main__":
    main()
