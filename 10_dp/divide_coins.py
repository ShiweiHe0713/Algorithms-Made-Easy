from typing import List

def divide_coins(coins: List[int], amount: int) -> List[int]:
    if amount in coins:
        return 1
    
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

            result[i] = count if rem == 0 else -1
    
    print(result)
    return result[-1]

coins = [1,3,5,8,17,21]
# result= [1,3,3,2,3,3]
memo = {}
divide_coins(coins, 21)

# 17, 8
# 17 = 8 + 8 + 1
