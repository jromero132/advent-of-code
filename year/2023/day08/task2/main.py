"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=8 ; task=2)
"""

import math
import sys

# NOTE: This solution is not correct for the general case, but it is correct for the AoC challenge. In my humble
#   opinion, it is not worth to solve the general case, since there is a big difference between the solution for the
#   general case and the solution to this silly problem where all inputs are constructed in a way that:
#       - each start node reaches only one end node.
#       - the distance from the start node to the end node is the same as the distance from the end to itself (the
#           period of the cycle).
# PD: After all, AoC challenge is to solve a problem based on your single input, not to solve the general problem :P


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
    while node[-1] != "Z":
        node = graph[node][instructions[i % len(instructions)]]
        i += 1
    return i


def main() -> None:
    instructions, edges = sys.stdin.read().strip().split("\n\n")
    graph, source = {}, []
    for edge in edges.split("\n"):
        node, target = edge.split(" = ")
        left, right = target[1:-1].split(", ")
        graph[node] = {"L": left, "R": right}
        if node[-1] == "A":
            source.append(node)

    print(math.lcm(*[bfs(instructions, graph, s) for s in source]))


if __name__ == "__main__":
    main()
