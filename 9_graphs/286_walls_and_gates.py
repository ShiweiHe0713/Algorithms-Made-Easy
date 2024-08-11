from typing import List
from collections import deque

class Solution:
    def wallsAndGates_bf(self, rooms: List[List[int]]) -> None:
        """Do not return anything, modify rooms in-place instead."""
        def bfs(r: int, c: int) -> None:
            visited = set()
            queue = deque()
            queue.append((r,c))
            # rooms[r][c] = 0
            directions = [(-1,0), (1,0), (0, -1), (0, 1)]

            while queue:
                i, j = queue.popleft()
                visited.add((i,j))

                for x, y in directions:
                    new_x, new_y = i + x, j + y
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or (new_x, new_y) in visited or rooms[new_x][new_y] != pow(2,31) - 1:
                        continue
                    if rooms[new_x][new_y] > rooms[i][j] + 1:
                        rooms[new_x][new_y] = rooms[i][j] + 1
                    queue.append((new_x, new_y)) # DON'T EVER FORGET THIS ENQUEUE
        
        m = len(rooms)
        n = len(rooms[0])

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    bfs(r, c)

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """Do not return anything, modify rooms in-place instead."""
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]

        # Enqueue all the gates
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r,c))

        while queue:
            i, j = queue.popleft()
            visited.add((r,c))

            for x, y in directions:
                new_x, new_y = i + x, j + y
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or rooms[new_x][new_y] != 2147483647:
                    continue
                # if empty cell
                rooms[new_x][new_y] = rooms[i][j] + 1
                queue.append((new_x, new_y))

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output =  [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

s1 = Solution()
s1.wallsAndGates(rooms)

for room in rooms:
    print(room)
