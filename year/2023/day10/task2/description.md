# --- Part Two ---

You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is **within the area enclosed by the loop**?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:
```
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
```

The above loop encloses merely **four tiles** - the two pairs of `.` in the southwest and southeast (marked `I` below). The middle `.` tiles (marked `O` below) are **not** in the loop. Here is the same loop again with those regions marked:
```
...........
.S-------7.
.|F-----7|.
.||**OOOOO**||.
.||**OOOOO**||.
.|L-7**O**F-J|.
.|**II**|**O**|**II**|.
.L--J**O**L--J.
.....**O**.....
```

In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, `I` is still within the loop and `O` is still outside the loop:
```
..........
.S------7.
.|F----7|.
.||**OOOO**||.
.||**OOOO**||.
.|L-7F-J|.
.|**II**||**II**|.
.L--JL--J.
..........
```

In both of the above examples, `**4**` tiles are enclosed by the loop.

Here's a larger example:
```
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
```

The above sketch has many random bits of ground, some of which are in the loop (`I`) and some of which are outside it (`O`):
```
**O**F----7F7F7F7F-7**OOOO**
**O**|F--7||||||||FJ**OOOO**
**O**||**O**FJ||||||||L7**OOOO**
FJL7L7LJLJ||LJ**I**L-7**OO**
L--J**O**L7**III**LJS7F-7L7**O**
**OOOO**F-J**II**F7FJ|L7L7L7
**OOOO**L7**I**F7||L7|**I**L7L7|
**OOOOO**|FJLJ|FJ|F7|**O**LJ
**OOOO**FJL-7**O**||**O**||||**OOO**
**OOOO**L---J**O**LJ**O**LJLJ**OOO**
```

In this larger example, `**8**` tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:
```
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
```

Here are just the tiles that are **enclosed by the loop** marked with `I`:
```
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ**I**F7FJ-
L---JF-JLJ**IIII**FJLJJ7
|F|F-JF---7**III**L7L|7|
|FFJF7L7F-JF7**II**L---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
```

In this last example, `**10**` tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. **How many tiles are enclosed by the loop?**
