from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'], ['8', '8'],
            ['6', '9'], ['9', '6']
        ]
        
        def generate_strobo(n, final_length):
            if n == 0:
                return [""]
            if n == 1:
                return ['0', '1', '8']
            
            prev_strobo_nums = generate_strobo(n - 2, final_length)
            cur_strobo = []

            for prev_strobo in prev_strobo_nums:
                for pair in reversible_pairs:
                    if pair[0] != '0' or n != final_length:
                        cur_strobo.append(pair[0] + prev_strobo + pair[1])
            
            return cur_strobo

        return generate_strobo(n, n)