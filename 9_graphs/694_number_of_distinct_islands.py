from typing import List, Set

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def transform_island(island: List[List[int]]) -> List[List[int]]:
            x, y = island[0]

            for co_ord in island:
                co_ord[0] -= x
                co_ord[1] -= y
                    
            return str(sorted(island))

        def dfs(i: int, j: int, cur_island: List[int]) -> List[List[int]]:
            if 0 <= i < m and 0 <= j < n and (i, j) not in visited and grid[i][j] == 1:
                cur_island.append([i, j])
                visited.add((i, j))

                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = i + x, j + y
                    dfs(nx, ny, cur_island)

                return cur_island[:]
        
        islands = set()
        visited = set()
        m, n = len(grid), len(grid[0])
        islands = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island = dfs(i, j, [])
                    islands.append(island)

        result = set()
        # count the number of distinct islands
        for island in islands:
            result.add(transform_island(island))
        
        return len(result)

s = Solution()
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
num = s.numDistinctIslands(grid)
print(num)