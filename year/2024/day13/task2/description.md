# --- Part Two ---

As you go to win the first prize, you discover that the claw is nowhere near where you expected it would be. Due to a unit conversion error in your measurements, the position of every prize is actually `10000000000000` higher on both the `X` and `Y` axis!

Add `10000000000000` to the `X` and `Y` position of every prize. After making this change, the example above would now look like this:
```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279
```

Now, it is only possible to win a prize on the second and fourth claw machines. Unfortunately, it will take **many more than `100` presses** to do so.

Using the corrected prize coordinates, figure out how to win as many prizes as possible. **What is the fewest tokens you would have to spend to win all possible prizes?**
