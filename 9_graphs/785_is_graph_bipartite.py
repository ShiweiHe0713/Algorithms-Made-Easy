from typing import List
from collections import deque

class Solution:
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