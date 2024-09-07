from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = max(days)
        dp = [None] * (n+1)
        dp[0] = 0
        
        j = 0
        for i in range(1, n+1):
            if i < days[j]:
                dp[i] = dp[i-1]
            else:
                j += 1
                dp[i] = min(dp[i-1] + costs[0], 
                dp[max(i-7, 0)] + costs[1], 
                dp[max(i-30, 0)] + costs[2])
        
        return dp[-1]