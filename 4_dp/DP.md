# Dynammic Programming

## DP问题的一些特征

- Current decision will have impact on the future



[746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/)
Reverse order DP:
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
```
Natural ordered DP:
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            if i == len(cost):
                cost[i] = min(cost[i], cost[i-1])
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[len(cost)-2])
```

[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
[198. House Robber](https://leetcode.com/problems/house-robber/description/)
**All used two integer variable instead of creating a DP array**

[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)
My first attempt was only using one for loop, but it turned out two for loops are required. 



[1770. Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/)

The hardest part for me is to understand the meaning of dp function or array very clearly, the direction(forward or backward), the index.

> **State variable `i` and dp(i) means very different things, we need to distinguish them**

For example, in 1770, one of the state variables `i` means how many multupliers used so far, also suggest the index of the current multiplier to be used. On the other hand, `dp(i)` means the max score we can get by using the **first** `i` multipliers(It doesn't matter i is counting from left or right.)

nums = [<u>-1,2</u>,-5,7,3,-8,1]
multipliers = [<u>3,-5,2</u>,-9]

**Like underscored range, i == 2, left = 1, dp(2, 1) = (-5) * (-9) + dp(3, 2).**



### Some questions to ask

1. **How should I size the DP array?**
2. **How should I initialize the DP array?**