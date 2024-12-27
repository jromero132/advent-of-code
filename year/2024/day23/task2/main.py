"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=23 ; task=2)
"""

import sys
from collections import defaultdict
from collections.abc import Iterator


def bron_kerbosch(graph: dict[str, set], r: set, p: set, x: set) -> Iterator[set]:
    """
    Implement the Bron-Kerbosch algorithm to find all maximal cliques in an undirected graph.

    This function uses a recursive backtracking method to systematically discover and generate all maximal cliques in
    the given graph. It works by progressively building cliques and exploring different vertex combinations while
    maintaining sets of potential, excluded, and current clique vertices.

    Args:
        graph (dict[str, set]): An adjacency list representation of the graph.
        r (set): The current clique being constructed.
        p (set): The set of potential vertices to add to the clique.
        x (set): The set of excluded vertices.

    Returns:
        Iterator[set]: An iterator yielding all maximal cliques found in the graph.

    """
    if not p and not x:
        yield r
    while p:
        v = p.pop()
        yield from bron_kerbosch(graph, r | {v}, p & graph[v], x & graph[v])
        x.add(v)


def main() -> None:
    graph = defaultdict(set)
    for line in sys.stdin:
        v, w = line.strip().split("-")
        graph[v].add(w)
        graph[w].add(v)

    print(",".join(sorted(max(bron_kerbosch(graph, set(), set(graph.keys()), set()), key=len))))


if __name__ == "__main__":
    main()
