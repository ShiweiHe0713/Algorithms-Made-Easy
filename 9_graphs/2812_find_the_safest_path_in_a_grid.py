from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # gather all thieves for bfs
        thieves = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append((i, j))
        
        level = 0
        visited = set()
        
        while thieves:
            i, j = thieves.popleft()
            flag = True
            visited.add((i, j))

            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = i + x, j + y
                # stop if reached start or end cell or visted
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) not in visited and (nx, ny) not in [(0,0), (m-1,n-1)]:
                    thieves.append((nx, ny))
                else:
                    flag = False
            
            if flag:
                level += 1

        return level

s = Solution()
grid = [[1,0,0],[0,0,0],[0,0,1]]
print(s.maximumSafenessFactor(grid))