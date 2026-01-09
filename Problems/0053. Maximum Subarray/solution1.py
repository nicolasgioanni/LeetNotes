# Brute Force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')

        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                result = max(result, currSum)

        return result
