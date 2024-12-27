"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=23 ; task=1)
"""

import sys
from collections import defaultdict


def is_clique(nodes: list, graph: dict[str, set]) -> bool:
    s, n = set(nodes), len(nodes) - 1
    for node in nodes:
        s.remove(node)
        if len(graph[node] & s) != n:
            return False
        s.add(node)
    return True


def main() -> None:
    graph = defaultdict(set)
    edges = []
    for line in sys.stdin:
        v, w = line.strip().split("-")
        edges.append((v, w))
        graph[v].add(w)
        graph[w].add(v)

    print(
        sum(
            node not in (v, w)
            and any(pc[0] == "t" for pc in (node, v, w))
            and v in connections
            and w in connections
            for node, connections in graph.items()
            for v, w in edges
        )
        // 3,  # divided by 3 since each clique will be detected on each of the 3 nodes :P
    )


if __name__ == "__main__":
    main()
