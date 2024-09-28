class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount
        dp = [[0] * (m+1) for _ in range(amount+1)]
        
        for i in range(m+1):
            dp[0][i] = 1

        for cur_amount in range(n+1):
            for i in range(1, m+1):
                if coins[i-1] > cur_amount:
                    dp[cur_amount][i] = dp[cur_amount][i-1]
                else:
                    dp[cur_amount][i] = dp[cur_amount-coins[i-1]][i] + dp[cur_amount][i-1]
                
        return dp[-1][-1]