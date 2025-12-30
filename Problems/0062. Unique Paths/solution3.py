# DP Optimal Time + Space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[n - 1] = 1

        for row in range(m - 1, -1, -1):
            prev = 0
            for col in range(n - 1, -1 , -1):
                dp[col] += prev
                prev = dp[col]

        return dp[0]
