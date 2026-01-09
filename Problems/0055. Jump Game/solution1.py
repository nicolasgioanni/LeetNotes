# DP Brute Force
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        dp[len(nums) - 1] = True

        for i in range(len(dp) - 2, -1, -1):
            counter = 0
            while counter < nums[i]:
                if i + nums[i] - counter < len(dp):
                    dp[i] = dp[i + nums[i] - counter] or dp[i]
                counter += 1

        return dp[0]
