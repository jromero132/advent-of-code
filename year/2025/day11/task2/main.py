"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=11 ; task=2)
"""

import sys
from functools import cache


def dfs_with_memoization(graph: dict[str, list[str]]) -> int:
    # Same solution as before, the only thing is that we now calculate the amount of paths and use cache :)
    @cache
    def _wrapped_func(cur_node: int, parent_node: int, pass_dac: bool, pass_fft: bool) -> int:
        ans = 0
        for next_node in graph[cur_node]:
            if next_node == "out":
                return 1 if pass_dac and pass_fft else 0

            if next_node != parent_node:
                ans += _wrapped_func(
                    next_node,
                    cur_node,
                    pass_dac or (next_node == "dac"),
                    pass_fft or (next_node == "fft"),
                )

        return ans

    return _wrapped_func("svr", "", False, False)


def main() -> None:
    graph = {u: nodes.split() for u, nodes in (line.split(": ") for line in sys.stdin.read().splitlines())}
    print(dfs_with_memoization(graph))


if __name__ == "__main__":
    main()
