from typing import List
from collections import deque

class Solution:

    def isBipartite_color(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        if n == 1:
            return True
        
        color = {}
        
        # for loop to include multiple connected components
        for i in range(n):
            if i not in color:
                queue = deque([i])
                color[i] = 1

                while queue:
                    cur = queue.popleft()
                    for i in range(len(graph[cur])):
                        ele = graph[cur][i]
                        if ele in color and color[ele] == color[cur]:
                            return False
                        
                        if ele not in color:
                            if color[cur] == 1:
                                color[ele] = 0
                            else:
                                color[ele] = 1
                            queue.append(ele)

        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        if n == 1:
            return True
        set_a = set()
        set_b = set()
        queue = deque()
        visited = set()

        # for loop to include multiple connected components
        for i in range(n):
            # start a new bfs for every component
            if i not in visited:
                queue.append(i)
                set_a.add(i)

                while queue:
                    cur = queue.popleft()
                    visited.add(cur)
                    for i in range(len(graph[cur])):
                        ele = graph[cur][i]
                        if ele not in visited:
                            if cur in set_a:
                                set_b.add(ele)
                            else:
                                set_a.add(ele)
                            queue.append(ele)
        
        return not (set_a & set_b)
    