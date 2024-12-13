"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2016 ; day=8 ; task=2)
"""

import itertools
import sys


def main() -> None:
    operations = sys.stdin.read().strip().splitlines()
    n, m = (3, 7) if len(operations) <= 10 else (6, 50)  # Sample cases should have <= 10 operations
    grid = [[False] * m for _ in range(n)]
    for operation in operations:
        op_parts = operation.split()

        if op_parts[0] == "rect":  # turn on
            w, h = (int(x) for x in op_parts[1].split("x"))
            for i, j in itertools.product(range(h), range(w)):
                grid[i][j] = True

        else:
            idx = int(op_parts[2][2:])
            k = int(op_parts[-1])

            if op_parts[1] == "row":  # rotate row
                k %= m
                new_row = [0] * m
                for i in range(m):
                    new_row[k] = grid[idx][i]
                    k += 1
                    if k == m:
                        k = 0

                grid[idx] = new_row

            else:
                k %= n
                new_col = [0] * n
                for i in range(n):
                    new_col[k] = grid[i][idx]
                    k += 1
                    if k == n:
                        k = 0

                for i in range(n):
                    grid[i][idx] = new_col[i]

    print("\n".join("".join("█" if c else "░" for c in row) for row in grid))  # RURUCEOEIL


if __name__ == "__main__":
    main()
