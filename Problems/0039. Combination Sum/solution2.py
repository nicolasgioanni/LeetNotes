class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(i, currSum, subset):
            if currSum == target:
                result.append(list(subset))
                return
            elif currSum > target or i == len(nums):
                return
            
            dfs(i + 1, currSum, subset)

            subset.append(nums[i])
            dfs(i, currSum + nums[i], subset)
            subset.pop()

            return

        dfs(0, 0, [])
        return result
