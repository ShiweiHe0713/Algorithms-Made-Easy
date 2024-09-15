from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        l, r = 0, n-1
        result = []
        
        while l < r:
            mid = l + (r - l) // 2
            # found left bound, and we only have to find the left bound
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                result.append(mid)
                j = mid
                while j < n and nums[j] == target:
                    j += 1
                result.append(j-1)
                break

            # move l and r pointer
            if nums[mid] < target:
                l = mid + 1
            # we only have to find left bound, so we can alway shrink to the left
            else:
                r = mid

        if not result and nums[l] == target:
            result += [l, l]
        
        return result if result else [-1, -1]