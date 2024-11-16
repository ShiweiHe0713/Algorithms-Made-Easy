# Bit Manipulation

- If we were to add two strings together like "123" + "87", we will want to avoid converting to string and int back-and-forth, since the `str()` max take 4000 digits and it inefficient. We want to mimic doing addition by hand(digit plus digit and have carry-overs.)



1. **Use array instead of str to manip**
2. I forgot the i -=1 in the while loop(use for loop AMAP)
3. Forgot the **convert cur_val to str** before appending to result
   - **If want to do a `"".join(array)` at the end, make sure it's str in the array not int.**
4. Forgot the append **carry over** to result to handle two single digits



- Use 1 or -1 as a multiplier when dealing with postive or negatives



## Bitwise operation

| Operation Name     | Symbol | Python Operator |
| ------------------ | ------ | --------------- |
| AND                | `& `   | `&`             |
| OR                 | `|`    | `|`             |
| XOR (Exclusive OR) | `⊕`    | `^`             |
| NOT (Bitwise NOT)  | `~`    | `~`             |
| Left Shift         | `<<`   | `<<`            |
| Right Shift        | `>>`   | `>>`            |



### XOR (`^`)

**The XOR compare two bit and generate 1 or 0:**

- **1 if they're different**
  1 ^ 0 = 0 ^ 1 = 1
- **0 if they're the same**

​	1 ^ 1 = 0 ^ 0 = 0


**Which leads to:**

- x ^ 0 = x

- x ^ x = 0



**Carry and Borrow**

- Carry: y = (x&y) << 1
- Borrow: y = ((~x)&y) << 1



### Python Docs

**x << y**

Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

**x >> y**

Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.

**x & y**

Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

**x | y**

Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

**~ x**

Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.

**x ^ y**

Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

# Bit mask

| Operator    | Symbol | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| AND         | `&`    | Sets bits that are set in both operands.                     |
| OR          | `      | Inclusive Or, sets a bit to 1 if either input value is 1     |
| XOR         | `^`    | Sets bits that are different between the two operands.       |
| NOT         | `~`    | Inverts all the bits (1 becomes 0, and vice versa).          |
| Left Shift  | `<<`   | Shifts the bits to the left, filling the right with 0.       |
| Right Shift | `>>`   | Shifts the bits to the right, filling the left with 0 or sign bit for negative numbers. |
