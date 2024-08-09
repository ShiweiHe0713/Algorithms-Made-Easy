from typing import List
from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def bfs(source: int, destination: int) -> bool:
            if source == destination:
                return True
            
            visited = set()
            queue = deque()
            queue.append(source)
            
            while queue:
                u = queue.popleft()
                visited.add(u)
                    
                for neighbor in graph[u]:
                    if neighbor not in visited:
                        if neighbor == destination:
                            return True
                        queue.append(neighbor)
                        visited.add(neighbor) # don't forget adding here
                
            return False
            
        # construct adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        return bfs(source, destination)