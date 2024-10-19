# Greedy

## Conclusion

Many greedy problems start with sorting by one attribute(like start time etc.,) then pick elements that contributes to the result more greedily. 



## Problems

In [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/), we will have and `end`,  `furthest`, and `jumps`:

- **Furthest** : The furthest index the **unfinished** jump can reach.
- **End** : The index that the **last finished** jump reached.
  - When i < end, it's all possible range that last jump covered.

For example, in `[3,2,1,1,4]`, we made a jump at the index 0, now 1st, 2nd, and 3rd can all be our next possible jump start point `[0,3]`.





[134. Gas Station](https://leetcode.com/problems/gas-station/)

