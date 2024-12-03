"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2021 ; day=1 ; task=2)
"""

import sys


def main() -> None:
    ans, prev, cur, window = 0, 0, 0, []

    for _ in range(3):
        window.append(int(sys.stdin.readline()))
        prev += window[-1]

    for i, cur in enumerate(int(x) for x in sys.stdin):
        window.append(cur)
        tmp = cur + prev - window[i]
        ans += prev < tmp
        prev = tmp

    print(ans)


if __name__ == "__main__":
    main()
