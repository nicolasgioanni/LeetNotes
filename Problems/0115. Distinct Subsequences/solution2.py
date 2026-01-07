# DP Top-Down
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(t):
                return 1
            elif i == len(s):
                return 0

            dp[(i, j)] = dp.get((i, j), 0) + dfs(i + 1, j) + (dfs(i + 1, j + 1) if s[i] == t[j] else 0)

            return dp[(i, j)]

        return dfs(0, 0)
