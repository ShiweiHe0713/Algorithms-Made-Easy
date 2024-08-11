from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hash_set = set(nums)
        max_result = 1

        for num in hash_set:
            result = 1
            if num - 1 in hash_set:
                continue
            
            while num + 1 in hash_set:
                result += 1
                max_result = max(result, max_result)
                num = num + 1
        
        return max_result