class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        
        result = nums[0]
        cur_max = float('-inf')

        for num in nums:
            if cur_max < 0:
                cur_max = 0

            cur_max += num
            result = max(result, cur_max)

        return result
