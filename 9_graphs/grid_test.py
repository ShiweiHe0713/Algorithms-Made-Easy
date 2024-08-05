from typing import List

class Grid:
    count = 0
    visit = set()

    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if (i, j) in self.visit:
            return
        self.visit.add((i,j))
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == 1:
            self.count += 1
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
grid = [
    [1,0,1,0,1,1],
    [0,1,1,1,0,0],
    [1,1,1,0,0,0],
    [0,1,1,0,0,0]
]

g = Grid()
g.dfs(grid, 0, 0)
print(g.count)
