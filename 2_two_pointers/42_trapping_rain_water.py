from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        l_max, r_max = 0, 0
        result = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] < l_max:
                    result += l_max - height[l]
                else:
                    l_max = height[l]
                l += 1
            else:
                if height[r] < r_max:
                    result += r_max - height[r]
                else:
                    r_max = height[r]
                r -= 1
        
        return result