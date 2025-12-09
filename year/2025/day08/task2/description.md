# --- Part Two ---

The Elves were right; they **definitely** don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in **one large circuit**.

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at `216,146,977` and `117,168,530`. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (`216` and `117`) produces `**25272**`.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit[^1]. **What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?**

[^1]: [all in the same circuit] I strongly recommend making an interactive visualizer for this one; it reminds me a lot of maps from futuristic space games.
