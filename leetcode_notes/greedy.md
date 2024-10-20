# Greedy

## Conclusion

Many greedy problems start with sorting by one attribute(like start time etc.,) then pick elements that contributes to the result more greedily. 



## Problems

#### [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)

we will have and `end`,  `furthest`, and `jumps`:

- **Furthest** : The furthest index the **unfinished** jump can reach.
- **End** : The index that the **last finished** jump reached.
  - When i < end, it's all possible range that last jump covered.

For example, in `[3,2,1,1,4]`, we made a jump at the index 0, now 1st, 2nd, and 3rd can all be our next possible jump start point `[0,3]`.



#### [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

Can either sort by start or end time



#### [134. Gas Station](https://leetcode.com/problems/gas-station/)

In this problem, we keep track of the cur_sum of gas[i] - cost[i], if cur_sum drop below 0, we reset to 0 and update result to i + 1. The reason why we're doing this is to always trying to find the first positive after the **cur_sum become positve.** So if we encounter a postive number but adding the diff doesn't make the cur_sum postive, it's still not valid so we have to keep going.



#### [135. Candy](https://leetcode.com/problems/candy/)

