"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=8 ; task=1)
"""

import sys


def bfs(instructions: str, graph: dict[str, dict[str, str]], source: str) -> int:
    """
    Perform breadth-first search to find path length to a terminal node.

    Traverses a graph using cyclic instructions until reaching a node ending with 'Z'. The function tracks the number of
    steps taken to reach the terminal node from a given starting point.

    Args:
        instructions (str): A string of navigation instructions ('L' or 'R').
        graph (dict[str, dict[str, str]]): A dictionary representing the graph with node connections.
        source (str): The starting node for the search.

    Returns:
        int: The number of steps taken to reach a node ending with 'Z'.

    """
    node = source
    i = 0
    while node != "ZZZ":
        node = graph[node][instructions[i % len(instructions)]]
        i += 1
    return i


def main() -> None:
    instructions, edges = sys.stdin.read().strip().split("\n\n")
    graph = {}
    for edge in edges.split("\n"):
        node, target = edge.split(" = ")
        left, right = target[1:-1].split(", ")
        graph[node] = {"L": left, "R": right}

    print(bfs(instructions, graph, "AAA"))


if __name__ == "__main__":
    main()
