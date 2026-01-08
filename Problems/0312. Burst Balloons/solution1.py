# Brute Force
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0

            coins = 0
            for i in range(l, r + 1):
                coins = max(coins, 
                                (nums[l - 1] * nums[i] * nums[r + 1]) + dfs(l, i - 1) + dfs(i + 1, r))

            return coins

        return dfs(1, len(nums) - 2)
