from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # letter => frequency in `s`
        hashmap = defaultdict(int)
        for c in s: 
            hashmap[c] += 1
        
        result = ""
        for c in order:
            if c in hashmap:
                while hashmap[c]:
                    result += c
                    hashmap[c] -= 1
        
        for k, v in hashmap.items():
            while v != 0:
                result += k
                v -= 1
        
        return result