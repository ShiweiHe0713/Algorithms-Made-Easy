from collections import defaultdict
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:        
        result = {}
        for c in words[0]:
            if c not in result:
                result[c] = 0
            result[c] += 1
        
        for i in range(1, len(words)):
            # count number of each letter
            cur_word = defaultdict(int)
            for c in words[i]:
                cur_word[c] += 1

            # calculate the duplicates
            for c in result.keys():
                if c not in words[i]:
                    result[c] = 0
                else:
                    result[c] = min(result[c], cur_word[c])

        builder = []
        for key, value in result.items():
            while value:
                builder.append(key)
                value -= 1
            
        return builder
