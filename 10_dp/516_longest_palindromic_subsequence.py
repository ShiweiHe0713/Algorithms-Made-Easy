class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            if i == j:
                return 1
            if i > j:
                return 0
            
            if s[i] == s[j]:
                cache[(i, j)] = dfs(i+1, j-1) + 2
            else:
                cache[(i, j)] = max(dfs(i+1, j), dfs(i, j-1))
            
            return cache[(i, j)]

        cache = {}
        n = len(s)
        return dfs(0, n-1)
    
    def longestPalindromeSubseq_tab(self, s: str) -> int:
        pass
        