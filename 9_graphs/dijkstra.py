from queue import PriorityQueue

INFINITE = 10000000000

def extract_min(S):
    PQ = PriorityQueue(min)
    return PQ.get()

def dijkstra(G, s, W):
    """
    O((m+n)logn)
    """
    S = set()
    s.d = 0
    s.parent = None
    for v in G.V:
        if v != s:
            v.d = INFINITE
            v.parent = None
    
    while len(S) <= G.V.value():
        u = extract_min(G.V - S)
        S.add(u)
        for v in u.adj_list():
            v.d = min(v.d, u.d + W(u,v))
            v.parent = u
    return 
        