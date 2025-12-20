# DP Solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        dp = [[False] * len(s) for i in range(len(s))]

        for row in range(len(s) - 1, -1, -1):
            for col in range(row, len(s)):
                if s[row] == s[col] and (col - row < 2 or dp[row + 1][col - 1]):
                    dp[row][col] = True
                    result += 1

        return result
