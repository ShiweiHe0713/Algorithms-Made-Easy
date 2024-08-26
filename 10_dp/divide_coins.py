from typing import List

def divide_coins(coins: List[int], amount: int) -> List[int]:
    if amount in memo:
        return memo[amount]
    
    result = [None] * len(coins)

    for i,num in enumerate(coins):
        if i == 0:
            result[0] = 1
            continue
        
        rem = num
        count = 0

        for j in range(i - 1, -1, -1):
            if rem <= 0:
                break
            if rem < coins[j]:
                continue
        
            while rem - coins[j] >= 0:
                rem -= coins[j]
                count += 1
            
        if rem == 0:
            result[i] = count
        else:
            result[i] = -1

    return result[-1]

coins = [1,3,5,8,17,21]
memo = {}
print(divide_coins(coins, 21))