"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=19 ; task=2)
"""

import sys
from math import prod


def main() -> None:
    workflows, _ = sys.stdin.read().strip().split("\n\n")

    workflow = {}
    for w in workflows.split("\n"):
        idx = w.find("{")
        name, rules = w[:idx], w[idx + 1 : -1]
        rules = rules.split(",")
        rules[-1] = ["True", rules[-1]]
        for i in range(len(rules) - 1):
            rules[i] = rules[i].split(":")
        workflow[name] = rules

    ans = 0
    queue = [("in", [(1, 4000)] * 4, ["in"])]
    while queue:
        cur_workflow, cur_range, p = queue.pop()

        if cur_workflow in ("A", "R"):
            ans += prod(hi - lo + 1 for lo, hi in cur_range) if cur_workflow == "A" else 0
            continue

        rules = workflow[cur_workflow]
        for cond, dest in rules[:-1]:
            i = "xmas".index(cond[0])
            n = int(cond[2:])
            next_range = cur_range.copy()
            if cur_range[i][0] < n < cur_range[i][1]:
                next_range[i] = (
                    (cur_range[i][0], n - 1) if cond[1] == "<" else (n + 1, cur_range[i][1])
                )
                cur_range[i] = (n, cur_range[i][1]) if cond[1] == "<" else (cur_range[i][0], n)
                queue.append((dest, next_range, [*p, dest]))

        queue.append((rules[-1][1], cur_range, [*p, rules[-1][1]]))

    print(ans)


if __name__ == "__main__":
    main()
