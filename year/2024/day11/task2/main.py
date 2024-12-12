"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=11 ; task=2)
"""

import sys


def get_stones_at_blink(stone_id: str, blink: int, memo: dict[tuple[int, int], int]) -> int:
    if (stone_id, blink) not in memo:
        if blink == 0:
            stones = 1

        elif stone_id == "0":
            stones = get_stones_at_blink("1", blink - 1, memo)

        elif len(stone_id) % 2 == 0:
            mid = len(stone_id) // 2
            stones = get_stones_at_blink(stone_id[:mid], blink - 1, memo)
            stones += get_stones_at_blink(str(int(stone_id[mid:])), blink - 1, memo)

        else:
            stones = get_stones_at_blink(str(int(stone_id) * 2024), blink - 1, memo)

        memo[(stone_id, blink)] = stones

    return memo[(stone_id, blink)]


def main() -> None:
    total_blinks = 75
    stones = sys.stdin.read().strip().split()
    memo = {}
    print(sum(get_stones_at_blink(s, total_blinks, memo) for s in stones))


if __name__ == "__main__":
    main()
