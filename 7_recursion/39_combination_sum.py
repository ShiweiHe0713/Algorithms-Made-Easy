from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start: int, arr: List[int]) -> None:
            if sum(arr) == target:
                result.append(arr[:])
                return
            if sum(arr) > target:
                return

            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                dfs(i, arr)
                arr.pop()
    
        result = []
        dfs(0, [])
        return result

# [2,3,6,7]
# 7
# [2,3,5]
# 8
# [2]
# 1