from typing import List

class Solution:
    def rotate_bf(self, nums: List[int], k: int) -> None:
        """Time: O(nk), space: O(1)"""
        n = len(nums)
        k %= n

        for i in range(k):
            prev = nums[-1]
            for j in range(n):
                nums[j], prev = prev, nums[j]

    def rotate(self, nums: List[int], k: int) -> None:
        """Time: O(n), space: O(n)"""
        n = len(nums)
        arr = [None] * n

        for i, num in enumerate(nums):
            idx = (i + k) % n
            arr[idx] = num
        
        nums[:] = arr

    def rotate_reverse(self, nums: List[int], k: int) -> None:
        def reverse(nums: List[int], l: int, r: int) -> None:
            """r pointer inclusive"""
            if not nums or l == r:
                return

            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k %= len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
        