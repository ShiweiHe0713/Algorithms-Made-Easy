def bellman_ford(G, s):
    # 1. Initialization
    s.d = 0
    for v in G:
        v.d = float('inf')
    
    # 2. Relaxing the edges
    n = len(G.v)
    for i in range(1, n):
        for (u,v) in G:
            v.d = min(v.d, u.d + w(u,v))
    
    # 3. Detect the negative cycles
    for v in G:
        if v.d < u.d + w(u,v):
            raise ValueError("Negative cycles detected!")
        
    return 

def bellman_ford_modified(graph, source):
    # Step 1: Initialize distances from source to all other vertices as INFINITE
    distance = {v: float('inf') for v in graph}
    distance[source] = 0
    
    # Step 2: Relax all edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Step 3: Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distance
