from collections import deque
from typing import List
import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()
        l = 0
        max_length = 0

        for r, num in enumerate(nums):
            # maintain the decremental order in a max_que
            while max_queue and num > max_queue[-1]:
                max_queue.pop()
            max_queue.append(num)
            
            # maintain the incremental order in a min_queu
            while min_queue and num < min_queue[-1]:
                min_queue.pop()
            min_queue.append(num)

            # If the largest - smallest is greater than limit
            while max_queue[0] - min_queue[0] > limit:
                # popleft if left element is the largest
                if max_queue[0] == nums[l]:
                    max_queue.popleft()
                # popleft if left element is the smallest
                if min_queue[0] == nums[l]:
                    min_queue.popleft()
                # increment left until encounter either largest or smallest
                l += 1
            
            max_length = max(max_length, r - l + 1)

        return max_length

    def longestSubarray_heap(self, nums: List[int], limit: int) -> int:
        max_heap = []
        min_heap = []
        l = 0
        max_size = 0

        for r, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, r))
            heapq.heappush(min_heap, (num, r))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                l = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < l:
                    heapq.heappop(min_heap)
                
            max_size = max(max_size, r - l + 1)
        
        return max_size