"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=7 ; task=1)
"""

import heapq
import sys
from collections import defaultdict


def main() -> None:
    edges, in_degree = defaultdict(list), defaultdict(int)
    for line in sys.stdin:
        parts = line.split()
        v, w = parts[1], parts[-3]
        edges[v].append(w)
        in_degree[w] += 1

    topo, ans = [], []
    for v in edges:
        if in_degree[v] == 0:
            heapq.heappush(topo, v)

    while topo:
        v = heapq.heappop(topo)
        ans.append(v)
        for w in edges[v]:
            in_degree[w] -= 1
            if in_degree[w] == 0:
                heapq.heappush(topo, w)

    print("".join(ans))


if __name__ == "__main__":
    main()
