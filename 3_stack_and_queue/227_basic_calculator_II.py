from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        # traverse the string, use `num` to keep track of cur number, pre_sign for last op
        # use a stack to keep all the numbers to plus
        stack = deque()
        num = 0
        pre_sign = '+'
        n = len(s)

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in "+-*/":
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                pre_sign = s[i]
                num = 0
        print(stack)
        return sum(stack)

a = "3+2*2"
b = " 3/2 "
c = " 3+5 / 2 "
# ['1', '-', '3', '+', '10', '+', '0']
s1 = Solution()
print(s1.calculate(c))