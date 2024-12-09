"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2018 ; day=7 ; task=2)
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

    if len(edges) <= 5:
        base_time = 0
        total_workers = 2

    else:
        base_time = 60
        total_workers = 5

    topo, workers, time = [], [], 0
    for v in edges:
        if in_degree[v] == 0:
            heapq.heappush(topo, v)

    while topo or workers:
        while topo and len(workers) < total_workers:
            v = heapq.heappop(topo)
            heapq.heappush(workers, (base_time + ord(v) - ord("A") + 1, v))

        t, v = heapq.heappop(workers)
        time += t
        for w in edges[v]:
            in_degree[w] -= 1
            if in_degree[w] == 0:
                heapq.heappush(topo, w)

        for i in range(len(workers)):
            workers[i] = (workers[i][0] - t, workers[i][1])

    print(time)


if __name__ == "__main__":
    main()
