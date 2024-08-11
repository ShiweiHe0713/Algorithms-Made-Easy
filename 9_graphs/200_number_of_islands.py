from typing import List
from collections import defaultdict, deque

class Solution:
    def numberIslands(self, island: List[List[int]]) -> int:
        if not island:
            return 0
        
        def dfs(r: int, c: int):
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or island[r][c] == 0:
                return 
            visited.add((r, c))
            for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r+x, c+y)
            
        m = len(island)
        n = len(island[0])
        visited = set()
        count = 0

        for r in range(m):
            for c in range(n):
                if island[r][c] == 1 and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        print(count)
        return count 
    
graph = [
    [0,0,1,0],
    [0,1,1,1],
    [0,0,1,0],
    [1,1,1,0]
]
# output: 2
s1 = Solution()
s1.numberIslands(graph)
