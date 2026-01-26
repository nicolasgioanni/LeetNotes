# Brute Force
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combitations = set()
        
        def dfs(i, currSum, sumSet):
            nonlocal result
            nonlocal combitations
            if currSum == target and i == len(nums) and tuple(sumSet) not in combitations:
                combitations.add(tuple(sumSet))
                result.append(list(sumSet))
                return
            elif currSum == target and tuple(sumSet) not in combitations:
                combitations.add(tuple(sumSet))
                result.append(list(sumSet))
                return
            elif i == len(nums):
                return

            dfs(i + 1, currSum, sumSet) # skip
            
            currSum += nums[i]
            if currSum <= target:
                sumSet.append(nums[i])
                dfs(i, currSum, sumSet) # take
                sumSet.pop()
            return

        dfs(0, 0, [])
        return result
