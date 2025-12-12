"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=9 ; task=2)
"""

import sys


def get_rectangle_fill(
    grid: list[list[int]],
    compressed_x: list[int],
    compressed_y: list[int],
    p1: tuple[int, int],
    p2: tuple[int, int],
) -> bool:
    # To calculate the sum of the rectangle in the grid, we need the top-left and bottom-right points
    x1, y1 = min(p1[0], p2[0]), min(p1[1], p2[1])
    x2, y2 = max(p1[0], p2[0]), max(p1[1], p2[1])

    cx1, cy1 = compressed_x[x1], compressed_y[y1]
    cx2, cy2 = compressed_x[x2], compressed_y[y2]

    rect_sum = grid[cx2 + 1][cy2 + 1] - grid[cx1][cy2 + 1] - grid[cx2 + 1][cy1] + grid[cx1][cy1]
    return (x2 - x1 + 1) * (y2 - y1 + 1) if rect_sum == (cx2 - cx1 + 1) * (cy2 - cy1 + 1) else 0


def main() -> None:
    points = [tuple(map(int, line.split(",")))[::-1] for line in sys.stdin.read().splitlines()]
    points_x, points_y = set(), set()
    for x, y in points:
        points_x.update((x - 1, x, x + 1))
        points_y.update((y - 1, y, y + 1))

    compressed_x = {x: i for i, x in enumerate(sorted(points_x))}
    compressed_y = {y: i for i, y in enumerate(sorted(points_y))}

    n, m = len(compressed_x), len(compressed_y)
    grid = [[-1] * m for _ in range(n)]

    # Create the boundary
    for i in range(len(points)):
        x1, y1 = points[i - 1]  # When i = 0 then i - 1 = -1 and that's the last point :)
        x2, y2 = points[i]

        x1, y1 = compressed_x[x1], compressed_y[y1]
        x2, y2 = compressed_x[x2], compressed_y[y2]

        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][j] = 1

        else:  # y1 == y2 -> the input guarantees this
            for j in range(min(x1, x2), max(x1, x2) + 1):
                grid[j][y1] = 1

    # Fill out of the boundary -> Assuming that (0, 0) is out of the boundary :)
    stack = [(0, 0)]
    grid[0][0] = 0
    while stack:
        x, y = stack.pop()
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == -1:
                stack.append((nx, ny))
                grid[nx][ny] = 0

    # Fill inside the boundary -> Easy since you are either inside the boundary or outside
    # and we check the outside already :)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == -1:
                grid[i][j] = 1

    # Prefix sum to check wheter a rectangle is completely filled
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            prefix_sum[i + 1][j + 1] = grid[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]

    ans = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ans = max(ans, get_rectangle_fill(prefix_sum, compressed_x, compressed_y, points[i], points[j]))

    print(ans)


if __name__ == "__main__":
    main()
