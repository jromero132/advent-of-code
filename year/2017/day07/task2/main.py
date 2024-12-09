"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=7 ; task=2)
"""

import sys
from collections import defaultdict


def dfs(
    graph: dict[str, list[str]],
    weight: dict[str, int],
    node: str,
    memo: dict[str, int],
) -> int:
    """
    Perform a depth-first search (DFS) on a directed graph to compute the total weight of a specified node. The function
    checks for discrepancies in the weights of child nodes and prints the corrected weight if a discrepancy is found.

    Args:
        graph (dict[str, list[str]]): A dictionary representing the directed graph, where keys are node identifiers
            and values are lists of child node identifiers.
        weight (dict[str, int]): A dictionary mapping node identifiers to their respective weights.
        node (str): The identifier of the current node being processed.
        memo (dict[str, int]): A dictionary used to store previously computed weights for nodes to optimize performance.

    Returns:
        int: The total weight of the specified node, including the weights of its children.

    Raises:
        SystemExit: If a discrepancy in child weights is detected, the function will print the corrected weight and
            exit.

    """
    if node not in memo:
        if len(graph[node]) == 0:
            memo[node] = weight[node]

        else:
            child_weights = sorted(
                ((dfs(graph, weight, child, memo), child) for child in graph[node]),
                key=lambda x: x[0],
            )
            # Since it is assured that only one weight differs, then there must be at least 3 values so they can differ
            if len(child_weights) >= 3 and (
                child_weights[0][0] != child_weights[1][0]
                or child_weights[1][0] != child_weights[-1][0]
            ):
                diff = (
                    child_weights[-1]
                    if child_weights[0][0] == child_weights[1][0]
                    else child_weights[0]
                )
                print(weight[diff[1]] + child_weights[1][0] - diff[0])
                sys.exit(0)

            memo[node] = weight[node] + child_weights[0][0] * len(graph[node])
    return memo[node]


def main() -> None:
    graph, weight, above = defaultdict(list), {}, set()
    for line in sys.stdin:
        program_def = line.strip().split(" -> ")
        program, w = program_def[0].split()
        weight[program] = int(w[1:-1])

        if len(program_def) == 2:
            for p in program_def[1].split(", "):
                graph[program].append(p)
                above.add(p)

    origin = (set(graph.keys()) - above).pop()
    dfs(graph, weight, origin, {})


if __name__ == "__main__":
    main()
