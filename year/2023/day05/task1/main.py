"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=5 ; task=1)
"""

import sys


def main() -> None:
    input_parts = sys.stdin.read().strip().split("\n\n")
    seeds = [int(n) for n in input_parts[0].split()[1:]]
    maps = [
        [[int(num) for num in section.split()] for section in map_.split("\n")[1:]]
        for map_ in input_parts[1:]
    ]

    for map_ in maps:
        checked = [False] * len(seeds)
        for sector in map_:
            for i in range(len(seeds)):
                if not checked[i] and sector[1] <= seeds[i] < sector[1] + sector[2]:
                    seeds[i] = sector[0] + seeds[i] - sector[1]
                    checked[i] = True

    print(min(seeds))


if __name__ == "__main__":
    main()
