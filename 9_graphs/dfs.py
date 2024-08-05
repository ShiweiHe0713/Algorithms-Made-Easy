def dfs_visit(v, time):
    """DFS recursive body"""
    time += 1
    v.start = time
    v.color = "grey"
    
    # Visit child
    for node in v.adj_list:
        if node.color == "white":
            node.parent = v
            dfs_visit(node, time)
    
    v.color = "black"
    time += 1
    v.finish = time
    return time

def dfs(G):
    """DFS driver"""
    for node in G:
        node.color = "white"
    
    time = 0
    for node in G:
        if node.color == "white":
            time = dfs_visit(G.s, time)
    return
