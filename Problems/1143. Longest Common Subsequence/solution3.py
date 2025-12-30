# DP Optimal Time + Space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        
        for row in range(len(text1) - 1, -1, -1):
            prevDiag = 0
            for col in range(len(text2) - 1, -1, -1):
                temp = dp[col]
                if text1[row] == text2[col]:
                    dp[col] = 1 + prevDiag
                else:
                    dp[col] = max(dp[col], dp[col + 1]) 
                prevDiag = temp
        return dp[0]
