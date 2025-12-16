# Brute Force
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(house):
            if house >= len(nums):
                return 0
            
            return max(dfs(house + 1), nums[house] + dfs(house + 2))


        return dfs(0)
