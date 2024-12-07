"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2019 ; day=6 ; task=1)
"""

import sys
from collections import defaultdict


def main() -> None:
    edges_lst = [[x.strip() for x in line.split(")")] for line in sys.stdin]
    edges, in_degree = defaultdict(list), defaultdict(int)
    for v, w in edges_lst:
        edges[v].append(w)
        in_degree[w] += 1

    queue = [node for node in edges if node not in in_degree]
    i, ans, orbits = 0, 0, defaultdict(int)
    while i < len(queue):
        cur_node = queue[i]
        ans += orbits[cur_node]
        for w in edges[cur_node]:
            orbits[w] += orbits[cur_node] + 1
            in_degree[w] -= 1
            if in_degree[w] == 0:
                queue.append(w)

        i += 1

    print(ans)


if __name__ == "__main__":
    main()
