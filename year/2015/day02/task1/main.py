"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2015 ; day=2 ; task=1)
"""

import sys


def main() -> None:
    ans = 0
    for line in sys.stdin:
        dims = [int(n) for n in line.split("x")]
        faces = [dims[i] * dims[j] for i in range(len(dims)) for j in range(i + 1, len(dims))]
        ans += 2 * sum(faces) + min(faces)

    print(ans)


if __name__ == "__main__":
    main()
