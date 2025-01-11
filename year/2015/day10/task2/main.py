"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=10 ; task=2)
"""

import sys


def main() -> None:
    line = sys.stdin.read().strip()
    for _ in range(50):
        ans, cnt = "", 1
        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                cnt += 1

            else:
                ans += str(cnt) + line[i - 1]
                cnt = 1

        ans += str(cnt) + line[-1]
        line = ans
    print(len(ans))


if __name__ == "__main__":
    main()
