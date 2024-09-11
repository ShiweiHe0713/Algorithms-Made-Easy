from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def dp() -> None:
            for i in range(1, n+1):
                for j in range(1, i+1):
                    if rating[i-1] > rating[j-1]:
                        dp[i] += 1
                        if dp[j] >= 1:
                            result += dp[j]

        result = 0
        n = len(rating)
        dp = [0 for _ in range(n+1)]
        dp()
        
        rating = rating[::-1]
        dp = [0 for _ in range(n+1)]
        dp()

        return result