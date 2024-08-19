from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False


# [3,4,5,6],3,2
# 0,1,2,3,4,5
# k == 3
# remove, add, check order
# 1. check window size 
# 2. check if num in the set
# 3. if num not in, add it