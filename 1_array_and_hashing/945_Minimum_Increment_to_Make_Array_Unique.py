class Solution:
    def minIncrementForUnique(self, nums) -> int:
        """Time: O(nlogn), Space: O(n)"""
        min_increment = 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                increment = nums[i-1] + 1 - nums[i]
                min_increment += increment
            nums[i] = nums[i-1] + 1
        
        return min_increment

    def minIncrementForUnique_counting(self, nums) -> int:
            """Time: O(n+max), O(n+max)"""
            n = len(nums)
            max_num = max(nums)
            # notice the size of counting
            counting = [0 for _ in range(n + max_num + 1)]
            moves = 0

            for num in nums:
                counting[num] += 1
            
            for num, freq in enumerate(counting):
                if freq <= 1:
                    continue
                # duplicates exist
                duplicates = freq - 1
                counting[num + 1] += duplicates
                counting[num] = 1
                moves += duplicates

            return moves


