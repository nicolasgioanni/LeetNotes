# Linear * Exponential Time + Space
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(i, subset):
            nonlocal result
            if i == len(nums):
                result.append(subset)
                return
            
            skip = dfs(i + 1, list(subset))

            newSet = list(subset)
            newSet.append(nums[i])
            take = dfs(i + 1, newSet)
            return

        dfs(0, [])
        return result
