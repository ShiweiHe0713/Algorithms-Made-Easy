from typing import List, Dict

# Has to be directed graph to use topological sort
# How to use topological sort to sort nodes?
# How to use topological sort to detect edges?

def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    def dfs(cur_node: int, stack: List[int], visited):
        """we will append to stack in each dfs call"""
        if cur_node in visited:
            return
        visited.add(cur_node)

        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                dfs(neighbor, stack, visited)

        stack.append(cur_node)

    stack = []
    visited = set()

    # node is an integer here
    for node in graph:
        if node not in visited:
            dfs(node, stack, visited)

    return stack[::-1]

graph = {
    6: [],
    2: [4, 5],
    1: [2, 3],
    3: [6, 7],
    4: [],
    5: [],
    7: []
}

sorted_graph = topological_sort(graph)
print(sorted_graph)

# graph = {
#     0: [1, 2],    # Edges from node 0
#     1: [3],       # Edges from node 1
#     2: [3],       # Edges from node 2
#     3: [4],       # Edges from node 3
#     4: []         # Node 4 has no outgoing edges
# }