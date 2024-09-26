from typing import List

class Solution:
    def two_sum_2(self, nums: List[int], l: int, target: int) -> List[int]:
        r = len(nums) - 1
        local_result = []

        while l < r:
            if nums[l] + nums[r] == target:
                local_result.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while r > l and nums[r] == nums[r+1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

        return local_result
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.two_sum_2(nums, i+1, -nums[i])

            if pairs:
                for pair in pairs:
                    pair.append(nums[i])
                    result.append(pair)
        
        return result