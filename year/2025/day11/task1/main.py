"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=11 ; task=1)
"""

import sys


def main() -> None:
    graph = {u: nodes.split() for u, nodes in (line.split(": ") for line in sys.stdin.read().splitlines())}

    ans = 0
    stack = [("you", "")]
    while stack:
        cur_node, parent_node = stack.pop()
        for next_node in graph[cur_node]:
            if next_node == "out":
                ans += 1

            elif next_node != parent_node:
                stack.append((next_node, cur_node))

    print(ans)


if __name__ == "__main__":
    main()
