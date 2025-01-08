# --- Part Two ---

After inspecting the monitoring device more closely, you determine that the system you're simulating is trying to **add two binary numbers**.

Specifically, it is treating the bits on wires starting with `x` as one binary number, treating the bits on wires starting with `y` as a second binary number, and then attempting to add those two numbers together. The output of this operation is produced as a binary number on the wires starting with `z`. (In all three cases, wire `00` is the least significant bit, then `01`, then `02`, and so on.)

The initial values for the wires in your puzzle input represent **just one instance** of a pair of numbers that sum to the wrong value. Ultimately, **any** two binary numbers provided as input should be handled correctly. That is, for any combination of bits on wires starting with `x` and wires starting with `y`, the sum of the two numbers those bits represent should be produced as a binary number on the wires starting with `z`.

For example, if you have an addition system with four `x` wires, four `y` wires, and five `z` wires, you should be able to supply any four-bit number on the `x` wires, any four-bit number on the `y` numbers, and eventually find the sum of those two numbers as a five-bit number on the `z` wires. One of the many ways you could provide numbers to such a system would be to pass `11` on the `x` wires (`1011` in binary) and `13` on the `y` wires (`1101` in binary):
```
x00: 1
x01: 1
x02: 0
x03: 1
y00: 1
y01: 0
y02: 1
y03: 1
```

If the system were working correctly, then after all gates are finished processing, you should find `24` (`11+13`) on the `z` wires as the five-bit binary number `11000`:
```
z00: 0
z01: 0
z02: 0
z03: 1
z04: 1
```

Unfortunately, your actual system needs to add numbers with many more bits and therefore has many more wires.

Based on forensic analysis[^1] of scuff marks and scratches on the device, you can tell that there are exactly **four** pairs of gates whose output wires have been **swapped**. (A gate can only be in at most one such pair; no gate's output was swapped multiple times.)

For example, the system below is supposed to find the bitwise `AND` of the six-bit number on `x00` through `x05` and the six-bit number on `y00` through `y05` and then write the result as a six-bit number on `z00` through `z05`:
```
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
```

However, in this example, two pairs of gates have had their output wires swapped, causing the system to produce wrong answers. The first pair of gates with swapped outputs is `x00 AND y00 -> z05` and `x05 AND y05 -> z00`; the second pair of gates is `x01 AND y01 -> z02` and `x02 AND y02 -> z01`. Correcting these two swaps results in this system that works as intended for any set of initial values on wires that start with `x` or `y`:
```
x00 AND y00 -> z00
x01 AND y01 -> z01
x02 AND y02 -> z02
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z05
```

In this example, two pairs of gates have outputs that are involved in a swap. By sorting their output wires' names and joining them with commas, the list of wires involved in swaps is `**z00,z01,z02,z05**`.

Of course, your actual system is much more complex than this, and the gates that need their outputs swapped could be **anywhere**, not just attached to a wire starting with `z`. If you were to determine that you need to swap output wires `aaa` with `eee`, `ooo` with `z99`, `bbb` with `ccc`, and `aoc` with `z24`, your answer would be `**aaa,aoc,bbb,ccc,eee,ooo,z24,z99**`.

Your system of gates and wires has **four** pairs of gates which need their output wires swapped - **eight** wires in total. Determine which four pairs of gates need their outputs swapped so that your system correctly performs addition; **what do you get if you sort the names of the eight wires involved in a swap and then join those names with commas?**

[^1]: [forensic analysis] ENHANCE
