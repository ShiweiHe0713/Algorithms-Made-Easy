from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        i, m = 1, len(intervals)
        # assuming the intervals not sorted
        intervals = sorted(intervals, key=lambda interval: interval[0])
        stack.append(intervals[0])
        
        while stack and i < m:
            cur = stack.pop()
            # if not over lap: push back cur and intervals[i]
            print(cur, intervals[i])
            if cur[1] < intervals[i][0]:
                stack.append(cur)
                stack.append(intervals[i])
            # if over lap: push back merged intervals
            else:
                left = min(cur[0], intervals[i][0])
                right = max(cur[1], intervals[i][1])
                stack.append([left, right])
                # [1,3],[2,6]; [1,6],[2,3], 
            i += 1
        
        return stack