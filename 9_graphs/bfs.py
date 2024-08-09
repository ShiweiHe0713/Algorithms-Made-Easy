from typing import List
from collections import deque, defaultdict
from queue import Queue

def bfs_pseudo(G, S) -> None:
    """
    G(V,E), S is the source node
    bfs runtime: O(m+n)
    """
    for node in G:
        if node == S:
            continue
        node.d = -1
    S.d = 0
    S.parent = None
    Q = Queue()
    Q.put(S)

    while Q is not None:
        v = Q.get()
        for node in v.adj_list:
            if node.d == -1:
                node.d = v.d + 1
                node.parent = v
                Q.put(v)
    return 

def bfs_grid(grid: List[List[int]], r: int, c: int) -> None:
    if not grid:
        return 
    visited = set()
    queue = deque()
    queue.append((r,c))
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    grid[r][c] = 0

    while queue:
        # enqueue all grid[r][c]'s neighbors
        i, j = queue.popleft()
        visited.add((i, j))

        for x, y in direction:
            new_x, new_y = i + x, j + y
            if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or (new_x, new_y) in visited:
                continue
            grid[new_x][new_y] = grid[i][j] + 1
            queue.append((new_x, new_y))

    print(grid)

grid = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'V', 'K', 'L'],
    ['W', 'N', 'O', 'S']
]

graph = [
    [1,2,3,4],
    [4,2,14,6],
    [12,34,1,4]
]


bfs_grid(graph, 0, 0)
