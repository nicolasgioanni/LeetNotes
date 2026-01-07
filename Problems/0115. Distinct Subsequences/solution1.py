# Brute Force
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def dfs(i, j):
            if j == len(t):
                return 1
            elif i == len(s):
                return 0

            skip = dfs(i + 1, j)
            
            take = dfs(i + 1, j + 1) if s[i] == s[j] else 0

            return skip + take

        return dfs(0, 0)
