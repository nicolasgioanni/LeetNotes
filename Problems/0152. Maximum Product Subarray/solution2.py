# DP Prefix/Suffix Linear Time + Constant Space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result, prefix, suffix = max(nums), 1, 1

        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums) - 1 - i]

            result = max(prefix, suffix, result)

            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1

        return result
