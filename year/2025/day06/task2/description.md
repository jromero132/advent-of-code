# --- Part Two ---

The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written **right-to-left in columns**. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:
```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

Reading the problems right-to-left one column at a time, the problems are now quite different:
    - The rightmost problem is `4` + `431` + `623` = `**1058**`
    - The second problem from the right is `175` * `581` * `32` = `**3253600**`
    - The third problem from the right is `8` + `248` + `369` = `**625**`
    - Finally, the leftmost problem is `356` * `24` * `1` = `**8544**`

Now, the grand total is `1058` + `3253600` + `625` + `8544` = `**3263827**`.

Solve the problems on the math worksheet again. **What is the grand total found by adding together all of the answers to the individual problems?**
