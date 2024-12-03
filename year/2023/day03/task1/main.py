"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=3 ; task=1)
"""

import sys


def main() -> None:
    grid = [line.strip() for line in sys.stdin]
    ans = 0
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].isdigit():
                neighbour_symbol = False
                p = j
                while p < len(grid[i]) and grid[i][p].isdigit():
                    if (i > 0 and grid[i - 1][p] != "." and not grid[i - 1][p].isdigit()) or (
                        i + 1 < len(grid) and grid[i + 1][p] != "." and not grid[i + 1][p].isdigit()
                    ):
                        neighbour_symbol = True
                    p += 1

                for dj in (j - 1, p):
                    for di in range(i - 1, i + 2):
                        if (
                            0 <= di < len(grid)
                            and 0 <= dj < len(grid[di])
                            and grid[di][dj] != "."
                            and not grid[di][dj].isdigit()
                        ):
                            neighbour_symbol = True

                if neighbour_symbol:
                    ans += int(grid[i][j:p])

                j = p

            else:
                j += 1

    print(ans)


if __name__ == "__main__":
    main()
