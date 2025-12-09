"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=8 ; task=2)
"""

import sys


class DisjointSetUnion:
    def __init__(self, n: int) -> None:
        self.parent = [-1] * n
        self.n_sets = n

    def root(self, u: int) -> int:
        if self.parent[u] < 0:
            return u

        self.parent[u] = self.root(self.parent[u])
        return self.parent[u]

    def join(self, u: int, v: int) -> None:
        u = self.root(u)
        v = self.root(v)
        if u == v:
            return

        if self.parent[u] > self.parent[v]:
            u, v = v, u

        self.parent[u] += self.parent[v]
        self.parent[v] = u
        self.n_sets -= 1

    def get_set_size(self, u: int) -> int:
        return abs(self.parent[self.root(u)])


def main() -> None:
    points = [tuple(map(int, line.split(","))) for line in sys.stdin.read().splitlines()]
    n = len(points)

    array = []
    for i in range(n):
        for j in range(i + 1, n):
            array.append((sum((p1 - p2) ** 2 for p1, p2 in zip(points[i], points[j])), i, j))

    dsu = DisjointSetUnion(len(points))
    for _, p1, p2 in sorted(array):
        dsu.join(p1, p2)
        if dsu.n_sets == 1:
            print(points[p1][0] * points[p2][0])
            break


if __name__ == "__main__":
    main()
