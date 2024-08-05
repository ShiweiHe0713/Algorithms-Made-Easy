# Dynammic Programming

## DP问题的一些特征
1. Can be divided into subproblems
2. Have optimal substructures
3. Current decision will have impact on the future
   **- If current decision don't have future impact, it will be a greedy problem**


For [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/), let's change the condition to we can jump up to k steps each time. 
After adding this condition, we will have to consider in each dp(i) call, we have to find the minimum cost for [0,k] steps or [0,i] steps(if i < k). We simply add a for loop in a dp recursive call to calculate every dp value from i-1 to i - min(i,k), and update the min value, then return it.
```python
def minCostClimbingStairs_ksteps_tab(self, cost, k):
        n = len(cost)
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            upper_bound = min(i, k)
            minimum = float('inf')
            for j in range(1, upper_bound + 1):
                minimum = min(minimum, dp[i - j] + cost[i - j])
            dp[i] = minimum
        
        return dp[n]
```
**And remember clear that we start to fill dp array at 2, becase 0 and 1 is base case.**

[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
Skipped.

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