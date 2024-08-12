from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        w_sum = 0
        self.prefix_sum = [None] * len(w)
        self.hashmap = {}
        for i, weight in enumerate(w):
            w_sum += weight
            self.prefix_sum[i] = w_sum
            self.hashmap[weight] = i
        self.sum_all = w_sum

    def pickIndex(self) -> int:
        target = random.random() * self.sum_all
        # prefix sum is already sorted
        for i, p in enumerate(self.prefix_sum):
            if target <= p:
                return i
