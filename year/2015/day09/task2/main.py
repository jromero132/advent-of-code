"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=9 ; task=2)
"""

import sys
from collections import defaultdict
from itertools import permutations


def main() -> None:
    edges = [line.strip().split() for line in sys.stdin]
    edges = [(line[0], line[2], int(line[4])) for line in edges]
    graph = defaultdict(dict)
    ans = 0
    for u, v, w in edges:
        graph[u][v] = w
        graph[v][u] = w
        ans += w

    # This is the Traveling Salesman Problem
    print(
        max(
            sum(graph[u][v] for u, v in zip(path, path[1:])) for path in permutations(graph.keys())
        ),
    )


if __name__ == "__main__":
    main()
