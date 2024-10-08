"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=4 ; task=1)
"""

import sys
from collections import defaultdict


def main():
    ans = 0
    for line in sys.stdin:
        parts = line.split("-")
        counter = defaultdict(int)
        for part in parts[:-1]:
            for c in part:
                counter[c] += 1

        correct_checksum = "".join(
            char for char, _ in sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:5]
        )

        p1 = 1
        while parts[-1][p1].isdigit():
            p1 += 1

        p2 = p1 + 1
        while parts[-1][p2] != "]":
            p2 += 1

        sector_id, checksum = parts[-1][:p1], parts[-1][p1 + 1 : p2]
        if checksum == correct_checksum:
            ans += int(sector_id)

    print(ans)


if __name__ == "__main__":
    main()
