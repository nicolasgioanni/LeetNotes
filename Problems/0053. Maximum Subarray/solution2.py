# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest, currSum = float('-inf'), 0

        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            largest = max(largest, currSum)

        return largest
