"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=10 ; task=2)
"""

import sys


def polygon_area(vertices: list[list[int]]) -> float:  # shoelace theorem
    n = len(vertices)
    return (
        abs(
            sum(
                vertices[i][0] * vertices[(i + 1) % n][1]
                - vertices[(i + 1) % n][0] * vertices[i][1]
                for i in range(n)
            ),
        )
        / 2
    )


def interior_points(points: list[list[int]]) -> int:  # Pick's theorem
    return int(polygon_area(points) - len(points) / 2) + 1


def main() -> None:
    pipes = {
        "|": ((-1, 0), (1, 0)),
        "-": ((0, -1), (0, 1)),
        "L": ((-1, 0), (0, 1)),
        "J": ((-1, 0), (0, -1)),
        "7": ((1, 0), (0, -1)),
        "F": ((1, 0), (0, 1)),
    }
    graph, start = {}, None
    for i, line in enumerate(sys.stdin):
        for j, c in enumerate(line.strip()):
            if c == "S":
                start = (i, j)

            elif c in pipes:
                graph[i, j] = [(i + dr, j + dc) for dr, dc in pipes[c]]

    graph[start] = [k for k, v in graph.items() if start in v]
    queue, dist = [start], {start: 0}
    i = 0
    while i < len(queue):
        cur = queue[i]
        for nxt in graph[cur]:
            if nxt in graph and nxt not in dist:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
                break

        i += 1

    print(interior_points(queue))


if __name__ == "__main__":
    main()
