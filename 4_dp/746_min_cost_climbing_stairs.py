from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # end on the last cell or the one after last cell
        n = len(cost)
        if n < 2:
            return 0
        
        dp = [0] * n  
        dp[0] = cost[0] # Initialization clined to 0 not cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n): # tend to overflow by setting the last index of dp to nums
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
        return dp[-1]
    
# cost =   [10,15,20]
#   dp = [0,10,15,30]
