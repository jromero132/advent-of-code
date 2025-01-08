"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=24 ; task=1)
"""

import sys
from collections import defaultdict, deque
from operator import and_, or_, xor


def main() -> None:
    gate_func = {"AND": and_, "OR": or_, "XOR": xor}
    initial_values, gates_str = sys.stdin.read().strip().split("\n\n")
    node_values = {}
    for line in initial_values.split("\n"):
        node, value = line.split(": ")
        node_values[node] = int(value)

    unknown_values = {}
    graph = defaultdict(list)
    gates = {}
    queue = deque()
    for line in gates_str.split("\n"):
        v, gate, w, _, node = line.split()
        unknown_value = (v not in initial_values) + (w not in initial_values)
        unknown_values[node] = unknown_value
        graph[v].append(node)
        graph[w].append(node)
        gates[node] = (v, gate, w)
        if unknown_value == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        v, gate, w = gates[node]
        node_values[node] = gate_func[gate](node_values[v], node_values[w])
        for v in graph[node]:
            unknown_values[v] -= 1
            if unknown_values[v] == 0:
                queue.append(v)

    print(
        int(
            "".join(
                str(node_values[v])
                for v in sorted(node_values.keys(), reverse=True)
                if v.startswith("z")
            ),
            2,
        ),
    )


if __name__ == "__main__":
    main()
