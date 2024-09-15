from typing import List

def knapsack_01(capacity: int, weights: List[int], values: List[int]) -> int:
    # i is the ID of an element, j is the a current capacity
    # dp[i][j]: The larget value we get from using the first i elements with a capacity of j
    # i == len(weights), j == capacity, return dp[len(weights)][capacity] aka dp[-1][-1]
    # recurrence relationship:
    # dp[i][j] = max(dp[i-1][j-weights[i]] + values[i], dp[i-1][capacity])
    m, n = len(weights), capacity
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(n+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j] - weights[i-1] + values[i-1])
    
    return dp[-1][-1]

def knapsack_01_1d(capacity: int, weights: List[int], values: List[int]) -> int:
    pass

def knapsack_complete(capacity: int, weights: List[int], values: List[int]) -> int:
    # i is the ID of an element, j is the a current capacity
    # dp[i][j]: The larget value we get from using the first i elements with a capacity of j
    # i == len(weights), j == capacity, return dp[len(weights)][capacity] aka dp[-1][-1]
    # recurrence relationship:
    # dp[i][j] = max(dp[i-1][j-weights[i]] + values[i], dp[i-1][capacity])
    m, n = len(weights), capacity
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(n+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-weights[i-1]] + values[i-1])
    
    return dp[-1][-1]