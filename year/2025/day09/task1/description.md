# --- Day 9: Movie Theater ---

You slide down[^1] the [firepole](https://en.wikipedia.org/wiki/Fireman%27s_pole) in the corner of the playground and land in the North Pole base movie theater!

The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are **red**; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

For example:
```
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
```

Showing red tiles as `#` and other tiles as `.`, the above arrangement of red tiles would look like this:
```
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
```

You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

For example, you could make a rectangle (shown as `O`) with an area of `24` between `2,5` and `9,7`:
```
..............
.......#...#..
..............
..#....#......
..............
..**O**OOOOOOO....
..OOOOOOOO....
..OOOOOOO**O**.#..
..............
```

Or, you could make a rectangle with area `35` between `7,1` and `11,7`:
```
..............
.......**O**OOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOO**O**..
..............
```

You could even make a thin rectangle with an area of only `6` between `7,3` and `2,3`:
```
..............
.......#...#..
..............
..**O**OOOO**O**......
..............
..#......#....
..............
.........#.#..
..............
```

Ultimately, the largest rectangle you can make in this example has area `**50**`. One way to do this is between `2,5` and `11,1`:
```
..............
..OOOOOOOOO**O**..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..**O**OOOOOOOOO..
..............
.........#.#..
..............
```

Using two red tiles as opposite corners, **what is the largest area of any rectangle you can make?**

[^1]: [slide down] wheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
