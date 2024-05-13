from queue import Queue

def bfs(G, S) -> None:
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
