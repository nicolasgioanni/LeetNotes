# DP Top-Down Exponential Time + Linear Space 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        LIS = 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            LIS = dp[i] if dp[i] > LIS else LIS
        
        return LIS
