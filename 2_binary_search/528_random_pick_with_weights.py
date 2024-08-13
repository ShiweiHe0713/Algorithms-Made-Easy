from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        w_sum = 0
        self.prefix_sum = [None] * len(w)
        for i, weight in enumerate(w):
            w_sum += weight
            self.prefix_sum[i] = w_sum
        self.sum_all = w_sum

    def pickIndex(self) -> int:
        target = random.random() * self.sum_all
        # prefix sum is already sorted
        arr = self.prefix_sum
        left, right = 0, len(arr)

        while left <= right:
            mid = left + (right - left) // 2
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left