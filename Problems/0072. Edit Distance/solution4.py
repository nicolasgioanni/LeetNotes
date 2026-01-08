# DP Optimal Time + Space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [0] * (m + 1)

        for col in range(m + 1):
            dp[col] = m - col

        for i in range(n - 1, -1, -1):
            diag = dp[m]
            dp[m] = n - i
            for j in range(m - 1, -1, -1):
                nextDiag = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = diag
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], diag)
                diag = nextDiag

        return dp[0]
