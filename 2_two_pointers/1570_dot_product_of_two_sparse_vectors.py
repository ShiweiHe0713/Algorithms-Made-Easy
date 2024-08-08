from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.hashmap = {}
        self.length = 0
        # O(n)
        for i, num in enumerate(nums):
            if num != 0:
                self.hashmap[i] = num
                # it's the largest index instead of element counts
                self.length = max(i, self.length)

    # { 0: 1, 3: 2, 4: 3}
    # { 1: 3, 3: 4}
    # Return the dotProduct of two sparse vectors
    # m = 3, n = 2, i = 0, j = 0
    # i = 3, j = 3
    def dotProduct(self, vec: 'SparseVector') -> int:
        acc_product = 0
        m = self.length
        n = vec.length
        i = j = 0
        # less or equal to cuz i,j stand for key in hashmap, not index in array
        # O(max(m,n))
        while i <= m and j <= n:
            if i == j and i in self.hashmap and j in vec.hashmap:
                acc_product += self.hashmap[i] * vec.hashmap[j]
                i += 1
                j += 1
            elif i < j:
                i += 1
            else:
                j += 1

        return acc_product

# nums1 = [1,0,0,2,3]
# nums2 = [0,3,0,4,0]

# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
