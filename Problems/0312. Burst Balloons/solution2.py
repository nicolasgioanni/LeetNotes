# DP Optimal Time + Space
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0

            for i in range(l, r + 1):
                dp[(l, r)] = max(dp.get((l, r), 0), 
                                (nums[l - 1] * nums[i] * nums[r + 1]) + dfs(l, i - 1) + dfs(i + 1, r))

            return dp[(l, r)]

        return dfs(1, len(nums) - 2)
