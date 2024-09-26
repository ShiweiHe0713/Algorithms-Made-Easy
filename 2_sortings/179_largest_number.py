from typing import List

class Solution:
    def custom_sort(self, num1: int, num2: int) -> int:
        comb1 = int(str(num1) + str(num2))
        comb2 = int(str(num2) + str(num1))
        if comb1 >= comb2:
            # we should put num1 first
            return 1
        else:
            return -1

    def merge_sort(self, nums: List[int], l: int, r: int) -> List[int]:
        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            i, j = 0, 0
            m, n = len(nums1), len(nums2)
            # should decremental
            result = []
            while i < m and j < n:
                if self.custom_sort(nums1[i], nums2[j]) > 0:
                    result.append(nums1[i])
                else:
                    result.append(nums2[j])
            
            while i < m:
                result.append(nums1[i])
                i += 1
            while j < n:
                result.append(nums2[j])
                j += 1
            return result
        
        m = l + (r - l) // 2
        nums1 = self.merge_sort(nums, l, m)
        nums2 = self.merge_sort(nums, m + 1, r)

        return merge(nums1, nums2)

    def largestNumber(self, nums: List[int]) -> str:
        return "".join(self.merge_sort(nums, 0, len(nums) - 1))
