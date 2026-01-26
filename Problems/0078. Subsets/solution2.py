# Linear * Exponential Time + Linear Space
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(i, subset):
            nonlocal result
            if i == len(nums):
                result.append(list(subset))
                return
            
            skip = dfs(i + 1, subset)

            subset.append(nums[i])
            take = dfs(i + 1, subset)
            subset.pop()
            return

        dfs(0, [])
        return result
