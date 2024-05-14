def connecting(U, V_U):
    # 1. w_i must not create cycles
    # 2. w_i connecting these two components
    # 3. w_i is the smallest
    return U

def prims(G):
    """prims"""
    # 1. Arbitrarily pick a node from G
    S = G.V[0][0]
    n = G.V.value()
    U = set()
    U.add(S)

    for i in range(1, n):
        # find the smallest weight connecting U and V-U
        w_i = connecting(U, G.V-U)
        U.add(w_i)
    return T(G.V,U)
