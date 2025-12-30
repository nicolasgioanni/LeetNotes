# DP Linear Time + Space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
        for row in range(len(text1) - 1, -1, -1):
            for col in range(len(text2) - 1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1]) 

        return dp[0][0]
