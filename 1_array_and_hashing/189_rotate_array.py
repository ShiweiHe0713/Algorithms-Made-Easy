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