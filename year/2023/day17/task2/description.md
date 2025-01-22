# --- Part Two ---

The crucibles of lava simply aren't large enough to provide an adequate supply of lava to the machine parts factory. Instead, the Elves are going to upgrade to **ultra crucibles**.

Ultra crucibles are even more difficult to steer than normal crucibles. Not only do they have trouble going in a straight line, but they also have trouble turning!

Once an ultra crucible starts moving in a direction, it needs to move **a minimum of four blocks** in that direction before it can turn (or even before it can stop at the end). However, it will eventually start to get wobbly: an ultra crucible can move a maximum of **ten consecutive blocks** without turning.

In the above example, an ultra crucible could follow this path to minimize heat loss:
```
2**>****>****>****>****>****>****>****>**1323
32154535**v**5623
32552456**v**4254
34465858**v**5452
45466578**v****>****>****>****>**
143859879845**v**
445787698776**v**
363787797965**v**
465496798688**v**
456467998645**v**
122468686556**v**
254654888773**v**
432267465553**v**
```

In the above example, an ultra crucible would incur the minimum possible heat loss of `**94**`.

Here's another example:
```
111111111111
999999999991
999999999991
999999999991
999999999991
```

Sadly, an ultra crucible would need to take an unfortunate path like this one:
```
1**>****>****>****>****>****>****>**1111
9999999**v**9991
9999999**v**9991
9999999**v**9991
9999999**v****>****>****>****>**
```

This route causes the ultra crucible to incur the minimum possible heat loss of `**71**`.

Directing the **ultra crucible** from the lava pool to the machine parts factory, **what is the least heat loss it can incur?**
