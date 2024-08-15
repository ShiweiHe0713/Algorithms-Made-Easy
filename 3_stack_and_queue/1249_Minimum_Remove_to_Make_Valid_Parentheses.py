from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        to_remove = set()

        for i, c in enumerate(s):
            if c.isalpha():
                continue
            if c == '(':
                stack.append((c, i))
            # c == ')' and stack is empty
            elif not stack:
                to_remove.add(i)
            # c == ')' and stack is not empty
            else:
                stack.pop()
        
        # what's in the stack now is also invalid
        while stack:
            cur = stack.pop()
            to_remove.add(cur[1])

        # started to build the new string
        result = ""
        for i in range(len(s)):
            if i not in to_remove:
                result += s[i]
        
        return result