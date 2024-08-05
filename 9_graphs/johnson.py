# Sketchy versio
from dijkstra import dijkstra
from bellman_ford import bellman_ford

def johnson(graph):
    graph = bellman_ford(graph)
    W_prime = shift(W)
    n = len(graph.vertices)
    for i in range(1,n):
        for j in range(1,n):
            dijkstra(i,j)
    return 