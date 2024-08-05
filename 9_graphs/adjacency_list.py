from typing import List

grid = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'V', 'K', 'L'],
    ['W', 'N', 'O', 'S']
]

composition_graph = {
    'C': ['G', 'Am', 'F'],
    'G': ['C', 'Em', 'D'],
    'Am': ['F', 'G'],
    'F': ['C', 'Dm'],
}

def bfs(adj_list: dict):
    for node in adj_list.keys():
        neighbors = ', '.join(adj_list[node])
        print(f"{node} [{neighbors}]")
    return

# bfs(adjacency_list)