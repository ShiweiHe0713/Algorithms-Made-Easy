from typing import List
from collections import deque

class Solution:
    def solve_dfs(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'E'
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + x, j + y)
        
        boarder_cells = []
        m = len(board)
        n = len(board[0])

        for r in [0, m-1]:
            for c in range(n):
                if board[r][c] == "O":
                    boarder_cells.append((r,c))
        
        for c in [0, n-1]:
            for r in range(1, m-1):
                if board[r][c] == "O":
                    boarder_cells.append((r,c))

        # mark all the boarder related cells to 'E'
        print(len(boarder_cells))
        for i, j in boarder_cells:
            dfs(i, j)

        # traverse the graph and revert
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'

    def solve_bfs(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        def bfs(i: int, j: int) -> None:
            queue = deque([(i, j)])
            while queue:
                r, c = queue.popleft()
                board[r][c] = 'E'
                
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + r, y + c
                    # write it postive way to avoid redundant memory usage
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        board[nx][ny] = 'E'  # Mark as visited immediately
                        queue.append((nx, ny))
                
        m = len(board)
        n = len(board[0])

        for r in [0, m-1]:
            for c in range(n):
                if board[r][c] == "O":
                    bfs(r, c)
        
        for c in [0, n-1]:
            for r in range(1, m-1):
                if board[r][c] == "O":
                    bfs(r, c)

        # traverse the graph and revert
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'

