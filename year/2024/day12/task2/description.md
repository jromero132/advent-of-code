# --- Part Two ---

Fortunately, the Elves are trying to order so much fence that they qualify for a **bulk discount**!

Under the bulk discount, instead of using the perimeter to calculate the price, you need to use the **number of sides** each region has. Each straight section of fence counts as a side, regardless of how long it is.

Consider this example again:
```
AAAA
BBCD
BBCC
EEEC
```

The region containing type `A` plants has `4` sides, as does each of the regions containing plants of type `B`, `D`, and `E`. However, the more complex region containing the plants of type `C` has `8` sides!

Using the new method of calculating the per-region price by multiplying the region's area by its number of sides, regions `A` through `E` have prices `16`, `16`, `32`, `4`, and `12`, respectively, for a total price of `**80**`.

The second example above (full of type `X` and `O` plants) would have a total price of `**436**`.

Here's a map that includes an E-shaped region full of type `E` plants:
```
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
```

The E-shaped region has an area of `17` and `12` sides for a price of `204`. Including the two regions full of type `X` plants, this map has a total price of `**236**`.

This map has a total price of `**368**`:
```
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
```

It includes two regions full of type `B` plants (each with `4` sides) and a single region full of type `A` plants (with `4` sides on the outside and `8` more sides on the inside, a total of `12` sides). Be especially careful when counting the fence around regions like the one full of type `A` plants; in particular, each section of fence has an in-side and an out-side, so the fence does not connect across the middle of the region (where the two `B` regions touch diagonally). (The Elves would have used the Möbius Fencing Company instead, but their contract terms were too one-sided.)

The larger example from before now has the following updated prices:
    - A region of `R` plants with price `12 * 10 = 120`.
    - A region of `I` plants with price `4 * 4 = 16`.
    - A region of `C` plants with price `14 * 22 = 308`.
    - A region of `F` plants with price `10 * 12 = 120`.
    - A region of `V` plants with price `13 * 10 = 130`.
    - A region of `J` plants with price `11 * 12 = 132`.
    - A region of `C` plants with price `1 * 4 = 4`.
    - A region of `E` plants with price `13 * 8 = 104`.
    - A region of `I` plants with price `14 * 16 = 224`.
    - A region of `M` plants with price `5 * 6 = 30`.
    - A region of `S` plants with price `3 * 6 = 18`.

Adding these together produces its new total price of `**1206**`.

**What is the new total price of fencing all regions on your map?**
