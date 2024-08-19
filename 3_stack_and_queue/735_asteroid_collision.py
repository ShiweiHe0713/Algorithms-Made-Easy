from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
            else:
                # -> -> or <- <-
                if (stack[-1] < 0 and ast < 0) or (stack[-1] > 0 and ast > 0):
                    stack.append(ast)
                # <- -> 
                elif stack[-1] < 0 and ast > 0:
                    stack.append(ast)
                else:
                    # -> <-
                    print(stack)
                    while stack and 0 < stack[-1] < -ast:
                        stack.pop()
                    if not stack:
                        stack.append(ast)
                    elif stack[-1] == -ast:
                        stack.pop()
                    elif stack[-1] < 0 and ast < 0:
                        stack.append(ast)
        return stack
