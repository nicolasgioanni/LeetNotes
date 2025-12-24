# DP Kadane's Algorithm Linear Time + Constant Space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax, currentMin, result = 1, 1, max(nums)

        for i in range(len(nums)):
            temp = currentMax * nums[i]
            currentMax = max(temp, currentMin * nums[i], nums[i])
            currentMin = min(temp, currentMin * nums[i], nums[i])

            result = max(result, currentMax)

        return result
