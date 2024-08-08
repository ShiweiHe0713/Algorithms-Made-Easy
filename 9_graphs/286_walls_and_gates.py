from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        Constraints: 1 <= m, n <= 250
        room[i][j] is either -1, 0 or INF
        """
        def dfs(rooms, i, j, dis):
            nonlocal m, n, INF
            # return if visit out of boundary
            if i < 0 or i >= m or j < 0 or j >= n or (i,j) in visited:
                return INF
            visited.add((i,j))
            
            result = INF
            if rooms[i][j] == -1:
                result = INF
            elif rooms[i][j] == 0:
                result =  dis
            else:
                # whether visited or not
                b = dfs(rooms, i + 1, j, dis+1)
                u = dfs(rooms, i - 1, j, dis+1)
                l = dfs(rooms, i, j - 1, dis+1)
                r = dfs(rooms, i + 1, j - 1, dis+1)
                rooms[i][j] = min(b, u, l, r)
                result = rooms[i][j]
            visited.remove((i,j))
            return result
        
        INF = 2147483647
        m = len(rooms)
        n = len(rooms[0])

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == INF:
                    visited = set()
                    dfs(rooms, r, c, 0)

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output =  [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

s1 = Solution()
s1.wallsAndGates(rooms)
print(rooms)
