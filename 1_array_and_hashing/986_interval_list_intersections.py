from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        m, n = len(firstList), len(secondList)
        result = []
        while i < m and j < n:
                left = max(firstList[i][0], secondList[j][0])
                right = min(firstList[i][1], secondList[j][1])
                if left <= right:
                    result.append([left, right])
                
                # only compare right end of the arrays
                if firstList[i][1] <= secondList[j][1]:
                    i += 1
                else:
                    j += 1

        return result
