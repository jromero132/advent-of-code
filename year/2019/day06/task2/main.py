"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=6 ; task=2)
"""

import sys
from collections import defaultdict


def main() -> None:
    edges_lst = [[x.strip() for x in line.split(")")] for line in sys.stdin]
    edges = defaultdict(list)
    for v, w in edges_lst:
        edges[v].append(w)
        edges[w].append(v)

    origin, destination = "YOU", "SAN"
    queue = [origin]
    i, dist = 0, {origin: 0}
    while i < len(queue):
        cur_node = queue[i]

        if cur_node == destination:
            break

        for w in edges[cur_node]:
            if w not in dist:
                queue.append(w)
                dist[w] = dist[cur_node] + 1
        i += 1
    print(dist[destination] - 2)


if __name__ == "__main__":
    main()
