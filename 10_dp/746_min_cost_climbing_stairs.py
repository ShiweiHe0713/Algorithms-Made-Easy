from typing import List
from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            step1 = cost[i-1] + dp[i-1]
            step2 = cost[i-2] + dp[i-2]
            dp[i] = min(step1, step2)
        
        return dp[-1]
    
    def minCostClimbingStairs_cache(self, cost: List[int]) -> int:
        @lru_cache(maxsize=128)
        def dp(i: int) -> int:
            if i in (0,1):
                return 0
            return min(dp(i-1)+cost[i-1], dp(i-2)+cost[i-2])

        return dp(len(cost))
    
    def minCostClimbingStairs_ksteps_memo(self, cost: List[int], k: int) -> int:
        """This time, we can take [1,k] steps each time, we can also start at 0 or 1"""
        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i in (0,1):
                return 0
            best = float('inf')
            upper_bound = min(i, k)
            for j in range(1, upper_bound + 1):
                best = min(best, dp(i-j)+cost[i-j])
            return best
        
        return dp(len(cost))
    
    def minCostClimbingStairs_ksteps_tab(self, cost, k):
        n = len(cost)
        dp = [0] * (n+1)

        # Have to start from 2 not 1 or 0
        for i in range(2, n+1):
            ceiling = min(i,k)
            best = float('inf')
            for j in range(1, ceiling + 1):
                best = min(best, dp[i-j] + cost[i-j])
            dp[i] = best

        return dp[-1]
    
cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,100,100,1,1,100,1,100,100,1]
cost3 = [1,100,1,1,1,100,1,1,100,1]
# i = 15, j = 15, i - k = 15- 5 = 10

s1 = Solution()
# print(s1.minCostClimbingStairs(cost2))
print(s1.minCostClimbingStairs_ksteps_memo(cost3, 2))
print(s1.minCostClimbingStairs_ksteps_tab(cost3, 2))
