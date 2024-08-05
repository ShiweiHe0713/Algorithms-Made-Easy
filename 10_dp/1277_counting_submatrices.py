from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m+1)]
        ans = 0

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = matrix[r][c]
                elif matrix[r][c] == 0:
                    dp[r][c] = 0
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                ans += dp[r][c]
        
        return ans

