import heapq

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        count = 0

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                count += 1
                heapq.heappop(min_heap)
        
        print(count)
        return min_heap[0]
    
test = [3,2,1,5,6,4]
s1 = Solution()
s1.findKthLargest(test,2)