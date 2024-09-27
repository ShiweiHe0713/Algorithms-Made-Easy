from collections import defaultdict
from typing import List

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        hashmap = defaultdict(int)
        max_count = 0
        target = ""

        for c in s:
            hashmap[c] += 1
            if hashmap[c] > (n + 1) // 2:
                return ""
            if hashmap[c] > max_count:
                max_count = hashmap[c]
                target = c

        result = target * max_count
        hashmap[target] = 0

        for i in range(1, n, 2):
            cand = ""

            for letter, freq in hashmap.items():
                if freq > 0 and target != letter:
                    cand = letter
                    hashmap[letter] -= 1
                    break

            if cand:
                left = result[:i][:]
                right = result[i:][:]
                result = left + cand + right

        for letter, freq in hashmap.items():
            if freq > 0:
                result += letter

        return result

s = "eqmeyggvp"
sol = Solution()
print(sol.reorganizeString(s))
