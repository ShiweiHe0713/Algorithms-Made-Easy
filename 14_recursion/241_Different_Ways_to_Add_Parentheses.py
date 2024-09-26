from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(expression: str, start: int, end: int) -> List[int]:
            if (start, end) in memo:
                return memo[(start, end)]
            
            if expression.isdigit():
                return [int(expression)]
            result = []

            for i, c in enumerate(expression):
                if c.isdigit():
                    continue
                lefts = helper(expression[:i], start, (start + end) // 2)
                rights = helper(expression[i+1:], (start + end) // 2 + 1, end)

                for left in lefts:
                    for right in rights:
                        if c == '+':
                            cur = left + right
                        elif c == '-':
                            cur = left - right
                        elif c == '*':
                            cur = left * right
                        result.append(cur)
            memo[(start, end)] = result
            return result

        memo = {}
        return helper(expression, 0, len(expression) - 1)
    
    def diffWaysToCompute_DP(self, expression: str) -> List[int]:
        def helper(start: int, end: int) -> List[int]:
            if (start, end) in memo:
                return memo[(start, end)]
            
            result = []
            
            sub_expr = expression[start:end+1]
            if sub_expr.isdigit():
                result.append(int(sub_expr))
                memo[(start, end)] = result
                return result
            
            for i in range(start, end+1):
                c = expression[i]
                if c.isdigit():
                    continue

                lefts = helper(start, i-1)
                rights = helper(i+1, end)

                for left in lefts:
                    for right in rights:
                        if c == '+':
                            cur = left + right
                        elif c == '-':
                            cur = left - right
                        elif c == '*':
                            cur = left * right
                        result.append(cur)

            memo[(start, end)] = result
            return result

        memo = {}
        return helper(0, len(expression) - 1)