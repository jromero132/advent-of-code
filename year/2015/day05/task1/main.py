"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=5 ; task=1)
"""

import sys


def main():
    invalid_substr = ["ab", "cd", "pq", "xy"]
    ans = 0
    for line in sys.stdin:
        if (
            all(substr not in line for substr in invalid_substr)
            and sum(line.count(c) for c in "aeiou") >= 3
        ):
            for i in range(1, len(line)):
                if line[i] == line[i - 1]:
                    ans += 1
                    break

    print(ans)


if __name__ == "__main__":
    main()
