from typing import List

class Solution:
    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        result = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                result = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return result

    def search(self, nums: List[int], target: int) -> int:
        result = -1
        n = len(nums)
        pivot = 0
        
        # find the pivot using linear search
        while pivot + 1 < n:
            if nums[pivot] < nums[pivot + 1]:
                pivot += 1
            else:
                break

        if (result := self.binary_search(nums, 0, pivot, target)) == -1:
            result = self.binary_search(nums, pivot + 1, n - 1, target)

        return result

        