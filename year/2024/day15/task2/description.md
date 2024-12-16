# --- Part Two ---

The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a **second** warehouse's robot is **also** malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is **twice as wide**! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:
    - If the tile is `#`, the new map contains `##` instead.
    - If the tile is `O`, the new map contains `[]` instead.
    - If the tile is `.`, the new map contains `..` instead.
    - If the tile is `@`, the new map contains `@.` instead.

This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by `[]`. (The robot does not change size.)

The larger example from before would now look like this:
```
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
```

Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:
```
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
```

After appropriately resizing this map, the robot would push around these boxes as follows:
```
Initial state:
##############
##......##..##
##..........##
##....[][]**@**.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]**@**..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].**@**..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......**@**..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......**@**...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....**@**....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....**@**....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....**@**....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....**@**.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...**@**......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...**@**[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...**@**.[]...##
##....[]....##
##..........##
##..........##
##############
```

This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of `1` from the top edge of the map and `5` from the left edge of the map, resulting in a GPS coordinate of `100 * 1 + 5 = 105`.
```
##########
##...[]...
##........
```

In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:
```
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..**@**......[].[][]##
##......[][]..[]..##
####################
```

The sum of these boxes' GPS coordinates is `**9021**`.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. **What is the sum of all boxes' final GPS coordinates?**
