from collections import defaultdict
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def dp(i: int, left: int) -> int:
            if i == len(multipliers):
                return 0
            if (i, left) in memo:
                return memo[(i, left)]
            
            right = len(nums) - 1 - (i-left)
            mult = multipliers[i]
            
            memo[(i, left)] = max(nums[left] * mult + dp(i+1, left+1), nums[right]*mult + dp(i+1, left))
            return memo[(i, left)]
        
        memo = defaultdict(list)
        return dp(0, 0)