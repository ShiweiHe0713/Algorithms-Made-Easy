# Dynammic Programming

**Table of content**
- [Dynammic Programming](#dynammic-programming)
  - [错误总结](#错误总结)
  - [DP问题的一些特征](#dp问题的一些特征)
    - [Some questions to ask](#some-questions-to-ask)
  - [Typical Problems](#typical-problems)

## 错误总结
Budget equals to 0 situation
- m row, n cols issue, in python list comprehension, n comes before m

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

[139 Word Break](./139_word_break.py)
|    |    |    |    |    |    |    |    |    |    |
|----|----|----|----|----|----|----|----|----|----|
| i  |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |
| s  | **l** |  e |  e |  t | **c** |  o |  d |  e | base |
| dp | **True** | False | False | False | **True** | False | False | False | **True** |

**The current dp(i) or dp[i] only is true iff the current word matches and the previous word matches(which depends on its previous word recursively.)**

### Some questions to ask

1. **How should I size the DP array?**
2. **How should I initialize the DP array?**

## Typical Problems

| Category                      | Problems                               | LeetCode Link                                               |
|-------------------------------|----------------------------------------|-------------------------------------------------------------|
| **Fibonacci**                  | Climbing Stairs                        | [LeetCode](https://leetcode.com/problems/climbing-stairs)    |
|                               | House Robber                           | [LeetCode](https://leetcode.com/problems/house-robber)       |
|                               | Fibonacci Number                       | [LeetCode](https://leetcode.com/problems/fibonacci-number)   |
|                               | Maximum Alternation                    | N/A                                                         |
| **0-1 Knapsack**               | Partition Equal Subset Sum             | [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum) |
|                               | Target Sum                             | [LeetCode](https://leetcode.com/problems/target-sum)         |
| **Unbounded Knapsack**         | Coin Change                            | [LeetCode](https://leetcode.com/problems/coin-change)        |
|                               | Coin Change II                         | [LeetCode](https://leetcode.com/problems/coin-change-2)      |
|                               | Minimum Cost For Tickets               | [LeetCode](https://leetcode.com/problems/minimum-cost-for-tickets) |
| **Longest Common Subsequence** | Longest Common Subsequence             | [LeetCode](https://leetcode.com/problems/longest-common-subsequence) |
|                               | Longest Increasing Subsequence         | [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence) |
|                               | Edit Distance                          | [LeetCode](https://leetcode.com/problems/edit-distance)      |
|                               | Distinct Subsequence                   | [LeetCode](https://leetcode.com/problems/distinct-subsequences) |
| **Palindrome**                 | Longest Palindromic Substring          | [LeetCode](https://leetcode.com/problems/longest-palindromic-substring) |
|                               | Palindromic Substrings                 | [LeetCode](https://leetcode.com/problems/palindromic-substrings) |
|                               | Longest Palindromic Subsequence        | [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence) |



动态规划（Dynamic Programming）
    基础知识：这里指的是用for循环方式的动态规划，非Memoization Search方式。DP可以在多项式时间复杂度内解决DFS需要指数级别的问题。常见的题目包括找最大最小，找可行性，找总方案数等，一般结果是一个Integer或者Boolean。动态规划有很多分支，暂时还没想好怎么去写这部分，后面想好了再具体写吧。
   常见题目：
        Leetcode 674 Longest Continuous Increasing Subsequence (接龙型dp)
        Leetcode 62 Unique Paths II
        Leetcode 70 Climbing Stairs
        Leetcode 64 Minimum Path Sum
        Leetcode 368 Largest Divisible Subset (接龙型dp)
        Leetcode 300 Longest Increasing Subsequence (接龙型dp)
        Leetcode 354 Russian Doll Envelopes (接龙型dp， 300的2D版)
        Leetcode 256 Paint House
        Leetcode 121 Best Time to Buy and Sell Stock
        Leetcode 55 Jump Game
        Leetcode 45 Jump Game II
        Leetcode 132 Palindrome Partitioning II
        Leetcode 312 Burst Balloons (区间型dp)
        Leetcode 1143 Longest Common Subsequence (前缀型dp)
        Leetcode 1062 Longest Repeating Substring (dp方法与longest common substring一致)
        Leetcode 718 Maximum Length of Repeated Subarray (和1062本质上一样)
        Leetcode 174 Dungeon Game
        Leetcode 115 Distinct Subsequences
        Leetcode 72 Edit Distance
        Leetcode 91 Decode Ways
        Leetcode 639 Decode Ways II
        Leetcode 712 Minimum ASCII Delete Sum for Two Strings
        Leetcode 221 Maximal Square
        Leetcode 1277 Count Square Submatrices with All Ones (可以使用221一样的解法)
        Leetcode 198 House Robber
        Leetcode 213 House Robber II
        Leetcode 740 Delete and Earn
        Leetcode 87 Scramble String
        Leetcode 1140 Stone Game II
        Leetcode 322 Coin Change
        Leetcode 518 Coin Change II (01背包型)
        Leetcode 1048 Longest String Chain
        Leetcode 44 Wildcard Matching
        Leetcode 10 Regular Expression Matching
        Leetcode 32 Longest Valid Parentheses
        Leetcode 1235 Maximum Profit in Job Scheduling (DP + binary search)
        Leetcode 1043 Partition Array for Maximum Sum
        Leetcode 926 Flip String to Monotone Increasing
