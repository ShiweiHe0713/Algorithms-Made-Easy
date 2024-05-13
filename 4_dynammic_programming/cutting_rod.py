prompt = """
    Given a rod of length n, and current prices of rods 
    of different lengths, find a way to cut the rod to 
    maximize the profit of selling the cut pieces.
"""

ROD_LENGTH = 8
rod = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20,}

recursive_relation = """
    F(n) = max_\{ 1<=i<=n \} (rod[i] + F(n-i))
"""

def cutting_rod_bf(n):
    if n == 0: return 0
    # Find the opt(n) = max_{1~n}(rod[i]+opt(n-i))
    result = -1
    for i in range(1,n+1):
        cur_val = rod[i] + cutting_rod_bf(n-i)
        if cur_val > result:
            result = cur_val
    return result

def cutting_rod_tab(n):
    if n == 0: return 0
    table = [None] * (n+1)
    table[0] = 0
    result = -1

    for i in range(1, n+1):
        for j in range(1, i+1):
            cur_val = rod[j] + table[i-j]
            if cur_val > result:
                result = cur_val
        table[i] = result

    return table[n]

def cutting_rod_memo(n, memo):
    if n == 0: return 0
    if n in memo:
        return memo[n]
    
    result = -1
    cur_val = -1
    
    if memo is None:
        memo = {}
    memo[0] = 0

    for i in range(1, n+1):
        cur_val = rod[i] + cutting_rod_memo(n - i, memo)
        if cur_val > result:
            result = cur_val
    
    memo[n] = result
    return result

dp = {}

print(cutting_rod_bf(ROD_LENGTH))
print(cutting_rod_tab(ROD_LENGTH))
print(cutting_rod_memo(ROD_LENGTH, dp))