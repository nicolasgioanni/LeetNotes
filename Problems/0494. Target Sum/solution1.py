# Brute Force
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(currentSum, i):
            if i == len(nums):
                return 1 if currentSum == target else 0

            return dfs(currentSum - nums[i], i + 1) + dfs(currentSum + nums[i], i + 1)

        return dfs(0, 0)
