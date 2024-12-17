# --- Part Two ---

Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (`S`, `.`, or `E`) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is **whether the tile is on one of the best paths through the maze**. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of **any** best path through the maze, including the `S` and `E` tiles.

In the first example, there are `**45**` tiles (marked `O`) that are part of at least one of the various best paths through the maze:
```
###############
#.......#....**O**#
#.#.###.#.###**O**#
#.....#.#...#**O**#
#.###.#####.#**O**#
#.#.#.......#**O**#
#.#.#####.###**O**#
#..**O****O****O****O****O****O****O****O****O**#**O**#
###**O**#**O**#####**O**#**O**#
#**O****O****O**#**O**....#**O**#**O**#
#**O**#**O**#**O**###.#**O**#**O**#
#**O****O****O****O****O**#...#**O**#**O**#
#**O**###.#.#.#**O**#**O**#
#**O**..#.....#**O****O****O**#
###############
```

In the second example, there are `**64**` tiles that are part of at least one of the best paths:
```
#################
#...#...#...#..**O**#
#.#.#.#.#.#.#.#**O**#
#.#.#.#...#...#**O**#
#.#.#.#.###.#.#**O**#
#**O****O****O**#.#.#.....#**O**#
#**O**#**O**#.#.#.#####**O**#
#**O**#**O**..#.#.#**O****O****O****O****O**#
#**O**#**O**#####.#**O**###**O**#
#**O**#**O**#..**O****O****O****O****O**#**O****O****O**#
#**O**#**O**###**O**#####**O**###
#**O**#**O**#**O****O****O**#..**O****O****O**#.#
#**O**#**O**#**O**#####**O**###.#
#**O**#**O**#**O****O****O****O****O****O****O**..#.#
#**O**#**O**#**O**#########.#
#**O**#**O****O****O**..........#
#################
```

Analyze your map further. **How many tiles are part of at least one of the best paths through the maze?**
