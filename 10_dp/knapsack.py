from typing import List

def knapsack_01(capacity: int, weights: List[int], values: List[int]) -> int:
    # i is the ID of an element, j is the a current capacity
    # dp[i][j]: The larget value we get from using the first i elements with a capacity of j
    # i == len(weights), j == capacity, return dp[len(weights)][capacity] aka dp[-1][-1]
    # recurrence relationship:
    # dp[i][j] = max(dp[i-1][j-weights[i]] + values[i], dp[i-1][capacity])
    m, n = len(weights), capacity
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m):
        for j in range(1, n):
            if weights[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
    
    return dp[-1][-1]