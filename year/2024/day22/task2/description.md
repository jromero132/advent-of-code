# --- Part Two ---

Of course, the secret numbers aren't the prices each buyer is offering! That would be ridiculous[^1]. Instead, the **prices** the buyer offers are just the **ones digit** of each of their secret numbers.

So, if a buyer starts with a secret number of `123`, that buyer's first ten **prices** would be:
```
3 (from 123)
0 (from 15887950)
6 (from 16495136)
5 (etc.)
4
4
6
4
4
2
```

This price is the number of **bananas** that buyer is offering in exchange for your information about a new hiding spot. However, you still don't speak [monkey](/2022/day/21), so you can't negotiate with the buyers directly. The Historian speaks a little, but not enough to negotiate; instead, he can ask another monkey to negotiate on your behalf.

Unfortunately, the monkey only knows how to decide when to sell by looking at the **changes** in price. Specifically, the monkey will only look for a specific sequence of **four consecutive changes** in price, then immediately sell when it sees that sequence.

So, if a buyer starts with a secret number of `123`, that buyer's first ten secret numbers, prices, and the associated changes would be:
```
     123: 3
15887950: 0 (-3)
16495136: 6 (6)
  527345: 5 (-1)
  704524: 4 (-1)
 1553684: 4 (0)
12683156: 6 (2)
11100544: 4 (-2)
12249484: 4 (0)
 7753432: 2 (-2)
```

Note that the first price has no associated change because there was no previous price to compare it with.

In this short example, within just these first few prices, the highest price will be `6`, so it would be nice to give the monkey instructions that would make it sell at that time. The first `6` occurs after only two changes, so there's no way to instruct the monkey to sell then, but the second `6` occurs after the changes `-1,-1,0,2`. So, if you gave the monkey that sequence of changes, it would wait until the first time it sees that sequence and then immediately sell your hiding spot information at the current price, winning you `6` bananas.

Each buyer only wants to buy one hiding spot, so after the hiding spot is sold, the monkey will move on to the next buyer. If the monkey **never** hears that sequence of price changes from a buyer, the monkey will never sell, and will instead just move on to the next buyer.

Worse, you can only give the monkey **a single sequence** of four price changes to look for. You can't change the sequence between buyers.

You're going to need as many bananas as possible, so you'll need to **determine which sequence** of four price changes will cause the monkey to get you the **most bananas overall**. Each buyer is going to generate `2000` secret numbers after their initial secret number, so, for each buyer, you'll have **`2000` price changes** in which your sequence can occur.

Suppose the initial secret number of each buyer is:
```
1
2
3
2024
```

There are many sequences of four price changes you could tell the monkey, but for these four buyers, the sequence that will get you the most bananas is `-2,1,-1,3`. Using that sequence, the monkey will make the following sales:
    - For the buyer with an initial secret number of `1`, changes `-2,1,-1,3` first occur when the price is `**7**`.
    - For the buyer with initial secret `2`, changes `-2,1,-1,3` first occur when the price is `**7**`.
    - For the buyer with initial secret `3`, the change sequence `-2,1,-1,3` **does not occur** in the first 2000 changes.
    - For the buyer starting with `2024`, changes `-2,1,-1,3` first occur when the price is `**9**`.

So, by asking the monkey to sell the first time each buyer's prices go down `2`, then up `1`, then down `1`, then up `3`, you would get `**23**` (`7 + 7 + 9`) bananas!

Figure out the best sequence to tell the monkey so that by looking for that same sequence of changes in every buyer's future prices, you get the most bananas in total. **What is the most bananas you can get?**

[^1]: [ridiculous] Some might say it would be... bananas.
