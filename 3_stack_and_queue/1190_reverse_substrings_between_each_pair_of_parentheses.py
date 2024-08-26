from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # O(n^2)
        stack = []
        
        for c in s:
            if c == ')':
                cur_word = []
                while stack[-1] != '(':
                    ele = stack.pop()
                    cur_word.append(ele)

                stack.pop()
                stack.extend(cur_word)
            else:
                stack.append(c)

        return "".join(stack)

    