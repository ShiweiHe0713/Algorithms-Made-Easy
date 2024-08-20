from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # if the island connected to the boarder cell, mark the closed as False
        def dfs(i: int, j: int) -> bool:
            # reaching the boundary, threatening the flag
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            # Return true if the cell is water or visited land(not threatening to closed flag)
            if grid[i][j] in (1, 2):
                return True
            grid[i][j] = 2

            closed = True
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + x, j + y
                if not dfs(nx, ny):
                    closed = False
            
            return closed
        
        # increment count iff grid is land and dfs(grid) is True
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1
        
        return count