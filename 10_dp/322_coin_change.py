from functools import lru_cache
from typing import List

class Solution:
    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        # i: the value of the coin, 
        # dp(i): smallest coins number to build `i`-valuing coin
        def dp(i: int) -> int:
            if i < 0:
                return -1
            if i == 0:
                return 0
            min_change = float('inf')
            for coin in coins:
                if i >= coin:
                    min_change = min(min_change, dp(i - coin) + 1)
            
            return min_change

        return dp(amount) if dp(amount) != float('inf') else -1
    
    def coinChange_tab(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
    
    def coinChange_bf(self, coins: List[int], amount: int) -> int:
        pass