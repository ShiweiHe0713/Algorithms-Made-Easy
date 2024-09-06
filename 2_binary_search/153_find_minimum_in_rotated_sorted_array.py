from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] > nums[l] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[r]