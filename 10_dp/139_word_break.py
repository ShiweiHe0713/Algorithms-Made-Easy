from typing import List
from functools import cache

class Solution:
    def wordBreak_tab_in(self, s: str, wordDict: List[str]) -> bool:
        """Bottom-up, incremental"""
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = [True]

        for i in range(1, n+1):
            for word in wordDict:
                if i >= len(word) and s[i-len(word):i] == word:
                    dp[i] = dp[i - len(word)]
                if dp[i]:
                    break
        
        return dp[n]

    def wordBreak_tab_de(self, s: str, wordDict: List[str]) -> bool:
        """Bottom-up, decremental"""
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = [True]

        for i in range(n, -1, -1):
            for word in wordDict:
                if i + len(word) <= n and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word) - 1]
                if dp[i]:
                    break
        
        return dp[0]

    def wordBreak_memo(self, s: str, wordDict: List[str]) -> bool:
        """top-down"""
        @cache
        def dp(i: int) -> bool:
            # reach base case dp(n)
            if i >= len(s):
                return True
            
            for word in wordDict:
                # if word match and if the last word also matches 
                if i + len(word) <= n and s[i: i + len(word)] == word and dp(i + len(word)):
                        return True
                    
            return False

        n = len(s)
        return dp(0)
    