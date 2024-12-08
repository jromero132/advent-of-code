"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=12 ; task=2)
"""

import itertools
import sys


def main() -> None:
    rs, cs = -1, -1
    re, ce = -1, -1
    lines = sys.stdin.read().splitlines()
    n, m = len(lines), len(lines[0])
    q = []
    for i, j in itertools.product(range(n), range(m)):
        match lines[i][j]:
            case "S":  # one of the possible starting points
                rs, cs = i, j
                q.append((i, j))

            case "E":  # ending point
                re, ce = i, j

            case "a":  # other possible starting points
                q.append((i, j))

    lines[rs] = lines[rs].replace("S", "a")
    lines[re] = lines[re].replace("E", "z")

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    steps = [[-1] * m for _ in range(n)]
    for i, j in q:
        steps[i][j] = 0  # it costs 0 to start at any of these points

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
