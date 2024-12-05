"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2017 ; day=6 ; task=1)
"""

import sys


def get_index_of_max(memory: tuple[int]) -> int:
    """
    Find the index of the maximum value in a tuple of integers.

    This function iterates through the provided tuple and identifies the index of the largest integer. It returns the
    index of the first occurrence of the maximum value found.

    Args:
        memory (tuple[int]): A tuple of integers to search for the maximum value.

    Returns:
        int: The index of the maximum value in the tuple.

    """
    index_of_max = 0
    for i in range(1, len(memory)):
        if memory[i] > memory[index_of_max]:
            index_of_max = i
    return index_of_max


def redistribute_grid(memory: tuple[int]) -> tuple[int]:
    """
    Redistribute memory blocks across a grid based on the maximum value.

    This function takes a tuple representing memory blocks and redistributes them evenly across the grid, starting from
    the index of the maximum value. The maximum value is set to zero, and the blocks are distributed to the subsequent
    indices.

    Args:
        memory (tuple[int]): A tuple of integers representing memory blocks.

    Returns:
        tuple[int]: A new tuple representing the redistributed memory blocks.

    """
    n, idx = len(memory), get_index_of_max(memory)
    blocks, blocks_remaining = memory[idx] // n, memory[idx] % n
    result = list(memory)
    result[idx] = 0
    for i in range(1, n + 1):
        idx = idx + 1 if idx != n - 1 else 0
        result[idx] += blocks + (i <= blocks_remaining)
    return tuple(result)


def main() -> None:
    grid = tuple(int(x) for x in sys.stdin.read().split())
    seen_states = set()
    while grid not in seen_states:
        seen_states.add(grid)
        grid = redistribute_grid(grid)

    print(len(seen_states))


if __name__ == "__main__":
    main()
