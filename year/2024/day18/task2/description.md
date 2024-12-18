# --- Part Two ---

The Historians aren't as used to moving around in this pixelated universe as you are. You're afraid they're not going to be fast enough to make it to the exit before the path is completely blocked.

To determine how fast everyone needs to go, you need to determine **the first byte that will cut off the path to the exit**.

In the above example, after the byte at `1,1` falls, there is still a path to the exit:
```
**O**..#**O****O****O**
**O**##**O****O**#**O**
**O**#**O****O**#**O****O**
**O****O****O**#**O****O**#
###**O****O**##
.##**O**###
#.#**O****O****O****O**
```

However, after adding the very next byte (at `6,1`), there is no longer a path to the exit:
```
...#...
.##..#**#**
.#..#..
...#..#
###..##
.##.###
#.#....
```

So, in this example, the coordinates of the first byte that prevents the exit from being reachable are `**6,1**`.

Simulate more of the bytes that are about to corrupt your memory space. **What are the coordinates of the first byte that will prevent the exit from being reachable from your starting position?** (Provide the answer as two integers separated by a comma with no other characters.)
