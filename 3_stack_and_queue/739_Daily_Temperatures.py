from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # traverse the temperatures array
        # create a mono decreasing stack
        # if the cur_temp > than stack.top(), we update the result arr
        # if not, we push cur_temp's index into the stack
        n = len(temperatures)
        stack = []
        result = [0] * n

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and cur_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = cur_day - prev_day
            # if it cold than top
            stack.append(cur_day)
        
        return result
