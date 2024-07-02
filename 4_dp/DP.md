# Dynammic Programming

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