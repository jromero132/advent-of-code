"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=22 ; task=1)
"""

import sys
from dataclasses import dataclass


@dataclass
class Brick:
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int


def overlaps(brick1: Brick, brick2: Brick) -> bool:
    """Check if two bricks overlaps in the X-Y plane (when viewed from above)"""
    return max(brick1.x1, brick2.x1) <= min(brick1.x2, brick2.x2) \
        and max(brick1.y1, brick2.y1) <= min(brick1.y2, brick2.y2)

def main() -> None:
    # Parse input: convert each line "x1,y1,z1~x2,y2,z2" into a Brick object
    bricks = [Brick(*map(int, line.strip().replace("~", ",").split(","))) for line in sys.stdin]

    # Normalize: ensure z1 <= z2 for all bricks (input may have reversed coordinates)
    for brick in bricks:
        if brick.z1 > brick.z2:
            brick.z1, brick.z2 = brick.z2, brick.z1

    # KEY STEP: Sort bricks by lowest Z coordinate to process from bottom to top
    bricks = sorted(bricks, key=lambda brick: brick.z1)

    # Let bricks fall and settle
    for i, brick in enumerate(bricks):
        # Find the highest supporting surface below this brick
        # Look at all already-settled bricks (bricks[:i]) that overlap in X-Y plane
        max_z = max(
            (brick_below.z2 + 1 for brick_below in bricks[:i] if overlaps(brick, brick_below)),
            default=1,
        )

        # Move brick down while preserving its height (z2 - z1 remains constant)
        brick.z2 -= brick.z1 - max_z  # Adjust top coordinate
        brick.z1 = max_z              # Set bottom to resting position

    # Build support relationship graph
    bricks_above = { i: set() for i in range(len(bricks)) }  # Set of bricks that brick i supports
    bricks_below = { i: set() for i in range(len(bricks)) }  # Set of bricks that support brick i

    # After all bricks are settled, find which bricks touch each other
    for i, upper in enumerate(bricks):
        for j, below in enumerate(bricks[:i]):  # Only check bricks below current one
            # Bricks touch if they overlap in X-Y AND upper sits directly on top of below
            if overlaps(upper, below) and upper.z1 == below.z2 + 1:
                bricks_below[i].add(j)
                bricks_above[j].add(i)

    # Count bricks that can be safely removed
    # A brick is safe if ALL bricks it supports have at least another supporters below it (at least 2 supporters)
    print(sum(all(len(bricks_below[j]) >= 2 for j in bricks_above[i]) for i in range(len(bricks))))


if __name__ == "__main__":
    main()
