from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        pre_sum = 0
        result = 0

        for num in nums:
            pre_sum += num
            
            if pre_sum - k in hashmap:
                result += hashmap[pre_sum - k]
            
            hashmap[pre_sum] += 1

        return result