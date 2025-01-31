"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=19 ; task=1)
"""

import sys


def main() -> None:
    workflows, parts = sys.stdin.read().strip().split("\n\n")

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
    for part in parts.split("\n"):
        part_vals = {(q := p.split("="))[0]: int(q[1]) for p in part[1:-1].split(",")}
        cur_workflow = "in"
        while cur_workflow not in ("A", "R"):
            rules = workflow[cur_workflow]
            for cond, dest in rules:
                if eval(cond, {}, part_vals):
                    cur_workflow = dest
                    break

        if cur_workflow == "A":
            ans += sum(part_vals.values())

    print(ans)


if __name__ == "__main__":
    main()
