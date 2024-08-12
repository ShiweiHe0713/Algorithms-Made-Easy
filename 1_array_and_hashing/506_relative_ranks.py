from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        hashmap = {}
        for i, num in enumerate(score):
            hashmap[num] = i
        
        # sort by key (eg. {10: 0, 9: 3})
        hashmap_sorted = sorted(hashmap, reverse=True)

        # modify the array by the value in hashmap, and in the order of key
        result = [None] * n
        count = 0
        for score, index in hashmap_sorted.items():
            if count == 0:
                result[index] = "Gold Medal"
            elif count == 1:
                result[index] = "Silver Medal"
            elif count == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(count+1)
            count += 1
        return result
