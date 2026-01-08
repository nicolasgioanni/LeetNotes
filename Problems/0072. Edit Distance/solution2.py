# DP Top-Down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            elif i == len(word1):
                dp[(i, j)] = len(word2) - j
            elif j == len(word2):
                dp[(i, j)] = len(word1) - i
            elif word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1)) # insert, delete, replace

            return dp[(i, j)]

        return dfs(0, 0)
