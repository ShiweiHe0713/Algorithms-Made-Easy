from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(start: List[int], destination: List[int]) -> bool:
            i, j = start[0], start[1]
            if visited[i][j]:
                return False
            if i == destination[0] and j == destination[1]:
                return True
            visited[i][j] = True
            
            direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for x, y in direct:
                nx, ny = i, j
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    # all the way to the dead-end to four directions
                    nx += x
                    ny += y
                # then dfs on that cell
                if dfs([nx-x, ny-y], destination): # Que: revert one step to valid range
                    return True
            return False

        m = len(maze)
        n = len(maze[0])
        visited = [[False] * n for _ in range(m)]
        return dfs(start, destination)
            
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
des = [4,4]

s = Solution()
s.hasPath(maze, start, des)