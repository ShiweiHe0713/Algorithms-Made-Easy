from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # 200 - 100 = 100, score : 1
        # 400 + 100 = 500, score : 0
        # 0, score : 2
        tokens.sort()
        
        if tokens[0] > power:
            return 0
        
        left, right = 0, len(tokens) - 1
        max_score = score = 0
        
        while left < right:
            if power > tokens[left]:
                power -= tokens[left]
                score += 1
                max_score = max(score, max_score)
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
        
        return max_score
      	
s1 = Solution()
case = [200,100,500]
s1.bagOfTokensScore(list, 300)