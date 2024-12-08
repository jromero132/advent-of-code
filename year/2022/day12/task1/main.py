"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=12 ; task=1)
"""

import itertools
import sys


def main() -> None:
    rs, cs = -1, -1
    re, ce = -1, -1
    lines = sys.stdin.read().splitlines()
    n, m = len(lines), len(lines[0])
    for i, j in itertools.product(range(n), range(m)):
        match lines[i][j]:
            case "S":  # starting point
                rs, cs = i, j

            case "E":  # ending point
                re, ce = i, j

    lines[rs] = lines[rs].replace("S", "a")
    lines[re] = lines[re].replace("E", "z")

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    steps = [[-1] * m for _ in range(n)]
    steps[rs][cs] = 0  # it costs 0 to start at this point
    q = [(rs, cs)]
    i = 0
    while i < len(q) and q[i] != (re, ce):  # BFS
        rs, cs = q[i]
        for mr, mc in moves:
            nr, nc = rs + mr, cs + mc
            if (
                0 <= nr < n
                and 0 <= nc < m
                and steps[nr][nc] == -1
                and ord(lines[rs][cs]) + 1 >= ord(lines[nr][nc])
            ):
                steps[nr][nc] = steps[rs][cs] + 1
                q.append((nr, nc))
        i += 1

    print(steps[re][ce])


if __name__ == "__main__":
    main()
