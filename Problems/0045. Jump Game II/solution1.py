# Brute Force
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def dfs(i):
            if i >= len(nums) - 1:
                return 0

            jumps = float('inf')
            for j in range(i + 1, i + nums[i] + 1):
                jumps = min(jumps, dfs(j))

            return 1 + jumps

        return dfs(0)
