from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            j = i
            while i + 1 < len(chars) and chars[i+1] == chars[i]:
                i += 1
            i += 1
            count = i - j

            if count != 1:
                # we can replace a subarray with an array!???
                chars[j+1:i] = list(str(count))
                # decremen i to next differnt char
                i -= (i-j-1) - len(str(count))

        return len(chars)