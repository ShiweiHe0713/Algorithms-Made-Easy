from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        strobo_pairs = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        def generate_strobo_numbers(cur_len: int, fin_len: int) -> List[str]:
            # base case
            if cur_len == 0:
                return [""]
            if cur_len == 1:
                return ['0', '1', '8']
            # non-base case: cur_len == cur_len
            # result = generate_strobo_numbers(cur_len - 2)
            # append a pair on the two side of newly generate rated strobo array
            prev_strobo = generate_strobo_numbers(cur_len - 2, fin_len)
            cur_strobo = []

            for key, value in strobo_pairs.items():
                for number in prev_strobo:
                    if key != '0' or cur_len != fin_len:
                        tmp = key + "".join(number) + value
                        cur_strobo.append(tmp)

            return cur_strobo

        return generate_strobo_numbers(n, n)
    
s1 = Solution()
print(s1.findStrobogrammatic(2))