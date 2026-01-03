# DP O(numbers * possible sums) Time + Space
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(currentSum, i):
            if (currentSum, i) in dp:
                return dp[(currentSum, i)]
            if i == len(nums):
                return 1 if currentSum == target else 0

            dp[(currentSum, i)] = dfs(currentSum - nums[i], i + 1) + dfs(currentSum + nums[i], i + 1)
            return dp[(currentSum, i)]

        return dfs(0, 0)
