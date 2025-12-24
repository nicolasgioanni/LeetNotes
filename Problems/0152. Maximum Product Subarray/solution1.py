# Brute Force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0] if nums else -10

        for l in range(len(nums)):
            currentSum = 1
            for r in range(l, len(nums)):
                currentSum *= nums[r]
                if currentSum > result:
                    result = currentSum

        return result
