from collections import defaultdict, deque
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            mid = (r + l) // 2

            if mid + 1 < n and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return r
    