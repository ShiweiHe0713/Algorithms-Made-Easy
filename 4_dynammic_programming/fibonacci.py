import sys

def fibonacci_bf(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci_bf(n - 1) + fibonacci_bf(n - 2)

def fibonacci_table(n):
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

def fibonacci_memo(n):
    memo = {}
    memo[0] = 0
    memo[1] = 1

    if n not in memo:
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    
    result = memo[n]
    return result

print(fibonacci_table(100))