from typing import List, Set, Tuple

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def transform_island(island: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            new_set = set()

            for co_ord in island:
                new_set.add((co_ord[0] - x, co_ord[1] - y))
                    
            return new_set

        def dfs(i: int, j: int, cur_island: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            if 0 <= i < m and 0 <= j < n and (i, j) not in visited and grid[i][j] == 1:
                cur_island.add((i, j))
                visited.add((i, j))

                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = i + x, j + y
                    dfs(nx, ny, cur_island)

                return cur_island
        
        visited = set()
        islands: Set[Tuple[int, int]] = set()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    new_set = set()
                    island = dfs(i, j, new_set)
                    if island:
                        x, y = i, j
                        islands.add(frozenset(transform_island(island)))

        return len(islands)
    
    
s = Solution()
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
num = s.numDistinctIslands(grid)
print(num)