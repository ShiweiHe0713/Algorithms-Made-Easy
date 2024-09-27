from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid: List[List[int]], i: int, j: int) -> int:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in visit:
                return 0

            visit.add((i,j))

            bottom = dfs(grid, i+1, j)
            top = dfs(grid, i-1, j)
            right = dfs(grid, i, j+1)
            left = dfs(grid, i, j-1)

            visit.remove((i,j))
            cur_max = max(bottom, top, right, left) + grid[i][j]
            return cur_max
        	
        m = len(grid)
        n = len(grid[0])
        max_gold = 0
        visit = set()        
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    max_gold = max(max_gold, dfs(grid, r, c))
                    visit.clear()
        		
        return max_gold