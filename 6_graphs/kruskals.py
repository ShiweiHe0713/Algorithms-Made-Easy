def kruskals(G, W):
    sorted_w = sorted(W) # O(nlogn)
    S = {}

    for w in sorted_w: # Θ(n)
        if w not in S and S.append(w, inplace=False).acyclic():
            if S.size() > G.V - 1: 
                break
            S.append(w)
    return T(V,S)

