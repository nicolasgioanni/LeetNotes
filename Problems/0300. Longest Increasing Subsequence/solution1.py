# Brute Force
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(prev, index):
            if index == len(nums):
                return 0
            
            skip = dfs(prev, index + 1)
            take = 0

            if prev == None or nums[prev] < nums[index]:
                take = 1 + dfs(index, index + 1)

            return max(skip, take)

        return dfs(None, 0)
