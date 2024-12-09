"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=9 ; task=2)
"""

import sys


def get_interval_sum(n: int, m: int) -> int:
    """
    Calculate the sum of integers in the interval from n to m, inclusive.

    This function uses the formula for the sum of the first n integers to efficiently compute the result of the sum all
    integers in the interval from n to m, inclusive.

    Args:
        n (int): The starting integer of the interval.
        m (int): The ending integer of the interval.

    Returns:
        int: The sum of all integers from n to m, inclusive.

    """
    return (m * (m + 1) - n * (n + 1)) // 2


def main() -> None:
    line = sys.stdin.read().strip()
    tot_memory, memory_slots, free_space = 0, [], []
    for i in range(len(line)):
        n = int(line[i])
        if n == 0:
            continue

        if i % 2 == 0:
            _id = i // 2
            memory_slots.append((n, tot_memory, i // 2))

        else:
            _id = -1
            free_space.append((n, tot_memory))

        tot_memory += n

    memory = []
    for cnt, pos, _id in memory_slots[::-1]:
        starting_pos = pos
        for i in range(len(free_space)):
            if pos < free_space[i][1]:
                break

            if free_space[i][0] >= cnt:
                starting_pos = free_space[i][1]

                if free_space[i][0] == cnt:
                    free_space.pop(i)

                else:
                    free_space[i] = (free_space[i][0] - cnt, free_space[i][1] + cnt)

                break

        memory.append((_id, starting_pos, starting_pos + cnt - 1))

    print(sum(_id * get_interval_sum(start_pos - 1, end_pos) for _id, start_pos, end_pos in memory))


if __name__ == "__main__":
    main()
