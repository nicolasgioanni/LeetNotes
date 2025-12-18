# DP Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        dp = [[False] * len(s) for i in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i + 1 <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > len(result):
                        result = s[i:j + 1]
        return result
