"""
Author: Jose A. Romero
Puzzle: Advent of Code (year=2023 ; day=22 ; task=2)
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

    ans = 0  # Total number of bricks that would fall across all chain reactions
    # For each brick, simulate what happens if we disintegrate it
    for i in range(len(bricks)):
        # STEP 1: Find initial bricks that would fall immediately
        # These are bricks that ONLY have brick i as their support
        # (they have exactly 1 supporter, and that's brick i)
        queue = [j for j in bricks_above[i] if len(bricks_below[j]) == 1]

        # STEP 2: Initialize set of all bricks that will fall
        # Includes brick i itself (the one we're disintegrating)
        # plus any bricks that lose their only support immediately
        bricks_falling = set(queue) | {i}

        # STEP 3: Process chain reaction using BFS (breadth-first search)
        idx = 0
        while idx < len(queue):
            j = queue[idx]  # Current brick that has fallen
            idx += 1

            # Check all bricks that j supports
            for k in bricks_above[j] - bricks_falling:
                # Brick k will fall if ALL of its supporters are in bricks_falling
                # (i.e., all its supports have already fallen)
                if bricks_below[k] <= bricks_falling:
                    queue.append(k)        # Add to processing queue
                    bricks_falling.add(k)  # Mark as falling

        # STEP 4: Count how many OTHER bricks fell (excluding brick i itself)
        # Add to running total for all bricks
        ans += len(bricks_falling) - 1

    print(ans)


if __name__ == "__main__":
    main()
