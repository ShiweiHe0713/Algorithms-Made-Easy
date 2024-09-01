from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = (r + l) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
    
s = Solution()
arr = [3,4,5,1]
print(s.peakIndexInMountainArray(arr))