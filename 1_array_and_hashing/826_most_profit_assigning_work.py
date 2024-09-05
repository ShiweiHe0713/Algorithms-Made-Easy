from typing import List
from bisect import bisect_left

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Create a hashmap of max profit for each difficulty
        hashmap = {}
        
        # make sure don't over the larger diff in the hashmap 
        for dif, prof in zip(difficulty, profit):
            if dif not in hashmap:
                hashmap[dif] = prof
            else:
                tmp = hashmap[dif]
                hashmap[dif] = max(tmp, prof)
        
        # Sort the hashmap by difficulty
        sorted_hashmap = dict(sorted(hashmap.items()))

        # Update sorted_hashmap to ensure each difficulty has the maximum possible profit
        last_diff = -1
        for dif in sorted_hashmap:
            if last_diff != -1:
                sorted_hashmap[dif] = max(sorted_hashmap[dif], sorted_hashmap[last_diff])
            last_diff = dif

        # Create the sorted difficulty array directly from sorted_hashmap keys
        diff_arr = list(sorted_hashmap.keys())

        # Sort the workers by ability
        worker.sort()

        result = 0
        for w in worker:
            # Find the largest difficulty that the worker can handle
            idx = bisect_left(diff_arr, w)

            # Skip workers whose ability is less than the smallest difficulty
            if idx == 0 and w < diff_arr[0]:
                continue

            # Handle case where idx points to a larger difficulty, or it's beyond the list
            if idx == len(diff_arr) or (idx > 0 and diff_arr[idx] > w):
                idx -= 1

            # Add the corresponding profit
            result += sorted_hashmap[diff_arr[idx]]

        return result
