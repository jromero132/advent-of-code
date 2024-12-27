"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=21 ; task=2)
"""

import sys
from functools import cache


def get_all_shortest_paths(pad: dict[str, tuple[int, int]]) -> dict[tuple[str, str], str]:
    """
    Calculate the shortest paths between all points in a given pad configuration.

    This function determines the shortest routes between points in a grid-like structure, considering horizontal and
    vertical movements. It generates paths that minimize the total distance traveled while avoiding a designated empty
    cell.

    Args:
        pad (dict[str, tuple[int, int]]): A dictionary mapping keys to grid coordinates.

    Returns:
        dict[tuple[str, str], str]: A dictionary of shortest paths between each pair of points.

    """
    shortest_paths = {}
    for k1, v1 in pad.items():
        if k1 == " ":
            continue
        for k2, v2 in pad.items():
            if k2 == " ":
                continue

            r, c = v2[0] - v1[0], v2[1] - v1[1]
            paths = []
            # There are only two important (optimal) paths:
            #   - path 1: all the way left/right and then down/up
            #   - path 2: all the way down/up and then left/right

            if pad[" "] != (v1[0], v2[1]):  # Check if path 1 is not passing by the empty cell
                paths.append(
                    (">" if c > 0 else "<") * abs(c) + ("v" if r > 0 else "^") * abs(r) + "A",
                )

            if pad[" "] != (v2[0], v1[1]):  # Check if path 2 is not passing by the empty cell
                paths.append(
                    ("v" if r > 0 else "^") * abs(r) + (">" if c > 0 else "<") * abs(c) + "A",
                )

            shortest_paths[k1, k2] = paths
    return shortest_paths


numpad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    " ": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}
all_shortest_numpad = get_all_shortest_paths(numpad)

keypad = {
    " ": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}
all_shortest_keypad = get_all_shortest_paths(keypad)


@cache
def get_shortest_path_length(code: str, bot: int) -> int:
    """
    Recursively calculates the shortest path length for a given code sequence.

    This function uses dynamic programming with memoization to efficiently compute the shortest path length across a
    sequence of characters. It selects the appropriate shortest path dictionary based on the first character and
    recursively finds the minimum path length for the given bot count.

    Args:
        code (str): The sequence of characters to navigate through.
        bot (int): The number of bots available for path traversal.

    Returns:
        int: The length of the shortest possible path.

    """
    if bot == 0:
        return len(code)

    shortest_path = all_shortest_numpad if code[0] in numpad else all_shortest_keypad
    return sum(
        min(get_shortest_path_length(path, bot - 1) for path in shortest_path[cur, nxt])
        for cur, nxt in zip(f"A{code}", code)
    )


def main() -> None:
    print(
        sum(
            get_shortest_path_length(code, 26) * int(code[:-1])
            for code in sys.stdin.read().strip().split("\n")
        ),
    )


if __name__ == "__main__":
    main()
