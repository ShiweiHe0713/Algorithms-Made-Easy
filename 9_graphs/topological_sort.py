from typing import List, Dict

# Has to be directed graph to use topological sort
# How to use topological sort to sort nodes?
# How to use topological sort to detect edges?

def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    def dfs(cur_node: int, stack: List[List[int]], visisted):
        """we will append to stack in each dfs call"""
        if cur_node in visited:
            return
        visited.add(cur_node)

        for neighbor in graph[cur_node]:
            if cur_node not in visited:
                dfs(neighbor, stack, visisted)

        visited.remove(cur_node)
        stack.append(cur_node)

    stack = []
    visited = set()

    # node is an integer here
    for node in graph:
        if node not in visited:
            dfs(node, stack, visited)

    return stack

graph = {
    0: [1, 2],    # Edges from node 0
    1: [3],       # Edges from node 1
    2: [3],       # Edges from node 2
    3: [4],       # Edges from node 3
    4: []         # Node 4 has no outgoing edges
}

sorted_graph = topological_sort(graph)
print(sorted_graph)
