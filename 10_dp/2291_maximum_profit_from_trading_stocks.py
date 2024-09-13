from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        m, n = len(present), budget
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            profit = future[i-1] - present[i-1]
            # j can be starting from 0
            for j in range(n+1):
                if present[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-present[i-1]] + profit)

        return dp[-1][-1]