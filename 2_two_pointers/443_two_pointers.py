from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        n = len(chars)
        i = 0
        while i < n:
            s += chars[i]
            j = i
            while i + 1 < n and chars[i+1] == chars[i]:
                i += 1
            count = i - j + 1
            i += 1
            
            if count != 1:
                s += str(count)

        while chars:
            chars.pop()
        
        for c in s:
            chars.append(c)

        return len(chars)