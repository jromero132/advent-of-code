"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2022 ; day=8 ; task=2)
"""

import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    n, m = len(lines) - 1, len(lines[0]) - 1
    dp1 = [
        [0] * len(lines[0]) for _ in range(len(lines))
    ]  # how many trees to the left can tree [i][j] see
    dp2 = [
        [0] * len(lines[0]) for _ in range(len(lines))
    ]  # how many trees to the right can tree [i][j] see
    dp3 = [
        [0] * len(lines[0]) for _ in range(len(lines))
    ]  # how many trees to the bottom can tree [i][j] see
    dp4 = [
        [0] * len(lines[0]) for _ in range(len(lines))
    ]  # how many trees to the top can tree [i][j] see

    for i in range(1, n):  # run for rows
        stack1, stack2 = [0], [n]
        for j, k in zip(range(1, m), range(m - 1, 0, -1)):
            while stack1 and lines[i][stack1[-1]] < lines[i][j]:  # run from left to right
                stack1.pop()

            while stack2 and lines[i][stack2[-1]] < lines[i][k]:  # run from right to left
                stack2.pop()

            dp1[i][j] = j - stack1[-1] if stack1 else j
            dp2[i][k] = stack2[-1] - k if stack2 else m - k

            stack1.append(j)
            stack2.append(k)

    for i in range(1, m):  # run for columns
        stack1, stack2 = [0], [m]
        for j, k in zip(range(1, n), range(n - 1, 0, -1)):
            while stack1 and lines[stack1[-1]][i] < lines[j][i]:  # run from top to bottom
                stack1.pop()

            while stack2 and lines[stack2[-1]][i] < lines[k][i]:  # run from bottom to top
                stack2.pop()

            dp3[j][i] = j - stack1[-1] if stack1 else j
            dp4[k][i] = stack2[-1] - k if stack2 else n - k

            stack1.append(j)
            stack2.append(k)

    print(
        max(
            dp1[i][j] * dp2[i][j] * dp3[i][j] * dp4[i][j]
            for i in range(len(dp1))
            for j in range(len(dp1[0]))
        ),
    )


if __name__ == "__main__":
    main()
