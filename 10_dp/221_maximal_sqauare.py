from typing import List

class Solution:
    def maximalSquare_bf(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_side = 0
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    edge = 1
                    flag = True
                    while r + edge < m and c + edge < n and flag:
                        for k in range(c, c + edge + 1):
                            if matrix[r + edge][k] == '0':
                                flag = False
                                break
                        for k in range(r, r + edge + 1):
                            if matrix[k][c + edge] == '0':
                                flag = False
                                break
                        if flag:
                            edge += 1
                    max_side = max(edge, max_side)
        
        return max_side * max_side

    def maximalSquare_tab(self, matrix: List[List[str]]) -> int:
        # DP
        m = len(matrix)
        n = len(matrix[0])
        max_side = 0
        dp = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = int(matrix[r][c])
                elif matrix[r][c] == '0':
                    dp[r][c] = 0
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                
                max_side = max(dp[r][c], max_side)
        
        return max_side * max_side
    
test1 = [["0"]]
test2 = [["0","1"],["1","0"]]
test3 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
test4 = [["1","1","1","0","0"],["1","1","1","1","1"],["1","1","1","0","1"],["1","0","0","1","0"]]

sol = Solution()
result = sol.maximalSquare_bf(test4)
result2 = sol.maximalSquare_tab(test4)
print(result2)
